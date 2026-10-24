
import asyncio
import random
from typing import Sequence

import discord
from discord import app_commands
from discord.ext import commands
from sqlalchemy import select

from models.economy import EconomyUser
from models.slot import SlotSymbol
from tools.database import SessionLocal


DEFAULT_SYMBOLS = ["🍓", "🍉", "🍊", "🥕", "7️⃣", "🎵"]

MAX_SYMBOLS = 10
MAX_BET = 1000
STARTING_COINS = 1500


class SlotCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        print("Init -> SlotCog")

    async def get_slot_symbol(self, guild_id: int) -> list[str]:
        async with SessionLocal() as session:
            row = await session.scalar(
                select(SlotSymbol).where(
                    SlotSymbol.guild_id == str(guild_id)
                )
            )

            if row is None:
                return DEFAULT_SYMBOLS.copy()

            if not isinstance(row.symbols, list):
                return DEFAULT_SYMBOLS.copy()

            symbols = [
                s.strip()
                for s in row.symbols
                if isinstance(s, str) and s.strip()
            ]

            return symbols or DEFAULT_SYMBOLS.copy()

    async def get_or_create_symbols(
        self, session, guild_id: str
    ) -> SlotSymbol:
        row = await session.scalar(
            select(SlotSymbol).where(
                SlotSymbol.guild_id == guild_id
            )
        )

        if row is None:
            row = SlotSymbol(
                guild_id=guild_id,
                symbols=DEFAULT_SYMBOLS.copy(),
            )
            session.add(row)
            await session.flush()

        return row

    async def get_or_create_user(
        self, session, user_id: str, guild_id: str
    ) -> EconomyUser:
        row = await session.scalar(
            select(EconomyUser)
            .where(
                EconomyUser.user_id == user_id,
                EconomyUser.guild_id == guild_id,
            )
            .with_for_update()
        )

        if row is None:
            row = EconomyUser(
                user_id=user_id,
                guild_id=guild_id,
                coin=STARTING_COINS,
            )
            session.add(row)
            await session.flush()

        return row

    @staticmethod
    def generate_slot(symbols: Sequence[str]) -> list[str]:
        return [random.choice(symbols) for _ in range(3)]

    @staticmethod
    def make_embed(
        result: Sequence[str],
        title: str = "🎰 スロット",
        color: discord.Color | None = None,
    ) -> discord.Embed:
        return discord.Embed(
            title=title,
            description="　".join(result),
            color=color or discord.Color.blurple(),
        )

    @app_commands.command(
        name="slot",
        description="コインを賭けてスロットを回します。",
        extras={"category": "🎰スロット"},
    )
    @app_commands.guild_only()
    @app_commands.describe(
        coin="賭けるコイン（1〜1000）"
    )
    @app_commands.allowed_installs(guilds=True, users=False)
    async def slot(
        self,
        interaction: discord.Interaction,
        coin: app_commands.Range[int, 1, MAX_BET],
    ):
        await interaction.response.defer()

        if interaction.guild_id is None:
            await interaction.followup.send(
                "❌ サーバー内で実行してください。",
                ephemeral=True,
            )
            return

        guild_id = str(interaction.guild_id)
        user_id = str(interaction.user.id)

        async with SessionLocal() as session:
            async with session.begin():
                user = await self.get_or_create_user(
                    session, user_id, guild_id
                )

                if user.coin < coin:
                    balance = user.coin
                    insufficient = True
                else:
                    user.coin -= coin
                    balance = user.coin
                    insufficient = False

        if insufficient:
            await interaction.edit_original_response(
                content=(
                    f"❌ コインが足りません。\n"
                    f"所持コイン: **{balance:,}**\n"
                    f"賭け金: **{coin:,}**"
                ),
                embed=None,
            )
            return

        symbols = await self.get_slot_symbol(
            interaction.guild_id
        )

        if not symbols:
            async with SessionLocal() as session:
                async with session.begin():
                    user = await session.scalar(
                        select(EconomyUser)
                        .where(
                            EconomyUser.user_id == user_id,
                            EconomyUser.guild_id == guild_id,
                        )
                        .with_for_update()
                    )
                    if user is not None:
                        user.coin += coin

            await interaction.edit_original_response(
                content="❌ シンボルが設定されていません。賭け金を返却しました。",
                embed=None,
            )
            return

        for _ in range(3):
            await interaction.edit_original_response(
                content=None,
                embed=self.make_embed(
                    self.generate_slot(symbols),
                    title="🎰 スロット回転中...",
                ),
            )
            await asyncio.sleep(0.8)

        result = self.generate_slot(symbols)
        won = result[0] == result[1] == result[2]

        async with SessionLocal() as session:
            async with session.begin():
                user = await session.scalar(
                    select(EconomyUser)
                    .where(
                        EconomyUser.user_id == user_id,
                        EconomyUser.guild_id == guild_id,
                    )
                    .with_for_update()
                )

                if won and user is not None:
                    user.coin += coin * 2

                balance = user.coin if user is not None else 0

        if won:
            title = "🎉 大当たり！"
            color = discord.Color.green()
            message = (
                f"✅ 3つ揃いました！\n"
                f"💰 払い戻し: **{coin * 2:,}コイン**\n"
                f"📈 純利益: **+{coin:,}コイン**"
            )
        else:
            title = "❌ はずれ..."
            color = discord.Color.red()
            message = f"💸 **{coin:,}コイン**を失いました。"

        embed = self.make_embed(result, title, color)
        embed.add_field(
            name="現在の所持コイン",
            value=f"{balance:,} コイン",
            inline=False,
        )

        await interaction.edit_original_response(
            content=message,
            embed=embed,
        )

    @app_commands.command(
        name="symbol",
        description="スロットのシンボルを追加・削除します。",
        extras={"category": "🎰スロット"},
    )
    @app_commands.guild_only()
    @app_commands.describe(
        symbol="追加または削除する絵文字"
    )
    @app_commands.allowed_installs(guilds=True, users=False)
    @app_commands.checks.has_permissions(manage_guild=True)
    async def symbol(
        self,
        interaction: discord.Interaction,
        symbol: str,
    ):
        await interaction.response.defer(ephemeral=True)

        if interaction.guild_id is None:
            await interaction.followup.send(
                "❌ サーバー内で実行してください。",
                ephemeral=True,
            )
            return

        symbol = symbol.strip()

        if not symbol or len(symbol) > 32:
            await interaction.followup.send(
                "❌ シンボルは1〜32文字で指定してください。",
                ephemeral=True,
            )
            return

        guild_id = str(interaction.guild_id)

        async with SessionLocal() as session:
            async with session.begin():
                row = await self.get_or_create_symbols(
                    session, guild_id
                )

                symbols = list(row.symbols or DEFAULT_SYMBOLS)

                if symbol in symbols:
                    symbols.remove(symbol)
                    row.symbols = symbols
                    response = (
                        f"🗑️ シンボル {symbol} を削除しました。"
                    )
                elif len(symbols) >= MAX_SYMBOLS:
                    response = (
                        f"❌ シンボルは最大{MAX_SYMBOLS}種類です。"
                    )
                else:
                    symbols.append(symbol)
                    row.symbols = symbols
                    response = (
                        f"✅ シンボル {symbol} を追加しました。"
                    )

                current_symbols = list(row.symbols)

        await interaction.followup.send(
            f"{response}\n\n"
            f"現在のシンボル（{len(current_symbols)}/{MAX_SYMBOLS}）:\n"
            + " ".join(current_symbols),
            ephemeral=True,
        )

    @app_commands.command(
        name="balance",
        description="現在の所持コインを確認します。",
        extras={"category": "🎰スロット"},
    )
    @app_commands.guild_only()
    @app_commands.allowed_installs(guilds=True, users=False)
    @app_commands.describe(
        user="指定しない場合は自分が指定されます"
    )
    async def balance(
        self,
        interaction: discord.Interaction,
        user: discord.User = None
    ):
        if not user:
            user = interaction.user
        
        await interaction.response.defer()

        if interaction.guild_id is None:
            await interaction.followup.send(
                "❌ サーバー内で実行してください。",
            )
            return

        async with SessionLocal() as session:
            async with session.begin():
                user = await self.get_or_create_user(
                    session,
                    str(user.id),
                    str(interaction.guild_id),
                )
                balance = user.coin

        embed = discord.Embed(
            description=f"**{balance:,} コイン**",
            color=discord.Color.random(),
        )
        await interaction.followup.send(
            content="✅️ 所持コインを表示しました。",
            embed=embed,
        )


async def setup(bot: commands.Bot):
    await bot.add_cog(SlotCog(bot))
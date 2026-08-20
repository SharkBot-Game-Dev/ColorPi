from discord.ext import commands
import discord
from discord import app_commands

class AdminCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.ADMIN_USERS = [1335428061541437531]
        print("Init -> AdminCog")

    admin = app_commands.Group(name="admin", description="Bot管理者用コマンド", guild_ids=[1539202334238707822], guild_only=True)

    @admin.command(name="reload", description="Cogをリロードします。")
    @app_commands.describe(cog_name="Cog名")
    async def admin_reload(self, interaction: discord.Interaction, cog_name: str):
        if interaction.user.id not in self.ADMIN_USERS:
            await interaction.response.send_message(ephemeral=True, content="❌ 権限がありません。")
            return

        await interaction.response.defer()

        await self.bot.reload_extension(f"cogs.{cog_name}")

        await interaction.followup.send(content=f"✅ `cogs.{cog_name}` をリロードしました。")

    @admin.command(name="load", description="Cogをロードします。")
    @app_commands.describe(cog_name="Cog名")
    async def admin_load(self, interaction: discord.Interaction, cog_name: str):
        if interaction.user.id not in self.ADMIN_USERS:
            await interaction.response.send_message(ephemeral=True, content="❌ 権限がありません。")
            return

        await interaction.response.defer()

        await self.bot.load_extension(f"cogs.{cog_name}")

        await interaction.followup.send(content=f"✅ `cogs.{cog_name}` をロードしました。")

    @admin.command(name="sync", description="スラッシュコマンドを同期します。")
    @app_commands.describe(guild_id="サーバーid")
    async def admin_sync(self, interaction: discord.Interaction, guild_id: str = None):
        if interaction.user.id not in self.ADMIN_USERS:
            await interaction.response.send_message(ephemeral=True, content="❌ 権限がありません。")
            return

        await interaction.response.defer()

        if not guild_id:
            await self.bot.tree.sync()
        else:
            await self.bot.tree.sync(guild=discord.Object(int(guild_id)))

        text = 'グローバルに' if guild_id else f'`{guild_id}`に'
        await interaction.followup.send(content=f"✅ {text}同期しました。")

async def setup(bot):
    await bot.add_cog(AdminCog(bot))
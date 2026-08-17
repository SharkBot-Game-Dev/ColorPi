from discord.ext import commands
import discord
from discord import app_commands

class SearchCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        print("Init -> SearchCog")

    @app_commands.command(name="avatar", description="指定したユーザーのアバターを表示します。", extras={"category": "✨その他"})
    @app_commands.describe(user="指定したユーザーのアバターを表示します。")
    async def avatar_command(self, interaction: discord.Interaction, user: discord.User = None):
        await interaction.response.defer()

        user = user if user else interaction.user

        embed = discord.Embed(color=discord.Color.random())
        embed.set_image(url=user.display_avatar.url)

        await interaction.followup.send(embed=embed, content="✅ アバターを表示しました。")

    @app_commands.command(name="banner", description="指定したユーザーのバナーを表示します。", extras={"category": "✨その他"})
    @app_commands.describe(user="指定したユーザーのバナーを表示します。")
    async def banner_command(self, interaction: discord.Interaction, user: discord.User = None):
        await interaction.response.defer()

        user = user if user else interaction.user
        user = await interaction.client.fetch_user(user.id)

        if not user.banner:
            await interaction.followup.send(content="❌ そのユーザーにはバナーが存在しません。")
            return

        embed = discord.Embed(color=discord.Color.random())
        embed.set_image(url=user.banner.url)

        await interaction.followup.send(embed=embed, content="✅ バナーを表示しました。")

    @app_commands.command(name="user", description="指定したユーザーの情報を表示します。", extras={"category": "✨その他"})
    @app_commands.describe(user="指定したユーザーの情報を表示します。")
    async def user_command(self, interaction: discord.Interaction, user: discord.User = None):
        await interaction.response.defer()

        user = user if user else interaction.user

        embed = discord.Embed(color=discord.Color.random())
        embed.set_thumbnail(url=user.display_avatar.url)

        embed.add_field(name="✨ユーザーid", value=str(user.id), inline=False)
        embed.add_field(name="🤖Botですか？", value="はい" if user.bot else "いいえ", inline=False)
        embed.add_field(name="⏰アカウント作成日", value=str(user.created_at), inline=False)

        if user.primary_guild.tag:
            embed.add_field(name="🔖サーバータグ", value=str(user.primary_guild.tag), inline=False)

        await interaction.followup.send(embed=embed, content=f"✅ {user.name}の情報を表示しました。")

async def setup(bot):
    await bot.add_cog(SearchCog(bot))
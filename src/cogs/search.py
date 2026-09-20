import asyncio
import io

from PIL import Image
from discord.ext import commands
import discord
from discord import app_commands

class SearchCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        print("Init -> SearchCog")

    @app_commands.command(name="avatar", description="指定したユーザーのアバターを表示します。", extras={"category": "🔍検索と情報"})
    @app_commands.describe(user="指定したユーザーのアバターを表示します。")
    async def avatar_command(self, interaction: discord.Interaction, user: discord.User = None):
        await interaction.response.defer()

        user = user if user else interaction.user

        embed = discord.Embed(color=discord.Color.random())
        embed.set_image(url=user.display_avatar.url)

        await interaction.followup.send(embed=embed, content="✅ アバターを表示しました。")

    @app_commands.command(name="banner", description="指定したユーザーのバナーを表示します。", extras={"category": "🔍検索と情報"})
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

    @app_commands.command(name="user", description="指定したユーザーの情報を表示します。", extras={"category": "🔍検索と情報"})
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

    @app_commands.command(name="server", description="サーバーの情報を表示します。", extras={"category": "🔍検索と情報"})
    @app_commands.allowed_installs(guilds=True, users=False)
    async def server_command(self, interaction: discord.Interaction):
        await interaction.response.defer()

        embed = discord.Embed(color=discord.Color.random())
        embed.set_thumbnail(url=interaction.guild.icon.url if interaction.guild.icon else None)

        embed.add_field(name="✨サーバーid", value=str(interaction.guild.id), inline=False)
        embed.add_field(name="📛サーバー名", value=str(interaction.guild.name), inline=False)
        embed.add_field(name="⏰サーバー作成日", value=str(interaction.guild.created_at), inline=False)

        await interaction.followup.send(embed=embed, content=f"✅ {interaction.guild.name}の情報を表示しました。", allowed_mentions=discord.AllowedMentions.none())

    @app_commands.command(name="role", description="ロールの情報を表示します。", extras={"category": "🔍検索と情報"})
    @app_commands.describe(role="指定したロールの情報を表示します。")
    @app_commands.allowed_installs(guilds=True, users=False)
    async def role_command(self, interaction: discord.Interaction, role: discord.Role):
        await interaction.response.defer()

        embed = discord.Embed(color=discord.Color.random())

        embed.add_field(name="✨ロールid", value=str(role.id), inline=False)
        embed.add_field(name="📛ロール名", value=str(role.name), inline=False)
        embed.add_field(name="⏰ロール作成日", value=str(role.created_at), inline=False)
        hex_code = f"#{role.color.value:06x}"
        embed.add_field(name="🎨ロールの色", value=str(hex_code), inline=False)

        embed.set_image(url="attachment://role_color.png")

        def draw():

            image = Image.new("RGBA", (300, 150), hex_code)

            save = io.BytesIO()
            image.save(save, "png")
            save.seek(0)

            return save

        image = await asyncio.to_thread(draw)

        await interaction.followup.send(embed=embed, content=f"✅ {role.mention}の情報を表示しました。", allowed_mentions=discord.AllowedMentions.none(), file=discord.File(image, filename="role_color.png"))

        image.close()

    @app_commands.command(name="rolecount", description="ロール一覧とメンバー数を表示します。", extras={"category": "🔍検索と情報"})
    @app_commands.describe(role="指定したロールの情報を表示します。")
    @app_commands.allowed_installs(guilds=True, users=False)
    async def rolecount_command(self, interaction: discord.Interaction):
        await interaction.response.defer()

        roles = await interaction.guild.role_member_counts()
        rolescount = len(interaction.guild.roles)
        
        text = ""
        for role, count in roles.items():
            text += f"<@&{role.id}> .. {count}人\n"
        embed = discord.Embed(color=discord.Color.random(), description=text)

        await interaction.followup.send(embed=embed, content=f"✅ {rolescount}個のロールを表示しました。", allowed_mentions=discord.AllowedMentions.none())

async def setup(bot):
    await bot.add_cog(SearchCog(bot))

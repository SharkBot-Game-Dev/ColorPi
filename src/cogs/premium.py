import aiohttp
from discord.ext import commands
import discord
from discord import app_commands
import os

class PremiumCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        print("Init -> PremiumCog")

    @app_commands.command(name="premium", description="プレミアム機能を入手します。")
    async def premium_command(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)

        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.sharkbot.xyz/premium/check/' + str(interaction.user.id), headers={"authorization": os.environ.get('PREMIUM_API_KEY')}) as resp:
                json = await resp.json()

                if json.get('premium'):
                    await interaction.followup.send(ephemeral=True, content="""✅️ プレミアムに加入しています。

以下の機能が使用できます👇️
```
✨SharkBotのメンバーシップ機能
🎨ColorPiのアイコン、バナーを変更
```
""")
                else:
                    await interaction.followup.send(ephemeral=True, content="""❌ プレミアムに加入していません。

加入すると以下の機能が
使用できるようになります👇️
```
✨SharkBotのメンバーシップ機能
🎨ColorPiのアイコン、バナーを変更
```
""", view=discord.ui.View(timeout=None).add_item(discord.ui.Button(label="今すぐ加入する（月額500円）", url="https://www.sharkbot.xyz/membership/login")))

    @app_commands.command(name="custom", description="[有料] Botのアバターを変更します。")
    @app_commands.describe(avatar="不適切な画像のアップロードは禁止です。", banner="不適切な画像のアップロードは禁止です。", bio="自己紹介を指定できます。")
    @app_commands.allowed_installs(guilds=True, users=False)
    @app_commands.checks.has_permissions(manage_channels=True)
    async def custom_command(self, interaction: discord.Interaction, avatar: discord.Attachment = None, banner: discord.Attachment = None, bio: str = None):
        await interaction.response.defer()

        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.sharkbot.xyz/premium/check/' + str(interaction.user.id), headers={"authorization": os.environ.get('PREMIUM_API_KEY')}) as resp:
                json = await resp.json()

                if json.get('premium'):
                    if avatar:
                        avatar = await avatar.read()
                    if banner:
                        banner = await banner.read()
                    await interaction.guild.me.edit(avatar=avatar, banner=banner, bio=bio)
                    await interaction.followup.send(content="✅ アバターを変更しました。\n-# 💡リセットには何も指定せず/customを実行してください。")
                else:
                    await interaction.followup.send(content="❌ プレミアムが必要です。\n✨ 加入することで変更できるようになります。", view=discord.ui.View(timeout=None).add_item(discord.ui.Button(label="今すぐ加入する（月額500円）", url="https://www.sharkbot.xyz/membership/login")))

async def setup(bot):
    await bot.add_cog(PremiumCog(bot))
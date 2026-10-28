from discord.ext import commands
import discord
from discord import app_commands

import aiohttp

class NewsCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        print("Init -> NewsCog")

    @app_commands.command(name="news", description="最新ニュースを確認します。", extras={"category": "✨その他"})
    async def news_command(self, interaction: discord.Interaction):
        await interaction.response.defer()

        async with aiohttp.ClientSession() as session:
            async with session.get('https://api.sharkbot.xyz/search/news') as resp:
                json = await resp.json()

        news_url = json["news_url"]
        await interaction.followup.send(content=f"✅ 最新ニュースを取得しました。\n\n{news_url}")

async def setup(bot):
    await bot.add_cog(NewsCog(bot))
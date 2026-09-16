import os

import aiohttp
from discord.ext import commands, tasks
import discord

class BadgeCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        print("Init -> BadgeCog")

    @tasks.loop(seconds=10)
    async def change_status(self):
        await self.bot.change_presence(activity=discord.CustomActivity(name=f"/help | {len(self.bot.guilds)}鯖"))

    @commands.Cog.listener("on_ready")
    async def on_ready_start_loop(self):
        self.change_status.start()

        print("Ready.")

        async with aiohttp.ClientSession() as session:
            await discord.Webhook.from_url(os.environ.get('STATUS_WEBHOOK'), session=session).send(content=f"✅起動しました。\n\n😆サーバー数: {len(self.bot.guilds)}")

async def setup(bot):
    await bot.add_cog(BadgeCog(bot))
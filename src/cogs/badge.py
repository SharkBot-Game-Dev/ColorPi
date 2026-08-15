from discord.ext import commands, tasks
import discord
import asyncio
import random

from tools import drawAvatar

class BadgeCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        print("Init -> BadgeCog")

    @tasks.loop(seconds=10)
    async def change_status(self):
        await self.bot.change_presence(activity=discord.CustomActivity(name="/draw"))

    @tasks.loop(hours=3)
    async def change_avatar(self):
        red = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        green = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        blue = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        image = await asyncio.to_thread(drawAvatar.drawAvatar, red, green, blue)
        byte = await asyncio.to_thread(image.read)

        await self.bot.user.edit(avatar=byte)

        await asyncio.to_thread(image.close)

    @commands.Cog.listener("on_ready")
    async def on_ready_start_loop(self):
        self.change_status.start()
        self.change_avatar.start()

        print("Ready.")

async def setup(bot):
    await bot.add_cog(BadgeCog(bot))
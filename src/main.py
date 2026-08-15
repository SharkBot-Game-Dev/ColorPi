import asyncio
import traceback

from discord.ext import commands
import discord
import dotenv
import os

dotenv.load_dotenv()

intents = discord.Intents.none()
intents.guilds = True

async def load_cogs(bot: commands.Bot, base_folder="cogs"):
    tasks = []

    for root, _, files in os.walk(base_folder):
        for file in files:
            if file.endswith(".py") and not file.startswith("_"):
                full_path = os.path.join(root, file)
                relative_path = os.path.relpath(full_path, os.path.dirname(base_folder))

                module = relative_path.replace(os.sep, ".")[:-3]
                tasks.append(module)

    async def load_extension_safe(mod: str):
        try:
            await bot.load_extension(mod)
        except Exception as e:
            print(f"Failed to load {mod}: {e}")
            traceback.print_exc()

    if tasks:
        await asyncio.gather(*(load_extension_safe(mod) for mod in tasks))

class ColorPi(commands.Bot):
    def __init__(self):
        super().__init__("!", help_command=None, intents=intents)

    async def setup_hook(self):
        await load_cogs(self)

        await self.tree.sync()

bot = ColorPi()

bot.run(os.environ.get('DISCORD_TOKEN'))
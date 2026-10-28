from discord.ext import commands
import discord
from discord import app_commands
from PIL import Image
import io
import asyncio
import random

from tools import drawAvatar

class ColorCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        print("Init -> ColorCog")

    @app_commands.command(name="color", description="色から単色画像を作成します。", extras={"category": "🖌️色"})
    @app_commands.describe(color="16進数のrgbで指定")
    async def color_command(self, interaction: discord.Interaction, color: str):
        await interaction.response.defer()

        try:
            discord.Color.from_str(color)
        except:
            await interaction.followup.send(content="❌ 不正な色です。")
            return

        def draw():
            image = Image.new("RGBA", (500, 300), color)

            save = io.BytesIO()
            image.save(save, "png")
            save.seek(0)

            return save

        image = await asyncio.to_thread(draw)

        await interaction.followup.send(file=discord.File(image, filename="color.png"), content="✅ 作成しました。")

        await asyncio.to_thread(image.close)

    @app_commands.command(name="random", description="ランダム色から単色画像を作成します。", extras={"category": "🖌️色"})
    async def random_command(self, interaction: discord.Interaction):
        await interaction.response.defer()

        def draw():
            image = Image.new("RGB", (500, 300), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

            save = io.BytesIO()
            image.save(save, "png")
            save.seek(0)

            return save

        image = await asyncio.to_thread(draw)

        await interaction.followup.send(file=discord.File(image, filename="color.png"), content="✅ 作成しました。")

        await asyncio.to_thread(image.close)

    @app_commands.command(name="draw", description="このBotのアバターを描画します。", extras={"category": "🖌️色"})
    async def draw_command(self, interaction: discord.Interaction):
        await interaction.response.defer()

        red = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        green = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        blue = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        image = await asyncio.to_thread(drawAvatar.drawAvatar, red, green, blue)

        await interaction.followup.send(file=discord.File(image, filename="color.png"), content="✅ 描画しました。")

        await asyncio.to_thread(image.close)

async def setup(bot):
    await bot.add_cog(ColorCog(bot))
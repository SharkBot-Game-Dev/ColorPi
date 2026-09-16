from discord.ext import commands
import discord
from discord import app_commands

import random

class OmikujiCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        print("Init -> OmikujiCog")

    @app_commands.command(name="omikuji", description="おみくじを引きます。", extras={"category": "🤣楽しい"})
    async def omikuji_command(self, interaction: discord.Interaction):
        await interaction.response.defer()

        kuji = random.choice(["大吉", "中吉", "吉", "小吉", "末吉", "凶", "大凶"])
        color = random.choice(["❤️赤", "💙青", "🟢緑", "🟡黃", "🟪紫", "🤍白", "⚫黒", "🟤茶"])
        
        await interaction.followup.send(content=f"✅おみくじを引きしました。", embed=discord.Embed(color=discord.Color.random(), description=f"🥠引いたくじ: {kuji}\n🎨ラッキーカラー: {color}"))

async def setup(bot):
    await bot.add_cog(OmikujiCog(bot))
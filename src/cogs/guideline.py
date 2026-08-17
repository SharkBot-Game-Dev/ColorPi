from discord.ext import commands
import discord
from discord import app_commands

from tools import guidelineBuilder

class GuidelineCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        print("Init -> GuidelineCog")

    @app_commands.command(name="guideline", description="サーバーのルールパネルを作成します。")
    @app_commands.allowed_installs(guilds=True, users=False)
    @app_commands.describe(role="ルール同意後に付与するロール")
    @app_commands.checks.has_permissions(manage_roles=True)
    async def guideline_command(self, interaction: discord.Interaction, role: discord.Role):
        await interaction.response.send_modal(guidelineBuilder.GuidelineBuilder(role=role))

async def setup(bot):
    await bot.add_cog(GuidelineCog(bot))
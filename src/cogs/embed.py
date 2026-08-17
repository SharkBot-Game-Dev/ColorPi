from discord.ext import commands
import discord
from discord import app_commands

from tools import embedBuilder

class EmbedCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        print("Init -> EmbedCog")

    @app_commands.command(name="embed", description="埋め込みを作成します。", extras={"category": "✨その他"})
    @app_commands.allowed_installs(guilds=True, users=False)
    @app_commands.checks.has_permissions(manage_channels=True)
    async def embed_command(self, interaction: discord.Interaction):
        await interaction.response.send_modal(embedBuilder.EmbedBuilder())

async def setup(bot):
    await bot.add_cog(EmbedCog(bot))
import traceback
from discord.ext import commands
import discord

class ErrorHandleCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

        @bot.tree.error
        async def on_app_command_error(
            interaction: discord.Interaction,
            error: discord.app_commands.AppCommandError,
        ):
            if isinstance(error, discord.app_commands.CommandOnCooldown):
                e = 0
                return e

            if isinstance(error, discord.app_commands.CommandNotFound):
                e = 0
                return e

            if isinstance(error, discord.app_commands.MissingPermissions):
                if not interaction.response.is_done():
                    await interaction.response.send_message(
                        content="❌ 実行に必要な権限がありません。",
                        ephemeral=True,
                    )
                return

            traceback.print_exception(error)
            if not interaction.response.is_done():
                await interaction.response.send_message(
                    content="❌ 予期しないエラーが発生しました。",
                    ephemeral=True,
                )
            else:
                await interaction.followup.send(content="❌ 予期しないエラーが発生しました。")

async def setup(bot):
    await bot.add_cog(ErrorHandleCog(bot))
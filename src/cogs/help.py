import datetime

from discord.ext import commands
import discord
from discord import app_commands

class HelpCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        print("Init -> HelpCog")

    @app_commands.command(name="help", description="Botの使い方を表示します。", extras={"category": "✨その他"})
    async def help_command(self, interaction: discord.Interaction):
        await interaction.response.defer()

        embed = discord.Embed(color=discord.Color.random())

        commands_catrgory = {}

        for command in self.bot.tree.walk_commands():
            category = command.extras.get('category', '✨その他')
            if commands_catrgory.get(category):
                commands_catrgory[category].append(command)
            else:
                commands_catrgory[category] = []

        for key, value in commands_catrgory.items():
            cmd_texts = [cmd.name + f" ({cmd.description})" for cmd in value]
            if len(cmd_texts) != 1:
                embed.add_field(name=key, value="\n".join(cmd_texts), inline=False)
            else:
                embed.add_field(name=key, value=cmd_texts[0], inline=False)

        await interaction.followup.send(embed=embed)

async def setup(bot):
    await bot.add_cog(HelpCog(bot))
from discord.ext import commands
import discord
from discord import app_commands

from tools import guidelineBuilder

class GuidelineCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        print("Init -> GuidelineCog")

    @app_commands.command(name="guideline", description="サーバーのルールパネルを作成します。", extras={"category": "😀ロール"})
    @app_commands.allowed_installs(guilds=True, users=False)
    @app_commands.describe(role="ルール同意後に付与するロール")
    @app_commands.checks.has_permissions(manage_roles=True)
    async def guideline_command(self, interaction: discord.Interaction, role: discord.Role):
        await interaction.response.send_modal(guidelineBuilder.GuidelineBuilder(role=role))

    @commands.Cog.listener(name="on_interaction")
    async def on_interaction_guideline(self, interaction: discord.Interaction):
        try:
            if interaction.data["component_type"] == 2:
                try:
                    custom_id = interaction.data["custom_id"]
                except:
                    return
                if custom_id.startswith("guideline_"):
                    try:
                        await interaction.response.defer(ephemeral=True)
                        if (
                            interaction.guild.get_role(int(custom_id.split("_")[1]))
                            not in interaction.user.roles
                        ):
                            await interaction.user.add_roles(
                                interaction.guild.get_role(int(custom_id.split("_")[1]))
                            )
                            await interaction.followup.send(
                                "ルールに同意しました。", ephemeral=True
                            )
                        else:
                            await interaction.followup.send(
                                "すでに同意しています。", ephemeral=True
                            )

                        try:
                            new_embed = interaction.message.embeds[0].copy()
                            new_embed.color = discord.Color.random()
                            await interaction.message.edit(embed=new_embed)
                        except:
                            return
                    except discord.Forbidden:
                        await interaction.followup.send(
                            "付与したいロールの位置がColorPiのロールよりも\n上にあるため付与できませんでした。\nhttps://i.imgur.com/fGcWslT.gif",
                            ephemeral=True,
                        )
                    except:
                        await interaction.followup.send(
                            "追加に失敗しました。", ephemeral=True
                        )
        except:
            return

async def setup(bot):
    await bot.add_cog(GuidelineCog(bot))
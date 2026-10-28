from discord.ext import commands
import discord
from discord import app_commands

class PanelCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        print("Init -> PanelCog")

    @app_commands.command(name="panel", description="ロールパネルを作成します。", extras={"category": "😀ロール"})
    @app_commands.allowed_installs(guilds=True, users=False)
    @app_commands.describe(role_1="ロール1", role_2="ロール2", role_3="ロール3", role_4="ロール4", role_5="ロール5", title="ロールパネルのタイトル", description="ロールパネルの説明", button_only="ボタンだけを送信するか")
    @app_commands.checks.has_permissions(manage_roles=True)
    async def panel_command(self, interaction: discord.Interaction, role_1: discord.Role, role_2: discord.Role = None, role_3: discord.Role = None, role_4: discord.Role = None, role_5: discord.Role = None, title: str = "ロールパネル", description: str = "ボタンを押してロールを入手できます", button_only: bool = False):
        await interaction.response.defer()

        roles = [role_1, role_2, role_3, role_4, role_5]
        roles = [r for r in roles if r]

        view = discord.ui.View(timeout=None)
        for r in roles:
            view.add_item(discord.ui.Button(label=r.name, custom_id=f"role_{r.id}"))

        args = {
            "view": view,
        }

        if not button_only:
            args["embed"] = discord.Embed(title=title, color=discord.Color.green(), description=description)

        await interaction.channel.send(**args)

        await interaction.delete_original_response()

    @commands.Cog.listener(name="on_interaction")
    async def on_interaction_panel(self, interaction: discord.Interaction):
        try:
            if interaction.data["component_type"] == 2:
                try:
                    custom_id = interaction.data["custom_id"]
                except:
                    return
                if custom_id.startswith("role_"):
                    try:
                        await interaction.response.defer(ephemeral=True)

                        roles = [r.id for r in interaction.user.roles]

                        if (
                            int(custom_id.split("_")[1])
                            not in roles
                        ):
                            await interaction.user.add_roles(
                                interaction.guild.get_role(int(custom_id.split("_")[1]))
                            )
                            await interaction.followup.send(
                                "ロールを追加しました。", ephemeral=True
                            )
                        else:
                            await interaction.user.remove_roles(
                                interaction.guild.get_role(int(custom_id.split("_")[1]))
                            )
                            await interaction.followup.send(
                                "ロールを剥奪しました。", ephemeral=True
                            )
                    except discord.Forbidden:
                        await interaction.followup.send(
                            "付与したいロールの位置がColorPiのロールよりも\n上にあるため付与できませんでした。\nhttps://i.imgur.com/fGcWslT.gif",
                            ephemeral=True,
                        )
                    except Exception:
                        await interaction.followup.send(
                            "追加に失敗しました。", ephemeral=True
                        )
        except:
            return

async def setup(bot):
    await bot.add_cog(PanelCog(bot))
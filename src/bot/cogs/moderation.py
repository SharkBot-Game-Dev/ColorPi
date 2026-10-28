import datetime

from discord.ext import commands
import discord
from discord import app_commands

class ModerationCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        print("Init -> ModerationCog")

    @app_commands.command(name="clear", description="このチャンネルのメッセージを削除します。", extras={"category": "🔨モデレーション"})
    @app_commands.describe(count="指定した分削除します。", user="指定したユーザーのメッセージを削除します。")
    @app_commands.allowed_installs(guilds=True, users=False)
    @app_commands.checks.has_permissions(manage_channels=True)
    async def clear_command(self, interaction: discord.Interaction, count: int, user: discord.User = None):
        await interaction.response.defer()

        now = discord.utils.utcnow()
        two_weeks = datetime.timedelta(days=14)

        def check(msg: discord.Message):
            if (now - msg.created_at) > two_weeks:
                return False
            if user is not None and msg.author.id != user.id:
                return False
            return True

        try:
            deleted = await interaction.channel.purge(limit=count + 1, check=check)

            await interaction.channel.send(content=f"✅️ メッセージを{len(deleted) - 1}個削除しました。\n-# このメッセージは10秒後に削除されます。", delete_after=10)
        except:
            await interaction.user.send(content=f"❌ {interaction.channel.mention}にBotがアクセスできません。")
            return

    @app_commands.command(name="slowmode", description="チャンネルに低速モードを指定します。", extras={"category": "🔨モデレーション"})
    @app_commands.describe(seconds="指定した秒の低速モードを指定できます。")
    @app_commands.allowed_installs(guilds=True, users=False)
    @app_commands.checks.has_permissions(manage_channels=True)
    async def slowmode_command(self, interaction: discord.Interaction, seconds: int = 0):
        await interaction.response.defer()

        try:
            await interaction.channel.edit(slowmode_delay=seconds)
        except:
            await interaction.followup.send(content="❌ 設定に失敗しました。")
            return

        await interaction.followup.send(content=f"✅ {seconds}秒の低速モードを指定しました。")

    @app_commands.command(name="lock", description="チャンネルでの発言権限を剥奪します。", extras={"category": "🔨モデレーション"})
    @app_commands.allowed_installs(guilds=True, users=False)
    @app_commands.checks.has_permissions(manage_channels=True)
    async def lock_command(self, interaction: discord.Interaction):
        await interaction.response.defer()

        try:
            overwrite = interaction.channel.overwrites_for(interaction.guild.default_role)
            overwrite.send_messages = False
            overwrite.create_polls = False
            overwrite.use_application_commands = False
            overwrite.attach_files = False
            overwrite.create_public_threads = False
            overwrite.create_private_threads = False
            overwrite.add_reactions = False
            await interaction.channel.set_permissions(
                interaction.guild.default_role, overwrite=overwrite
            )
        except:
            await interaction.followup.send(content="❌ ロックに失敗しました。")
            return

        await interaction.followup.send(content=f"✅ チャンネルで発言できなくしました。")

    @app_commands.command(name="unlock", description="チャンネルで発言できるようにします。", extras={"category": "🔨モデレーション"})
    @app_commands.allowed_installs(guilds=True, users=False)
    @app_commands.checks.has_permissions(manage_channels=True)
    async def unlock_command(self, interaction: discord.Interaction):
        await interaction.response.defer()

        try:
            overwrite = interaction.channel.overwrites_for(interaction.guild.default_role)
            overwrite.send_messages = True
            overwrite.create_polls = True
            overwrite.use_application_commands = True
            overwrite.attach_files = True
            overwrite.create_public_threads = True
            overwrite.create_private_threads = True
            overwrite.add_reactions = True
            await interaction.channel.set_permissions(
                interaction.guild.default_role, overwrite=overwrite
            )
        except:
            await interaction.followup.send(content="❌ ロック解除に失敗しました。")
            return

        await interaction.followup.send(content=f"✅ チャンネルで発言できるようにしました。")

async def setup(bot):
    await bot.add_cog(ModerationCog(bot))
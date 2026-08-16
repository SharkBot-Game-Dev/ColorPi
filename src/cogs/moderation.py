import datetime

from discord.ext import commands
import discord
from discord import app_commands

class ModerationCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        print("Init -> ModerationCog")

    @app_commands.command(name="clear", description="このチャンネルのメッセージを削除します。")
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

            await interaction.channel.send(content=f"✅️ メッセージを{len(deleted) + 1}個削除しました。\n-# このメッセージは10秒後に削除されます。", delete_after=10)
        except:
            await interaction.user.send(content=f"❌ {interaction.channel.mention}にBotがアクセスできません。")
            return

async def setup(bot):
    await bot.add_cog(ModerationCog(bot))
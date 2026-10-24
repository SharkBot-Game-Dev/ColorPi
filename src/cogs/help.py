import datetime

from discord.ext import commands
import discord
from discord import app_commands

class HelpCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        print("Init -> HelpCog")

    @app_commands.command(name="help", description="Botのコマンドを表示します。", extras={"category": "✨その他"})
    async def help_command(self, interaction: discord.Interaction):
        await interaction.response.defer()

        category_map = {}
        for command in self.bot.tree.get_commands(type=discord.AppCommandType.chat_input):
            cat = command.extras.get('category', '✨その他')
            if cat not in category_map:
                category_map[cat] = []
            category_map[cat].append(command)

        pages = []
        COMMANDS_PER_PAGE = 4
        command_page = 0
        command_count = 0

        for cat_name, cmds in category_map.items():
            if command_count > COMMANDS_PER_PAGE:
                command_page += 1
                command_count = 0
            pages.append({
                "category": cat_name,
                "commands": cmds,
                "page": command_page
            })

        if not pages:
            await interaction.followup.send("表示できるコマンドがありません。")
            return

        total_pages = len(pages)

        class HelpView(discord.ui.LayoutView):
            def __init__(self, *, timeout = 180):
                super().__init__(timeout=timeout)

                self.build_help_container(0)

                self.page = 0

            res_text = discord.ui.TextDisplay(f"✅ Botのコマンドを表示しました。")

            container = discord.ui.Container(accent_color=discord.Color.random())

            async def back_button(self, interaction_button: discord.Interaction):
                if interaction.user.id != interaction_button.user.id:
                    await interaction.response.send_message(content="❌️ これはあなたのボタンではありません。")
                    return
                if self.page > 0:
                    self.page -= 1
                self.build_help_container(self.page)
                await interaction_button.message.edit(view=self)

            async def next_button(self, interaction_button: discord.Interaction):
                if interaction.user.id != interaction_button.user.id:
                    await interaction.response.send_message(content="❌️ これはあなたのボタンではありません。")
                    return
                if self.page < total_pages - 1:
                    self.page += 1
                self.build_help_container(self.page)
                await interaction_button.message.edit(view=self)

            def build_help_container(self, page: int):
                self.container.clear_items()

                for page in pages:
                    if page["page"] != page:
                        continue
                    cat_name = page["category"]
                    cmds = page["commands"]

                    cmd_list_str = "\n".join([f"`/{cmd.name}` - {cmd.description}" for cmd in cmds])

                    text_display = discord.ui.TextDisplay(content=f"## {cat_name}\n" + cmd_list_str)
                    self.container.add_item(text_display)

                backbutton = discord.ui.Button(label="⬅️")
                backbutton.callback = self.back_button
                nextbutton = discord.ui.Button(label="➡️")
                nextbutton.callback = self.next_button
                self.container.add_item(discord.ui.ActionRow(backbutton, nextbutton))

        await interaction.followup.send(view=HelpView())

async def setup(bot):
    await bot.add_cog(HelpCog(bot))
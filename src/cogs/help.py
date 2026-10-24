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

        commands_catrgory = {}
        page_count = 0
        page_category = 0
        
        for command in self.bot.tree.get_commands(type=discord.AppCommandType.chat_input):
            if page_count > 3:
                page_count = 0
                page_category += 1
            category = command.extras.get('category', '✨その他')
            if isinstance(commands_catrgory.get(category), list):
                commands_catrgory[category + f"_{page_category}"].append(command)
            else:
                commands_catrgory[category + f"_{page_category}"] = [command]
            page_count += 1

        class HelpView(discord.ui.LayoutView):
            def __init__(self, *, timeout = 180):
                super().__init__(timeout=timeout)

                self.build_help_container(0)

                self.page = 0

            res_text = discord.ui.TextDisplay("✅ Botのコマンドを表示しました。")

            container = discord.ui.Container(accent_color=discord.Color.random())

            async def back_button(self, interaction_button: discord.Interaction):
                if interaction.user.id != interaction_button.user.id:
                    await interaction.response.send_message(content="❌️ これはあなたのボタンではありません。")
                    return
                if self.page < page_category:
                    self.page = page_category
                self.build_help_container(self.page)
                await interaction_button.message.edit(view=self)

            async def next_button(self, interaction_button: discord.Interaction):
                if interaction.user.id != interaction_button.user.id:
                    await interaction.response.send_message(content="❌️ これはあなたのボタンではありません。")
                    return
                if self.page > page_category:
                    self.page = 0
                self.build_help_container(self.page)
                await interaction_button.message.edit(view=self)

            def build_help_container(self, page: int):
                self.container.clear_items()

                for key, value in commands_catrgory.items():
                    if not key.endswith(f"_{page}"):
                        continue

                    clean_key = key.split("_")[0]

                    cmd_texts = [f"`{cmd.name}`" + f" ({cmd.description})" for cmd in value]
                    if len(cmd_texts) != 1:
                        text_display = discord.ui.TextDisplay(content=f"### {clean_key}\n" + "\n".join(cmd_texts))
                    else:
                        text_display = discord.ui.TextDisplay(content=f"### {clean_key}\n{cmd_texts[0]}")
                    self.container.add_item(text_display)

                backbutton = discord.ui.Button(label="⬅️")
                backbutton.callback = self.back_button
                nextbutton = discord.ui.Button(label="➡️")
                nextbutton.callback = self.next_button
                self.container.add_item(discord.ui.ActionRow(backbutton, nextbutton))

        await interaction.followup.send(view=HelpView())

async def setup(bot):
    await bot.add_cog(HelpCog(bot))
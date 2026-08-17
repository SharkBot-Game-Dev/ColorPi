import discord

class GuidelineBuilder(discord.ui.Modal):
    def __init__(self, role: discord.Role):
        super().__init__(title="サーバールールを設定する", timeout=180)

        self.rule = discord.ui.TextInput(label="ルール", style=discord.TextStyle.long, required=True)
        self.add_item(self.rule)

        self.role = role

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)

        embed = discord.Embed(title="このサーバーのルールに同意する必要があります。", description=self.rule.value, color=discord.Color.random())
        if interaction.guild.icon:
            embed.set_thumbnail(url=interaction.guild.icon.url)

        embed.set_footer(
            text="Discord コミュニティガイドライン も忘れないようにして下さい。"
        )
        
        view = discord.ui.View(timeout=None)
        view.add_item(discord.ui.Button(label="同意します", style=discord.ButtonStyle.success, custom_id=f"guideline_{self.role.id}"))

        try:
            await interaction.channel.send(embed=embed, view=view)
        except:
            await interaction.followup.send(content="❌ 送信に失敗しました。")
            return
import discord

class EmbedBuilder(discord.ui.Modal):
    def __init__(self):
        super().__init__(title="埋め込みを作成する", timeout=180)

        self.embed_title = discord.ui.TextInput(label="タイトル", style=discord.TextStyle.short, required=True)
        self.add_item(self.embed_title)

        self.embed_description = discord.ui.TextInput(label="説明", style=discord.TextStyle.long, required=True)
        self.add_item(self.embed_description)

        self.embed_image_url = discord.ui.TextInput(label="画像URL", style=discord.TextStyle.short, required=False)
        self.add_item(self.embed_image_url)

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.defer(ephemeral=True)

        embed = discord.Embed(title=self.embed_title.value, description=self.embed_description.value)
        if self.embed_image_url.value:
            embed.set_image(url=self.embed_image_url.value)

        embed.set_footer(text=interaction.guild.name, icon_url=interaction.guild.icon.url if interaction.guild.icon else interaction.user.default_avatar.url)

        try:
            await interaction.channel.send(embed=embed)
        except:
            await interaction.followup.send(content="❌ 送信に失敗しました。")
            return
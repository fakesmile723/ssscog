from redbot.core import commands
import discord

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def sss(self, ctx):
        embed = discord.Embed(title="Button Demo", description="Click a button to perform an action", color=discord.Color.blue())

        role_button = discord.ui.Button(style=discord.ButtonStyle.primary, label="Assign Role", emoji="✅")
        role_button.callback = self.assign_role_callback

        message_button = discord.ui.Button(style=discord.ButtonStyle.primary, label="Send Ephemeral Message", emoji="📬")
        message_button.callback = self.send_ephemeral_message_callback

        action_row = discord.ui.ActionRow()
        action_row.add_button(role_button)
        action_row.add_button(message_button)

        await ctx.send(embed=embed, components=[action_row])

    async def assign_role_callback(self, interaction: discord.Interaction, button: discord.ui.Button, user: discord.User):
        role_id = 959146966892298302

        role = interaction.guild.get_role(role_id)
        if role:
            await user.add_roles(role)

        button.disabled = True
        await interaction.response.edit_message(embed=interaction.message.embeds[0], view=interaction.message.view)

    async def send_ephemeral_message_callback(self, interaction: discord.Interaction, button: discord.ui.Button, user: discord.User):
        await user.send("This is an ephemeral message.", ephemeral=True)

        button.disabled = True
        await interaction.response.edit_message(embed=interaction.message.embeds[0], view=interaction.message.view)

def setup(bot):
    bot.add_cog(MyCog(bot))

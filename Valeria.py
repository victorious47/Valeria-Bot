import discord
from discord import app_commands
import base64

# Enable privileged intents
intents = discord.Intents.default()
intents.message_content = True

# Define bot
class MyBot(discord.Client):
    def __init__(self):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def on_ready(self):
        print(f'Logged in as {self.user}')
        await self.tree.sync()  # Sync commands with Discord

bot = MyBot()

@bot.tree.command(name="base64encode", description="Encode text to Base64")
async def base64_encode(interaction: discord.Interaction, text: str):
    encoded_text = base64.b64encode(text.encode()).decode()
    await interaction.response.send_message(f'Encoded: `{encoded_text}`', ephemeral=True)

@bot.tree.command(name="base64decode", description="Decode Base64 text")
async def base64_decode(interaction: discord.Interaction, text: str):
    try:
        decoded_text = base64.b64decode(text.encode()).decode()
        await interaction.response.send_message(f'Decoded: `{decoded_text}`', ephemeral=True)
    except Exception as e:
        await interaction.response.send_message(f'Error: {str(e)}', ephemeral=True)

# Run the bot
TOKEN = "MTM0MTY2MjU5NzYyNzM3OTcxMg.GUNlZo.Bvkvvt92Ukx_J1lXBguyM8wPho9zg44ZWaB4UE"
bot.run(TOKEN)

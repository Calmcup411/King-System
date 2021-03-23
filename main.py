import discord
client = discord.Client()

@client.event
async def on_ready():
    print("on_ready")
    print(discord.__version__)

client.run("あなたのbotのトークン")

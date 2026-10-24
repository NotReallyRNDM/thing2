
import os
import discord
from dotenv import load_dotenv
from discord.ext import tasks
from datetime import date, datetime
now = datetime.now()





load_dotenv("discordtoken2.env")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

CHANNEL_ID = 1277519826465587253  




@client.event
async def on_ready():
    print(f"Logged in as {client.user}")



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if client.user in message.mentions:
        await message.channel.send(f"Hey {message.author.mention}, you pinged me!")

    elif message.content == "h":
        await message.channel.send("<@1022723519462776892>")

    elif message.content == "time":
        await message.channel.send(datetime.now().strftime("%H:%M:%S"))

    elif message.content == "date":
        await message.channel.send(datetime.now().strftime("%d-%m-%Y"))

    elif message.content.startswith("since"):
        text = message.content[6:].strip()
        try:
            then = datetime.strptime(text, "%d-%m-%Y").date()
        except ValueError:
            await message.channel.send("Use: `since 01-10-2026`")
        else:
            days = (date.today() - then).days
            await message.channel.send(f"{days} days since {then}")


client.run(os.getenv("DISCORD_TOKEN"))

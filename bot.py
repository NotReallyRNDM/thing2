


import os
import discord
import asyncio
from dotenv import load_dotenv
from discord.ext import tasks
from datetime import date, datetime, timedelta
now = datetime.now()






load_dotenv("discordtoken.env")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

pending = []
async def send_reminder(channel, user, minutes, text, entry):
    await asyncio.sleep(minutes * 60)
    pending.remove(entry)
    await channel.send(f"{user.mention} reminder: {text}")



@client.event 
async def on_ready():
    print(f"Logged in as {client.user}")



@client.event
async def on_message(message):
    if message.author == client.user:
        return


    if client.user in message.mentions:
        await message.channel.send(f"Hey {message.author.mention}, you pinged me!")

    
    if message.content == "h":
        await message.channel.send("<@1022723519462776892>")

    elif message.content == "angry":
        await message.channel.send("aww don't be so angry- Try yelling at Paull instead")

    elif message.content == "william":
        await message.channel.send("you mean billy??")

    elif message.content == "yea mb":
        await message.channel.send(" yes good boy")

    elif message.content == "excuse me??": 
        await message.channel.send("yea you heard me")

    elif message.content == "igb": 
        await message.channel.send(" <3")

    elif message.content == "meow":
        await message.channel.send("meow to you too m' dear")

    elif message.content == "um":
        await message.channel.send("indecisive")

    elif message.content == "umm":
        await message.channel.send("indecisive")

    elif message.content == "ummm":
        await message.channel.send("indecisive")

    elif message.content == "hi":
        await message.channel.send("oh to me? hii")

    elif message.content == "no stupid":
        await message.channel.send("oh.. okay. well. i guess i'll just go cry in the corner then")

    elif message.content == "gm":
        await message.channel.send("it's too early go away ")

    elif message.content == "gn":
        await message.channel.send("shut up and go to sleep alr idc abt your wishes to us")

    elif message.content == "not you, bot":
        await message.channel.send("yea okay. i know. i just wanted to say hi. but if you don't want me to, then i won't. i'll just go cry in the corner now")

    elif message.content == "celina":
        await message.channel.send("who's that")

    elif message.content == "idk why amI asing a bot":
        await message.channel.send("you dumb")

    elif message.content == "ily":
        await message.channel.send("ew.....    I sure don't love that person")

    elif message.content == "time":
        await message.channel.send(now.strftime("%I:%M %p"))
        await message.channel.send(now.strftime("%Y-%m-%d %H:%M:%S"))
        await message.channel.send(now.strftime("%A, %d %B %Y"))


    elif message.content == "gmm":
        await message.channel.send("go away")








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








    elif message.content.startswith("alarm "):
        parts = message.content.split(" ", 2)
        if len(parts) < 3 or not parts[1].isdigit():
            await message.channel.send("bad syntax try 'alarm 60 pika' in minutes")
        else:
            minutes = int(parts[1])
            text = parts[2]
            due = datetime.now() + timedelta(minutes=minutes)
            entry = (message.author.id, due, text)
            pending.append(entry)
            await message.channel.send(f"alarm in {minutes} minutes")
            asyncio.create_task(
                send.reminder(message.channel, message.author, minutes, text, entry)
            )            


    elif message.content == "reminders":
        mine = [e for e in pending if e[0] == message.author.id]
        if not mine:
            await message.channel.send("You have no alarms set.")
        else:
            lines = [f"- {e[2]} (at {e[1].strftime('%H:%M')})" for e in mine]
            await message.channel.send("\n".join(lines))







    elif message.content == "":
        await message.channel.send("")

    elif message.content == "":
        await message.channel.send("")

    elif message.content == "":
        await message.channel.send("")

    elif message.content == "":
        await message.channel.send("")

    elif message.content == "":
        await message.channel.send("")

    elif message.content == "":
        await message.channel.send("")

    elif message.content == "":
        await message.channel.send("")

    elif message.content == "":
        await message.channel.send("")

    elif message.content == "":
        await message.channel.send("")

    elif message.content == "":
        await message.channel.send("")

    elif message.content == "":
        await message.channel.send("")

    elif message.content == "":
        await message.channel.send("")

client.run(os.getenv("DISCORD_TOKEN"))



































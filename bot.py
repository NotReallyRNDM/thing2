#
'''
git add bot2.py
git commit -m "describe what you changed"
git push

'''
#

import os
import discord
import asyncio
import random
import io
from PIL import Image, ImageDraw, ImageFont
from discord import app_commands
from dotenv import load_dotenv
from discord.ext import tasks
from datetime import date, datetime, timedelta







load_dotenv("discordtoken.env")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

pending = []
async def send_reminder(channel, user, minutes, text, entry):
    await asyncio.sleep(minutes * 60)
    pending.remove(entry)
    await channel.send(f"{user.mention} reminder: {text}")



@client.event 
async def on_ready():
    await tree.sync()
    print(f"Logged in as {client.user}")

counting = False
counting2 = False

@client.event
async def on_message(message):
    if message.author == client.user:
        return



#Random message reactions of messages from message writing people 

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

    elif message.content == "go cry":
        await message.channel.send("I hate you too dim sum dumdum")

    elif message.content == "67":
        await message.channel.send("67 in the big 26😭")

    elif message.content == "rat":
        await message.channel.send(random.choice(["olivia?","john smith","not a fan"]))

    elif message.content == "yay":
        await message.channel.send("yay-ER BEAT THAT LURKLITE")

    elif message.content == "ily":
        await message.channel.send("ew.....    \nI sure don't love that person")

    elif message.content == "gmm":
        await message.channel.send("go away")

    elif message.author.id == 776947006237179934:
        await message.channel.send("-# meow")   

    elif message.content == "aww":
        await message.channel.send("computer analysis deems this is the best possible move as it sets up for the greatest follow up play of decagonal. nigel made no bingoes but his game was utterly genius an amazing understanding of board dynamics and endgame stratergy are unmatched. This game between Joey Mallick and Nigel Richards definitely stands out as one of the most impressive games of scrabble history.")

    elif message.content == "don't spam":
        await message.channel.send("spam")

    elif message.content == "shut up":
        await message.channel.send("how 'bout you shut up :I")

    elif message.content == "dte":
        await message.channel.send("stakeholder commented on the potential difficulty one might have in installing the filament hinge due to high friction between the hinges and the curve of the filament itself. This comment led to my adding of a fillet to every face on one side of the hinge such that the filament would guide itself into the hole. The same stakehoder commented on when after the tracks were assembled the same stakeholder expressesd that the tracks' hinge ends need to be hidden to look good. It's current state of an overhaning and bent filament, the stakeholder fonund to be unacceptable")   

    elif message.content == "":
        await message.channel.send("")







#Date and time stuff

    elif message.content == "now":
        now = datetime.now()
        await message.channel.send(now.strftime("%I:%M %p"))
        await message.channel.send(now.strftime("%Y-%m-%d %H:%M:%S"))
        await message.channel.send(now.strftime("%A, %d %B %Y"))

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






#Kinda useless but was like kinda fun  time counting magic import thingy

    elif message.content.startswith("alarm "):
        parts = message.content.split(" ", 2)
        if len(parts) < 3 or not parts[1].isdigit():
            await message.channel.send("bad syntax try 'alarm 60 message' in minutes")
        else:
            minutes = int(parts[1])
            text = parts[2]
            due = datetime.now() + timedelta(minutes=minutes)
            entry = (message.author.id, due, text)
            pending.append(entry)
            await message.channel.send(f"alarm in {minutes} minutes")
            asyncio.create_task(
                send_reminder(message.channel, message.author, minutes, text, entry)
            )            


    elif message.content == "reminders":
        mine = [e for e in pending if e[0] == message.author.id]
        if not mine:
            await message.channel.send("You have no alarms set.")
        else:
            lines = [f"- {e[2]} (at {e[1].strftime('%H:%M')})" for e in mine]
            await message.channel.send("\n".join(lines))




#Hehe other people's discord account public info and avatar pic as a square!

    elif message.content.startswith("userinfo"):
        if message.mentions:
         user = message.mentions[0]


        await message.channel.send(
            f"**User Info**\n"
            f"Username: {user.name}\n"
            f"Display name: {user.display_name}\n"
            f"User ID: {user.id}\n"
            f"Bot account: {user.bot}\n"
            f"Account created: {user.created_at.strftime('%d/%m/%Y')}\n"
            f"Profile picture: {user.display_avatar.url}\n"
            f"Nick: {user.nick}\n"
        )
        

    elif message.content.startswith ("roles"):
        if message.mentions:
            user = message.mentions[0]

            roles = [role.name for role in user.roles
                    if role.name != "@everyone"]

            if roles:
                await message.channel.send(
                    f"{user.display_name}'s roles:d\n"+ "\n".join(roles)
                )
            else:
                await message.channel.send(f"{user.display_name} has no roles")
                
        else:
                await message.channel.send("do roles @someone" )



#MATHS WITH AN S HAHAHAHHAHAHAH Learning python hurts.

    elif message.content.startswith("do"):
        maths = message.content.split(" ", 1)[1]

        try:
            ans = eval(maths)     



            response = random.choice([
                "stop asking, it's",
                "urlgh I just woke up :I maths now?? it's",
                "",
                "nahh~~ \n \n \n \n \n jk it's ",
                "it's not not not not not not",
                "ok geez, rude~~ it's"
            ])

            await message.channel.send(f"{response} {ans}")

        except maths:
            await message.channel.send("error")




#DICE?? GAMBILGING HEHEHEHE NO. Yay random stuff that's like simpler than I thought    

    elif message.content == "dice":
        A =  random.randint(1, 6)
        await message.channel.send(A)

    elif message.content.startswith("roll "):
        C = int(message.content.split(" ")[1])
        B = random.randint(1, C)
        await message.channel.send(B)


#bascially spam icl

    global counting

    if message.content == "break":
        counting = False
        await message.channel.send("counting has stopped")

    elif message.content.startswith("count to "):
        E = int(message.content.split(" ")[2])
        counting = True
    

        for F in range(1, E + 1):
            if not counting:
                break

            await message.channel.send(F)


    global counting2

    if message.content == "break":
        counting2 = False
        await message.channel.send("counting has stopped")

    elif message.content.startswith("count from "):
        G = int(message.content.split(" ")[2])
        counting2 = True
    

        for G in range(G, 0, -1):
            if not counting2:
                break

            await message.channel.send(G)







#woah so that's how they do /commands

@tree.command(name="hello", description="Make bot say hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"hi<@{interaction.user.id}>")







@tree.command(name="cat", description="Make bot say meow")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("meow~~\n \n just like <@776947006237179934>")

    








@tree.command(name="countdown", description="Count down from a number")
async def countdown(interaction: discord.Interaction, number: int):
    
    await interaction.response.send_message(
        f"Counting down from {number}..."
    )

    for i in range(number, 0, -1):
        await interaction.followup.send(str(i))
        await asyncio.sleep(0.2)











###
#yg
#
#yay 
#actually cool gif thing better than thingy thing on googley doohley do


@tree.command(
    name = "gifmaker",
    description = "make into a gif")

@app_commands.describe(
    frame1="first png",
    frame2="second png",
    duration="ms per frame 30-2000 | leave blank is 600ms",
    top_text="text on image top",
    bottom_text="text on image bottom",
    coloura="hex a | leave blank is 255",
    colourb="hex b | leave blank is 255",
    colourc="hex c | leave blank is 255",
    size2="font size (60 is good | leave blank is 60)",
    background2="thickness of text background | leave blank = 30"

)

async def gifmaker(
    interaction: discord.Interaction, 
    frame1: discord.Attachment,
    frame2: discord.Attachment,
    duration: app_commands.Range[int, 30, 2000] = 600,
    top_text: str = "",
    bottom_text: str = "",
    coloura: app_commands.Range[int, 0, 255] = 255,
    colourb: app_commands.Range[int, 0, 255] = 255,
    colourc: app_commands.Range[int, 0, 255] = 255,
    size2: app_commands.Range[int, 1, 400] = 60,
    background2: app_commands.Range[int, 1, 500] = 30
):
    await interaction.response.defer()

    try:
        frames = []

        for attachment in (frame1, frame2):
            data = await attachment.read()

            with Image.open(io.BytesIO(data)) as image:
                frames.append(image.convert("RGBA").copy())


        width, height = frames[0].size

        frames = [
            image.resize((width, height)) 
            for image in frames]

        try:
            font = ImageFont.truetype(
                "C:/Windows/Fonts/arial.ttf", size2 #rip linux
            )
        except OSError:
            font = ImageFont.load_default()

        for image in frames:
            draw = ImageDraw.Draw(image)

            width, height = image.size

            if top_text:
                draw.text(
                    (width //2, 40),
                    top_text,
                    font=font,
                    fill=(coloura, colourb, colourc),
                    stroke_width=background2,
                    stroke_fill=(0,0,0),
                    anchor="mt"
                )

            if bottom_text:
                draw.text(
                    (width //2, height -40),
                    bottom_text,
                    font=font,
                    fill=(coloura, colourb, colourc),
                    stroke_width=background2,
                    stroke_fill=(0,0,0),
                    anchor="mb"
                )



#tp
        gif_frames = [
            image.convert("P", palette=Image.Palette.ADAPTIVE)
            for image in frames

        ]



        output = io.BytesIO()

        gif_frames[0].save(
            output, 
            format="gif",
            save_all=True,
            append_images=gif_frames[1:],
            duration=duration,
            loop=0,
            disposal=2

        )

        output.seek(0)

        await interaction.followup.send(
            file=discord.File(output, filename="wowitsa.gif")
        )

    except Exception as error:
        await interaction.followup.send("error")

    


client.run(os.getenv("DISCORD_TOKEN"))

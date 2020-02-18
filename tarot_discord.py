#tarrot
import routes
#discord
import asyncio
import discord
from discord.ext.commands import Bot
#random delay
import time
import random
#setup

TOKEN = "<DISCORD TOKEN HERE>"

client = discord.Client()
BOT_PREFIX = ("!")
#
descp = "Tarot BOT for discord./n Based on: https://github.com/jeremytarling/python-tarot "
#

client = Bot(command_prefix=BOT_PREFIX, description = descp)

@client.event
async def on_ready():
    game = discord.Game("tarot")
    discord.Colour.blurple()
    await client.change_presence(status=discord.Status.idle, activity=game)
    print("Logged in as %s" %(client.user.name))
        
@client.command()
async def tarot(context):   
    user = context.message.author.mention
    cmd_string = context.message.content
    try:
        num = abs(int(cmd_string[-1]))
    except ValueError:
        num = 1
    if num > 3:
        await context.send("%s Max 3 cards!" %(user))
    else:    
        hand = routes.max_cards(num)
        for card in range(num):
            is_rev = hand[card][1]
            if is_rev == -1:
                name = (hand[card][0]["name"] + " reversed")
                desc = hand[card][0]["rdesc"]      
            else:
                name = hand[card][0]["name"]
                desc = hand[card][0]["desc"]
            await context.send("%s : **%s** *%s*"%(user,name,desc))    
            time.sleep(random.randrange(1, 9))
        
client.run(TOKEN)

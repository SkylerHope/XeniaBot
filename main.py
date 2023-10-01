import discord
import os
import asyncio
import random
from dotenv import load_dotenv
intents = discord.Intents.all()
intents.members = True
intents.message_content = True
intents.presences = True
intents.guilds = True
intents.messages = True

#Declare bot
bot = discord.Bot(intents = intents)

#Bot activity
@bot.event
async def on_ready():
    await bot.change_presence(status = discord.Status.do_not_disturb, activity = discord.Game(name = "Dota 2"))
    print("Bot {0.user} is running...".format(bot))

#Run bot <--Always keep that at the end-->
load_dotenv
bot.run(os.getenv('TOKEN'))
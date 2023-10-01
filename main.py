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


# <----COMMANDS---->
@bot.slash_command(name = 'patchnotes', description = 'See what changed with the new update')
async def self(ctx: discord.ApplicationContext):
    patchnotes_embed = discord.Embed(title = 'Patch Notes 1.0', color = discord.Color.random())
    patchnotes_embed.add_field(name = 'App just launched', value = 'This is the launch (first) version of Xenia', inline = False)
    patchnotes_embed.set_thumbnail(url = "https://i.ibb.co/6YdkfgB/836b6427b9d3ff4c.png")
    await ctx.respond(embed = patchnotes_embed)


#Run bot <--Always keep that at the end-->
load_dotenv
bot.run(os.getenv('TOKEN'))
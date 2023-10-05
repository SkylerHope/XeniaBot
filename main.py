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

#Patch notes
@bot.slash_command(name = 'patchnotes', description = 'See what changed with the new update')
async def self(ctx: discord.ApplicationContext):
    patchnotes_embed = discord.Embed(title = 'Patch Notes 1.0', color = discord.Color.random())
    patchnotes_embed.add_field(name = 'App just launched', value = 'This is the launch (first) version of Xenia', inline = False)
    patchnotes_embed.set_thumbnail(url = "https://i.ibb.co/6YdkfgB/836b6427b9d3ff4c.png")
    await ctx.respond(embed = patchnotes_embed)

#Say
@bot.slash_command(name = 'say', description = 'Make Xenia say something')
async def say(ctx: discord.ApplicationContext, *, text):
    async with ctx.typing():
        await asyncio.sleep(0.7)
        await ctx.send(text)

#Announcement
@bot.slash_command(name = 'announcement', description = 'Make Xenia create a simple announcement')
@discord.default_permissions(administrator = True)
async def announce(ctx: discord.ApplicationContext):
    await ctx.respond('Answer the following questions (20 mins left)')
    
    questions = ["Announcement title: ", "Short description: ", "Detailed title: ", "Detailed description: ", "Mention the target channel: "]
    replies = []

    def check(user):
        return user.author == ctx.author and user.channel == ctx.channel
    
    for question in questions:
        await ctx.send(question)
        try:
            msg = await bot.wait_for('message', timeout = 1200, check = check)
        except asyncio.TimeoutError:
            await ctx.send("Ran out of time, try again!")
            return
        else:
            replies.append(msg.content)

    main_title = replies[0]
    short_desc = replies[1]
    field_title = replies[2]
    field_desc = replies[3]
    channel_id = int(replies[4][2:-1])
    channel = bot.get_channel(channel_id)

    announcement_embed = discord.Embed(title = main_title, description = short_desc, color = discord.Color.random())
    announcement_embed.add_field(name = field_title, value = field_desc, inline = False)
    announcement_embed.set_thumbnail(url = ctx.guild.icon)

    await channel.send(embed = announcement_embed)
    await ctx.respond("Done! Go check your new announcement!")



#Run bot <--Always keep that at the end-->
load_dotenv
bot.run(os.getenv('TOKEN'))
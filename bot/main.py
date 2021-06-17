import discord
from discord.ext import commands
from discord.ext.commands import Bot
import os
c
import random
import asyncio
import time
import requests
import sys
sys.path.append('./tokenforbot')
import bottoken
bot = commands.Bot(command_prefix='Mint ', status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.listening, name='Lofi Coding playlist'))
bot.remove_command('help')

@bot.event
async def on_ready():
    print('Connected to bot: {}'.format(bot.user.name))
    print('Bot ID: {}'.format(bot.user.id))

@bot.command()
async def help(ctx):
    await ctx.channel.send("Hi, im Mint!")

@bot.command()
async def hello(ctx):
    await ctx.channel.send("Hi, im Mint! Find out my commands by typing Mint help!")

@bot.command()
async def ping(ctx):
    embed = discord.Embed(title = "Pong!", color = discord.Colour.green())
    embed.add_field(name = "The Bot ping is:", value = f' {round(bot.latency * 1000)}ms!')
    embed.set_footer (icon_url = ctx.author.avatar_url, text = f"Executed by {ctx.author.name}")
    await ctx.send(embed=embed)

@bot.command()
async def remindme(ctx, time, *, task):
    def convert(time):
        pos = ['s','m','h','d']

        time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600*24}

        unit = time[-1]

        if unit not in pos:
            return -1
        try:
            val = int(time[:-1])
        except:
            return -2

        return val * time_dict[unit]

    converted_time = convert(time)

    if converted_time == -1:
        await ctx.send("You didnt enter the time correctly!")
        return
    if converted_time == -2:
        await ctx.channel.send("The time you enter must be a intiger")
        return

    await ctx.send(f"I have set a reminder for **{task}** I will remind you in **{time}**!")

    await asyncio.sleep(converted_time)
    await ctx.send(f"{ctx.author.mention} your reminder for **{task}** is done!")
    await ctx.send(f"{ctx.author.mention}")
    await ctx.send(f"{ctx.author.mention}")

response = requests.get('https://ll.thespacedevs.com/2.1.0/launch/upcoming/?mode=list&limit=5')
if response:
    rocketapidata = json.loads(response.text)
    file = open("cache.json", "w+")
    file.write(response.text)
    file.close()
else:
    file = open("cache.json", "r")
    cachedata = file.read()
    file.close()
    rocketapidata = json.loads(cachedata)

for i in rocketapidata["results"]:
  print(i["name"])

bot.run(token)

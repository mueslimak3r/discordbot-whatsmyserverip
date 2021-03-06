# bot.py
import os

import discord
from discord.ext import tasks
from dotenv import Dotenv

import pathlib
from requests import get

script_location = pathlib.Path(__file__).parent.absolute()
env_dict = Dotenv(str(script_location) + '/.env')

TOKEN = env_dict['DISCORD_TOKEN']
GUILD = env_dict['DISCORD_GUILD']

client = discord.Client()

@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    channel = discord.utils.get(guild.text_channels, name='serverip')
    myLoop.start(channel=channel)

@tasks.loop(minutes = 5) # repeat after every 5 minutes
async def myLoop(channel):
    ip = get('https://api.ipify.org').text
    ip_string = '{}'.format(ip)
    message = 'My public IP address is: ' + ip_string
    await channel.send(message)

client.run(TOKEN)

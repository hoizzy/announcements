import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game

TOKEN = 'NTM2MjgyNDE3MDg2OTg4Mjk4.DyUbnw.gyI8KAaCxSWarzNk1YzVARaTvTw'
client = commands.Bot(command_prefix = 'p!')
client.remove_command('help')
@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name="Annoucnements", url="https://twitch.tv/bqpkke_rblx", type=1))

@client.command()
@commands.has_permissions(administrator=True)
async def announcementhere(*args, pass_context=True):
    output = ''
    for word in args:
        output += word
        output += ' '
    embed = discord.Embed(
        colour = discord.Colour.blue()
    )


    embed.add_field(name='Announcement', value =output, inline=False)
    await client.say('@here')
    await client.say(embed=embed)

@client.command()
@commands.has_permissions(administrator=True)
async def announcementeveryone(*args, pass_context=True):
    output = ''
    for word in args:
        output += word
        output += ' '
    embed = discord.Embed(
        colour = discord.Colour.blue()
    )


    embed.add_field(name='Announcement', value =output, inline=False)
    await client.say('@everyone')
    await client.say(embed=embed)

@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.blue()
    )

    embed.set_author(name='Help')
    embed.add_field(name=':mega: p!announcementhere (text, ADMINISTRATORS)', value='Announces your text', inline=False)
    embed.add_field(name=':mega: p!announcementeveryone (text, ADMINISTRATORS)', value='Announces text and mentions everyone.', inline=False)
    embed.add_field(name='Clear', value='Clears an amount of messages.', inline=False)
    embed.add_field(name='Creator', value='Made by enderman slayerr#6780', inline=False)
    

    await client.send_message(author, embed=embed)
    await client.say(':white_check_mark: Help is on its way!')



@client.command(pass_context=True)
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say('Messages deleted.')

@client.command()
async def stats():
    servers = list(client.servers)
    embed = discord.Embed(title="Servers:", description=f"{str(len(servers))}", color=0xFFFF)
    embed.add_field(name="Users:", value=f"{str(len(set(client.get_all_members())))}")
    await client.say(embed=embed)

    




client.run(TOKEN)
    

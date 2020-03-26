import discord
import os
from discord.ext import commands

bot = commands.Bot(command_prefix = 'c!')
bot.remove_command('help')

@bot.event
async def on_ready():
    print('logged on')

@bot.command()
async def load(ctx, extention):
    bot.load_extension(f'cogs.{extention}')

@bot.command()
async def unload(ctx, extention):
    bot.unload_extension(f'cogs.{extention}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run('NjkxNjg2MjUwMzg5ODMxNjkw.XnjlDQ.DflV6IxGKZWbVfvisjTeIff0FYk')
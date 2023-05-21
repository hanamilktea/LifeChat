# bot.py
import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    print('-----')

@bot.command(name='99', help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

@bot.command(name='need_help', help='Responds with an uplifting message')
async def uplift(ctx):
    messages = [
        "Remember that you are not alone. I'm here for you.",
        "You are stronger than you realize. Keep going!",
        "You are loved and valued. You matter." ,
        "Take a moment to breathe. You are doing your best.",
        "Don't forget to take care of yourself. You deserve self-compassion.",
        "Believe in yourself. You have the power to create a brighter future.",
        "You are capable of great things. Keep pushing forward.",
        "Remember that progress takes time. Celebrate the small victories."
    ]
    message = random.choice(messages)
    await ctx.send(f"{ctx.author.mention}, {message} ❤️")

bot.run(TOKEN)
import discord
from discord.ext import commands
import random

class ToD(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def tod(self, ctx, choice=None):
        if(choice == None):
            await ctx.send('Please enter either **Truth** or **Dare**')
        else:
            choice = choice.title()

        if ctx.author.id == 497418437086281728:
            await ctx.send('bahinchod pehle nitro de')
        else:        
            if(choice == 'Truth'):
                response = ['What was the last thing you googled?',
                            'Have you ever walked in on your parents doing it?',
                            'What is your guilty pleasure?',
                            'What was your most embarrassing moment in public?',
                            'Who is your secret crush?',
                            'How many selfies do you take a day?',
                            'Is your crush in this server?',
                            'What is the craziest thing you would do sexually?',
                            'Who in this server would be the worst person to date? Why?',
                            'Have you ever eaten something off the floor?',
                            'What’s the stupidest thing you were scared of as a kid?',
                            'How many orgasms have you had in one sexual encounter?',
                            'What is your favourite season of the year?',
                            'Where is the strangest place you’ve ever had sex?',
                            'Do you still know your first crush?',
                            'How many kids would you like to have?',
                            'What is your best talent?',
                            'What animal are you scared of?',
                            'Who is your favourite person in this server?',
                            'What is your favourite cartoon/anime from your generation?',
                            'What is your favourite childhood song?',
                            'At what age did you learn to ride a bike?',
                            'If you could be any super villain; who would you be?',
                            'What is the longest that you have ever been without taking a shower?',
                            'What is the best dish that you mom makes for dinner?',
                            'What is the funniest dream that you have ever had?',
                            'If you had the choice to live on your own right now; would you do it?',
                            'What is the most expensive thing you own?',
                            'If you could put one person in your family on mute for a day; who would it be?',
                            'Are you still a virgin?']
                await ctx.send(f'{random.choice(response)}')
            elif(choice == 'Dare'):
                response = ["propose your teacher during online zoom class",
                            "tell your parents you're going to become dad/mom",
                            'put your mouth full of ice cubes and keep them until they melt',
                            'go outside and belly dance',
                            'make up a short rap about another player',
                            "go to the neighbour’s house and ask for a banana",
                            'twerk for a minute',
                            'tag owner of this server 5 times in a row',
                            'tag the admin of this server and call him/her gay',
                            'go a whole minute without blinking',
                            'eat dry pack of noodles',
                            'sing your favourite song',
                            'hold your breath for as long as you can',
                            'type blindfolded',
                            'wear socks on your hands and type',
                            'make a song about first person to comment after this',
                            'go outside and sing National Anthem as loud as you can',
                            'try to seduce the first person who comments after this',
                            "tell your mom that you didn't like todays food she cooked",
                            'put on makeup with without looking into mirror',
                            'lick person nearest to you',
                            'tell your parents you are gay',
                            'roast the first person to comment after this',
                            'tag a random person who is participating in this game and make him/her cringe',
                            'wear your underwear backwards for 1 hour',
                            'to do anything the first one to comment would tell you to do',
                            'Pound on your chest and act like a gorilla for the next minute',
                            'go to your neighbors house and have a meaningless conversation with them for 10 minutes']
                await ctx.send(f'I dare you to {random.choice(response)}')
            else:
                await ctx.send('Please enter `c!tod truth` or `c!tod dare`')


def setup(bot):
    bot.add_cog(ToD(bot))
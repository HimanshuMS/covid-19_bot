import discord
from discord.ext import commands
import pandas as pd
from pandas import DataFrame

class State(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    data = pd.read_json('https://api.covid19india.org/state_district_wise.json')

    '''m = pd.DataFrame(data[''][0])
    mt = m.T
    sums = mt[''].sum()'''

    @commands.command()
    async def s(self, ctx, *, location=None):
        if(location == None):
            await ctx.send('Please enter name of a state!')
        else:
            location = location.title()

        k = location.split(',')

        if(len(k) > 1):
            confirmed = pd.DataFrame(self.data[k[0]][0])[k[1].strip()]['confirmed']
            active = pd.DataFrame(self.data[k[0]][0])[k[1].strip()]['active']
            death = pd.DataFrame(self.data[k[0]][0])[k[1].strip()]['deceased']
            recovered = pd.DataFrame(self.data[k[0]][0])[k[1].strip()]['recovered']
        else:
            confirmed = pd.DataFrame(self.data[location][0]).T['confirmed'].sum()
            active = pd.DataFrame(self.data[location][0]).T['active'].sum()
            death = pd.DataFrame(self.data[location][0]).T['deceased'].sum()
            recovered = pd.DataFrame(self.data[location][0]).T['recovered'].sum()

        embed = discord.Embed(
            title = f'Coronavirus (Covid-19) cases for {location}',
            description = f'``\n-----------------------------------------------\n:warning: **confirmed**: {confirmed}\n-----------------------------------------------\n:skull: **Deaths**: {death}\n-----------------------------------------------\n:heart: **Recovered**: {recovered}\n-----------------------------------------------\n:mask: **Active Cases**: {active}\n-----------------------------------------------\n',
            color = discord.Color.blue()
        )

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(State(bot))
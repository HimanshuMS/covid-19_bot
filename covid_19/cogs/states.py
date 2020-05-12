import discord
from discord.ext import commands
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import io
from datetime import datetime, timedelta, date

class State(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    '''m = pd.DataFrame(data[''][0])
    mt = m.T
    sums = mt[''].sum()'''

    @commands.command()
    async def s(self, ctx, *, location=None):
        data = pd.read_json('https://api.covid19india.org/districts_daily.json')
        if(location == None):
            await ctx.send('Please enter name of a state!')
            return
        else:
            location = location.title()
   
        k = location.split(',')
        if(len(k) == 1):
            data = pd.DataFrame(data['districtsDaily'])
            state_data = pd.DataFrame(data.loc[k[0],:]).loc['districtsDaily',:]
            state_data = pd.DataFrame.from_dict(state_data[0], orient='index')
            state_data.transpose()
            days_list = []
            confirmed_list = []
            recovered_list = []
            active_list = []
            death_list = []

            for index, row in state_data.iterrows():
                for idx in range(len(row)):
                    if(row[idx] is None):
                        continue
                    df = pd.Series(row[idx], dtype='object')
                    if(not(str(df['date']) in days_list)):
                        days_list.append(str(df['date']))
                        confirmed_list.append(df['confirmed'])
                        recovered_list.append(df['deceased'])
                        death_list.append(df['recovered'])
                        active_list.append(df['active'])
                    else:
                        for i in range(len(days_list)):
                            if str(df['date']) == days_list[i]:
                                break
                        confirmed_list[i] += df['confirmed']
                        recovered_list[i] += df['recovered']
                        death_list[i] += df['deceased']
                        active_list[i] += df['active']
                first = 1
                
        else:
            data = pd.DataFrame(data['districtsDaily'])
            state_data = pd.DataFrame(data.loc[k[0],:]).loc['districtsDaily',:]
            state_data = pd.DataFrame.from_dict(state_data[0], orient='index')
            state_data.transpose()
            city_data = pd.DataFrame(state_data.loc[k[1].strip(), :])

            days_list = []
            confirmed_list = []
            recovered_list = []
            death_list = []
            active_list = []

            for index, row in city_data.iterrows():
                df = pd.Series(row[0])
                days_list.append(df['date'])
                confirmed_list.append(df['confirmed'])
                recovered_list.append(df['recovered'])
                death_list.append(df['deceased'])
                active_list.append(df['active'])

        if(str(date.today()) == days_list[-1]):
            confirmed = confirmed_list[-1]
            confirmed_old = confirmed_list[-2]
            recovered = recovered_list[-1]
            recovered_old = recovered_list[-2]
            death = death_list[-1]
            death_old = death_list[-2]
            active = active_list[-1]
            active_old = active_list[-2]

            confirmed_new = f'+{confirmed - confirmed_old}'
            recovered_new = f'+{recovered - recovered_old}'
            death_new = f'+{death - death_old}'
            active_new = f'+{active - active_old}'
        else:
            data = pd.read_json('https://api.covid19india.org/state_district_wise.json')
            if(len(k) > 1):
                confirmed = pd.DataFrame(data[k[0]][0])[k[1].strip()]['confirmed']
                active = pd.DataFrame(data[k[0]][0])[k[1].strip()]['active']
                death = pd.DataFrame(data[k[0]][0])[k[1].strip()]['deceased']
                recovered = pd.DataFrame(data[k[0]][0])[k[1].strip()]['recovered']
            else:
                confirmed = pd.DataFrame(data[location][0].strip()).T['confirmed'].sum()
                active = pd.DataFrame(data[location][0].strip()).T['active'].sum()
                death = pd.DataFrame(data[location][0].strip()).T['deceased'].sum()
                recovered = pd.DataFrame(data[location][0].strip()).T['recovered'].sum()

        mortality_rate = round((death / confirmed * 100), 2)
        recovery_rate = round((recovered / confirmed * 100), 2) 

        embed = discord.Embed(
            title = f'Coronavirus (Covid-19) cases for {location}',
            description = f'``\n-----------------------------------------------\n:warning: **confirmed**: {confirmed} ({confirmed_new})\n-----------------------------------------------\n:skull: **Deaths**: {death} ({death_new})\n-----------------------------------------------\n:heart: **Recovered**: {recovered} ({recovered_new})\n-----------------------------------------------\n:mask: **Active Cases**: {active} ({active_new})\n-----------------------------------------------\n:coffin: **Mortality Rate:** {mortality_rate}%\n------------------------------------------------\n:+1: **Recovery Rate:** {recovery_rate}%\n------------------------------------------------',
            color = discord.Color.blue()
        )

        embed.set_footer(text=f"Information collected from Worldometers and GitHub page CSSEGISandData, inspired by picklejason ;)")
        fig = plt.figure(dpi=150)
        plt.style.use('seaborn')

        filename = './graphs/graph.png'

        plt.title(f"number of coronavirus cases over time for {location}") 

        plt.plot(days_list, confirmed_list, 'b-', label='confirmed')
        plt.plot(days_list, recovered_list, 'g-', label='recovered')
        plt.plot(days_list, death_list, 'r-', label='deaths')
        plt.xlabel("dates")
        plt.ylabel("number of cases")
        plt.legend(loc='upper left', fancybox=True, facecolor='1')
        ymax = int(max(confirmed_list) * 1.2)
        size = len(days_list)
        show_x_list = [days_list[0], days_list[int(size/4)], days_list[int(size/2)], days_list[int(size*3/4)], days_list[size - 1]]
        plt.ylim(0, ymax)
        plt.xticks(show_x_list)

        ymax = int(max(confirmed_list) * 1.2)
        plt.ylim(0, ymax)

        plt.savefig(filename)
        plt.cla()
        plt.close(fig)
        plt.close('all')
        with open(filename, 'rb') as f:
            file = io.BytesIO(f.read())
        image = discord.File(file, filename='graph.png')

        embed.set_image(url="attachment://graph.png")

        await ctx.send(file=image, embed=embed)

def setup(bot):
    bot.add_cog(State(bot))
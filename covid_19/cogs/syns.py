import discord
import io
import lxml
from discord.ext import commands
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests
from utils.codes import cont1, cont2, alt_names
import html5lib

class Stats(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['stat', 'stats'])
    async def data(self, ctx, location='all'):

        confirmed_cases = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
        deaths_reported = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
        recovered_cases = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
        
        '''url = 'https://www.worldometers.info/coronavirus/'
        header = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
        }

        r = requests.get(url, headers=header)
        data_list = pd.read_html(r.text)
        data_table = data_list[0].replace(to_replace = np.NaN, value = 0)'''
        
        cols = confirmed_cases.keys()
        date = list(confirmed_cases)[-1]
        r_cols = recovered_cases.keys()

        confirmed_f = confirmed_cases.loc[:, cols[4]:cols[-1]]
        deaths_f = deaths_reported.loc[:, cols[4]:cols[-1]]
        recovered_f = recovered_cases.loc[:, r_cols[4]:r_cols[-1]]

        dates = confirmed_f.keys()
        r_dates = recovered_f.keys()
        world_cases = []
        total_deaths = []
        mortality_rate = []
        total_recovered = []
        
        i=0

        for i in dates:
            world_cases.append(confirmed_f[i].sum())
            total_deaths.append(deaths_f[i].sum())
            mortality_rate.append(deaths_f[i].sum()/confirmed_f[i].sum())
            
        
        for i in r_dates:
            total_recovered.append(recovered_f[i].sum())

        if (len(location) == 2 or len(location) == 3):
            location = location.upper()
        else:
            location = location.title()

        if location in cont1:
            location = cont1[location]
        elif location in cont2:
            location = cont2[location]
        elif location in alt_names:
            location = alt_names[location]

        if location == 'ALL':
            confirmed = confirmed_cases[dates[-1]].sum()
            last_cf = confirmed_cases[dates[-2]].sum()
            deaths = deaths_reported[dates[-1]].sum()
            last_dt = deaths_reported[dates[-2]].sum()
            recovered = recovered_cases[r_dates[-1]].sum()
            last_rc = recovered_cases[r_dates[-2]].sum()

        elif (confirmed_cases['Country/Region'].str.contains(location).any()):
            confirmed = confirmed_cases[confirmed_cases['Country/Region'].str.contains(location)][dates[-1]].sum()
            last_cf = confirmed_cases[confirmed_cases['Country/Region'].str.contains(location)][dates[-2]].sum()
            deaths = deaths_reported[deaths_reported['Country/Region'].str.contains(location)][dates[-1]].sum()
            last_dt = deaths_reported[deaths_reported['Country/Region'].str.contains(location)][dates[-2]].sum()
            recovered = recovered_cases[recovered_cases['Country/Region'].str.contains(location)][r_dates[-1]].sum()
            last_rc = recovered_cases[recovered_cases['Country/Region'].str.contains(location)][r_dates[-2]].sum()

        else:
            await ctx.send("Location not found")

        if confirmed >= last_cf:
                confirmed_new = f'+{confirmed - last_cf}'
        else:
            confirmed_new = confirmed - last_cf
        
        if recovered >= last_rc:
            recovered_new = f'+{recovered - last_rc}'
        else:
            recovered_new = recovered - last_rc
        
        if deaths >= last_dt:
            death_new = f'+{deaths - last_dt}'
        else:
            death_new = deaths - last_dt

        mortality_rate = round((deaths/confirmed)*100, 2)
        recovery_rate = round((recovered/confirmed)*100, 2)

        if location == 'ALL':
            location = 'Total World Cases'
        elif location == 'USA':
            location = 'US'
        elif location == 'S. Korea':
            location = 'Korea, South'
        elif location == 'UK':
            location = 'United Kingdom'

        embed = discord.Embed(
            title = f'Coronavirus (COVID-19) cases over time',
            description = f'``\n**Showing Cases for {location}**\n------------------------------------------------\n:warning: **Confirmed Cases:** {confirmed} ({confirmed_new})\n------------------------------------------------\n:skull: **Deaths:** {int(deaths)} ({death_new})\n------------------------------------------------\n:heart: **Recovered:** {int(recovered)}\n------------------------------------------------\n:coffin: **Mortality Rate:** {mortality_rate}%\n------------------------------------------------\n:+1: **Recovery Rate:** {recovery_rate}%\n------------------------------------------------\nplease [vote here](https://top.gg/bot/691686250389831690/vote) if you find this information helpful\n------------------------------------------------\n',
            color = discord.Color.blue()
        )

        embed.set_footer(text=f"Information collected from GitHub page CSSEGISandData which is updated every 23:59 (UTC), inspired by picklejason ;)")

        fig = plt.figure(dpi=150)
        plt.style.use('seaborn')

        filename = './graphs/graph.png'

        if location=='Total World Cases':
            ax=confirmed_f.sum().plot(label="confirmed")
            ax=recovered_f.sum().plot(label="recovered")
            ax=deaths_f.sum().plot(label="deaths")
        else:
            ax=confirmed_cases[confirmed_cases['Country/Region'].str.contains(location)].loc[:, dates[4]:dates[-1]].sum().plot(label="confirmed")
            ax=recovered_cases[recovered_cases['Country/Region'].str.contains(location)].loc[:, r_dates[4]:r_dates[-1]].sum().plot(label="recovered")
            ax=deaths_reported[deaths_reported['Country/Region'].str.contains(location)].loc[:, dates[4]:dates[-1]].sum().plot(label="deaths")

        plt.title(f"number of coronavirus cases over time for {location}") 
        plt.xlabel("dates")
        plt.ylabel("number of cases")

        #ax.set_ylim(-10)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.legend(loc='upper left', fancybox=True, facecolor='1')

        l,_=plt.yticks()
        j=0
        ylables = []
        for i in l:
            l1 = float('{:.3g}'.format(i))
            m = 0
            if abs(l1) < 1000:
                ylables.append(l1)
            else:
                while abs(l1) >= 1000:
                    m += 1
                    l1 /= 1000.0
                    j = '{}{}'.format('{:f}'.format(l1).rstrip('0').rstrip('.'), ['', 'K', 'M', 'B', 'T'][m])
                    ylables.append(j)
        plt.yticks(l,ylables)
        
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
    bot.add_cog(Stats(bot))

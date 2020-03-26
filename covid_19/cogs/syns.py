import discord
import io
from discord.ext import commands
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from utils.codes import cont1, cont2, alt_names

class Stats(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    confirmed_cases = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv')
    deaths_reported = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
    recovered_cases = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
    
    data_list = pd.read_html('https://www.worldometers.info/coronavirus/')
    data_table = data_list[0].replace(to_replace = np.NaN, value = 0)
    
    cols = confirmed_cases.keys()

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

    @commands.command(aliases=['stat', 'stats', 's'])
    async def data(self, ctx, location='all'):

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
            confirmed = self.confirmed_cases[self.dates[-1]].sum()
            last_cf = self.confirmed_cases[self.dates[-2]].sum()
            deaths = self.deaths_reported[self.dates[-1]].sum()
            last_dt = self.deaths_reported[self.dates[-2]].sum()
            recovered = self.recovered_cases[self.r_dates[-1]].sum()
            last_rc = self.recovered_cases[self.r_dates[-2]].sum()

            confirmed_c = self.data_table[self.data_table['Country,Other'].str.contains('Total:')]['TotalCases'].sum()
            confirmed_new = f"+{int(self.data_table[self.data_table['Country,Other'].str.contains('Total:')]['NewCases'].sum())}"
            deaths_c = self.data_table[self.data_table['Country,Other'].str.contains('Total:')]['TotalDeaths'].sum()
            deaths_new = f"+{int(self.data_table[self.data_table['Country,Other'].str.contains('Total:')]['NewDeaths'].sum())}"
            recovered_c = self.data_table[self.data_table['Country,Other'].str.contains('Total:')]['TotalRecovered'].sum()
            active_cases = self.data_table[self.data_table['Country,Other'].str.contains('Total:')]['ActiveCases'].sum()

        elif (self.confirmed_cases['Country/Region'].str.contains(location).any() or self.data_table['Country,Other'].str.contains(location).any()):
            confirmed = self.confirmed_cases[self.confirmed_cases['Country/Region'].str.contains(location)][self.dates[-1]].sum()
            last_cf = self.confirmed_cases[self.confirmed_cases['Country/Region'].str.contains(location)][self.dates[-2]].sum()
            deaths = self.deaths_reported[self.deaths_reported['Country/Region'].str.contains(location)][self.dates[-1]].sum()
            last_dt = self.deaths_reported[self.deaths_reported['Country/Region'].str.contains(location)][self.dates[-2]].sum()
            recovered = self.recovered_cases[self.recovered_cases['Country/Region'].str.contains(location)][self.r_dates[-1]].sum()
            last_rc = self.recovered_cases[self.recovered_cases['Country/Region'].str.contains(location)][self.r_dates[-2]].sum()

            confirmed_c = self.data_table[self.data_table['Country,Other'].str.contains(location)]['TotalCases'].sum()
            confirmed_new = self.data_table[self.data_table['Country,Other'].str.contains(location)]['NewCases'].sum()
            deaths_c = self.data_table[self.data_table['Country,Other'].str.contains(location)]['TotalDeaths'].sum()
            deaths_new = f"+{int(self.data_table[self.data_table['Country,Other'].str.contains(location)]['NewDeaths'].sum())}"
            recovered_c = self.data_table[self.data_table['Country,Other'].str.contains(location)]['TotalRecovered'].sum()
            active_cases = self.data_table[self.data_table['Country,Other'].str.contains(location)]['ActiveCases'].sum()

        else:
            await ctx.send("Location not found")


        mortality_rate = round((deaths_c/confirmed_c)*100, 2)
        recovery_rate = round((recovered_c/confirmed_c)*100, 2)

        if location == 'ALL':
            location = 'Total World Cases'
        elif location == 'UK':
            location = 'United Kingdom'

        embed = discord.Embed(
            title = f'Coronavirus (COVID-19) cases over time',
            description = f'``\n**Showing Cases for {location}**\n------------------------------------------------\n:warning: **Confirmed Cases:** {confirmed_c} ({confirmed_new})\n------------------------------------------------\n:skull: **Deaths:** {int(deaths_c)} ({deaths_new})\n------------------------------------------------\n:heart: **Recovered:** {int(recovered_c)}\n------------------------------------------------\n:mask: **Active Cases:** {int(active_cases)}\n------------------------------------------------\n:coffin: **Mortality Rate:** {mortality_rate}%\n------------------------------------------------\n:+1: **Recovery Rate:** {recovery_rate}%\n------------------------------------------------',
            color = discord.Color.blue()
        )

        embed.set_footer(text="Information collected from Worldometers and from GitHub page CSSEGISandData, inspired by picklejason ;)")

        fig = plt.figure(dpi=150)
        plt.style.use('seaborn')

        filename = './graphs/graph.png'

        if location=='Total World Cases':
            ax=self.confirmed_f.sum().plot(label="confirmed")
            ax=self.recovered_f.sum().plot(label="recovered")
            ax=self.deaths_f.sum().plot(label="deaths")
        else:
            ax=self.confirmed_cases[self.confirmed_cases['Country/Region'].str.contains(location)].loc[:, self.dates[4]:self.dates[-1]].sum().plot(label="confirmed")
            ax=self.recovered_cases[self.recovered_cases['Country/Region'].str.contains(location)].loc[:, self.r_dates[4]:self.r_dates[-1]].sum().plot(label="recovered")
            ax=self.deaths_reported[self.deaths_reported['Country/Region'].str.contains(location)].loc[:, self.dates[4]:self.dates[-1]].sum().plot(label="deaths")

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

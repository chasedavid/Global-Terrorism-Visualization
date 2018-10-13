
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pprint import pprint
from scipy import stats


# In[2]:


import os
import seaborn
import pandas as pd

# File to Load
file_to_load = "./Resources/globalterrorism.csv"

# Read Purchasing File and store into Pandas data frame
terror_data = pd.read_csv(file_to_load, encoding = "ISO-8859-1", low_memory=False)


# In[3]:


def pull_format_data(df):
    #pull data needed to count number of attacks and number of fatalities/wounded
    attack_data = pd.DataFrame(df[['iyear','imonth','iday',
                                   'country_txt','region_txt',
                                   'nkill','nkillus','nkillter','nwound','nwoundus','nwoundte']])
    countries_df = attack_data[['iyear','country_txt','nkill','nkillter','nwound','nwoundte']]
    #rename to make columns more intuitive: 'Country' important for merge
    countries_df.columns = ['year','Country','nkill','nkillter','nwound','nwoundte']
    return(countries_df.fillna(0))


# In[4]:


def pull_year_attack_data(terror_data, yr):

    countries_df = pull_format_data(terror_data)

    #filter out only <year> data to compare with date collected for <year + 1> world happiness index
    year_df = countries_df[countries_df['year'] == yr]
    
    #groupby country then add the sum of kills 
    grouped_yr_df = year_df.groupby('Country')
    yr_kills_df = grouped_yr_df.sum()
    yr_kills_df['num_events'] = grouped_yr_df.Country.count()
    
    final = pd.DataFrame(yr_kills_df)
    final['Country'] = final.index.values
    final.reset_index(drop=True, inplace=True)
    #for final cleanliness, remove year col that was summed
    final.drop('year', axis=1, inplace=True)
    
    return(final)


# In[9]:


def graph_happy_terror(df, yr):
    #attach data pulled for given year from another function
    attack_data_df = pull_year_attack_data(df, yr)
    
    #import happness info: happiness report covered from previous year data
    happiness_df = pd.read_csv(f'./Resources/{(yr+1)}_whr_cleaned.csv')
    happiness_df.columns = ['Overall_Rank','Country','Score']
    
    merged_df = pd.merge(happiness_df, attack_data_df,
                        how='inner', on='Country')
    #save df
    merged_df.to_csv('./df_of_whr_terror_attack_information.csv')
    
    #plot graph number of fatalities to happiness score 
    plt.scatter(x=merged_df.Score,
               y = (merged_df.nkill + merged_df.nkillter),
               edgecolor='black')
    plt.title(f'{(yr+1)} WHR vs {yr} Terror Attack Fatalities')
    plt.xlabel('Happiness Score')
    plt.ylabel('Fatalities')

    plt.savefig(f"./WHRvsFatalities_{yr}.png")
    
    plt.show()
    
    #plot graph number of events to happiness score
    plt.scatter(x=merged_df.Score,
               y = merged_df.num_events,
               edgecolor='black')
    plt.title(f'{(yr+1)} WHR vs {yr} Terror Attacks')
    plt.xlabel('Happiness Score')
    plt.ylabel('Number of Events')

    plt.savefig(f"./WHRvsTerrorEvents_{yr}.png")
    

    plt.show()


# In[17]:


def graph_agro(events, fatals, wound):
    plt.scatter(x=events,
               y=fatals,
               s=wound,
               alpha = 0.35,
               edgecolor='black')
    #find and plot regression of data
    slope, intercept, r_value, p_value, std_err = stats.linregress(events, fatals)
    print(f"Fatalities to Events: r^2 = {r_value}")
    print(f'92% of the observed fatalities can be explained by the number of observed terror events in a given country.')
    #label
    plt.title('Fatalities Vs. Number of Events: 1970-2017')
    plt.xlabel('Number of Events')
    plt.ylabel('Number of Fatalities')
    
    plt.savefig('./FatalsVsEvents.png')
    
    plt.show()
    
    #second plot that now averages fatalities and wounded per event
    plt.scatter(x=events/48,
               y=fatals/events,
               s=wound*10/events,
               alpha=0.35,
               edgecolor='black')
    #label
    plt.title('Avg Fatalitity Count per Avg Number of Events')
    plt.xlabel('Average Events per Year')
    plt.ylabel('Average Fatlity Count')
    
    plt.savefig('./AvgFatalsVsAvgEvents.png')
    
    plt.show()
    
    return(0)
    
    
    


# In[18]:


def event_kills(df):
    pulled_df = pull_format_data(df)
    
    #group by country for further analysis
    countries_df = pulled_df.groupby('Country')
    #number of events = count of any rows under any given country (specificaly year here)
    num_events = countries_df.year.count()
    #number of fatalities
    num_fatals = countries_df.nkill.sum()
    #number wounded per country
    num_wound = countries_df.nwound.sum()
    
    graph_agro(num_events, num_fatals, num_wound)
    
    return(num_wound)


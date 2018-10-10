# This will allow us to create file paths across operating systems
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#import mplcursors
import seaborn as sns
sns.set(style="whitegrid")
import statsmodels.api as sm
def techline():

    # load Technology advance file
    tech_file_to_load = "TechTimeline.csv"
    tech_data = pd.read_csv(tech_file_to_load)
    return(tech_data)

def histo(terror_data, tech_data):      
    #Terror Data required for Tech assessment
    terror_data_groupby = terror_data.groupby(["iyear", "country", "country_txt"])
    terror_data_groupby.count()
      
    #Tech data split by type/year
    tech_social_yr = []
    tech_computer_yr = []
    tech_social = tech_data.loc[tech_data['Type'] == "Social"]
    tech_social_yr = list(set(tech_social["Year"]))
    tech_computer = tech_data.loc[tech_data['Type'] == "Computer"]
    tech_computer_yr = list(set(tech_computer["Year"]))
    tech_other = tech_data.loc[tech_data['Type'] == "Other"]
    tech_other_yr = list(set(tech_other["Year"]))
    tech_finance = tech_data.loc[tech_data['Type'] == "Finance"]
    tech_finance_yr = list(set(tech_finance["Year"]))
    tech_phone = tech_data.loc[tech_data['Type'] == "Phone"]
    tech_phone_yr = list(set(tech_phone["Year"]))
    
    years = []
    years = set(tech_data["Year"])
    years_unique = list(years)
    terror_years = []
    terror_years = terror_data["iyear"]

    # Create the figure and the axes
    fig, ax = plt.subplots()

    #for y in years_unique:
    #    ax.axvline(x=y, color='r', label='Tech Year', linestyle='--', linewidth=1)
    for y in tech_social_yr:
        ax.axvline(x=y, color='r', label='Social Year', Linestyle='--', Linewidth=1)
    #for y in tech_computer_yr:
    #    ax.axvline(x=y, color='g', label='Computer Year', Linestyle='--', Linewidth=1)
    #for y in tech_other_yr:
    #    ax.axvline(x=y, color='y', label='Other Year', Linestyle='--', Linewidth=1)
    for y in tech_finance_yr:
        ax.axvline(x=y, color='lightskyblue', label='Finance Year', Linestyle='--', Linewidth=1)
    for y in tech_phone_yr:
        ax.axvline(x=y, color='black', label='Social Year', Linestyle='--', Linewidth=1)

    # Set limits and labels
    ax.set_xlim([1970, 2018])
    plt.xticks(np.arange(1970, 2018, 5))
    plt.hist(terror_years, bins=25)
    plt.ylabel('No of events')
    plt.xlabel("Year of Terrorist events and Social, Phone advances")
    plt.title("Number of Terror Events Versus Tech Advances")

    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
    plt.figtext(.5, 1,"Red-Social advance, Lt Blue-Finance advance, Black-Mobile & IPhone", wrap=True,
                horizontalalignment='center', fontsize=10, bbox=props)

    plt.show()

def attack_type(terror_data):    
    #Create Violin plot
    sns.set(style="whitegrid", palette="pastel", color_codes=True)

    f, ax = plt.subplots(figsize=(8, 8))

    sns.violinplot(x=terror_data["iyear"], y=terror_data['attacktype1_txt'], data=terror_data)
    #               palette={"male": "b", "female": "y"})
    #sns.violinplot(x=terror_data["iyear"], y=terror_data['attacktype1_txt'], hue="sex", data=df,
    #               palette={"male": "b", "female": "y"})

    sns.despine(left=True)

    f.suptitle('Terror event by Atack Type', fontsize=18, fontweight='bold')
    ax.set_xlabel("Year",size = 16,alpha=0.7)
    ax.set_ylabel("Attack Type",size = 16,alpha=0.7)
    return(f)
    #plt.show()

def cntry_year(terror_data):    
    #Create 2nd violin chart
    sns.set(style="whitegrid", palette="pastel", color_codes=True)

    f, ax = plt.subplots(figsize=(8, 8))

    sns.violinplot(x=terror_data["iyear"], y=terror_data['country_txt'], data=terror_data)
    #               palette={"male": "b", "female": "y"})
    #sns.violinplot(x=terror_data["iyear"], y=terror_data['attacktype1_txt'], hue="sex", data=df,
    #               palette={"male": "b", "female": "y"})

    sns.despine(left=True)

    f.suptitle('Terror event by Country', fontsize=18, fontweight='bold')
    ax.set_xlabel("Year",size = 16,alpha=0.7)
    ax.set_ylabel("Country",size = 16,alpha=0.7)
    return(f)


def year_gang(terror_data):    
    #Event year by gname
    sns.set(style="whitegrid", palette="pastel", color_codes=True)

    f, ax = plt.subplots(figsize=(8, 8))

    sns.violinplot(x=terror_data["iyear"], y=terror_data['gname'], data=terror_data)
    #               palette={"male": "b", "female": "y"})
    #sns.violinplot(x=terror_data["iyear"], y=terror_data['attacktype1_txt'], hue="sex", data=df,
    #               palette={"male": "b", "female": "y"})

    sns.despine(left=True)

    f.suptitle('Event Year by gname', fontsize=18, fontweight='bold')
    ax.set_xlabel("Year",size = 16,alpha=0.7)
    ax.set_ylabel("gname",size = 16,alpha=0.7)
    return(f)
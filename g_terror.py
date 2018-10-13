
# coding: utf-8

# In[13]:


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import requests
import time
import json
import os
import seaborn
import glob
import datetime

# file_to_load = "../Group_Pro/globalterrorism.csv"

# terror_data = pd.read_csv(file_to_load, encoding="ISO-8859-1", low_memory = False)
# terror_data.head()
# # terror_df = pd.read_csv("../Group_Pro/globalterrorism.utf-8.csv", low_memory=False)
# # terror_df.head()


# In[14]:


# list(terror_data)


# In[25]:


def MajorEvents(terror_data):
    # kills_td = terror_data[terror_data["nkill"]>=100]
    kills_td = terror_data[terror_data["nkill"] >=100]
    f, ax = plt.subplots(figsize=(5,5))
    plt.scatter(kills_td['iyear'], 
            kills_td['nkill'],
            s=kills_td['nkill'],
            alpha = 0.35,
            edgecolor='black')
    #add labels
    plt.title('Major Events Over Time')
    plt.xlabel('Years', fontsize=15)
    plt.ylabel('Number of Events', fontsize=15)
    #show fig
#     plt.show()
#     plt.savefig('MajorEventsOverTime.png')
#     return(kills_td)
#MajorEvents(terror_data)
    return(f)


# In[26]:


# MajorEvents(terror_data)


# In[20]:


def FatalitiesbyAttack(terror_data):
    # group_td = terror_data.groupby(["iyear"]).sum()["nkill"]
    # group_td = terror_data.groupby(["iyear", "attacktype1_txt"]).count()["nkill"]

    # df2 = pd.terror_data(np.random.rand(2018, 55000), columns=["iyear", "attacktype1_txt", "nkill"])
    # df2.plot.bar()

    #group_td = terror_data.groupby(["iyear", "attacktype1_txt"]).count()["nkill"]
    group_td = terror_data.groupby(["attacktype1_txt"]).count()["nkill"]
    group_td2 = pd.DataFrame(group_td)
    group_td3 = group_td2.reset_index()

    group_td4 = group_td3.sort_values("nkill")
    # group_td2_rename = group_td2.rename(index=str, columns={"attacktype1_txt": "Attack_Type",
    #                                     "nkill" : "Fatalities"})
    #     group_td4
    f, ax = plt.subplots(figsize=(5,5))
    plt.bar(group_td4["attacktype1_txt"], group_td4["nkill"], width=.5)
    plt.xticks(group_td4["attacktype1_txt"], rotation="vertical")
    plt.title("Fatalities by Attack Type")
    plt.ylabel("Number of Fatalities", fontsize=18)
    plt.xlabel("Attack Type", fontsize=18 )
#     plt.show
#     plt.savefig("Fatalities by Attack Type.png")
    return(f)


# In[21]:


# FatalitiesbyAttack(terror_data)









# coding: utf-8

# In[2]:


# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
import seaborn
import pandas as pd
import matplotlib.pyplot as plt
from techline import techline, histo, attack_type, cntry_year

# File to Load
file_to_load = "Resources/globalterrorism.csv"

# Read Purchasing File and store into Pandas data frame
terror_data = pd.read_csv(file_to_load, encoding = "ISO-8859-1", low_memory=False)
terror_data.head()


# In[22]:


terror_data_groupby = terror_data.groupby(["iyear"])
terror_data_year = terror_data_groupby.count()

terror_data_year.head()


# In[ ]:


tech_data=techline()

f=histo(terror_data, tech_data)
f.show()
plt.savefig("tech_histo.png")

f=attack_type(terror_data)
f.show()
plt.savefig("attack_type.png")

f=cntry_year(terror_data)
f.show()
plt.savefig("country_year.png")



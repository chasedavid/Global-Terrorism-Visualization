
# coding: utf-8

# In[1]:


# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
import seaborn
import pandas as pd
import matplotlib.pyplot as plt
import gmaps
from config import gkey
from techline import techline, histo, attack_type, cntry_year
from Kyle1 import terrorism_frequency, terrorism_fatalities, heat_map, group_data

gmaps.configure(api_key=gkey)

# File to Load
file_to_load = "Resources/globalterrorism.csv"

# Read Purchasing File and store into Pandas data frame
terror_data = pd.read_csv(file_to_load, encoding = "ISO-8859-1", low_memory=False)
terror_data.head()


# In[2]:


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


# In[4]:


f=terrorism_frequency(terror_data)
f.show()
plt.savefig("TerrorismFrequency.png")


f=terrorism_fatalities(terror_data)
f.show()
plt.savefig("TerrorismFatalities.png")

g=group_data(terror_data)
g.head()


# In[5]:



terror_data_drop = terror_data.dropna(axis=0, subset=["latitude", "longitude"])
    
# Store latitude and longitude in locations
locations = terror_data_drop[["latitude", "longitude"]]

# Fill NaN values and convert to float
fatalities = terror_data_drop["nkill"]
    
# Plot Heatmap
fig = gmaps.figure()

# Create heat layer
heat_layer = gmaps.heatmap_layer(locations, weights=fatalities, 
                                     dissipating=False, max_intensity=10,
                                     point_radius=1)
# Add layer
fig.add_layer(heat_layer)

# Display figure
fig    


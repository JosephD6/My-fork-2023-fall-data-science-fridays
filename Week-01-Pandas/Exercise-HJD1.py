#!/usr/bin/env python
# coding: utf-8

# # First print your name in the cell below then save this file. (or something nice about your instructor)

# In[1]:


# In this cell print your name 

print('Henry Dugue')


# # Data wrangling with Pandas exercise
# * For this exercise we will be using the `listings.csv` data file.

# In[1]:


import pandas as pd
import numpy as np


# # Load in the data file using `pd.read_csv()`

# In[2]:


# Load data here
df = pd.read_csv("data/listings.csv")

df.head()


# ## Exercise 2 - Filtering
# 
# Return the following subsets of the dataframe.
# 
# 1. How many listings are there with a price less than 100? 
# 
# 
# 2. Find how many listings there are in just Brooklyn.
# 
# 
# 3. Find how many listings there are in Brooklyn with a price less than 100.
# 
# 
# 4. Using `.isin()` select anyone that has the host name of Michael, David, John, and Daniel.
# 
# 
# 5. Create a new column called `adjusted_price` that has $100 added to every listing in Williamsburg.  The prices for all other listings should be the same as the were before. 
# 
# 
# 6. What % of the rooms are private, and what % of the rooms are shared.  
#     * Hint, use `.value_counts()`
# 

# In[4]:


# 1. How many listings are there with a price less than 100? 


listings_less_than_100 = df[df['price'] < 100]
count_listings_less_than_100 = len(listings_less_than_100)
print(count_listings_less_than_100)


# In[5]:


# 2. Make a new DataFrame of listings in Brooklyn named `df_bk` 
# and find how many listings in just Brooklyn.

brooklyn_listings = df[df['neighbourhood_group'] == 'Brooklyn']
count_brooklyn_listings = len(brooklyn_listings)
print (count_brooklyn_listings)


# In[6]:


# 3. Find how many listings there are in Brooklyn with a price less than 100.


brooklyn_listings_less_than_100 = df[(df['neighbourhood_group'] == 'Brooklyn') & (df['price'] < 100)]
count_brooklyn_listings_less_than_100 = len(brooklyn_listings_less_than_100)
print(count_brooklyn_listings_less_than_100)


# In[18]:


# 4. Using `.isin()` select anyone that has the host name of Michael, David, John, and Daniel.
# How many total are there that have those names


selected_hosts = df[df['host_name'].isin(['Michael', 'David', 'John', 'Daniel'])]


# In[20]:


# 6. What % of the rooms are private, and what % of the rooms are shared.  


room_type_counts = df['room_type'].value_counts()
total_rooms = len(df)
percentage_private = (room_type_counts['Private room'] / total_rooms) * 100
percentage_shared = (room_type_counts['Shared room'] / total_rooms) * 100

print("Private rooms:", percentage_private)
print("Shared rooms:", percentage_shared)



# # Exercise 3 - Grouping
# 
# 1. Using `groupby`, count how many listings are in each neighbourhood_group.
# 
# 
# 2. Using `groupby`, find the mean price for each of the neighbourhood_groups. 
# 
# 
# 3. Using `groupby` and `.agg()`, find the min and max price for each of the neighbourhood_groups. 
# 
# 
# 4. Using `groupby`, find the median price for each room type in each neighbourhood_group.
# 
# 
# 5. Using `groupby` and `.agg()`, find the count, min, max, mean, median, and std of the prices for each room type in each neighbourhood_group.

# In[31]:


# 1. Using `groupby`, count how many listings are in each neighbourhood_group.


neighbourhood_group_counts = df.groupby('neighbourhood_group').sum()
print(neighbourhood_group_counts)


# In[42]:


# 2. Using `groupby`, find the mean price for each of the neighbourhood_groups. 


neighbourhood_group_mean_prices = df.groupby('neighbourhood_group')['price'].mean()
print(neighbourhood_group_mean_prices)


# In[15]:


# 5. Create a new column called `adjusted_price` that has $100 added to every listing in Williamsburg.  
# The prices for all other listings should be the same as the were before. 
get_ipython().run_line_magic('pinfo2', '')


# In[40]:


# 2.5. Using `groupby`, find the mean price for each room_type. 

room_type_mean_prices = df.groupby('room_type')['price'].mean()
print(room_type_mean)



# In[36]:


# 3. Using `groupby` and `.agg()`, find the min and max price for each of the neighbourhood_groups. 


neighbourhood_group_price_stats = df.groupby('neighbourhood_group')['price'].agg(['min', 'max'])
print(neighbourhood_group_price_stats)


# In[44]:


# 4. Using `groupby`, find the mean price for each room_type in each neighbourhood_group.

room_type_mean_prices_by_group = df.groupby(['neighbourhood_group', 'room_type'])['price'].mean()
print(room_type_mean_prices_by_group)


# In[47]:


# 5. Using `groupby` and `.agg()`, find the count, min, max, mean, median, and std of the prices 
# for each room type in each neighbourhood_group.


room_type_price_stats_by_group = df.groupby(['neighbourhood_group', 'room_type'])['price'].agg(['count', 'min', 'max', 'mean', 'median', 'std'])
print(room_type_price_stats_by_group)



# # Join and file saving.
# 1. Load the `prices.csv` and the `n_listings.csv`
# 
# 
# 2. Do join that keeps all the records for each table.
#     * Neighbourhood groups should include ['Bronx', 'Brooklyn', 'Manhattan', 'Queens', 'Staten Island',
#        'LongIsland']
#        
#        
# 3. Save your joined csv as `joined.csv`
# 
# 
# 4. Load your saved table and see if it looks the same or different that the DataFrame you used to create it. 

# In[52]:


# 1. Load the `prices.csv` and the `n_listings.csv`

prices_df = pd.read_csv('data/prices.csv')


n_listings_df = pd.read_csv('data/n_listings.csv', ';')


# In[55]:


# 2. Do join that keeps all the records for each table.
neighborhood_groups_to_include = ['Bronx', 'Brooklyn', 'Manhattan', 'Queens', 'Staten Island', 'LongIsland']
filtered_joined_df = joined_df[joined_df['neighbourhood_group'].isin(neighborhood_groups_to_include)]
get_ipython().run_line_magic('pinfo2', '')


# # Extra Credit
# Every question below this cell is extra credit and optional.

# ### 1. (Easy) Explore this new PandasAI Package and tell me what its all about because I've never used it. 
# * https://www.youtube.com/watch?v=5w6eZaoDVVk&ab_channel=CodingIsFun  
# * See if you can use it on the listings.csv to find out some cool info. or answer some of the questions above. 

# ### 2. (Very Easy) Find other cool Panda packages / add ons and show us what they can do well. And how you installed them. 

# ### 3. (Medium) Use the grammys.csv data for the next section of questions.
# 
# 1. Who was won Album of the Year in 2016?
# 
# 
# 2. Who won Best Rap Album in 2009?
# 
# 
# 3. How many awards was Kendrick Lamar nomiated for, and how many did he win...?

# ### (Hard) Load the Game Logs for 2022 and add the column names using a dictionary.  
# * [Link to the data page](https://www.retrosheet.org/gamelogs/)
# * [Link to the column names](https://procatinator.com/)
# * haha, gotta find them yourself!

# ### (Extra Hard) Download the files for the past 5 years into a new folder and add them all into one data frame using pandas, then save that new file.
# * Try to not hard code in the file names. We want to do this programmatically because what if we want to add new/more file names in the future.

# In[ ]:





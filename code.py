# Data Loading
# Let's start with the simple task of loading the data and do a little bit of renaming.

#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path
#Code starts here
data = pd.read_csv(path)
#print(data.head())
data.rename({'Total':'Total_Medals'},axis=1,inplace=True)
print(data.head(10))


# Some countries love Summer, some Winter. We think it has to do something with their Olympic performance.
# For this task we will try to figure out which olympic event does a country perform better in.
data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'],'Summer','Winter')


data['Better_Event'] = np.where(data['Total_Summer'] == data['Total_Winter'],'Both',data['Better_Event'])
better_event = data['Better_Event'].value_counts().idxmax()
print(better_event)

# So we figured out which is a better event for each country. Let's move on to finding out the best performing countries across all events
# In this task we will try to find which are the top 10 performing teams at summer event (with respect to total medals), winter event and overall? How many teams are present in all of the three lists above?

#Code starts 
top_countries = data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
#print(top_countries.head())
#top_countries = top_countries.drop('Total_Medals',axis=1)
top_countries = top_countries[:-1]
#print(top_countries.head())

def top_ten(data,col):
    country_list = []
    country_list = list((data.nlargest(10,col)['Country_Name']))
    return country_list

top_10_summer = top_ten(top_countries,'Total_Summer')
print(top_10_summer)
top_10_winter = top_ten(top_countries,'Total_Winter')
print(top_10_winter)
top_10 = top_ten(top_countries,'Total_Medals')
print(top_10)
common = list(set(top_10_summer) & set(top_10_winter) & set(top_10))
print(common)



# From the lists that are created from the previous task, let's plot the medal count of the top 10 countries for better visualisation

summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]

summer_df.plot(kind='bar')
winter_df.plot(kind='bar')
top_df.plot(kind='bar')
plt.show()


# Winning silver or bronze medals is a big achievement but winning gold is bigger.
# Using the above created dataframe subsets, in this task let's find out which country has had the best performance with respect to the ratio between gold medals won and total medals won.

summer_df['Golden_Ratio'] = summer_df['Gold_Summer']/summer_df['Total_Summer']
summer_max_ratio = max(summer_df['Golden_Ratio'])
summer_country_gold = summer_df.loc[summer_df['Golden_Ratio'].idxmax(),'Country_Name']
#print(summer_country_gold)

winter_df['Golden_Ratio'] = winter_df['Gold_Winter']/winter_df['Total_Winter']
winter_max_ratio = max(winter_df['Golden_Ratio'])
winter_country_gold = winter_df.loc[winter_df['Golden_Ratio'].idxmax(),'Country_Name']
#print(winter_country_gold)

top_df['Golden_Ratio'] = top_df['Gold_Total']/top_df['Total_Medals']
top_max_ratio = max(top_df['Golden_Ratio'])
top_country_gold = top_df.loc[top_df['Golden_Ratio'].idxmax(),'Country_Name']
#print(top_country_gold)


# Winning Gold is great but is winning most gold equivalent to being the best overall perfomer? Let's find out.

data_1 = data[:-1]

data_1['Total_Points'] = data_1['Gold_Total']*3 + data_1['Silver_Total']*2 + data_1['Bronze_Total']*1
most_points = max(data_1['Total_Points'])
best_country = data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']
print(most_points)
print(best_country)


# We know which country is best when it comes to winning the most points in Olympic Games. Let's plot the medal count to visualise their success better.

best = data[data['Country_Name']==best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]

best.plot.bar(stacked=True)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)
plt.show()



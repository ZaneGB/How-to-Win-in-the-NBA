#!/usr/bin/env python
# coding: utf-8

# In[1]:



import pandas as pd
import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt


# In[2]:


nba_2017_2018_df=pd.read_csv("./2017_2018_nba.csv",delimiter=",")
#nba_2017_2018_df.head()
nba_2017_2018_df['Year']=2018
nba_2017_2018_df.set_index(["Team"])
nba_2017_2018_df['Shots']=nba_2017_2018_df['2PA']+nba_2017_2018_df['3PA']
new_nba_17_18=nba_2017_2018_df[["Team", "Year", "3P", "3PA", "3P%", "2PA", "2P%", "Shots"]]
new_nba_17_18.head()


# In[3]:


misc_nba_2017_2018_df=pd.read_csv("./misc_2017_2018_nba.csv",delimiter=",")
new_misc_nba_17_18=misc_nba_2017_2018_df[["Team", "W"]]
new_misc_nba_17_18.head()


# In[4]:


nba_17_18_complete = pd.merge(new_nba_17_18, new_misc_nba_17_18, how="left", on=["Team"])  
nba_17_18_complete.head()


# In[5]:


nba_2016_2017_df=pd.read_csv("./2016_2017_nba.csv",delimiter=",")
nba_2016_2017_df['Year']=2017
nba_2016_2017_df.set_index(["Team"])
nba_2016_2017_df['Shots']=nba_2016_2017_df['2PA']+nba_2016_2017_df['3PA']
new_nba_16_17=nba_2016_2017_df[["Team", "Year", "3P", "3PA", "3P%", "2PA", "2P%", "Shots"]]
new_nba_16_17.head()


# In[6]:


misc_nba_2016_2017_df=pd.read_csv("./misc_2016_2017_nba.csv",delimiter=",")
new_misc_nba_16_17=misc_nba_2016_2017_df[["Team", "W"]]
new_misc_nba_16_17.head()


# In[7]:


nba_16_17_complete = pd.merge(new_nba_16_17, new_misc_nba_16_17, how="left", on=["Team"])  
nba_16_17_complete.head()


# In[8]:


nba_2015_2016_df=pd.read_csv("./2015_2016_nba.csv",delimiter=",")
#nba_2015_2016_df.head()
nba_2015_2016_df['Year']=2016
nba_2015_2016_df.set_index(["Team"])
nba_2015_2016_df['Shots']=nba_2015_2016_df['2PA']+nba_2016_2017_df['3PA']
new_nba_15_16=nba_2015_2016_df[["Team", "Year", "3P", "3PA", "3P%", "2PA", "2P%", "Shots"]]
new_nba_15_16.head()


# In[9]:


misc_nba_2015_2016_df=pd.read_csv("./misc_2015_2016_nba.csv",delimiter=",")
new_misc_nba_15_16=misc_nba_2015_2016_df[["Team", "W"]]
new_misc_nba_15_16.head()


# In[10]:


nba_15_16_complete = pd.merge(new_nba_15_16, new_misc_nba_15_16, how="left", on=["Team"])  
nba_15_16_complete.head()


# In[11]:


nba_2014_2015_df=pd.read_csv("./2014_2015_nba.csv",delimiter=",")
nba_2014_2015_df['Year']=2015
nba_2014_2015_df.set_index(["Team"])
nba_2014_2015_df['Shots']=nba_2014_2015_df['2PA']+nba_2016_2017_df['3PA']
new_nba_14_15=nba_2014_2015_df[["Team", "Year", "3P", "3PA", "3P%", "2PA", "2P%", "Shots"]]
new_nba_14_15.head()


# In[12]:


misc_nba_2014_2015_df=pd.read_csv("./misc_2014_2015_nba.csv",delimiter=",")
new_misc_nba_14_15=misc_nba_2014_2015_df[["Team", "W"]]
new_misc_nba_14_15.head()


# In[13]:


nba_14_15_complete = pd.merge(new_nba_14_15, new_misc_nba_14_15, how="left", on=["Team"])  
nba_14_15_complete.head()


# In[14]:


nba_2013_2014_df=pd.read_csv("./2013_2014_nba.csv",delimiter=",")
nba_2013_2014_df['Year']=2014
nba_2013_2014_df.set_index(["Team"])
nba_2013_2014_df['Shots']=nba_2013_2014_df['2PA']+nba_2013_2014_df['3PA']
new_nba_13_14=nba_2013_2014_df[["Team", "Year", "3P", "3PA", "3P%", "2PA", "2P%", "Shots"]]
new_nba_13_14.head()


# In[15]:


misc_nba_2013_2014_df=pd.read_csv("./misc_2013_2014_nba.csv",delimiter=",")
new_misc_nba_13_14=misc_nba_2013_2014_df[["Team", "W"]]
new_misc_nba_13_14.head()


# In[16]:


nba_13_14_complete = pd.merge(new_nba_13_14, new_misc_nba_13_14, how="left", on=["Team"])  
nba_13_14_complete.head()


# In[17]:


frames = [nba_13_14_complete, nba_14_15_complete, nba_15_16_complete, nba_16_17_complete, nba_17_18_complete]
nba_df = pd.concat(frames)
nba_df["3PA/Shots"]=(nba_df["3PA"]/nba_df["Shots"])*100
nba_df["2P%"]=nba_df["2P%"]*100
nba_df["3P%"]=nba_df["3P%"]*100
nba_df["W-PCT"]=nba_df["W"]/82
nba_df.head()


# In[18]:


nba_3PA_year=nba_df.groupby(["Year"]).mean()
del nba_3PA_year["3P"]
del nba_3PA_year["3P%"]
del nba_3PA_year["2PA"]
del nba_3PA_year["2P%"]
del nba_3PA_year["Shots"]
del nba_3PA_year["3PA/Shots"]
del nba_3PA_year["W"]
del nba_3PA_year["W-PCT"]
nba_3PA_year


# In[19]:


nba_3PA_year.plot(kind="bar", title="Long Range Bombers Rule the NBA",legend=False)
plt.ylabel("3 Point Attempts by Team per Game")
plt.ylim(15, 32)
plt.savefig("Graph1A-3PA-Team-Game.png")
plt.show()


# In[20]:


nba_3PA_year=nba_df.groupby(["Year"]).mean()
del nba_3PA_year["2P%"]
del nba_3PA_year["3P"]
del nba_3PA_year["3PA"]
del nba_3PA_year["3P%"]
del nba_3PA_year["2PA"]
del nba_3PA_year["Shots"]
del nba_3PA_year["W"]
del nba_3PA_year["W-PCT"]
nba_3PA_year


# In[21]:


nba_3PA_year.plot(kind="bar", title="Long Range Bombers Ruleth the NBA", color="red", legend=False)
plt.ylabel("3 Point Attempts as a % of All Shots")
plt.ylim(20, 37)
plt.savefig("Graph1B-3PA-Percent-Shots.png")
plt.show()


# In[22]:


nba_3PA_year=nba_df.groupby(["Year"]).mean()
del nba_3PA_year["3P"]
del nba_3PA_year["3PA"]
del nba_3PA_year["3PA/Shots"]
del nba_3PA_year["2PA"]
del nba_3PA_year["Shots"]
del nba_3PA_year["W"]
del nba_3PA_year["W-PCT"]
nba_3PA_year


# In[23]:


nba_3PA_year.reset_index(inplace=True) 
x_axis = nba_3PA_year["Year"]

points_2= nba_3PA_year["2P%"]
points_3= nba_3PA_year["3P%"]

points_2_handle = plt.plot(x_axis, points_2, marker ='o', color='red', label="2 Pointers")
points_3_handle = plt.plot(x_axis, points_3, marker='^', color='green', label="3 Pointers")

legend = plt.legend(fontsize="small", mode="Expanded", title="Shot", labelspacing=0.5)

#plt.title("The Short Game vs. The Long Game")

plt.xlabel("Year")
plt.ylabel("% of Shots Made")
plt.ylim(30, 60)

plt.xticks(np.arange(2014, 2019, 1.0))

#title="Even Tho their Accuracy Hasn't Improved"

plt.savefig("Graph2-2P-vs-3P.png")
plt.show()


# In[25]:


from scipy import stats

x_axis = nba_df["3PA"]
y_axis = nba_df["W"]

plt.xlim(10, 47)
plt.ylim(0, 80)

plt.title("Take More 3-Pointers, Win more Games")
plt.xlabel("# 3 Point Attempts Per Game")
plt.ylabel("Wins per Season (single years)")

#R-squared is a statistical measure of how close the data are to the fitted regression line.
#0% indicates that the model explains none of the variability of the response data around its mean. 
#100% indicates that the model explains all the variability of the response data around its mean.

slope, intercept, r_value, p_value, std_err = stats.linregress(x_axis,y_axis)

#When you perform a hypothesis test in statistics, a p-value helps you determine the significance of your results. 
#The p-value is a number between 0 and 1 and interpreted in the following way: 
#A small p-value (typically ≤ 0.05) indicates strong evidence against the null hypothesis.

textbox=("r-squared:","{:.3f}".format(r_value**2), "p_value:", "{:.4f}".format(p_value))

plt.text(20,2.8,textbox, size='small', weight='light')

plt.scatter(x_axis, y_axis, marker="o", facecolors="green", edgecolors="black", alpha=0.5)
plt.savefig("Graph3A-3PA-Wins.png")


# In[26]:


plt.xlim(30, 42)
plt.ylim(0, 100)

x_axis = nba_df["3P%"]
y_axis = nba_df["W-PCT"]*100

plt.title("But of course it's better to make 'em'")
plt.xlabel("3 Point Percentage of Shots Made")
plt.ylabel("Winning % (each circle represents a team year)")

#R-squared is a statistical measure of how close the data are to the fitted regression line.
#0% indicates that the model explains none of the variability of the response data around its mean. 
#100% indicates that the model explains all the variability of the response data around its mean.

slope, intercept, r_value, p_value, std_err = stats.linregress(x_axis,y_axis)

#When you perform a hypothesis test in statistics, a p-value helps you determine the significance of your results. 
#The p-value is a number between 0 and 1 and interpreted in the following way: 
#A small p-value (typically ≤ 0.05) indicates strong evidence against the null hypothesis.

textbox=("r-squared:","{:.3f}".format(r_value**2), "p_value:", "{:0.3e}".format(p_value))

plt.text(32.6,4,textbox, size='small', weight='light')

plt.scatter(x_axis, y_axis, marker="o", facecolors="purple", edgecolors="black", alpha=0.45)

plt.savefig("Graph3B-3Pct-WPct.png")


# In[ ]:





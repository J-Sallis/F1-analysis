#!/usr/bin/env python
# coding: utf-8

# insert section for reference
# # Race: Abu Dhabi
# 
# 
# Using the grid starting order from qualification, the Sunday event is a race to the finish line. Race finish order is determined by the order in which cars complete the required number of laps. Podium finishes are for the top 3 drivers. All drivers in the top 10 are awarded points based on finish position. Starting at 25pts for first all the way down to 1pt for 10th. Each team is required to make at least one pit stop and use two different tire compounds.
# 
# 
# create code blcoks/latex formuals for how points and podiums are assigned?
# 
# ![Quali](images/final_lap.jpg)
# ![VER](images/track.png)

# In[1]:


import fastf1 as ff1
import plotly.graph_objects as go
import plotly.express as px
import functions


# In[2]:


# enabling data cache, loading data from race and assigning lap data to df

ff1.Cache.enable_cache('cache')
race  = ff1.get_session(2022,'Abu Dhabi', 'R')
df = race.load_laps()


# In[3]:


# filtering for only Red Bull drivers
df = df[df.Driver.isin(['VER','PER'])]

# removing formation lap from lap times
df = df[df.LapNumber != 1]


# In[4]:


# figure 3
fig3  = px.scatter(df, x='LapNumber',y='LapTime',color='Driver')
fig3.update_yaxes(title=' Lap Time (S)').update_xaxes(title="Lap")
fig3 = fig3.update_layout(title_text='Fig 3: Red Bull: Lap time by lap')
functions.gluePlotly("Lap-times",fig3)


# ```{glue:figure} Lap-times
# :figwidth: 800px
# :name: "lap_fig"
# 
# All lap times for each driver
# ```
# Provide some comments on the above - re- 2 stop vs 1 stop strat
# 
# Perez getting caught behind Hamilton on lap 45

# In[5]:


# figure 4
speed_trap = df.groupby(['Driver',"LapNumber"]).mean(numeric_only=True)['SpeedST'].reset_index()

fig4  = px.scatter(speed_trap, x='LapNumber',y='SpeedST',color='Driver').update_layout(title_text="Fig 4: Speed Trap by Lap")
functions.gluePlotly("Speed-trap",fig4)


# discuss how the values for perez could be higher due to DRS/slipstreams 
# 
# ```{glue:figure} Speed-trap
# :figwidth: 800px
# :name: "ST_fig"
# 
# Speed for each driver/lap taken at the Speed Trap
# ```

# #### References
# 
# * https://medium.com/towards-formula-1-analysis
#     * Big shout out to Jasper for all the works he's done on sharing/teaching analysis
# * https://github.com/theOehrly/Fast-F1
#     * fastf1 github repo
# * https://www.formula1.com/en/racing/2022/United_Arab_Emirates.html
#     * F1 images

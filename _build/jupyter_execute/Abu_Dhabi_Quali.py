#!/usr/bin/env python
# coding: utf-8

# insert section
# # Qualification: Abu Dhabi
# 
# 
# Qualification is used to determine the starting grid for the Sunday race. There are 3 three rounds in total with pace determined over one lap. The slowest 5 drivers in first and second rounds are dropped with the final round used to determine starting order 
# 
# we can add in here formula and function on how we would determine the starting order for the grid, in latex then a code block on how it would look
# ```python
# def test(x):
#     return x
# 
# ```
# 
# ![Quali](images/Q.jpg)
# ![VER](images/VER_Q.jpg)
# 
# 
# add this in below
# #### Analysis
# 
# We will focus on comparing Red Bull drivers 
# 

# 

# In[1]:


import fastf1 as ff1
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import functions


# In[2]:


ff1.Cache.enable_cache('cache')
quali  = ff1.get_session(2022,'Abu Dhabi', 'Q')
quali.load()

#getting each Red Bull driver's fastest lap in quali
VER_q = quali.laps.pick_driver('VER').pick_fastest().get_car_data().add_distance()
PER_q = quali.laps.pick_driver('PER').pick_fastest().get_car_data().add_distance()


# In[3]:


# Figure 1
fig1  = go.Figure()
fig1.add_trace(go.Scatter(x=VER_q['Distance'],y=VER_q['Speed'],name='VER'))
fig1.add_trace(go.Scatter(x=PER_q['Distance'],y=PER_q['Speed'],name='PER'))
fig1.update_layout(title_text='Fig 1: Red Bull - Speed').update_xaxes(title='Distance').update_yaxes(title='KMP/H')


# talk briefly about above chart
# ```{figure}fig1
# ```

# In[4]:


fig2 = make_subplots(specs=[[{"secondary_y": True}]])
fig2.add_trace(go.Scatter(x=VER_q['Distance'],y=VER_q['nGear'],name='VER'))
fig2.add_trace(go.Scatter(x=PER_q['Distance'],y=PER_q['nGear'],name='PER'))
fig2.add_trace(go.Scatter(x=VER_q['Distance'],y=VER_q['RPM'],name='VER',line_color='blue'),secondary_y=True)
fig2.add_trace(go.Scatter(x=PER_q['Distance'],y=PER_q['RPM'],name='PER',line_color='red'),secondary_y=True)
fig2.update_traces(showlegend=False,secondary_y=True)
fig2.update_layout(title_text='Fig 2: Red Bull - Gears and Engine RPM').update_xaxes(title_text='Distance').update_yaxes(title_text='Gear',secondary_y=False)
fig2.update_yaxes(title_text='RPM',secondary_y=True)


# talk briefly about above chart

# #### References
# 
# * https://medium.com/towards-formula-1-analysis
#     * Big shout out to Jasper for all the works he's done on sharing/teaching
# * https://github.com/theOehrly/Fast-F1
#     * fastf1 github repo
# * https://www.formula1.com/en/racing/2022/United_Arab_Emirates.html
#     * F1 images
# * https://github.com/executablebooks/jupyter-book/issues/1815
#     * credit for panel function to wrap plotly object so that it can be used by glue

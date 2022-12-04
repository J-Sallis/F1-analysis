#!/usr/bin/env python
# coding: utf-8

# # Qualification: Abu Dhabi
# 
# 
# Qualification is used to determine the starting grid for the Sunday race. There are 3 three rounds in total with pace determined over one lap. The slowest 5 drivers in first and second rounds are dropped with the final round used to determine starting order.
# 
# Here's a recreation of qualification logic using a Python for loop:
# ```python
# def grid_starting_order(round,lap_time):
#     if round == "Q1":
#         return lap_time.nsmallest(15)
#     elif round == "Q2":
#         return lap_time.nsmallest(10)
#     else:
#         return sorted(lap_time)
# ```
# 
# ![Quali](images/Q.jpg)
# ![VER](images/VER_Q.jpg)
# 
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


fig1  = go.Figure()
fig1.add_trace(go.Scatter(x=VER_q['Distance'],y=VER_q['Speed'],name='VER'))
fig1.add_trace(go.Scatter(x=PER_q['Distance'],y=PER_q['Speed'],name='PER'))
fig1.update_layout(title_text='Fig 1: Red Bull - Speed').update_xaxes(title='Distance').update_yaxes(title='KMP/H')
functions.gluePlotly("Speed_Q",fig1)
fig1.show()


# ```{glue:figure} Speed_Q
# :figwidth: 800px
# :name: "speed_q"
# 
# Speed for each driver during fastest quali lap
# ```
# {numref}`speed_q` shows the speed for each Red Bull throughout each driver's fastest qualification lap. Looking at the above, there are corners where VER is coming off the throttle sooner to get on it fastest coming out. This is particulate true the last 5 corners where Max is carrying more speed and therefore has faster times. 

# In[4]:


fig2 = make_subplots(specs=[[{"secondary_y": True}]])
fig2.add_trace(go.Scatter(x=VER_q['Distance'],y=VER_q['nGear'],name='VER'))
fig2.add_trace(go.Scatter(x=PER_q['Distance'],y=PER_q['nGear'],name='PER'))
fig2.add_trace(go.Scatter(x=VER_q['Distance'],y=VER_q['RPM'],name='VER',line_color='blue'),secondary_y=True)
fig2.add_trace(go.Scatter(x=PER_q['Distance'],y=PER_q['RPM'],name='PER',line_color='red'),secondary_y=True)
fig2.update_traces(showlegend=False,secondary_y=True)
fig2.update_layout(title_text='Fig 2: Red Bull - Gears and Engine RPM').update_xaxes(title_text='Distance').update_yaxes(title_text='Gear',secondary_y=False)
fig2.update_yaxes(title_text='RPM',secondary_y=True)
functions.gluePlotly("RPM_Q",fig2)


# ```{glue:figure} RPM_Q
# :figwidth: 800px
# :name: "RPM_q"
# 
# Gears and engine RPM for both Red Bull drivers
# ```
# {numref}`RPM_q` contains 2 different metrics: engine gear and engine RPM for both Red Bull's during each drivers fastest qualification lap. There are multiple occasions where Max is able to gear down quicker heading into corners, resulting in being quicker gearing up and higher engine RPMs. These two factors result in higher speeds for VER. This is another example of Max outperforming his teammate.

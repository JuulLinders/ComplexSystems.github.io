#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.pylab as pylab
import pyhrv


# In[2]:


import os
os.getcwd()


# In[11]:


data = pd.read_csv('Actigraph.csv', usecols = ['HR', 'time'], header=0, index_col=1)
df = pd.DataFrame(data)
print(df.head())
print(df.tail())
print(df.describe())


# In[12]:


data2 = pd.read_csv('Actigraph.csv', usecols = ['HR', 'time'], header=0)
df2 = pd.DataFrame(data2)

time = df2['time']
print(data2)

HR2 = df2['HR']
time2 = df2['time']

print(HR2, time2)


# In[5]:


df.to_csv('time_HR_df.csv')


# In[13]:


HR = df['HR']
# time = df['time']
HR_wake = HR['10:10:22':'00:46:00']
HR_sleep = HR['00:46:00': '03:31:06']
HR_nightwake = HR['03:31:06': '03:57:06']
HR_sleep2 = HR['03:57:06': '07:30:00']
HR_wake2 = HR['07:30:00':]

print(HR, HR_sleep)


# In[14]:


from matplotlib.pyplot import figure


# In[15]:


df = pd.DataFrame(data)

plt.figure(figsize=(70, 30))
plt.plot(HR_wake, data=data, color='c')
plt.plot(HR_sleep, data=data, color='b')
plt.plot(HR_nightwake, data=data, color='c')
plt.plot(HR_sleep2, data=data, color='b')
plt.plot(HR_wake2, data=data, color='c')


plt.xlabel("time (hours:minutes:seconds)", fontsize = 30)
plt.ylabel("Heart rate (BPM)", fontsize = 30)
plt.xticks(ticks=['10:10:22', '11:00:00', '12:00:00', '13:00:00', '14:00:00', '15:00:00', '16:00:00',
                  '17:00:00', '18:00:02', '19:00:00', '20:00:06', '21:00:00', '22:00:03', '23:00:01',
                  '00:00:00','01:00:05', '02:00:01', '03:00:00', '04:00:37', '05:00:00', '06:00:00', 
                  '07:00:00', '08:00:00', '09:00:00', '09:45:35'], 
           labels=['10:10:22', '11:00:00', '12:00:00', '13:00:00', '14:00:00', '15:00:00', '16:00:00',
                  '17:00:00', '18:00:00', '19:00:00', '20:00:00', '21:00:00', '22:00:00', '23:00:00',
                  '00:00:00','01:00:00', '02:00:00', '03:00:00', '04:00:00', '05:00:00', '06:00:00', 
                  '07:00:00', '08:00:00', '09:00:00', '09:45:35'])
plt.tick_params(axis ='x', rotation = 20, labelsize = 30)
plt.tick_params(axis = 'y', labelsize = 30)

plt.savefig("HR_user1.png",facecolor = 'w', edgecolor = 'b' )

plt.show()


# In[17]:


hour1 = HR['10:10:22' : '11:00:00']
hour2 = HR['11:00:00' : '12:00:00']
hour3 = HR['12:00:00' : '13:00:00']
hour4 = HR['13:00:00' : '14:00:00']
hour5 = HR['14:00:00' : '15:00:00']
hour6 = HR['15:00:00' : '16:00:00']
hour7 = HR['16:00:00' : '17:00:00']
hour8 = HR['17:00:00' : '18:00:02']
hour9 = HR['18:00:02' : '19:00:00']
hour10 = HR['19:00:00' : '20:00:06']
hour11 = HR['20:00:06' : '21:00:00']
hour12 = HR['21:00:00' : '22:00:03']
hour13 = HR['22:00:03' : '23:00:01']
hour14 = HR['23:00:01' : '00:00:00']
hour15 = HR['00:00:00' : '00:46:00']
sleep  = HR['00:46:00' : '01:00:05']
hour16 = HR['01:00:05' : '02:00:01']
hour17 = HR['02:00:01' : '03:00:00']
hour18 = HR['03:00:00' : '03:31:06']
wake   = HR['03:31:06' : '03:57:06']
sleep2 = HR['03:57:06' : '04:00:37']
hour19 = HR['04:00:37' : '05:00:00']
hour20 = HR['05:00:00' : '06:00:00']
hour21 = HR['06:00:00' : '07:00:00']
wake2  = HR['07:00:00' : '07:30:00']
hour22 = HR['07:30:00' : '08:00:00']
hour23 = HR['08:00:00' : '09:00:00']
hour24 = HR['09:00:00' : '09:45:35']

hr_wake      = HR['10:10:22': '00:46:00']
hr_sleep     = HR['00:46:00': '03:31:06']
hr_nightwake = HR['03:31:06': '03:57:06']
hr_sleep2    = HR['03:57:06': '07:30:00']
hr_wake2     = HR['07:30:00':]


# In[18]:


hours = (hour1, hour2, hour3, hour4, hour5,
         hour6, hour7, hour8, hour9, hour10,
         hour11, hour12, hour13, hour14,
         hour15, sleep, hour16, hour17, hour18, 
         wake, sleep2, hour19, hour20, hour21,
         wake2, hour22, hour23, hour24)

sleep_wake_hours = (hr_wake, hr_sleep, hr_nightwake, hr_sleep2, hr_wake2)


# In[19]:


hours2 = ['10:10:22', '11:00:00', '12:00:00', '13:00:00', '14:00:00', '15:00:00', '16:00:00',
         '17:00:00', '18:00:02', '19:00:00', '20:00:06', '21:00:00', '22:00:03', '23:00:01',
            '00:00:00', '00:46:00','01:00:05', '02:00:01', '03:00:00', '03:31:06', '03:57:06', 
          '04:00:37', '05:00:00', '06:00:00', '07:00:00', '07:30:00', '08:00:00', '09:00:00']

hours3 = ['10:10:22', '11:30:00', '12:30:00', '13:30:00', '14:30:00', '15:30:00', '16:30:00',
          '17:30:00', '18:30:02', '19:30:00', '20:30:06', '21:30:00', '22:30:03', '23:30:01',
          '00:30:00', '00:46:00','01:30:05', '02:30:01', '03:00:00', '03:31:06', '03:57:06', 
          '04:30:37', '05:30:00', '06:30:00', '07:30:00', '07:30:00', '08:30:00', '09:30:00']

hours4 = ['10:10:22','00:46:00', '03:31:06', '03:57:06', '07:30:00']

hours5 = ['17:00:00', '02:10:00', '03:43:00', '05:45:00', '08:35:00' ]


# In[20]:


def hour_avg_HR(x):
    hour_avg_HR = []
    for i in x: 
        avg_HR = i.mean()
        hour_avg_HR.append(avg_HR)
    return hour_avg_HR


# In[21]:


hour_avg_HR = hour_avg_HR(hours)
print(hour_avg_HR)


# In[22]:


def sleep_wake_avg_HR(x):
    avg_HR_list = []
    for i in x:
        avg_HR = i.mean()
        avg_HR_list.append(avg_HR)
    return avg_HR_list

sleep_wake_avg_HR = sleep_wake_avg_HR(sleep_wake_hours)


# In[ ]:


print(hr_sleep)


# In[24]:


RRdata = pd.read_csv('RR.csv', usecols = ['ibi_s', 'time'], header=0, index_col=1)
dfRR = pd.DataFrame(RRdata)
print(dfRR.head())
print(dfRR.tail())
print(dfRR.describe())


# In[25]:


dfRR.drop(dfRR[(dfRR['ibi_s'] > 2)].index, inplace=True)
dfRR


# In[26]:


RR = dfRR['ibi_s']
RR_wake = RR['10:30:17':'00:46:00']
RR_sleep = RR['00:46:00': '03:31:06']
RR_nightwake = RR['03:31:06': '03:57:06']
RR_sleep2 = RR['03:57:06': '07:30:00']
RR_wake2 = RR['07:30:00':]


# In[27]:


RRhour1 = RR['10:10:22' : '11:00:00']
RRhour2 = RR['11:00:00' : '12:00:00']
RRhour3 = RR['12:00:00' : '13:00:00']
RRhour4 = RR['13:00:00' : '14:00:07']
RRhour5 = RR['14:00:07' : '15:00:00']
RRhour6 = RR['15:00:00' : '16:00:06']
RRhour7 = RR['16:00:06' : '17:00:00']
RRhour8 = RR['17:00:00' : '18:00:02']
RRhour9 = RR['18:00:02' : '19:00:00']
RRhour10 = RR['19:00:00' : '20:00:06']
RRhour11 = RR['20:00:06' : '21:00:00']
RRhour12 = RR['21:00:00' : '22:00:03']
RRhour13 = RR['22:00:03' : '23:00:01']
RRhour14 = RR['23:00:01' : '00:00:00']
RRhour15 = RR['00:00:00' : '00:46:00']
RRsleep  = RR['00:46:00' : '01:00:05']
RRhour16 = RR['01:00:05' : '02:00:01']
RRhour17 = RR['02:00:01' : '03:00:00']
RRhour18 = RR['03:00:00' : '03:31:06']
RRwake   = RR['03:31:06' : '03:57:06']
RRsleep2 = RR['03:57:06' : '04:00:37']
RRhour19 = RR['04:00:37' : '05:00:00']
RRhour20 = RR['05:00:00' : '06:00:00']
RRhour21 = RR['06:00:00' : '07:00:00']
RRwake2  = RR['07:00:00' : '07:30:00']
RRhour22 = RR['07:30:00' : '08:00:06']
RRhour23 = RR['08:00:06' : '09:00:00']
RRhour24 = RR['09:00:00' : '09:45:26']

RR_wake      = RR['10:10:22': '00:46:00']
RR_sleep     = RR['00:46:00': '03:31:06']
RR_nightwake = RR['03:31:06': '03:57:06']
RR_sleep2    = RR['03:57:06': '07:30:00']
RR_wake2     = RR['07:30:00':]


# In[28]:


RRhours = (RRhour1, RRhour2, RRhour3, RRhour4, RRhour5,
         RRhour6, RRhour7, RRhour8, RRhour9, RRhour10,
         RRhour11, RRhour12, RRhour13, RRhour14,
         RRhour15, RRsleep, RRhour16, RRhour17, RRhour18, 
         RRwake, RRsleep2, RRhour19, RRhour20, RRhour21,
         RRwake2, RRhour22, RRhour23, RRhour24)

RRsleep_wake_hours = (RR_wake, RR_sleep, RR_nightwake, RR_sleep2, RR_wake2)


# In[29]:


RRhours2 = ['10:10:22', '11:00:00', '12:00:00', '13:00:00', '14:00:07', '15:00:00', '16:00:06',
         '17:00:00', '18:00:02', '19:00:00', '20:00:06', '21:00:00', '22:00:03', '23:00:01',
            '00:00:00', '00:46:00','01:00:05', '02:00:01', '03:00:00', '03:31:06', '03:57:06', 
          '04:00:37', '05:00:00', '06:00:00', '07:00:00', '07:30:00', '08:00:06', '09:00:00']


# In[30]:


def hour_avg_RR(x):
    hour_avg_RR = []
    for i in x: 
        avg_RR = i.mean()
        hour_avg_RR.append(avg_RR)
    return hour_avg_RR

hour_avg_RR = hour_avg_RR(RRhours)
print(hour_avg_RR)


# In[ ]:


# def sleep_wake_avg_RR(x):
#     avg_RR_list = []
#     for i in x:
#         avg_RR = i.mean()
#         avg_RR_list.append(avg_RR)
# #     return avg_RR_list

# sleep_wake_avg_RR = sleep_wake_avg_RR(RRsleep_wake_hours)


# In[ ]:


plt.figure(figsize=(70, 30))
plt.plot(RR_wake, data=RRdata, color='c')
plt.plot(RR_sleep, data=RRdata, color='b')
plt.plot(RR_nightwake, data=RRdata, color='c')
plt.plot(RR_sleep2, data=RRdata, color='b')
plt.plot(RR_wake2, data=RRdata, color='c')
plt.plot(RRhours2, hour_avg_RR, color='r')


plt.xlabel("time", fontsize = 30)
plt.ylabel("Interbeat Interval (s)", fontsize = 30)

plt.xticks(ticks=['10:10:17', '11:00:00', '12:00:00', '13:00:00', '14:00:07', '15:00:00', '16:00:06',
                    '17:00:00', '18:00:02', '19:00:00', '20:00:06', '21:00:00', '22:00:03', '23:00:01',
                    '00:00:00', '00:46:00','01:00:05', '02:00:01', '03:00:00', '03:31:06', '03:57:06', 
                      '04:00:37', '05:00:00', '06:00:00', '07:00:00', '07:30:00', '08:00:06', '09:00:00'], 
           
           labels=['10:10:22', '11:00:00', '12:00:00', '13:00:00', '14:00:00', '15:00:00', '16:00:00',
                  '17:00:00', '18:00:00', '19:00:00', '20:00:00', '21:00:00', '22:00:00', '23:00:00',
                  '00:00:00','sleep', '01:00:00', '02:00:00', '03:00:00', 'wake', 'sleep', '04:00:00', '05:00:00', '06:00:00', 
                  '07:00:00', 'wake', '08:00:00', '09:00:00'])
plt.tick_params(axis ='x', rotation = 60, labelsize = 30)
plt.tick_params(axis = 'y', labelsize = 30)

plt.savefig("RR_user1_avg.png",facecolor = 'w', edgecolor = 'b' )

plt.show()


# In[106]:


plt.figure(figsize=(70, 30))
# plt.plot(RR_wake, data=RRdata, color='c')
plt.plot(RR['01:00:05': '01:26:00'], data=RRdata, color='b')
# plt.plot(RR_nightwake, data=RRdata, color='c')
# plt.plot(RR_sleep2, data=RRdata, color='b')
# plt.plot(RR_wake2, data=RRdata, color='c')
# plt.plot(RRhours2, hour_avg_RR, color='r')


plt.xlabel("time", fontsize = 30)
plt.ylabel("Interbeat Interval (s)", fontsize = 30)

plt.xticks(ticks=['01:00:05', '01:05:01', '01:10:00', '01:15:00', '01:20:00', '01:25:00', '01:26:00'], 
           
           labels=['01:00:00 (sleep)', '01:05:00', '01:10:00', '01:15:00', '01:20:00', '01:25:00', '01:26:00 (sleep)'])

plt.tick_params(axis ='x', rotation = 60, labelsize = 30)
plt.tick_params(axis = 'y', labelsize = 30)

plt.savefig("RR_user1_26minsleep.png",facecolor = 'w', edgecolor = 'b' )

plt.show()


# In[111]:


plt.figure(figsize=(70, 30))
# plt.plot(RR_wake, data=RRdata, color='c')
# plt.plot(RR_sleep, data=RRdata, color='b')
plt.plot(RR_nightwake, data=RRdata, color='c')
# plt.plot(RR_sleep2, data=RRdata, color='b')
# plt.plot(RR_wake2, data=RRdata, color='c')
# plt.plot(RRhours2, hour_avg_RR, color='r')


plt.xlabel("time", fontsize = 30)
plt.ylabel("Interbeat Interval (s)", fontsize = 30)

plt.xticks(ticks=['03:31:06', '03:35:00', '03:40:02', '03:45:00', '03:50:00', '03:55:00', '03:57:06'],
                     
           labels=['03:31:06 (wake)', '03:35:00', '03:40:00', '03:45:00', '03:50:00', '03:55:00', '03:57:06 (sleep)'])
                   
plt.tick_params(axis ='x', rotation = 60, labelsize = 30)
plt.tick_params(axis = 'y', labelsize = 30)

plt.savefig("RR_user1_26minwake.png",facecolor = 'w', edgecolor = 'b' )

plt.show()


# In[ ]:


def RMSSD(x):
    RMSSD_list = []
    for rr in x:
        RMSSD = np.sqrt(np.mean(rr)**2)
        RMSSD_list.append(RMSSD)
    return RMSSD_list

RMSSD_nightwake = RMSSD(RR_nightwake)


# In[114]:


RMSSD = np.sqrt(np.mean(RR['01:00:05': '01:26:00'])**2)
print (RMSSD)


# In[34]:


pyhrv.nonlinear.poincare(nni=None, rpeaks=RR, show=True, figsize=(15,15), ellipse=True, vectors=True, legend=True, marker='o')
plt.savefig('poincaré.png', facecolor = 'w', edgecolor = 'b')


# In[50]:


from PIL import Image
pyhrv.nonlinear.poincare(nni=None, rpeaks=RR_nightwake, show=True, figsize=(15,15), ellipse=True, vectors=True, legend=True, marker='o')


# In[38]:


pyhrv.nonlinear.poincare(nni=None, rpeaks=RR['01:00:05': '01:26:00'], show=True, figsize=(15,15), ellipse=True, vectors=True, legend=True, marker='o')


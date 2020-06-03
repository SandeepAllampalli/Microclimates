# -*- coding: utf-8 -*-
"""
Created on Sat May 16 18:50:43 2020

@author: admi
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn')

df = pd.read_csv('C:/Users/admi/Desktop/Ms ERM/Microclimates/Ex02_data.csv',
                 sep=';', header=0, parse_dates=[0], index_col=0)

print(type(df))
print(df.size)
print(df.ndim)
print(df.shape)
print(df.dtypes)
print(df.describe())

#Determine min and max value of each time series.
print(df.apply([np.min, np.max]))


#Calculate monthly mean values of each time series.
df_m = df[['Tmax','Tmin','RR']].resample('M').mean() 
print(df_m)

#Calculate monthly anomalies of each time series. Hint:An anomaly is defined as
#deviation from the mean value

df_stat = df.resample('M').apply([np.mean, np.min, np.max, np.std])
print(df_stat)

#-------------------------------------------------------------------------------

#Plotting

fig, ax = plt.subplots()

plt.plot(df_m['Tmax'], label='Tmax')
plt.plot(df_m['Tmin'], label='Tmin')
plt.plot(df_m['RR'], label='RR')

plt.legend()

plt.title('Title')
plt.xlabel('Years')
plt.ylabel('T')

plt.tight_layout()

plt.show()

#plt.gcf() #get current figure
#plt.gca() #get current axes

fig, (ax1,ax2) = plt.subplots(nrows=2, ncols=1)

ax1.plot(df_m['Tmax'], label='Tmax', linestyle='--')
ax1.plot(df_m['Tmin'], label='Tmin', color='green')
ax2.plot(df_m['RR'], label='RR')

ax1.legend()

ax1.set_title('Title')
ax1.set_label('Years')
ax1.set_ylabel('Tmax and Tmin')

ax2.legend()

ax2.set_title('Title')
ax2.set_label('Years')
ax2.set_ylabel('RR')

plt.tight_layout()

plt.show()

#--------------------------------------------------------------

#df_stat[df_stat.index.month==6]

tab = df_stat.reset_index()
tab.dtypes
tab['month'] = tab['Date'].dt.month
tab=tab.drop('month', axis=1)

tab




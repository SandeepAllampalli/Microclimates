# -*- coding: utf-8 -*-
"""
Created on Sun May 31 03:23:40 2020

@author: Sandeep
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn')

#Exercise1  
#Data preparation 
#1.Import the file ‘EX04.data.csv’ and calculate monthly mean values for 
#temperature and monthly sums of precipitation. 

df = pd.read_csv('C:/Users/admi/Desktop/Ms ERM/Microclimates/Ex04.data.csv',
                 sep=';', header=0, parse_dates=[0], index_col=0)

df_m = df[['Tmax','Tmin']].resample('M').mean() 
print(df_m)

df_s = df[['RR']].resample('M').sum() 
print(df_s)

#2.Select the winter season and 
#(i) calculate monthly precipitation anomalies on the basis of the average
#over the reference period ‘1981-2010’,

df_p = df['1981':'2010']

df_panm = df_p[['RR']].resample('M').apply([np.mean, np.min, np.max, np.std])
print(df_panm)

#(ii) monthly anomalies of the temperature range.

df_tanm = df[['Tmax','Tmin']].resample('M').apply([np.mean, np.min, np.max, np.std])
print(df_tanm)

#Exercise2  
#Visualization 
#Use the prepared data and generate a plot consisting of 4 subplots:

fig, [[ax1,ax2],[ax3,ax4]] = plt.subplots(nrows=2, ncols=2)

#i) monthly precipitation amount,
ax1.plot(df_s['2000':'2010'])

#ii) monthly precipitation anomalies,
ax2.plot(df_panm[('RR', 'mean')], label='mean', color='red', linewidth='0.5')
ax2.plot(df_panm[('RR', 'amin')], label='min', color='blue', linewidth='0.5')
ax2.plot(df_panm[('RR', 'amax')], label='max', color='green', linewidth='0.5')
ax2.plot(df_panm[('RR', 'std')], label='std', color='black', linewidth='0.5')

#iii) monthly mean Tmin and Tmax,
ax3.plot(df_m['Tmax'], label='Tmax', color='red', linewidth='0.5')
ax3.plot(df_m['Tmin'], label='Tmin', color='blue', linewidth='0.5')

#iv) monthly anomalies of the temperature range
ax4.plot(df_tanm[('Tmax', 'mean')], label='mean', color='red', linewidth='0.5')
ax4.plot(df_tanm[('Tmax', 'amin')], label='min', color='blue', linewidth='0.5')
ax4.plot(df_tanm[('Tmax', 'amax')], label='max', color='green', linewidth='0.5')
ax4.plot(df_tanm[('Tmax', 'std')], label='std', color='black', linewidth='0.5')
ax4.plot(df_tanm[('Tmin', 'mean')], label='mean', color='red', linewidth='0.5')
ax4.plot(df_tanm[('Tmin', 'amin')], label='min', color='blue', linewidth='0.5')
ax4.plot(df_tanm[('Tmin', 'amax')], label='max', color='green', linewidth='0.5')
ax4.plot(df_tanm[('Tmin', 'std')], label='std', color='black', linewidth='0.5')

ax1.legend()

ax1.set_title('Monthly precipitation amount')
ax1.set_label('Years')
ax1.set_ylabel('RR')

ax2.legend()

ax2.set_title('Monthly precipitation anamolies')
ax2.set_label('Years')
ax2.set_ylabel('PP anamolies')

ax3.legend()

ax3.set_title('Monthly mean Tmin and Tmax')
ax3.set_label('Years')
ax3.set_ylabel('Mean Tmin Tmax')

ax4.legend()

ax4.set_title('Monthly anamolies of the temperature range')
ax4.set_label('Years')
ax4.set_ylabel('T range')

plt.tight_layout()

plt.show() 
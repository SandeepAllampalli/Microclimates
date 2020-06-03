# -*- coding: utf-8 -*-
"""
Created on Sun May 24 15:14:01 2020

@author: sandeep
"""

import pandas as pd
import matplotlib.pyplot as plt


#Exercise1

#Combining data

#Generate 4 data frames, each with 2 columns and 4 rows of arbitrary data: 
#column 1 should be categorical data set and column 2 a metric data set. The 
#categories are: A,B,C,D.

d1 = pd.DataFrame({'colA':['A','B','C','D'], 'colB':[12,23,42,93]})
d2 = pd.DataFrame({'colA':['A','B','C','D'], 'colB':[43,22,77,58]})
d3 = pd.DataFrame({'colA':['A','B','C','D'], 'colB':[85,36,11,78]})
d4 = pd.DataFrame({'colA':['A','B','C','D'], 'colB':[66,54,99,76]})

#Combine the dataframes and generate a continuous numbering of the index.

d = [d1,d2,d3,d4]

com_D = pd.concat(d)

dd = com_D.reset_index(drop = True)

dd

#Calculate the average for each category.

dd_mean = dd.groupby([dd.colA]).mean()

dd_mean


#Exercise2

#Aggregating data

#Import the file ‘rcp85.climate.csv’ and calculate monthly mean values.

src = 'C:/Users/admi/Desktop/Ms ERM/Microclimates/'
file = 'rcp85.climate.csv'

df = pd.read_csv(src+file, sep=';', parse_dates=[0], index_col=0)
print(df)

df_m = df.resample('M').mean()
print(df_m)

#Use the generated monthly mean values and select the time periods
# a) 1960 – 2005, b) 2043 -2100 

a = df_m['1960-01-31':'2005-12-31']
print(a)

b = df_m['2043-01-31':'2100-12-31']
print(b)

#Calculate a mean annual cycle for both periods (a, b).

dfYear1 = a.groupby([pd.DatetimeIndex(a.index).year]).mean()
print(dfYear1)

dfYear2 = b.groupby([pd.DatetimeIndex(b.index).year]).mean()
print(dfYear2)

#Visualize your results

dfYear1.plot(kind='line', x='pcp', y='tmax',color='red')
dfYear2.plot(kind='line', x='pcp', y='tmin',color='blue')
plt.show()

print(dfYear1.describe())

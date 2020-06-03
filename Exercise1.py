# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
from uncertainties import unumpy
import pandas as pd


#Exercise1
#Generate the following objects in Python:

    #1. An array with the dimensions 3 x 5 with arbitrary values.

arr = np.array([(1,2,3,4,5),(4,5,6,7,8),(2,9,8,6,7)])
print(arr)
print(arr.ndim)
print(arr.shape)

    #2. An empty data frame

dfobj = pd.DataFrame()
print(dfobj)

    #3. A data frame with 5 rows. Hint: rows are called ‘index’ in a data frame.

dfobj1 = pd.DataFrame(index=['EmpName','EmpDOB','EmpPlace'])
print(dfobj1, sep='\n')

    #4. A data frame with 3 rows and 2 columns

dfobj2 = pd.DataFrame(columns=['Name','Age'], index=[1,2,3])
dfobj2.loc[1] = ['Kiran', 21]
dfobj2.loc[2] = ['Anand', 19]
dfobj2.loc[3] = ['Karthik', 23]
print(dfobj2)

#Exercise2

#Generate a list in python with 5 different values.

nums = [11,45,32,76,24]
print(nums)

    #1. Append an additional element with the value AA using the function append()

nums.append('AA')
print(nums)
#nums.insert(1,56)

    #2. remove the 2nd element

del nums[1]
#nums.pop(1)
print(nums)

    #3. determine the number of elements in your list

print(len(nums))

#Exercise3

#Read the file ‘climate.dat’ using pandas.

cliData = pd.read_table('climate.dat', sep=';')
print(cliData)

cliData.T.count()

    #1. Calculate the mean value of each column.

print(cliData.mean())

    #2. Calculate the mean value of the column T, i.e. Temperature


print(cliData['T'].mean())




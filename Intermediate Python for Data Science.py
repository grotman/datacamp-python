# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 06:08:30 2017

@author: mgrotowski
"""

# =============================================================================
#                MATPLOTLIB BASICS
# =============================================================================

# importing basic subpackkage for plotting
from matplotlib import pyplot as plt
import numpy as np

# data to plot
x = np.array([-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = x ** 2

# plotting
plt.plot(x, y)
plt.show()
plt.scatter(x, y)
plt.show()

y2 = np.exp(x)
plt.plot(x, y2)
plt.yscale('log')
plt.xlabel('my X variable')
plt.ylabel('my Y variable in log scale')
plt.title('my first customized plot')
plt.grid(True)
plt.xticks([-10, -5, 0, 5, 10], ['-Ten', '-Five', 'Zero', 'Five', 'Ten'])
plt.show()

plt.hist(x, bins=5, rwidth=0.6, color='red')
plt.show()

plt.hist(x, bins=5, normed=True, orientation='horizontal', cumulative=True,
         rwidth=0.8)
plt.show()

plt.clf()

# =============================================================================
#                DICTIONARIES
# =============================================================================
# Keys have to be immutable (lists are not)

countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']
europe = {'spain': 'madrid', 'france': 'paris', 'germany': 'berlin',
          'norway': 'oslo'}
print(europe)
print(europe['spain'])
print(europe.keys())

# adding new key-value pair
europe['poland'] = 'cracow'
print(europe)
# correcting existing key-value pair
europe['poland'] = 'warsaw'
print(europe)
# removing existing key-value pair
del(europe['poland'])
print(europe)

# dictionary of dictionaries & chaining the keys
europe = {'spain': {'capital': 'madrid', 'population': 46.77},
          'france': {'capital': 'paris', 'population': 66.03},
          'germany': {'capital': 'berlin', 'population': 80.62},
          'norway': {'capital': 'oslo', 'population': 5.084}}
print(europe['france']['capital'])
data = {'capital': 'rome', 'population': 59.83}
europe['italy'] = data
print(europe)

# =============================================================================
#                BOOLEAN OPERATORS
# =============================================================================
print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True or True)
print(True or False)
print(False or True)
print(False or False)

print(not True)
print(not False)
print(not(False))

# not has higher priority than and / or
print(not False and False)
print(not True or True)

my_numbers = np.array([1, 2, 3, 4, 5])
# and / or / not doesn't work for arrays of booleans. You need to use:
print(my_numbers[np.logical_and(my_numbers > 2, my_numbers < 4)])
print(my_numbers[np.logical_or(my_numbers > 2, my_numbers < 4)])
print(my_numbers[np.logical_not(my_numbers > 2)])
print(my_numbers[np.logical_xor(my_numbers > 1, my_numbers < 5)])

# =============================================================================
#                CONDITIONAL STATEMENTS
# =============================================================================
x = 10

if x > 3:
    print('x is greater than 3')

if x > 11:
    print('x is greater than 11')
else:
    print('x is NOT greater than 11')

if x > 15:
    print('x is greater than 15')
elif x > 10:
    print('x is greater than 10')
else:
    print('x is less than or equal to 10')

# =============================================================================
#                PANDAS BASICS
# =============================================================================
import pandas as pd

names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco',
         'Egypt']
dr = [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# pandas' dataframe out of a dictionary
my_dict = {'country': names, 'drives_right': dr, 'cars_per_cap': cpc}
cars = pd.DataFrame(my_dict)
print(cars)

# adding row indexes
row_labels = ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']
cars.index = row_labels
print(cars)

# accessing the columns in dataframe: Pandas Series object
print(cars["country"])
print(type(cars["country"]))

# accessing the columns in dataframe: Pandas Dataframe object
print(cars[["country"]])
print(type(cars[["country"]]))

# accessing the columns in dataframe: multiple columns
print(cars[["country", "cars_per_cap"]])

# accessing the rows in dataframes: slicing
# works the same as for lists and NumPy arrays so the index is zero-based and
# the last element is not included
print(cars[0:2])
print(type(cars[0:2]))

# accessing the rows in dataframes: loc() --> Pandas Series object
# loc <=> indexing based on labels
print(cars.loc["RU"])
print(type(cars.loc["RU"]))

# accessing the rows in dataframes: loc() --> Pandas DataFrame object
print(cars.loc[["RU"]])
print(type(cars.loc[["RU"]]))

# accessing the rows in dataframes: loc() & multiple rows
print(cars.loc[["RU", "JAP"]])

# accessing the rows & columns in dataframes: loc() & slicing across 2D
print(cars.loc[["RU"], ["country", "cars_per_cap"]])
print(cars.loc[:, ["country", "cars_per_cap"]])

# accessing the rows in dataframes: iloc() --> Pandas Series object
# iloc <=> indexing based on position (index)
print(cars.iloc[4])
print(type(cars.iloc[4]))

# accessing the rows in dataframes: iloc() --> Pandas DataFrame object
# iloc <=> indexing based on position (index)
print(cars.iloc[[4]])
print(type(cars.iloc[[4]]))

# accessing the rows in dataframes: iloc() & multiple rows
print(cars.iloc[[4, 2]])

# accessing the rows & columns in dataframes: iloc() & slicing across 2D
print(cars.iloc[[4], [1, 0]])
print(cars.iloc[:, [1, 0]])

# filtering pandas dataframe (needs to be done on the Series object!)
moreThan500 = cars["cars_per_cap"] > 500
print(moreThan500)
print(cars[moreThan500])
print(cars[cars["cars_per_cap"] > 500])
print(cars[np.logical_and(cars["cars_per_cap"] > 500, cars["cars_per_cap"] < 750)])

# =============================================================================
#                LOOPS
# =============================================================================

# while loop
myNumber = 100
while myNumber > 1:
    print('My number is still greater than 1: ' + str(myNumber))
    myNumber = myNumber / 6

# for loop over a list
myList = [0, 2, 5, 7, 9]
for m in myList:
    print(m)
for idx, m in enumerate(myList):
    print("myList has number " + str(m) + " at position " + str(idx))

# for loop over a string
for s in "word":
    print(s.capitalize())

# for loop over a range
for n in range(11):
    print(n)

# looping over a dictionary (notice the order in which it goes!)
myDict = {'var1': 1, 'var2': 2, 'var3': 3}
print(myDict)
for key, value in myDict.items():
    print(key + " is " + str(value))

# looping over a NumPy array
myArray = np.array([1, 3, 5, 7])
for ma in myArray:
    print(ma)
my2DArray = np.array([myArray, myArray])
print(my2DArray)
for m in my2DArray:
    print(m)
for m in np.nditer(my2DArray):
    print(m)

# iterating over Pandas dataframe
import pandas as pd
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco',
         'Egypt']
dr = [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
my_dict = {'country': names, 'drives_right': dr, 'cars_per_cap': cpc}
cars = pd.DataFrame(my_dict)
print(cars)

# getting just column names
for c in cars:
    print(c)

# getting row labels as well as rows as Pandas Series object:
for lab, row in cars.iterrows():
    print(lab)
    print(row)

for lab, row in cars.iterrows():
    print(str(lab) + ": " + row["country"])

# adding a column to Pandas DataFrame
for lab, row in cars.iterrows():
    cars.loc[lab, "COUNTRY"] = row["country"].upper()
print(cars)

cars["COUNTRY2"] = cars["COUNTRY"].apply(str.lower)
print(cars)

for idx, r in cars.iterrows():
    cars.loc[idx, 'COUNTRY3'] = r['COUNTRY2'].capitalize()
print(cars)

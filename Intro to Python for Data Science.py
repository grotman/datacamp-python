# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 06:28:30 2017

@author: mgrotowski
"""

# =============================================================================
#                PYTHON BASICS
# =============================================================================

# Variables: printing value and type
savings = 100
print(savings)
print(type(savings))
print(type(1.1))
print(type('abd'))
print(type("abd"))
print(type(True))

# Basic arithmetics
print(3 + 2)
print(3 - 2)
print(3 * 2)
print(3 / 2)
print(3 ** 2)
print(3 % 2)

# Basic string operations
myStr = "abc"
print(myStr)
print(type(myStr))
print(myStr + myStr)
print(myStr * 3)

# Data type conversions
print("myStr = " + str(myStr))
myNumberAsString = "963"
print("myNumberAsString = " + myNumberAsString)
type(myNumberAsString)
# string to integer
print(int(myNumberAsString))
print(type(int(myNumberAsString)))
# string to float
print(float(myNumberAsString))
print(type(float(myNumberAsString)))
# string to boolean
print(bool(myNumberAsString))
print(type(bool(myNumberAsString)))
# integer to boolean
print(bool(0))
print(bool(1))

# more commands on one line
print(bool(0)); print(bool(1))

# =============================================================================
#                LISTS
# =============================================================================
print('==========================')
print('LISTS')

myList = ['a', 'b', 'c', 'd', 'e', 'f']
print(myList)
print(type(myList))

# indexing into a list is ZERO-based!
print(myList[0])
print(myList[1])

# indexing one element returns it (not a list of it)
print(type(myList[1]))

# indexing elements counting from the end
print(myList[-1])
print(myList[-2])
print(myList[-3])

# slicing - beginning index is incluced, ending index is NOT.
# The outcome is a list
print(myList[1:3])
print(type(myList[1:3]))
print(myList[0:7])

# slicing all elements from the first one (including it)
print(myList[:4])

# slicing all elements till the last one (including it)
print(myList[4:])

# Lists of lists
myListOfLists = [['a', 'b', 'c'],
                 ['ab', 'bc', 'ca'],
                 ['e', 'f', 'd']]
print(myListOfLists)
print(myListOfLists[1])
print(myListOfLists[1][1])

# replacing elements of a list
print(myListOfLists)
myListOfLists[1][2] = 'deee'
print(myListOfLists)
myListOfLists[1] = 'no more list in list'
print(myListOfLists)
myListOfLists[0][:2] = ['e', 'd']
print(myListOfLists)

# appending to a list
myListOfLists = myListOfLists + ['some', 'new', 'shit']
print(myListOfLists)

# deleting an element from a list
del(myListOfLists[0])
print(myListOfLists)

# copy semantics: handle
print(myList)
myListCopy = myList
myListCopy2 = myList[:]   # could be myListCopy2 = list(myList)
print(myListCopy)
print(myListCopy2)
myListCopy[0] = 'aaaaaa'
print(myList)
print(myListCopy)
print(myListCopy2)
myListCopy2[-1] = 'fffffff'
print(myList)
print(myListCopy)
print(myListCopy2)

# =============================================================================
#                FUNCTIONS & METHODS
# =============================================================================

# listing function's help
# the argument in "[]" is an optional one
help(complex)
# the arguments with default values are also optional ones
help(sorted)

# some example string methods
room = "poolhouse"
room_up = room.upper()
print(room)
print(room_up)
print(room.count("o"))
print(room.replace("o", "a"))
print(room)
print(room.startswith('p'))

# some list methods (some modify the list; others do not)
print(myList)
myList.append('ggg')
print(myList)
print(myList.index('c'))
print(myList.count('f'))
myList.remove('ggg')
print(myList)
myList.reverse()
print(myList)

# =============================================================================
#                PACKAGES
# =============================================================================
# Package = directory of python scripts. Each script is a "module"
# Packages are installed via for example pip:
# pip3 install numpy
# Packages have to be imported and there are different ways of doing this:

import math          # <-- general import makes all package functions available
print(math.pi)

from math import pi  # <-- selective import; only pi is available
print(pi)

from math import pi as MyPie  # <-- selective import + assigning a name
print(MyPie)

# =============================================================================
#                NUMPY basics of basics
# =============================================================================
import numpy as np
python_list = [1, 2, 3]
numpy_array = np.array(python_list)
print(python_list + python_list)
print(numpy_array + numpy_array)

print(numpy_array + 2)
print(numpy_array / (numpy_array - 2))
print(numpy_array > 1)
print(numpy_array[numpy_array > 1])

# Type coercion - if numpy array is created out of a list with elements of
# different types then these types are unified
print(np.array([True, 1, 2]) + np.array([3, 4, False]))

# 2-D arrays
my2DArray = np.array([[1, 2, 3, 4], [-4, -3, -2, -1]])
print(my2DArray)
print(my2DArray[1][1])
print(my2DArray[1, 1])
print(my2DArray[:, 1])
print(my2DArray[1, :])
print(my2DArray.shape)

# basic statistics
print(np.mean(my2DArray[:, 1]))
print(np.mean(my2DArray))
print(np.median(my2DArray))
print(np.sum(my2DArray))

# random numbers
np.random.seed(111)
print(np.random.rand())
np.random.seed(111)
print(np.random.rand())

print(np.random.randint(0, 2))
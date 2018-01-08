# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 06:28:06 2017

@author: mgrotowski
"""

# =============================================================================
#                ITERATORS
# =============================================================================

# Iterables = objects over which one can iterate
# Examples of iterables: lists, strings, dictionaries, range objects
#
# More precise definition of an iterable: this is an object that has iter()
# method. This method, when applied, creates an iterator. The FOR loop, under
# the hood, calls the iter() method of an iterable.
#
# Iterator = object that has next() method
#
# Example:
word = 'abcde'
iterator_word = iter(word)
print(next(iterator_word))
print(next(iterator_word))
print(next(iterator_word))
print(next(iterator_word))
print(next(iterator_word))

# If you call next on iterator_word one more time then you'll get StopIteration
# exception

# Star (splat?) operator unpacks all elements of the iterator at once
iterator_word = iter(word)
print(*iterator_word)

# adding to any iterable an index and returning items of the iterable along
# with their indexes
myList = ['item1', 'item2', 'item3', 'item4']
e = enumerate(myList)
print(type(e))
e_list = list(e)
print(e_list)

# Using optional input 'start' one may change the starting value for indexes
e_list = list(enumerate(myList, start=1))
print(e_list)

# outcome of enumerate is an iterable so one can iterate over it
for index, value in enumerate(myList, start=8):
    print(index, value)

# zip(): combining any numer of iterables and returning tuples consisting of
# the first elements of the iterables, the second element of the iterables
# and so forth until the shortest sequence is exhausted
myList2 = ['n1', 'n2', 'n3']
zippo = zip(myList, myList2)
print(type(zippo))
print(zippo)

for el in zippo:
    print(el)

# before iterating over it again we have to reset the iterator!
zippo = zip(myList, myList2)
for el1, el2 in zip(myList, myList2):
    print(el1, el2)

# before iterating over it again we have to reset the iterator!
zippo = zip(myList, myList2)
print(*zippo)

# Unpacking to original tuples
myTupple1 = ('i1', 'i2', 'i3')
myTupple2 = ('a1', 'a2', 'a3')
zippo2 = zip(myTupple1, myTupple2)
myT1, myT2 = zip(*zippo2)
print(myT1 == myTupple1)
print(myT2 == myTupple2)

# Using iterators to load large data pieces into memory

#import pandas as pd
# results = 0
# for chunk in pd.read_csv('filepath', chunksize=1000):
#     results += sum(chunk['someColumn'])
# print(results)

# =============================================================================
#                LIST \ DICT COMPREHENSIONS
# =============================================================================

# creating list with elements being other list's elements plus 1
myList = [1, 3, 5, 10]
myList2 = [x + 1 for x in myList]
print(myList2)

# list comprehension may be used over any iterable(!)
myList3 = [x + 2 for x in range(5)]
print(myList3)

myList4 = [x + ': ' + y
           for x, y in {'x': 'first variable', 'y': 'second variable'}.items()]
print(myList4)

# list comprehension to replaces nested for loops
# The first example is an ordinary nested loop. In the second example the inner
# loop doesn't depend on the outer loop
# Mind that the order of "for" in list comprehension expression matters (it
# determines the order of nesting of the loops)
myList5 = [(x, y) for x in range(1, 3) for y in range(5, 7)]
print(myList5)

myList6 = [[col for col in range(5)] for row in range(5)]
print(myList6)

# using conditionals on the iterable
myList7 = [x ** 3 for x in range(7) if x % 3 == 0]
print(myList7)

# using conditionals on the output expression
myList8 = [x ** 3 if x % 3 == 0 else 0 for x in range(7)]
print(myList8)

# Dict comprehension: creating a dictionary
# Difference: using curly braces and separating key and value
myDict = {x: -x for x in range(5)}
print(myDict)

# =============================================================================
#                GENERATORS
# =============================================================================

# generator for myList2
# Generator: an object that unlike the list comprehension does not return a
# list but generator object. One can iterate over this object to get elements
# of the list but the list isn't stored in the memory
myList2Gen = (x + 2 for x in range(5))
print(myList2Gen)
for num in myList2Gen:
    print(num)

print(list(myList2Gen))

# One can iterate over a generator using the next method (one more call of next
# would yield StopIteration exception)
myList2Gen = (x + 2 for x in range(5))
print(next(myList2Gen))
print(next(myList2Gen))
print(next(myList2Gen))
print(next(myList2Gen))
print(next(myList2Gen))

# Generators are examples of "lazy evaluation": the expression is evaluated
# only when it's value is needed
# This is handy when having a huge list for which list comprehension would
# eat up the whole memory
hugeGen = (x ** 2 for x in range(10 ** 1000000))
for i in range(100):
    next(hugeGen)
print(next(hugeGen))

# Generator functions:
# - return a sequence of values in a form of a generator
# - this returned generator is output using yield keyword
    

def num_sequence(n):
    """Generate values from 0 to input n."""
    i = 0
    while i <= n:
        yield i
        i += 1

mySeq = num_sequence(10)
print(type(mySeq))
for num in mySeq:
    print(num)
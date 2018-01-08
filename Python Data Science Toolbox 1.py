# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 06:09:27 2017

@author: mgrotowski
"""

# =============================================================================
#                USER-DEFINED FUNCTIONS
# =============================================================================


# Function without inputs and outcomes
# Mind the docstring documenting the function
def sayHello():
    """Prints out a greeting."""
    print("Hey Dude!")


sayHello()


# Function with one mandatory input and without outcomes
def squareMe(value):
    """Squares an input and prints the outcome out."""
    print(value ** 2)


squareMe(2)
squareMe(4)


# Function with one mandatory input and one outcome
def cubeMe(value):
    """Returns cube of an input."""
    return value ** 3


print(cubeMe(2))
print(cubeMe(4))


# Function with multiple inputs
def raiseToPower(value, power):
    return value ** power


print(raiseToPower(2, 2))
print(raiseToPower(3, 3))

# NoneType outcomes
myOut = squareMe(2)
print(myOut)
print(type(myOut))

# tuples: like list but immutable (values cannot be changed after creation),
# may be unpacked
myTuple = (1, 2, 3)
print(myTuple)
a, b, c = myTuple
print(a)
print(b)
print(c)


# Function with multiple outputs - using the tuple
def sumAndDiff(a, b):
    """calculates sum and the difference of inputs"""
    return (a + b, a - b)


a = 10
b = 3
aPlusB, aMinusB = sumAndDiff(a, b)
print(aPlusB)
print(aMinusB)

# Scopes:
# - local     - a function
# - enclosing - scope of an enclosing function
# - global    - main script
# - built-in  - scope in predefined built-ins module
#
# IMPORTANT: when a value is not accessible in local scope then Python looks
#            for it in the enclosing scope. If no success then in global scope
#            If the name isn't present in the global scope then the built-in
#            scope is searched!
#
# So every function can use the local, enclosing and the global scope and even
# built-ins scope!
#
# The access to all "upper level scopes" is read only and is known as CLOSURE


newVal = 5


# This function is written with a gotcha: it does not use the value input
# it does NOT change the newVal variable value
def invertMe(value):
    """Returns reciprocal of the input value"""
    return 1 / newVal


print(invertMe(1))
print(invertMe(10))
print(newVal)


# This function is written with a gotcha: it does not use the value input
# and it does change the newVal variable value
def invertMe2(value):
    """Returns reciprocal of the input value"""
    global newVal
    newVal = 1 / newVal
    return newVal


print(invertMe2(1))
print(newVal)
print(invertMe2(10))
print(newVal)


# =============================================================================
#                NESTED FUNCTIONS
# =============================================================================
# Nested functions: if cannot find a variable they go first to the enclosing
# function's scope and only then to the global scope
# This is known as LEGB: L = local, E = enclosing, G = global and B = built-ins
def enclosingFunc(value1, value2, value3):
    """Returns sum of squared inputs"""

    def nestedFunc(value):
        return value ** 2

    return nestedFunc(value1) + nestedFunc(value2) + nestedFunc(value3)


print(enclosingFunc(3, 4, 5))


# Nested function: the enclosing function returns a function
def outerFunc(power):
    """Returns power function with power input by user"""

    def inner(x):
        """Raise x to power of "power" defined in enclosing function"""
        return x ** power

    return inner


mySmartFunc = outerFunc(3)
print(mySmartFunc(4))


# Use of "nonlocal" keyword to alter a value in scope of enclosing function
def outerFuncScrewed(power):
    """Returns power function with power input by user (but does not work;
    always cubes)"""

    def inner(x):
        """Raise x to power of "power" defined in enclosing function"""
        nonlocal power
        power = 3
        return x ** power

    return inner


mySmartFunc2 = outerFuncScrewed(1)
print(mySmartFunc2(4))

# =============================================================================
#                DEFAULT & FLEXIBLE ARGUMENTS
# =============================================================================


def myDiffFunc(a, b=10):
    """Subtracts from the first argument the second one, or 10 if the latter is
    not provided"""
    return a - b


print(myDiffFunc(10, 1))
print(myDiffFunc(10))


# function with flexible numeric arguments (args is a tuple)
# The star * is necessary; the "args" is not a keyword
# The flexible argument might follow some fixed argument
def mySumFunc(*args):
    """Sums all input arguments"""
    s = 0
    for a in args:
        s += a
    return s


print(mySumFunc(1, 2, 3))
print(mySumFunc(1))
print(mySumFunc(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# function with flexible key-value arguments (kwargs is a dictionary)
# The double star ** is necessary; the "kwargs" is not a keyword
# The flexible argument might follow some fixed argument
def myPrinterFunc(**kwargs):
    """Prints out all key-value inputs"""
    for key, value in kwargs.items():
        print(key + ": " + value)


myPrinterFunc(input1="myFirstInput", input2="mySecondInput")

# =============================================================================
#                LAMBDA FUNCTIONS
# =============================================================================

# simple lambda function
cubeMeLambda = lambda x: x ** 3
print(cubeMeLambda(2))

powerMeLambda = lambda x, y: x ** y
print(powerMeLambda(2, 4))

# anonymous function (provided as an input to map, filter or reduce)
someNums = [1, 2, 3, 5]

someNumsSquared = map(lambda x: x ** 2, someNums)
print(someNumsSquared)
print(list(someNumsSquared))

someNumsFiltered = filter(lambda x: x > 2, someNums)
print(list(someNumsFiltered))

from functools import reduce
someNumsSummed = reduce(lambda x, y: x + y, someNums)
print(someNumsSummed)

# =============================================================================
#                HANDLING ERRORS
# =============================================================================


# try - except blocks
def twoToPower(x):
    try:
        return 2 ** x
    except:
        print('x must be int or float type')
        

print(twoToPower(3))
print(twoToPower('hello'))


# being more specific about type of the exception
def twoToPowerBetter(x):
    try:
        return 2 ** x
    except TypeError:
        print('x must be int or float type')


print(twoToPowerBetter(3))
print(twoToPowerBetter('hello'))


# raising exceptions
def sqrt(x):
    try:
        if x < 0:
            raise ValueError('Input must be non-negative!')
        return x ** 0.5
    except TypeError:
        print('Input must be int or float')


print(sqrt(2))
print(sqrt('hello'))
print(sqrt(-2))


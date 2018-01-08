# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 06:41:59 2017

@author: mgrotowski
"""

# =============================================================================
#                DECORATORS
# =============================================================================
# In the context of design patterns, decorators dynamically alter the
# functionality of a function, method or class without having to directly use
# subclasses. This is ideal when you need to extend the functionality of
# functions that you don't want to modify.
# "dynamically" means it happens on a runtime. Using subclass would add the
# extra features already at compile time.


# Example #1: decorator function; Python syntax for decorators NOT used
# decorateWithPTags is an example of a simple decorator. It takes a function
# as an input and returns other function that augments functionality of the
# input function
def getMyText(name):
    return 'Given name is: ' + name


def decorateWithPTags(func):
    def funcWrapper(name):
        return '<p>' + func(name) + '</p>'
    return funcWrapper


print(getMyText('Micho'))
myDecoratedText = decorateWithPTags(getMyText)
print(myDecoratedText('Micho'))


# Example #2: using Python's syntax for building decorators
# This is the example #1 rewritten but using this special syntax
def decorateWithPTags2(func):
    def funcWrapper(name):
        return '<p>' + func(name) + '</p>'
    return funcWrapper


@decorateWithPTags2
def getMyText2(name):
    return 'Given name is: ' + name


print(getMyText2('Micho2'))


# Example #3: nesting the decorators (the order matters!)
def decorateWithDivTags(func):
    def funcWrapper(name):
        return '<div>' + func(name) + '</div>'
    return funcWrapper


def decorateWithHTMLTags(func):
    def funcWrapper(name):
        return '<html>' + func(name) + '</html>'
    return funcWrapper


@decorateWithPTags2
@decorateWithDivTags
@decorateWithHTMLTags
def getMyText3(name):
    return 'Given name is: ' + name


@decorateWithHTMLTags
@decorateWithDivTags
@decorateWithPTags2
def getMyText4(name):
    return 'Given name is: ' + name


print(getMyText3('Micho3'))
print(getMyText4('Micho4'))


# Example #4: decorating class' method
def decorateWithPTags4Method(func):
    def funcWrapper(self):
        return '<p>' + func(self) + '</p>'
    return funcWrapper


class Person(object):
    def __init__(self):
        self.name = "John"
        self.family = "Doe"

    @decorateWithPTags4Method
    def fullName(self):
        return self.name + ' ' + self.family


myPerson = Person()
print(myPerson.fullName())


# Example #5: passing arguments to decorators
def decoratorWithUniversalTags(tagName):
    def innerDecorator(func):
        def funcWrapper(name):
            return "<" + tagName + ">" + func(name) + "</" + tagName + ">"
        return funcWrapper
    return innerDecorator


@decoratorWithUniversalTags('html')
@decoratorWithUniversalTags('div')
def getMyText5(name):
    return 'Given name is: ' + name


print(getMyText5('Micho5'))

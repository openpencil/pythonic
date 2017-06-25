# This is a comment
""" This is a
multiline comment
"""

# Calculations
# Set count_to equal to the sum of two big numbers
count_to = 1000 + 8000
print(count_to)

# Exponentiation
eggs = 10 ** 2

# Modulo operator
spam = 4 % 3

# Sometime function adds on (if function adds on to the class)
# i.e if there is a method that belongs to the class of the object
# Methods that use dot notation only work with strings.
# On the other hand, len() and str() can work on other data types.
print(str(spam).lower())

# Replacement sprintf style
string_1 = "Rockville"
string_2 = "place"
print("Let's not go to %s. 'Tis a silly %s." % (string_1, string_2))

# Getting help from Python
 # help(<object>)
 # dir(), which shows you all the object’s methods,
 # <object>.__doc__, which shows you its documentation string:
# help(print)
# print(dir(print()))
print.__doc__

# Indentation and Dedentation
# Statements that expect an indentation level end in a colon (:)
#  increment/decrement values using the += and -= operators respectively by the right-hand amount).
# When applied to a string, += concatenates the right-hand string to the left-hand string
# This swaps the variables in one line(!).
# It doesn't violate strong typing because values aren't
# actually being assigned, but new objects are bound to
# the old names.
print(string_1)
print(string_2)
string_1, string_2 = string_2, string_1
print(string_1)
print(string_2)


# The data structures available in python are lists, tuples and dictionaries.
# Sets are available in the sets library (but are built-in in Python 2.5 and later).
# Similar to R list: Lists are like one-dimensional arrays (but you can also have lists of other lists)
# Named list in R: dictionaries are associative arrays (a.k.a. hash tables) and
# What is this in R? tuples are immutable one-dimensional arrays
# Python “arrays” can be of any type, so you can mix e.g. integers, strings, etc in lists/dictionaries/tuples).
# The index of the first item in all array types is 0.
# Negative numbers count from the end towards the beginning, -1 is the last item.
# Also true in R: Variables can point to functions. The usage is as follows:

# list of a number, another list, a tuple
sample = [1, ["another", "list"], ("a", "tuple")]
mylist = ["List item 1", 2, 3.14]
# Reassignment
mylist[0] = "List item 1 again" # We're changing the item.
mylist[-1] = 3.21 # Here, we refer to the last item.
# Similar to named list. Names are in quotes. Named list is in curly braces, and is called a dictionary
# Note that the keys (or names) are assigned to values (elements) using colon (and not the equal sign)
mydict = {"Key 1": "Value 1", 2: 3, "pi": 3.14}
mydict["pi"] = 3.15 # This is how you change dictionary values.
mytuple = (1, 2, 3)
myfunction = len
print(myfunction(mylist))

# You can access array ranges using a colon (:).
# Leaving the start index empty assumes the first item, leaving the end index assumes the last item.
# Indexing is inclusive-exclusive, so specifying [2:10] will return items [2] (the third item, because of 0-indexing)
# to [9] (the tenth item), inclusive (8 items).
# Negative indexes count from the last item backwards (thus -1 is the last item) like so:
# [:] is everything:everything
print(mylist[:])
print(mylist[0:2])
print(mylist[-3:-1])
print(mylist[1:])
# Adding a third parameter, "step" will have Python step in
# N item increments, rather than 1.
# E.g., this will return the first item, then go to the third and
# return that (so, items 0 and 2 in 0-indexing).
# Syntax (first index: last index : by increments)
print(mylist[::2])

# strings can use either single or double quotation marks, and you can have quotation marks of
# one kind inside a string that uses the other kind (i.e. “He said ’hello’.” is valid).
# Multiline strings are enclosed in triple double (or single) quotes (""").
# Python supports Unicode out of the box, using the syntax u”This is a unicode string”.
# To fill a string with values, you use the % (modulo) operator and a tuple.
# R reference: A tuple is used in filling in the sprintf like statement
# Each %s gets replaced with an item from the tuple, left to right, and
# you can also use dictionary substitutions, like so:
print("Name: %s\n Number: %s\n String: %s" % (string_1, 3, 3 * "-"))

strString = """This is
a multiline
string."""

# WARNING: Watch out for the trailing s in "%(key)s".
# QUECHIN!!!!!!!!!!
print("This %(verb) a %(noun)s." % {"noun": "test", "verb": "is"})

# Flow control statements are if, for, and while.
# There is no switch; instead, use if.
# Use for to enumerate through members of a list.
# To obtain a list of numbers, use range(<number>).
# This line below is a difference in python3. You have to convert the range(10) to list
rangelist = list(range(10))
print(rangelist)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in rangelist:
     # Check if number is one of
     # the numbers in the tuple.
     if number in (3, 4, 7, 9):
         # "Break" terminates a for loop without
         # executing the "else" clause.
         break
     else:
         # "Continue" starts the next iteration
         # of the loop. It's rather useless here,
         # as it's the last statement of the loop.
        print(number)
else:
     # The "else" clause is optional and is
     # executed only if the loop didn't "break".
     pass # Do nothing

if rangelist[1] == 2:
    print("The second item (lists are 0-based) is 2")
elif rangelist[1] == 3:
    print("The second item (lists are 0-based) is 3")
else:
    print("Dunno")

while rangelist[1] == 1:
    print("it is one")
    rangelist[1] = 2

# Functions are declared with the def keyword.
# Optional arguments are set in the function declaration with a default value.
# For named arguments, the name of the argument is assigned a value.
# Functions can return a tuple (and using tuple unpacking you can effectively return multiple values).
# Lambda functions are ad hoc functions that are comprised of a single statement.
funcvar = lambda x: x + 1
print(funcvar(1))

# Parameters are passed by reference, but immutable types (tuples, ints, strings, etc)
# cannot be changed in the caller by the callee.
# This is because only the memory location of the item is passed,
# and binding another object to a variable discards the old one,
# so immutable types are replaced. For example:
# Same as def funcvar(x): return x + 1


# an_int and a_string are optional, they have default values
# if one is not passed (2 and "A default string", respectively).
def passing_example(a_list, an_int=2, a_string="A default string"):
    a_list.append("A new item")
    # changed default value
    an_int = 4
    return a_list, an_int, a_string

my_list = [1, 2, 3]
my_int = 10
print(my_list)
print(passing_example(a_list = my_list, an_int = my_int))
# ([1, 2, 3, 'A new item'], 4, "A default string")
print(my_list)
print(my_int)

# Python supports a limited form of multiple inheritance in classes.
# Private variables and methods can be declared (by convention,
# this is not enforced by the language) by adding at least two leading
# underscores and at most one trailing one (e.g. __spam). We can
# also bind arbitrary names to class instances. An example follows:

# what is a class? Simply a logical grouping of data and functions
# (these functions are frequently referred to as "methods" when defined within a class).
# calling a class creates an object - an instance of a class.
#self is a reference to an instance of a class
class MyClass(object):
    # variable called common. this is an attribute of any instance of the class.
    # i.e. the "common" attribute is 10, common to all instances of the class, MyClass.
    common = 10
    # init is a constructor for the class
    # After this function, the class is initialized into an instance.
    # The rule of thumb is, don't introduce a new attribute outside of the __init__ method,
    # otherwise you've given the caller an object that isn't fully initialized.
    # An instance of MyClass will have a fully initialized object "myvariable" and nothing else.
    # A function in a class is called a method
    def __init__(self):
        self.myvariable = 3
    # This is an instance method i.e. can only run on an instance of the class
    def myfunction(self, arg1, arg2):
        return self.myvariable
    # static methods are universal methods - just like universal variables
#    @staticmethod
#    def make_car_sound():
#        print 'VRooooommmm!'
     # "child" class derives the data and behavior of a "parent" class.
#    @classmethod
#    def is_motorcycle(cls):
#        return cls.wheels == 2

# Abstract Base Classes are classes that are only meant to be inherited from; you can't create instance of an abstract base class
# If a class has an abstract method, it cannot be instantiated
# Keywords in python
import keyword
print(keyword.kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert', 'break',
# 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
# 'finally', 'for', 'from', 'global', 'if', 'import', 'in',
# 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
# 'return', 'try', 'while', 'with', 'yield']

# This is the class instantiation
classinstance = MyClass()
print(classinstance.myfunction(1, 2))
# 3
# This variable is shared by all instances.
classinstance2 = MyClass()
print(classinstance.common)
# 10
# Global class-wide reassignment of common variable
MyClass.common = 30
print(classinstance.common)
print(classinstance2.common)
# 30
# Instance-specific reassignment of common variable
classinstance.common = 10
print(classinstance.common)
# 10
print(classinstance2.common)
# 30
MyClass.common = 50
print(classinstance.common)
# # This has not changed, because "common" is
# # now an instance variable.
print(classinstance2.common)
#
# This class inherits from MyClass. The example
# class above inherits from "object", which makes
# it what's called a "new-style class".
# Multiple inheritance is declared as:
class OtherClass(MyClass):
    # The "self" argument is passed automatically
    # and refers to the class instance, so you can set
    # instance variables as above, but from inside the class.
    def __init__(self, arg1):
        self.myvariable = 3
        print(arg1)

classinstance = OtherClass("hello")
# hello
print(classinstance.myfunction(1, 2))
# 3
# This myfunction method comes from the parent class
classinstance.test = 10
print(classinstance.test)
# 10
# This class doesn't have a .test member, but
# # we can add one to the instance anyway. Note
# # that this will only be a member of classinstance.

# Exceptions in Python are handled with try-except [exceptionname] blocks:
#
import math
def some_function():
    try:
        # Division by zero raises an exception
        10 / math.log(0)
    except ZeroDivisionError:
        print("Oops, invalid.")
    except ValueError:
        print("Log zero is minus infinity")
    else:
        # Exception didn't occur, we're good.
        pass
    finally:
         # This is executed after the code block is run
         # and all exceptions have been handled, even
         # if a new exception is raised while handling.
         print("We're done with that.")

some_function()
# Oops, invalid.
# We're done with that.

# Importing
# External libraries are used with the import [libname] keyword.
# You can also use from [libname] import [funcname] for individual
# functions. Here is an example:

import random
from time import clock

randomint = random.randint(1, 100)
print(randomint)
# 64
# File I/O
# Python has a wide array of libraries built in.
# As an example, here is how serializing (converting data structures
# to strings using the pickle library) with file I/O is used:
#
# Write binary file
import pickle
mylist = ["This", "is", 4, 13327]
# Open the file ~/repos/pythonic/stats for writing.
# The letter r before the filename string is used to prevent backslash escaping.
# wb: writing a binary file | stats will not be human readable, its like RDS
myfile = open(r"/Users/jshankar/repos/pythonic/stats", "wb")
pickle.dump(mylist, myfile)
myfile.close()

myfile = open(r"/Users/jshankar/repos/pythonic/stats", "rb")
print(pickle.load(myfile))

# Write human-readable file | only strings can be written with the general function .write
myfile2 = open(r"/Users/jshankar/repos/pythonic/stats2", "w")
myfile2.write(str(mylist))
myfile2.close()
#
#
# Miscellaneous
# Conditions can be chained: 1 < a < 3 checks that a is both less than 3 and greater than 1.
# You can use del to delete variables or items in arrays.
# List comprehensions provide a powerful way to create and manipulate lists.
# They consist of an expression followed by a for clause followed by zero or more
# if or for clauses, like so:
lst1 = [1, 2, 3]
lst2 = [3, 4, 5]
print([x * y for x in lst1 for y in lst2])
print([(x,y) for x in lst1 for y in lst2])
print([x for x in lst1 if 4 > x > 1])
# [2, 3]
# Check if a condition is true for any items.
# # "any" returns true if any item in the list is true.
# print if there is a remainder i.e. not divisible by 3
print(any([i % 3 for i in [3, 9, 24, 24, 12]]))
#
# Check for how many items a condition is true.
print(sum(1 for i in [3, 3, 4, 4, 3] if i == 4))
print(sum(1 for i in [3, 3, 4, 4, 3]))
# 2
del lst1[0]
print(lst1)
# [2, 3]
# delete a created list. equivalent to rm
del lst1
# Global variables are declared outside of functions
# and can be read without any special declarations,
# but if you want to write to them you must declare
# them at the beginning of the function with the global
# keyword, otherwise Python will bind that object to a
# new local variable (be careful of that, it’s a small
# catch that can get you if you don’t know it). For example:
number = 5
def myfunc():
     # This will print 5.
     print(number)

myfunc()

def anotherfunc():
    # This raises an exception because the variable has not
    # been bound before printing. Python knows that it an
    # object will be bound to it later and creates a new, local
    # object instead of accessing the global one.
    print(number)
    number = 3

# anotherfunc()

def yetanotherfunc():
    global number
    print(number)
    # This will correctly change the global.
    number = 3
    print(number)

yetanotherfunc()

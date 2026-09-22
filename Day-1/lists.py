# Python Lists

# List
# Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
# Lists are created using square brackets:

thislist = ["apple", "banana", "cherry"]
print(thislist)


# List Items
# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.

# List Length
# To determine how many items a list has, use the len() function:
# Print the number of items in the list:

thislist = ["apple", "banana", "cherry"]
print(len(thislist))


# A list can contain different data types:
# A list with strings, integers and boolean values:
list1 = ["abc", 34, True, 40, "male"]


# What is the data type of a list?
mylist = ["apple", "banana", "cherry"]
print(type(mylist))


# Python Collections (Arrays)
# There are four collection data types in the Python programming language:
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members


# Range of Indexes
# Return the third, fourth, and fifth item:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])


# Change Item Value
# Change the second item:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)


# Change a Range of Item Values
# Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
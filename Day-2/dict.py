# Dictionary
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)


# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
# Print the "brand" value of the dictionary:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])


# The values in dictionary items can be of any data type:
# String, int, boolean, and list data types:

this_dict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(this_dict)



# Duplicates Not Allowed
# Dictionaries cannot have two items with the same key:
# Duplicate values will overwrite existing values:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)


# Print the data type of a dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))



# The dict() Constructor
# It is also possible to use the dict() constructor to make a dictionary.
# Using the dict() method to make a dictionary:

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)


# Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets:
# Get the value of the "model" key:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
# There is also a method called get() that will give you the same result:
y= thisdict.get("year")
print(y)

# Get Keys
# The keys() method will return a list of all the keys in the dictionary.
z = thisdict.keys()
print(z)

# Get Values
# The values() method will return a list of all the values in the dictionary.
g = thisdict.values()
print(g)


# ----------------------------------------------------------------------------------------
# Get Items
# The items() method will return each item in a dictionary, as tuples in a list.
# Get a list of the key:value pairs
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.items()
print(x)
# output: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])


# Change Values
# You can change the value of a specific item by referring to its key name:
# Change the "year" to 2018:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

# The update() method will update the dictionary with the items from the given argument
# Update the "year" of the car by using the update() method:
thisdict.update({"year": "2026"})
print(thisdict)


# Adding Items
# Adding an item to the dictionary is done by using a new index key and assigning a value to it:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)



# Removing Items
# There are several methods to remove items from a dictionary:
# The pop() method removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)




# The del keyword removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

# The del keyword can also delete the dictionary completely:
#************* del thisdict
# print(thisdict)


# The clear() method empties the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict) # output--- {}


# Copy a Dictionary
# You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
# There are ways to make a copy, one way is to use the built-in Dictionary method copy().

# Make a copy of a dictionary with the copy() method:

thisdict = {
  "brand": "brezza",
  "model": "Mustang",
  "year": 2019
}
mydict = thisdict.copy()
print(mydict)

# Another way to make a copy is to use the built-in function dict().
my_dict =dict(thisdict)
print(my_dict)


# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# Nested Dictionaries
# A dictionary can contain dictionaries, this is called nested dictionaries.

dict2 = {"name": "GAutam",
          "Age":"22",
          "city":"jaipur",
          "AddREss": {"street": "Krishna nagar", 
                      "flat":601,
                      "area":"patrakar Colony"}
        }
print(dict2)



# Or, if you want to add three dictionaries into a new dictionary:
# Create three dictionaries, then create one dictionary that will contain the other three dictionaries:

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)

# Access Items in Nested Dictionaries
# To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary:
# Print the name of child 2:

print(myfamily["child2"]["name"])
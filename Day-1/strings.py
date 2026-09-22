# Strings
# Strings in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello".

print("Hello")
print('Hello')

# Quotes Inside Quotes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# Multiline Strings
# we can use three double quotes:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)


# Or three single quotes:
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)


# Strings are Arrays
# Like many other popular programming languages, strings in Python are arrays of unicode characters.
# However, Python does not have a character data type, a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.
a = "Hello, World!"
print(a[1])


# Looping Through a String
# Loop through the letters in the word "banana":
for x in "banana":
  print(x)


# String Length
# To get the length of a string, use the len() function.  
a = "Hello, World!"
print(len(a))


# Check String
# To check if a certain phrase or character is present in a string, we can use the keyword in.

# Check if "free" is present in the following text:
txt = "The best things in life are free!"
print("free" in txt)



# Python - Slicing Strings
# We can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.
b = "Hello, World!"
print(b[2:5])


# Slice From the Start
b = "Hello, World!"
print(b[:5])


# Slice To the End
b = "Hello, World!"
print(b[2:])

# Negative Indexing
b = "Hello, World!"
print(b[-5:-2])


# Upper Case
# The upper() method returns the string in upper case:
a = "Radhe Radhe !"
print(a.upper())


# Lower Case
a = "Hello, World!"
print(a.lower())


# Remove Whitespace
# The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"


# Replace String
# The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))


# String Concatenation
a = "Hello"
b = "World"
c = a + " " + b
print(c)


# String Format
# F-Strings
# to specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
age = 36
txt = f"My name is John, I am {age}"
print(txt)
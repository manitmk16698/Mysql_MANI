"""
A string is a sequence of characters Python treats anything inside quotes as string.
Python has no char datatype ,python treats single char as a string of length one.
"""

#Creating string

Name="Manikanta"
Gender='Male'

#Creating multiline string 

s = """I am Learning
Python String on GeeksforGeeks"""
print(s)

s = '''I'm a 
Geek'''
print(s)

#Accessing characters  in a string 
"""
Strings in python are sequence of characters ,
so we can access each character using indexing.
Indexing starts from 0 and  -1 from end.
"""
s = "GeeksforGeeks"

# Accesses first character: 'G'
print(s[0])  

# Accesses 5th character: 's'
print(s[4]) 

"""
Note: Accessing an index out of range will cause an IndexError. 
Only integers are allowed as indices and using a float or other types will result in a TypeError.
"""

#Accessing strings with negative indexing

"""
Python allows negative address references to access characters from back of the String,
e.g. -1 refers to the last character, -2 refers to the second last character, and so on. 
"""
s = "GeeksforGeeks"

# Accesses 3rd character: 'k'
print(s[-10])  

# Accesses 5th character from end: 'G'
print(s[-5]) 

#Slicing 

s = "GeeksforGeeks"

# Retrieves characters from index 1 to 3: 'eek'
print(s[1:4])  

# Retrieves characters from beginning to index 2: 'Gee'
print(s[:3])   

# Retrieves characters from index 3 to the end: 'ksforGeeks'
print(s[3:])   

# Reverse a string
print(s[::-1])

#Immutability

"""
Strings in Python are immutable. This means that they cannot be changed after they are created.
If we need to manipulate strings then we can use methods like concatenation, 
slicing, or formatting to create new strings based on the original.
"""

s = "geeksforGeeks"

# Trying to change the first character raises an error
# s[0] = 'I'  # Uncommenting this line will cause a TypeError

# Instead, create a new string
s = "G" + s[1:]
print(s)

"""
Deleting a String
In Python, it is not possible to delete individual characters from a string since strings are immutable.
 However, we can delete an entire string variable using the del keyword.
"""
s = "GfG"

# Deletes entire string
del s  


"""
Updating a String
To update a part of a string we need to create a new string since strings are immutable.
"""
s = "hello geeks"

# Updating by creating a new string
s1 = "H" + s[1:]

# replacnig "geeks" with "GeeksforGeeks"
s2 = s.replace("geeks", "GeeksforGeeks")
print(s1)
print(s2)

#
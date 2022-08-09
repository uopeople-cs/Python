# -*- coding: utf-8 -*- 
#----------------------------------------------------------------------------
# Created By  : mawero83
# Created Date: 08/03/2022
# version ='1.0'

""" This program is an example of different Python variables """

# In Python you don't need to specify the datatype, the data itself drives the type

# Integer
my_integer=10
my_float=1.1
my_string="UoPeople"
my_list=[1,2,3,4,5]
# The following is a special type
my_dictionary={}

# A dictionary is a key, value pair, it is also called a hash table and comes with great
# performance benefits
my_dictionary['item1']="content 1"

# You can get the item by calling it like this:
my_dictionary['item1']

# or by using the get method
my_dictionary.get("item1")

# If the item doesn't exist in the dictionary, the response will be empty
# so you should consider to use a default
my_dictionary.get("item1","your default value")

# In this case, if the item doesn't exist, you will get a default value back

# Your dictionary object has iterable objects, like .keys(), or .values(), and .items()
# that makes it easy to iterate through it, for example.

# .items provides a list of sets = [()] with all the key value pairs.

for k, v in my_dictionary.items():
    print ("The key is "+k+" and the value is "+v)

# The example above walks a dictionary and shows the keys and values
# Note the usage of the print method, it is using in-t


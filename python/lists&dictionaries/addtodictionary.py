'''
Created on Jul 7, 2013

@author: jillian
'''
"""
A new key-value pair in a dictionary is created by assigning a new key, like so:

dict_name[new_key] = new_value
An empty pair of curly braces {} is an empty dictionary, just like an empty pair of [] is an empty list.

The length len() of a dictionary is the number of key-value pairs it has. Each pair counts only once, 
even if the value is a list. (That's right: you can put lists inside dictionaries!)

"""



menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print menu['Chicken Alfredo']

# Your code here: Add some dish-price pairs to menu!
menu["Bananas"] = 10.00
menu["Freshly baked cookies"] = 7.50
menu["French toast"] = 9.00



print "There are " + str(len(menu)) + " items on the menu."
print menu
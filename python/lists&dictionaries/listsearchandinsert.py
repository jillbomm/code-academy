'''
Created on Jul 4, 2013

@author: jillian
'''
"""
You can search through a list with the index() function. my_list.index("dog") will return the first index 
that contains the string "dog". An error will occur if there is no such item.

Items can be added to the middle of a list (instead of to the end) with the insert() function. my_list.insert(4,"cat") 
adds the item "cat" at index 4 of my_list, and moves the item previously at 
index 4 and all items following it to the next index (that is, they all get bumped forward by one).
"""

animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index =    animals.index("duck")# Use index() to find "duck"

# Your code here!
animals.insert(duck_index,"cobra")


print animals # Observe what prints after the insert operation
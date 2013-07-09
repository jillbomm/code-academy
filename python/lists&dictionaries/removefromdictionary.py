'''
Created on Jul 8, 2013

@author: jillian
'''
"""Finally, my_list.remove(value) will remove the the first item from my_list that has a value equal to value. 
The difference between del and .remove() is:
del deletes a key and its value based on the key you tell it to delete.
.remove() removes a key and its value based on the value you tell it to delete.
Instructions
Final challenge! Add code that modifies the dictionary inventory in the following ways:

Add a key to inventory called 'pocket'
Set the value of 'pocket' to be a list consisting of the strings 'seashell', 'strange berry', and 'lint'
.sort() the items in the list stored under the 'backpack' key
Remove 'dagger' from the list of items stored under the 'backpack' key
Add 50 to the number stored under the 'gold' key
"""

inventory = {'gold' : 500,
'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 
# Here the dictionary access expression takes the place of a list name 

# Your code here!
inventory["pocket"] = ["seashell","strange berry","lint"] #add a pocket to the list (and lists items in the pocket)
print inventory["backpack"].sort()
inventory["backpack"].remove("dagger")
inventory["gold"] +=50  
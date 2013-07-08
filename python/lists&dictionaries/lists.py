'''
Created on Jul 4, 2013

@author: jillian
'''
"""
You can access an individual item on the list by its index. An index is like an address that identifies the item's place in the list. 
The index appears directly after the list name, in between brackets, like this: list_name[index].

List indices begin with 0, not 1! You access the first item in a list like this: list_name[0]. 
The second item in a list is at index 1: list_name[1]. Computer scientists love to start counting from zero.


A list index behaves like any other variable name! It can be used to access as well as assign values.

You saw how to access a list index like this:

zoo_animals[0]
# Gets the value "pangolin"
You can see how assignment works on line 5:

zoo_animals[2] = "hyena"
# Changes "sloth" to "hyena"

"""
numbers = [5, 6, 7, 8]

print "Adding the numbers at indices 0 and 2..."
print numbers[0] + numbers[2]
print "Adding the numbers at indices 1 and 3..."
# Your code here!
print numbers[1] + numbers[3]

zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]
# Last night our zoo's sloth brutally attacked 
#the poor tiger and ate it whole.

# The ferocious sloth has been replaced by a friendly hyena.
zoo_animals[2] = "hyena"

# What shall fill the void left by our dear departed tiger?
# Your code here!
zoo_animals[3] = "baby otter"
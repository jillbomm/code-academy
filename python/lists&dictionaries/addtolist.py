'''
Created on Jul 4, 2013

@author: jillian
'''
"""
A list doesn't have to have a fixed length—you can add items to the end of a list any time you like! In Python, we say lists are mutable: that is, they can be changed.

You can add items to lists with the built-in list function append(), like this:

list_name.append(item)
Check it out: we've appended a string to suitcase on line 2.

You can get the number of items in a list with the len() function (short for "length"), like so:

len(list_name)
One note before we begin. On the last line we are printing suitcase. When this prints out, you will notice a that the contents seem a little different. 
Each word will have a small u at the beginning. This is because, under the hood, strings in our version of Python are really unicode objects. 
You don't need to know anything about that, except that strings will have type unicode and that "string" == u'string' is True. 
"""

suitcase = [] 
suitcase.append("sunglasses")

# Your code here!
suitcase.append("sunscreen")
suitcase.append("books")
suitcase.append("snacks")



list_length = len(suitcase)

print "There are %d items in the suitcase." % list_length
print suitcase
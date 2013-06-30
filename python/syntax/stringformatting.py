'''
Created on Jun 30, 2013

@author: jillian
'''
"""Did you see that? The % string formatter replaced the %s (the "s" is for "string") in our string with the variables in parentheses. 
(We could have done that by just putting "Camelot" and "place" in parentheses after the string, but we wanted to show you how it works with variables.)

The syntax went like this:

print "%s" % (string_variable)
You can have as many variables (or strings!) separated by commas between your parentheses as you like:

print "The %s who %s %s!" % ("Knights", "say", "Ni")
prints "The Knights who say Ni!" """

name = raw_input("What is your name?")
quest = raw_input("What is your quest?")
color = raw_input("What is your favorite color?")

print "Ah, so your name is %s, your quest is %s " \
"and your favorite color is %s." % (name, quest, color)
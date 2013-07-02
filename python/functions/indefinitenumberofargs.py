'''
Created on Jul 1, 2013

@author: jillian
'''

"""For use when you're not sure how many arguments the user will enter"""


def favorite_actors(*args):
    """Prints out your favorite actorS (plural!)"""
    print "Your favorite actors are:" , args
    
    
favorite_actors("Michael Palin", "John Cleese", "Graham Chapman")
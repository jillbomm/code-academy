'''
Created on Jul 3, 2013

@author: jillian
'''
def hotel_cost(nights):
    return nights * 140

bill = hotel_cost(5)

def add_monthly_interest(balance):
    return balance * (1 + (0.15 / 12))

def make_payment(payment, balance):
    balance -= payment 
    new_balance = add_monthly_interest(balance)
    return "You still owe: " + str(new_balance)
 
print make_payment(100,900)   
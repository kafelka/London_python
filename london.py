# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 15:37:03 2018

@author: nahas
"""
def ask_london():
    response = input("Do you live in London? y/n ")
    if response.lower() == "y":
        print("You're very lucky! Try not to breathe in too deeply :P")
        return True
    elif response.lower() == "n":
        print("Sorry to hear that... Maybe you should visit your capital city from time to time? ;-)")
        return False
    else:
        print("Please answer by typing y or n.")
        return ask_london()
    
    
def ask_activity():
    activity = input("""
 What sort of activity would you be interested in?
 Type first letter:
    * e for entertainment
    * s for shopping
    * c for cultural
    * f for food \n """)
        
        
    if activity.lower() == "e" or activity.lower() == "s" or activity.lower() == "c" or activity.lower() == "f":
        print("Good choice! You selected: {}".format(activity))
        return activity.lower()
    else:
        print("Type the first letter of the activity, please.")
        return ask_activity()
 
def ask_budget():
    
    budget = int(input("What's your budget in £? Please round up to the nearest £. "))
    
    if budget >= 0:
        return budget
    else:
        print("Type a positive number, please.")
        return ask_budget()
    
    
#class Activity():
#    def __init__(self, budget=0, ):
#        self.budget = budget
#        
#        
#class Entertainment(Activity):
#    def __init__(self, budget=0):
#        if budget < 25:
#            print("Your options are: cinemas, ice-skating or a view from Sky Garden.")
#        elif (budget > 25 and budget < 75):
#            print("Your options are: a view from Shard, London Eye or Tower of London.")
#        else:
#            print("Your options are: a night time dinner cruise on Thames, concerts at the O2 or a spa at a 5* hotel")
#            
#class Food(Activity):
#     def __init__(self, budget=0):
#        if budget < 25:
#            print("Your options are: J, K or L")
#        elif (budget > 25 and budget < 75):
#            print("Your options are: M, N or O")
#        else:
#            print("Your options are: P, R or S")
#            
#class Cultural(Activity):
#    def __init__(self, budget=0):
#        if budget < 25:
#            print("Your options are: T, U or V")
#        elif (budget > 25 and budget < 75):
#            print("Your options are: X, Y or Z")
#        else:
#            print("Your options are: AA, BB or CC")
#            
#class Shopping(Activity):
#        def __init__(self, budget=0):
#        if budget < 25:
#            print("Your options are: T, U or V")
#        elif (budget > 25 and budget < 75):
#            print("Your options are: X, Y or Z")
#        else:
#            print("Your options are: AA, BB or CC")

#--------------------------------

name = input("What's your name? ")
print("Hello {}!".format(name.title()))

is_london = ask_london()
activity_type = ask_activity()
user_budget = ask_budget()


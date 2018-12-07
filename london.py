# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 15:37:03 2018

@author: nahas
"""
def ask_london():
    response = input("Do you live in London? y/n ")
    if response.lower() == "y":
        print("Nice!")
        return True
    elif response.lower() == "n":
        print("Oh, maybe you should come and visit it?")
        return False
    else:
        print("Please answer by typing y or n.")
        return ask_london()
    
#class Activity():
#    def __init__(self, budget=0, ):
#        self.budget = budget
#        
#        
#class Entertainment(Activity):
#    def __init__(self, budget=0):
#        if budget < 25:
#            print("Your options are: A, B or C")
#        elif (budget > 25 and budget < 75):
#            print("Your options are: D, E or F")
#        else:
#            print("Your options are: G, H or I")
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



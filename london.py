# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 15:37:03 2018

@author: nahas
"""


def yes_no_london():

    if response == "n":
        print("Oh... You should visit it!")
    elif response == "y":
        print("you answered yes")
    #     activity_selection = input("Imagine you have a day for yourself in London. What sort of activity would you be interested in? Type e for entertainment, f for food, c for cultural or s for shopping")
    #     if activity_selection = "e":
    #         
             
    else: 
        print("Wrong answer. Go back to your city :P")
        
    
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
def yes_no_london(response):

    if response == "n":
        print("Oh... You should visit it!")
        return True
    elif response == "y":
        print("you answered yes")
        return True
    #     activity_selection = input("Imagine you have a day for yourself in London. What sort of activity would you be interested in? Type e for entertainment, f for food, c for cultural or s for shopping")
    #     if activity_selection = "e":
    #         
             
    else: 
        print("Wrong answer. Go back to your city :P")
        return False
        
name = input("What's your name? ")
print("Hello {}!".format(name.title()))

response = input("Do you live in London? y/n ")

if yes_no_london(response):
    print('do next')
else:
    yes_no_london(response)
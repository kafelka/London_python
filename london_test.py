# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 13:44:56 2018

@author: sarika, roxy & maggie
"""

from london_functions import *

name = input("What's your name? ")
print("Hello {}!".format(name.title()))



if ask_london(): 
    activity_type = ask_activity()
    user_budget = ask_budget()
    
    if activity_type == "e":
        bye = Entertainment(user_budget)
        bye.enjoy()
    
    elif activity_type == "s":
        bye = Shopping(user_budget)
        bye.enjoy()
        
    elif activity_type == "c":
        bye = Cultural(user_budget)
        bye.enjoy()
        
    else: #activity_type == "f":
        bye = Food(user_budget)
        bye.enjoy()
else:
    print("Thank you! Bye!")
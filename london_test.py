# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 13:44:56 2018

@author: nahas
"""

from london_functions import *

name = input("What's your name? ")
print("Hello {}!".format(name.title()))



is_london = ask_london()
activity_type = ask_activity()
user_budget = ask_budget()

if activity_type == "e":
    bye = Entertainment(user_budget)
    bye.enjoy()

if activity_type == "s":
    bye = Shopping(user_budget)
    bye.enjoy()
    
if activity_type == "c":
    bye = Cultural(user_budget)
    bye.enjoy()
    
if activity_type == "f":
    bye = Food(user_budget)
    bye.enjoy()
    
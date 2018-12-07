# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 11:31:07 2018

@author: RN
"""


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
        
        
    if activity.lower() == "e":
        print("Good choice! You selected: {}".format(e))
        return activity.lower()
    if activity.lower() =="s":
        print("Good choice! You selected: {}".format(s))
        return activity.lower()
    if  activity.lower() == "c":
        print("Good choice! You selected: {}".format(c))
        return activity.lower()
    if  activity.lower() == "f":
        print("Good choice! You selected: {}".format(f))
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
    
    
class Activity():
    def __init__(self, budget=0, ):
        self.budget = budget
        
        
class Entertainment(Activity):
    def __init__(self, budget=0):
        if budget < 25:
            print("Your options are: cinemas, ice-skating or a view from Sky Garden.")
        elif (budget > 25 and budget < 75):
            print("Your options are: a view from Shard, London Eye or Tower of London.")
        else:
            print("Your options are: a night time dinner cruise on Thames, concerts at the O2 or a spa at a 5* hotel.")
    
class Food(Activity):
     def __init__(self, budget=0):
        if budget <= 25:
            print("Your options are: Nandos, Franco Manca, Tibits, Wagamama or Kerb Food Market in Camden.")
        elif (budget > 25 and budget < 75):
            print("Your options are: Sketch, Tombo (japanese), Dishoom (indian), Jamie Oliver's, Polpo.")
        else:
            print("Your options are: Gordon Ramsey's, dinner by Heston Blumenthal, Benares (indian).")
            
class Cultural(Activity):
    def __init__(self, budget=0):
        if budget <= 25:
            print("Your options are: British Museum, the National Gallery, Tate Modern, Natural History Museum, Victoria and Albert Museum, Science Museum.")
        elif (budget > 25 and budget < 75):
            print("Your options are: theatres and musicals e.g.: The Book of Mormon, Kinky Boots, Chicago, Wicked, Hamilton.")
        else:
            print("Your options are: helicopter tour, ballet e.g. The Nutcracker, Swan Lake, opera: Carmen, La traviata,")
            
class Shopping(Activity):
    def __init__(self, budget=0):
        if budget <= 25:
            print("Your options are: Primark, H&M, New Look.")
        elif (budget > 25 and budget < 75):
            print("Your options are: COS, Next, M&S, Debenhams, John Lewis.")
        else:
            print("Your options are: Harrods, Harvey Nichols, Selfridges.")

#def entertainment_costam(self):
#         print("hi is this working")
     
e="entertainment"
s="shopping"
c="cultural activity"
f="food"
name = input("What's your name? ")
print("Hello {}!".format(name.title()))

is_london = ask_london()
activity_type = ask_activity()
user_budget = ask_budget()

if activity_type == "e":
    Entertainment(user_budget)
if activity_type == "s":
    Shopping(user_budget)
if activity_type == "c":
    Cultural(user_budget)
if activity_type == "f":
    Food(user_budget)
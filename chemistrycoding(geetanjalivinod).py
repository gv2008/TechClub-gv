# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 11:40:34 2021

@author: Geeta
"""

#TechClub Coding Challenge 1
print("Please type in two chemicals from the following: Oxygen,Hydrogen,Carbon,Chlorine")
Chem1 = input("Chem1: ").lower()
Chem2 = input("Chem2: ").lower()
s = (str(Chem1)+'+'+str(Chem2))
#print (s)
if s == ("hydrogen+oxygen") or s == ("oxygen+hydrogen"):
    print("H20")
elif s == ("oxygen+carbon") or s == ("carbon+oxygen"):
    print("CO2")
elif s == ("oxygen+chlorine") or s == ("chlorine+oxygen"):
    print("Cl2O")
elif s == ("chlorine+carbon") or s == ("carbon+chlorine"):
    print("CCl4")
elif s == ("chlorine+hydrogen") or s == ("hydrogen+chlorine"):
    print("HCl")
elif s == ("carbon+hydrogen") or s == ("hydrogen+carbon"):
    print("CH4")
elif Chem1 == Chem2:
    print("This is an element. Please try again and add two different elements for a compound.")
else:
    print("Sorry, this is either not an element within the given ones (Oxygen,Hydrogen,Carbon,Chlorine), or it's not an element. Please try again .")
    
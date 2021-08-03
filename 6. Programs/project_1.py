# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 19:37:35 2020

@author: Puruboii
"""
import random
# importing random module

health = 50 # initialising 

difficulty = 1 

# potion after drinking hw much will it increase

potion_health = int(random.randint(25,50) / difficulty)

#total health after adding portion 

health = health + potion_health

# printing health value 

print(health)


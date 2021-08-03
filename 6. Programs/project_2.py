# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 19:52:08 2020

@author: Puruboi
"""


hello = "Hello world! and Hy"

print(hello)

# Ask user for name

name = input("What is your name?: ")

# Ask user for age

age = input("How old are you?: ")

# Ask user for city

city = input("What city do you live in?: ")

# Ask user what they enjoy

love = input("What do you love doing?: ")

# Create output text

print("Your name is {} and you are {} years old. You live in {} and you love {}".format(name, age, city, love))

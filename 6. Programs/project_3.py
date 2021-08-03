# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 19:55:52 2020
Email Slicer
@author: Puruboi
"""


# get user email address

email = input("What is your email address?: ").strip()

# slice out user name

user = email[:email.index("@")]

# slice domain name

domain = email[email.index("@") + 1 :]

# format message

output = "Your username is {} and your domain name is {}".format(user, domain)

# display output message 

print(output)
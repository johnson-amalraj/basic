# ---------------------------------
# Program Description
#   1. 
#   2.  
#   3.  
# ---------------------------------

# ---------------------------------
# Import required packages 
# ---------------------------------
import os
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
import numpy as np
import time

# ---------------------------------
# Variable Declaration
# ---------------------------------
# get_user_name = input("Enter user name:")

# get_user_name = os.getlogin(); 
# str.upper(get_user_name)

# ---------------------------------
# user name and password DB
# ---------------------------------
# user_name_db = ["johnson", "amalraj", "unknown", "guest"]
# password_db = {'johnson':"@Jmht5rdx", 'amalraj':"$amalraj", 'unknown':"$unknown", 'guest':"@guest"}

# ---------------------------------
# Define a validate user name function
# ---------------------------------
def magic_text():
    get_text = input("Enter text:")

# ---------------------------------
# Define a validate user name
# ---------------------------------
# def validate_user_name():
# 
#   for user_name in user_name_db:
#     if (get_user_name == user_name):
#         get_password  = input("Enter Password:")
#         if (password_db.get(user_name) == get_password):
#           print("Hello,", user_name + "! How are you?")
#           magic_text()
#           break
#         else:
#           print("Sorry! password not matched")    
#           break
#     else:
#       print("Sorry! User name not matched")    
#       break

# ---------------------------------
# Main Program
# ---------------------------------
# call the function to check the user name and password 
# validate_user_name()
magic_text()
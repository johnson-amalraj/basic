# ---------------------------------
# Program Description
#   1. 
#   2.  
#   3.  
# ---------------------------------

# ---------------------------------
# Import required packages 
# ---------------------------------
import getpass

# ---------------------------------
# Variable Declaration
# ---------------------------------
get_user_name = input("Enter user name:")
# str.upper(get_user_name)

# ---------------------------------
# user name and password DB
# ---------------------------------
user_name_db = ["johnson", "amalraj", "unknown", "guest"]
password_dic = {'johnson':"@Jmht5rdx", 'amalraj':"Amalraj", 'unknown':"#unKnown", 'guest':"@guest"}

# ---------------------------------
# Define a function to check the credentials 
# ---------------------------------
def credential_check():

  user_found = 0;
  pswd_found = 0;

  for user_name in user_name_db:
    if (get_user_name == user_name):
      user_found = 1;
      print("Hey,", get_user_name + "! Enter your Password:")
      if (password_dic.get(user_name) == getpass.getpass(prompt="")):
        pswd_found = 1;
        break
      # else:
      #   break
    # else:

  if (user_found != 1):
    print("Sorry!,", get_user_name + "! not found")    
  elif (pswd_found != 1):
    print("Sorry! password not matched")    
  else:
    print("Hello,", get_user_name + "! How are you?")

# ---------------------------------
# Main Program
# ---------------------------------
# call the function to check the user name and password 
credential_check()

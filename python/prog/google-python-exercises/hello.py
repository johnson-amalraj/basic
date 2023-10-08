#!/usr/bin/python3
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""
A tiny Python program to check that Python is working.
Try running this program from the command line like this:
  python hello.py
  python hello.py Alice
That should print:
  Hello World -or- Hello Alice
Try changing the 'Hello' to 'Howdy' and run again.
Once you have that working, you're ready for class -- you can edit
and run Python code; now you just need to learn Python!
"""

import sys

# Define a main() function that prints a little greeting.
def main():
  # Get the name from the command line, using 'World' as a fallback.
  if len(sys.argv) >= 2:
    name = sys.argv[1]
  else:
    # name = input("Please enter something: ")
    # print("You entered:", name)
    # print('Hello', name)
    name = 'World'
  print('Hello', name)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()


''' 

Certainly! The code you provided is a simple Python script that takes command-line arguments and prints a "Hello" message based on the provided argument or a default value if no argument is given.
 
 Here's a breakdown of the code:
 
 1. `if len(sys.argv) >= 2:`:
    - This line checks whether there are at least two elements in the `sys.argv` list. `sys.argv` is a list in Python that stores the command-line arguments passed to the script. The first element (`sys.argv[0]`) is the script's name, and subsequent elements (`sys.argv[1]`, `sys.argv[2]`, and so on) are the arguments passed to the script.
 
 2. `name = sys.argv[1]`:
    - If there are at least two elements in `sys.argv`, this line assigns the value of the second element (i.e., `sys.argv[1]`) to the variable `name`. In other words, it takes the first command-line argument and assigns it to the `name` variable.
 
 3. `else:`:
    - If there are fewer than two elements in `sys.argv` (i.e., no command-line arguments were provided), this block of code is executed.
 
 4. `name = 'World'`:
    - In this case, since no command-line argument was provided, the script assigns the default value 'World' to the `name` variable.
 
 5. `print('Hello', name)`:
    - Finally, the script prints a "Hello" message, followed by the value stored in the `name` variable. If a command-line argument was provided, it will print "Hello" followed by that argument's value. If no argument was provided, it will print "Hello World."
 
 Here's how the script works in different scenarios:
 
 - If you run the script with a command-line argument, like this:
   ```
   python script.py Alice
   ```
   It will print:
   ```
   Hello Alice
   ```
 
 - If you run the script without any command-line arguments, like this:
   ```
   python script.py
   ```
   It will print:
   ```
   Hello World
   ```
 
 In summary, this script is a basic example of how you can use command-line arguments in Python to customize the behavior of your script based on user input. It provides a default value ('World') if no input is given.

'''

'''

 The code you provided is a common Python programming pattern that you'll often see at the bottom of Python scripts. 
 It's used to ensure that a specific block of code, typically the main() function, is executed when the script is run directly but not when it's imported as a module into another script. 
 Here's an explanation of how it works:
 
    # This is the standard boilerplate that calls the main() function.
    if __name__ == '__main__':
        main()
    if __name__ == '__main__'::
 
 This line checks whether the special Python variable __name__ is equal to the string '__main__'. In Python, __name__ is a built-in variable that represents the name of the current module (or script).
 When a Python script is run directly from the command line, its __name__ variable is set to '__main__'. This indicates that the script is the main program being executed.
 main():
 
 main is typically the name of a function in the script that contains the main logic of the program. It's where the primary functionality of the script is defined.
 if __name__ == '__main__': block:
 
 If the script is run directly, the code within this block (in this case, the main() function call) is executed. This ensures that the main functionality of the script is executed when you run the script from the command line.
 If the script is imported as a module into another Python script (using an import statement), the code within the if __name__ == '__main__': block is not executed. This allows you to reuse functions and variables defined in the script without running the main program logic.
 
 Here's an example to illustrate how this works:
 
 Suppose you have a Python script named my_script.py with the following content:
 
 def main():
     print("This is the main function.")
 
 if __name__ == '__main__':
     main()
 If you run my_script.py directly from the command line (python my_script.py), you will see the output "This is the main function."
 
 If you import my_script.py into another Python script using import my_script, the main() function will not be automatically executed when you import it. You can still use the functions and variables defined in my_script.py as needed in the importing script.

'''

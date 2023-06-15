# import the tkinter package
import tkinter as tk

# create the main gui_win
gui_win = tk.Tk()

# set the main gui_win title
gui_win.title("TODO")

# set the main gui_win size 
gui_win.geometry("645x525")

# Create a label widget
label = tk.Label(gui_win, text="Welcome to the ToDo!")

# Add the label widget to the gui_win
label.pack()

# Define a function to be called when the button is clicked
def button_click():
    label.config(text="+!")

# Create a button widget with some text and a command
button = tk.Button(gui_win, text="+", command=button_click)
button.pack(side='left', pady=10)

# Add the button widget to the gui_win
button.pack()

back_button = tk.Button(gui_win, text="Back", command=button_click)
back_button.pack(side='bottom', pady=10)

# run the main event loop
gui_win.mainloop()

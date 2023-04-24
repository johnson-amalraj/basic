import tkinter as tk

# Create a new window
window = tk.Tk()

# Set the window title and size
window.title("My Window")
window.geometry("300x200")

# Create a label widget
label = tk.Label(window, text="Hello, world!")

# Add the label widget to the window
label.pack()

# Define a function to be called when the button is clicked
def button_click():
    label.config(text="Welcome to Python GUI!")

# Create a button widget with some text and a command
button = tk.Button(window, text="Enter to GUI world!", command=button_click)

# Add the button widget to the window
button.pack()

# Start the main event loop
window.mainloop()

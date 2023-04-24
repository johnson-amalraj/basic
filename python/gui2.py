import tkinter as tk

# Create a new window
window = tk.Tk()

# Set the window title
window.title("My GUI")

# Create a label widget with some text
label = tk.Label(window, text="Hello, Tkinter!")

# Add the label widget to the window
label.pack()

# Define a function to be called when the button is clicked
def button_click():
    label.config(text="Button clicked!")

# Create a button widget with some text and a command
button = tk.Button(window, text="Click me!", command=button_click)

# Add the button widget to the window
button.pack()

# Start the main event loop to display the window
window.mainloop()

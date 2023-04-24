import tkinter as tk

# Create a new window
window = tk.Tk()

# Set the window title and size
window.title("My Window")
window.geometry("300x200")

# Create a label widget
label = tk.Label(window, text="Welcome to my app!")
label.pack(pady=10)

# Create a function to handle button clicks
def button_click():
    label.config(text="Button clicked!")

# Create a button widget
button1 = tk.Button(window, text="Button 1", command=button_click)
button1.pack(pady=5)

# Create another button widget
button2 = tk.Button(window, text="Button 2", command=button_click)
button2.pack(pady=5)

# Create a "Back" button widget
def go_back():
    label.config(text="Welcome to my app!")
    
back_button = tk.Button(window, text="Back", command=go_back)
back_button.pack(side='bottom', pady=10)

# Start the main event loop
window.mainloop()


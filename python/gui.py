import tkinter as tk

def update_label():
    label.config(text="Hello, Tkinter!")

# create the main window
root = tk.Tk()

# create a label with some text
label = tk.Label(root, text="Welcome to Tkinter!")
label.pack()

# create a button that updates the label text
button = tk.Button(root, text="Click me!", command=update_label)
button.pack()

# run the main event loop
root.mainloop()

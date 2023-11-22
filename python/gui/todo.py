from tkinter import *

# Create the main window
root = Tk()
root.title("ToDo List")

# Create a list to store the tasks
tasks = []

# Define a function to add a task
def add_task():
    task = task_input.get()
    if task != "":
        tasks.append(task)
        update_listbox()

# Define a function to remove a task
def remove_task():
    task = task_listbox.get(ANCHOR)
    tasks.remove(task)
    update_listbox()

# Define a function to update the listbox
def update_listbox():
    task_listbox.delete(0, END)
    for task in tasks:
        task_listbox.insert(END, task)

# Create the input box and add button
task_input = Entry(root, width=30)
task_input.pack(side=RIGHT, padx=30)
add_button = Button(root, text="Add", command=add_task)
add_button.pack(side=RIGHT)

# Create the task listbox and remove button
task_listbox = Listbox(root, width=50)
task_listbox.pack(side=LEFT, padx=10)
remove_button = Button(root, text="Remove", command=remove_task)
remove_button.pack(side=LEFT)

# Start the main loop
root.mainloop()

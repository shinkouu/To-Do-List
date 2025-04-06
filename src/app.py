"""
    Title: To-Do-List
    Brief description of the program: Basic To-Do-List created with Tkinter

    Name of the author: Kevin Pham
    Date of creation 06.04.2025
    Date of last edit: 06.04.2025
"""

import tkinter as tk
from tkinter import messagebox

# list to save each task
tasks = []

# function to update listbox
def update_listbox():
    # delete each element in the listbox
    listbox.delete(0, tk.END)
    for task in tasks:
        # rearrange listbox
        listbox.insert(0, task)

# function to add new task
def add_task():
    # get input
    task = task_entry.get()
    if task:
        # append task into list and update listbox
        tasks.append(task)
        update_listbox()
        # empty input
        task_entry.delete(0, tk.END)
    else:
        # show error if input is empty
        messagebox.showwarning("Input Error", "Please enter a task.")

#function to delete task
def delete_task():
    # get index of selected task
    selected = listbox.curselection()
    if selected:
        # pop selected element and update listbox
        tasks.pop(selected[0])
        update_listbox()

# GUI Setup
"""
To-Do:
- Mark tasks as “completed”
- Sort by priority
- Checkboxes instead of normal list box
"""
root = tk.Tk()
root.title("To-Do-List")

task_entry = tk.Entry(root, width = 35)
task_entry.pack(pady = 10)

add_button = tk.Button(root, text = "Add Task", command = add_task)
add_button.pack()

listbox = tk.Listbox(root, width = 40, height = 15)
listbox.pack(pady = 10)

delete_button = tk.Button(root, text = "Delete Task", command = delete_task)
delete_button.pack()

root.mainloop()
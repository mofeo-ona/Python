import tkinter as tk
from tkinter import messagebox

def addtask():
   taskk_entry = txt.get()
   if taskk_entry:
        # Number the task based on current listbox size
        task_number = lstbx.size() + 1
        numbered_task = f"{task_number}. {taskk_entry}"
        lstbx.insert(tk.END, numbered_task)
        txt.delete(0, tk.END)  # Clear the entry box
   else:
        messagebox.showwarning("Input Error", "Please enter a to-do item")

def dele():
    selected = lstbx.curselection()
    if selected:
        lstbx.delete(selected)
    else:
        messagebox.showwarning("Selection Error","Select a task to delete")

def clear():
    lstbx.delete(0, tk.END)

#creating an empty window
root = tk.Tk()
root.config(bg = "#FFD9E8")
root.title("to-do list")

#creating label
lbl = tk.Label(root, text = "MY TO-DO LIST APP", font = 20)
lbl.config(bg="#FFB2D1")
lbl.pack(pady=10)

#creating textbox
txt = tk.Entry(root, width = 40)
txt.config(bg='White')
txt.pack(pady=10)

#creating buttons
btna = tk.Button(root, text="ADD ITEM", width = 10, command=addtask)
btna.pack(pady=10)

btnd = tk.Button(root, text="DELETE", width = 10, command=dele)
btnd.pack(pady=10)

btnC = tk.Button(root, text="CLEAR ALL", width = 10,command=clear)
btnC.pack(pady=10)

#creating listbox
lstbx = tk.Listbox(root, width = 50, height = 10)
lstbx.config(bg = "#FF8BB9", fg="white", font = 15)
lstbx.pack(pady = 10)






root.mainloop()
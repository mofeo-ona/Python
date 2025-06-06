import tkinter as tk
from time import strftime

#creating an empty window
tyme = tk.Tk()
tyme.config(bg = "#00574B")
tyme.title("Digital Clock")
tyme.geometry("300x200")

#creating label
lbl = tk.Label(tyme, font = ("Times New Roman", 40), width = 20)
lbl.config(bg="black",fg="white")
lbl.pack(anchor="center")

labl=tk.Label(tyme, font = ("Times New Roman", 40), width = 20)
labl.config(bg="black",fg="white")
labl.pack(anchor="center")

# Greeting label
greet_lbl = tk.Label(tyme, font=("Times New Roman", 18), width = 46)
greet_lbl.config(bg="black", fg="white")
greet_lbl.pack(anchor="center")

def get_greeting():
    hour = int(strftime('%H'))  # %H gives hour in 24-hour format as string
    if 5 <= hour < 12:
        return "Good Morning!"
    elif 12 <= hour < 17:
        return "Good Afternoon!"
    elif 17 <= hour < 21:
        return "Good Evening!"
    else:
        return "Good Night!"

def updatetime():
    currenttime = strftime('%I:%M:%S %p')
    currentdate = strftime('%A, %B %d, %Y')
    greeting = get_greeting()
    lbl.config(text=currenttime)
    labl.config(text=currentdate)
    greet_lbl.config(text=greeting)
    lbl.after(1000, updatetime)



updatetime()



tyme.mainloop()
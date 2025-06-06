import tkinter as tk


root = tk.Tk()
root.config(bg="skyblue")
root.title("Temperature converter")
root.geometry("300x200")

title_lbl = tk.Label(root, text = "TEMPERATURE CONVERTER")
title_lbl.config(bg = "white", fg = "darkblue", font = 10)
title_lbl.pack(pady = 10, anchor = "center")

temp_lbl = tk.Label(root, text = "ENTER TEMPERATURE", font=50)
temp_lbl.config(bg = "white", fg = "darkblue")
temp_lbl.pack(pady = 10, anchor = "center")

enter_txt = tk.Entry(root)
enter_txt.config(bg = "white")
enter_txt.pack(pady = 10, anchor = "center")

coversion = tk.StringVar()
coversion.set("celsius to fahrenheit")

dropdown = tk.OptionMenu(root, coversion, "celsius to fahreheit","fahrenheit to celsius")
dropdown.pack(pady = 5)

disp_lbl = tk.Label(root, text = "", width = 10)
disp_lbl.config(bg = "darkblue", fg = "white")
disp_lbl.pack(pady = 10)

conv_btn = tk.Button(root, text="CONVERT")
conv_btn.pack(pady = 10)

def conv():
    try:
        temp = float(enter_txt.get())
        convtype = coversion.get()

        if convtype == "celsius to fahrenheit":
            





root.mainloop()
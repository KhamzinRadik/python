# -*- coding: cp1251 -*-


import tkinter as tk

def show_message():
    lable2["text"] = entry.get()     # получаем введенный текст
    return lable2


root = tk.Tk()
label=tk.Label(text='путь к фаилу')
entry = tk.Entry(root)
root.title("сальдо расход")
root.geometry('600x400')
label.grid(row=1, column=1)
entry.grid(row=1, column=20)

lable2=tk.Label()
lable2.grid(row=30, column=30)

 
btn = tk.Button(text="Click", command=show_message)

btn.grid(row=1,column=30)

   
root.mainloop()
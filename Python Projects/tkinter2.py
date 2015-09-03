from tkinter import *
from tkinter import ttk
root = Tk()
label = ttk.Label(root, text = 'Hello Tkinter')
label.pack()
root.wm_title("Hello World!")
label.config(foreground = 'blue', background = 'black')
label.config(font = ('Courier', 18, 'bold'))
label.config(text = 'Aloha Tkinter!')
logo = PhotoImage(file = 'C:\\Users\\Nic\\Desktop\\cat.gif')
label.config(compound = 'left')
label.img = logo
label.config(image = label.img)

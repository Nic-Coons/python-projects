__author__ = 'Nic'
from tkinter import *
from tkinter import ttk
from tkinter import messagebox, filedialog
import sqlite3


root = Tk()

#root config
root.resizable(False, False)
root.title('HTML Maker')
root.configure(background = '#ef3800')
conn = sqlite3.connect('C:\\Python34\\htmlBodies.db')
c = conn.cursor()
sql = "SELECT * FROM bodies"
sql2 = "SELECT ID FROM bodies"
sql3 = "SELECT text FROM bodies WHERE ID=?"



#configure defs
def shows():
    enterText.grid_forget()
    comLabel.grid(row = 5, column = 1)
    text.grid(row = 6, column = 1)
    submitB.grid(row = 7, column = 1)
    clearB.grid(row = 8, column = 1)
    preText.grid_forget()

def chews():
    c.execute(sql2)
    all_row = c.fetchall()
    all_rows = str(all_row).replace(')','').replace('(','').replace('u\'','').replace("'",'').replace(',','').replace('[','').replace(']','')
    print (all_rows)
    BG.combobox = ttk.Combobox(BG, textvariable = all_rows)
    BG.combobox.grid(row = 7, column = 1)
    BG.combobox.bind("<<ComboboxSelected>>")
    BG.combobox.config(values = (all_rows))
    BG.combobox.current(0)

    label3 = Label(BG, background = '#ef3800', text = "Please Choose the text ID",
               font = ('Arial', 10))
    label3.grid(row = 6, column = 1)
    submitC = ttk.Button(BG, text = "View")
    submitC.grid(row = 8, column = 1)
    BG.text2 = Label(BG, width = 30, height = 10, font = ("Arial", 11), text = '')
    BG.text2.grid(row = 9, column = 1)
    global comboChoice

    submitC.config(command = comboget)

# def comboget2():
#     comboChoice = BG.combobox.get()
#     top = Toplevel()
#     top.geometry("%dx%d%+d%+d" % (300, 200, 250, 125))
#
#     c.execute(sql3, comboChoice)
#     comboTex = c.fetchall()
#     comboText = str(comboTex).replace(')','').replace('(','').replace('u\'','').replace("'",'').replace(',','').replace('[','').replace(']','').replace('\n','')
#     msg = Message(top, text = comboText)
#     msg.pack()
#     def close_window():
#         top.destroy()
#     btn = ttk.Button(top, text = 'Close', command = close_window)
#     btn.pack()
#     BG.text2.config(text = '')
#     BG.text2.config(text = comboText)

def comboget():
    comboChoice = BG.combobox.get()
    c.execute(sql3, comboChoice)
    global comboText
    comboTex = c.fetchall()
    comboText = str(comboTex).replace(')','').replace('(','').replace('u\'','').replace("'",'').replace(',','').replace('[','').replace(']','').replace('\n','')
    BG.text2.config(text = '')
    BG.text2.config(text = comboText)
    BG.Finish = ttk.Button(BG, text='Finish', command=save2)
    BG.Finish.grid(row = 10, column = 1)

#widgets looks
BG = Label(root, background = '#ef3800', width = 480, height = 640)
BG.pack()

label2 = Label(BG, background = '#ef3800', text = "Please enter the webpage name and desired text!",
               font = ('Arial', 18))

label2.grid(row = 0, column = 1)

Name = StringVar()
namelabel = Label(BG, background = '#ef3800', text = "Page Name:", font = ('Arial', 11)).grid(row = 1, column = 1)
nameEntry = ttk.Entry(BG, width = 30, textvariable = Name, font = ("Arial", 11)).grid(row = 2, column = 1)


#choice 1
textLabel = Label(BG, background = '#ef3800', text = "Text Entry Style:", font = ('Arial', 11))
textLabel.grid(row = 3, column = 1)
enterText = ttk.Button(BG, text = "Create New Body Text", command = shows)
enterText.grid(row = 4, column = 1, columnspan = 1, ipadx = 30)
preText = ttk.Button(BG, text = "Choose from Available Body Text", command = chews)
preText.grid(row = 5, column = 1, columnspan = 2)


#2. Create New Body Text
comLabel = Label(BG, background = '#ef3800', text = "Body text: ", font = ('Arial', 11))
comLabel.grid(row = 5, column = 1)
comLabel.grid_forget()
text = Text(BG, width = 30, height = 10, wrap = 'word', font = ("Arial", 11))
text.grid(row = 6, column = 1)
text.grid_forget()



#buttons

def save():
    global page
    print('Name: {}'.format(Name.get()))
    page = Name.get()
    global body
    print('Comment: {}'.format(text.get(1.0, END)))
    body = text.get(1.0, END)

    text_save()


    dataEntry()

    Name.set('')
    text.delete(1.0, END)
    messagebox.showinfo(title = "HTML Maker", message = 'All Saved!')


def save2():
    global page

    page = Name.get()
    global body

    body = comboText

    text_save()


    dataEntry()

    Name.set('')

    messagebox.showinfo(title = "HTML Maker", message = 'All Saved!')



def text_save():
    f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if f is None: # asksaveasfile return `None` if dialog closed with "cancel".
        return
    text2save = """<html><body> """ + body + """ </body></html>"""
    f.write(text2save)
    f.close()


def clear():
    Name.set('')

    text.delete(1.0, END)


submitB = ttk.Button(BG, text = "Submit", command = save)
submitB.grid(row = 7, column = 1)
submitB.grid_forget()
clearB = ttk.Button(BG, text = "Clear", command = clear)
clearB.grid(row = 8, column = 1)
clearB.grid_forget()

def tableCreate():
    c.execute("CREATE TABLE bodies(ID INTEGER PRIMARY KEY, text TEXT, keyword TEXT)")


#----------------------------------------------------------------------
def dataEntry():

    c.execute("INSERT INTO bodies (text, keyword) VALUES (?, ?)",(body, page))

    conn.commit()


#f = open('helloworld.html','w')

##message = """<html>
##<body>
##Stay tuned for our amazing summer sale!
##</body>
##</html>"""

##f.write(message)
##f.close()
##    f = open(page + '.html','w')
##    message = """<html><body> """ + body + """ </body></html>"""
##    f.write(message)
##    f.close()

root.mainloop()

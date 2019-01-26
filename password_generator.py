import random
from tkinter import *
from tkinter import messagebox

p = ''
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
def inputpass():
    length = Entry.get(e)
    length = int(length)
    global p
    for c in range(length):
        p += random.choice(s)
    messagebox.showinfo("Password generated", p)

top = Tk()
top.title("Password generator")

e = Entry(top)
e.pack()
e.focus_set()

B = Button(top, text ="Generate", command=inputpass)
B.pack(side='bottom')
B.bind('<Return>', self.parse)
top.mainloop()

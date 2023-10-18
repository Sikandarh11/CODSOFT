from tkinter import *
from tkinter import ttk

top = Tk()
top.title("student")
top.geometry("300x400")

style = ttk.Style()  # Create an instance of ttk.Style
style.configure("TFrame", bg='blue')

def submit():
    name = e1.get()
    lb.insert(1, name)

def del_text():
    selected_indices = lb.curselection()
    for index in reversed(selected_indices):
        lb.delete(index)

lbl = Label(top, text="Name List", bg="blue", fg="white")  # Change background color to blue
lbl.place(x=10, y=190)

lb = Listbox(top, fg="green", bg="yellow")  # Change foreground color to green and background color to yellow
lb.place(x=10, y=220)

name = Label(top, text="Name")
name.place(x=50, y=50)

e1 = Entry(top)
e1.place(x=100, y=50)

bt1 = Button(top, text="submit", bg='#00a65c', fg='black', command=submit)
bt1.place(x=150, y=150)

delete_b = Button(top, text="Delete", bg='#00a65c', fg='black', command=del_text)
delete_b.place(x=100, y=150)

top.mainloop()

from tkinter import*
from tkinter import messagebox
root=Tk()
E=Entry(root, width=35, bg="grey", fg="Red", borderwidth=3)
E.pack()
def message():
    C=messagebox.showinfo("Greetings","Hello "+E.get())
    C.pack()
# to create an interaction with a function or a button you'll use .get() function while getting value from variable
A=Label(root, text="WElcome to the ABC website please proceed")
B=Button(root, text="Register!", command=message)

A.pack()
B.pack()
root.mainloop()
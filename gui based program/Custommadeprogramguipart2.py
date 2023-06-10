from tkinter import*
from tkinter import messagebox
root=Tk()
E=Entry(root, width=35, bg="grey", fg="Red", borderwidth=3)
E.pack()
F=Entry(root, width=35, bg="grey", fg="Red", borderwidth=3)
F.pack()
def message():
    C=messagebox.showinfo("Greetings","Hello "+E.get())
    C.pack()
def message2():
     D=Label(text="The given Email is valid! "+F.get())
     D.pack()
# to create an interaction with a function or a button you'll use .get() function while getting value from variable
A=Label(root, text="WElcome to the ABC website please proceed")
B=Button(root, text="Register!", command=message)
G=Button(root, text="Register and Log in!", bg="grey", fg="purple", command=message2)
A.pack()
B.pack()
G.pack()
root.mainloop()
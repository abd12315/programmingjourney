import tkinter
from tkinter import messagebox
import tkinter.font
top=tkinter.Tk()
def helloCallBack():
    messagebox.showinfo( "Look who's shown himself here you piece of shit")
def buttonclicked():
    print("I warned you")
C=tkinter.Button(text='Click Here',command=buttonclicked)
B = tkinter.Button(top,background="grey", text ="Don't Click here", command = helloCallBack)   
D = tkinter.Canvas(top, bg="blue", height=250, width=300)
coord = 10, 50, 240, 210
arc = D.create_arc(coord, start=0, extent=150, fill="red")
B.pack()
C.pack()
D.pack()
top.mainloop()
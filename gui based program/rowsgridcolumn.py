from tkinter import* 
root=Tk()
A=Label(root, text="hello there!")
B=Label(root, text="This is the library following the tkinter which supports gui based operations")
C=Label(root, text="Now as you can see the value are arranged instead of hovering around based on the expansion of windows compare to the fi9rst basic program")
D=Label(root, text="see the visible difference once i changed the column ...")
A.grid(rows=1, column=1)
B.grid(rows=2, column=1)
C.grid(rows=3, column=1)
D.grid(rows=3, column=2)
root.mainloop()
# this is the program that arranges the text in python in the form of grid I.e meaning rows and columns 


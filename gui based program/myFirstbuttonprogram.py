from tkinter import* 
root=Tk()
A=Label(root, text="hello there!")
B=Label(root, text="This is the library following the tkinter which supports gui based operations")
C=Button(root, text="Click here for more info")
# now to define the state of button wheather youwant it enabled or greyed out it's all depend upon you
# and if you decided to use it anyway so you're going  to use STATE attribute
D=Button(root, text="Register!", state=DISABLED)
# to increase the size of text we will use padx and pad y function
E=Button(root,text="Enter licence Key", padx=75, pady=20)
A.pack()
B.pack()
C.pack()
D.pack()
E.pack()
root.mainloop()
# this is the bas8ic gui program for python 


from tkinter import*
root=Tk()

A=Label(root, text="Hello world").grid(row=1, column=1)
B=Label(root, text="this is the object class base table").grid(row=2,column=1)
C=Label(root, text="as you can see we don't require extra function call at the end of program").grid(row=3,column=1)

root.mainloop()
# as you can see Idon't have to recall the program again and again
#useful in scenerio where you like big and complex code
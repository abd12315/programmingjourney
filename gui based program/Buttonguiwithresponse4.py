from tkinter import* 
root=Tk()
# create a function that defines the purpose of the button once it has been clicked
def Register():
    F=Label(root, text="Welcome to Abc comapny! please wait while requesting info from the server!...")
    F.pack()
A=Label(root, text="hello there!")
B=Label(root, text="This is the library following the tkinter which supports gui based operations")
C=Button(root, text="Click here for more info")
# now to define the state of button wheather youwant it enabled or greyed out it's all depend upon you
# and if you decided to use it anyway so you're going  to use STATE attribute
D=Button(root, text="Register!", state=DISABLED)
# to increase the size of text we will use padx and pad y function
#using commadn as an attribute you're telling the compiler that there exist a function before the main program
# and you're recalling that function by commanding it i.e command=Function_name
# to change the foreground and background color of the button you will use fg and bg command
# as demonstrated below 
E=Button(root,text="Enter licence Key", padx=75, pady=20, command=Register, fg="red", bg="grey")
A.pack()
B.pack()
C.pack()
D.pack()
E.pack()
root.mainloop()
# this is the bas8ic gui program for python 


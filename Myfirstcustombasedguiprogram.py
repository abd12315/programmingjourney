from tkinter import*
from tkinter import messagebox 
root=Tk()
# create a function that defines the purpose of the button once it has been clicked
def Register():
    F=Label(root, text="Welcome to Abc comapny! please wait while requesting info from the server!...")
    messagebox.askquestion("Confirm your identity","Please authorize yourself!")
    F.pack()
def message():
    messagebox.showinfo("Warning!","Please Connect to the internet")
    messagebox.showwarning("Warning!","Failed to connect oo https://www.abc.com exiting")
    messagebox.showerror("FATAL ERROR!","UNABLE TO CONNECT NETWORK SERVICE PLEASE MAKE SURE THAT INTERNET SERVICE IS AVAILABLE")
def message2():
    messagebox.showerror("Ërror","Network connection error")   
# to show info based messages use showinfo()
# for warning based messages use showwarning()
# observe the above function program carefully
A=Label(root, text="hello there!")
B=Label(root, text="This is the library following the tkinter which supports gui based operations")
C=Button(root, text="Click here for more info", command=message)
# now to define the state of button wheather youwant it enabled or greyed out it's all depend upon you
# and if you decided to use it anyway so you're going  to use STATE attribute
D=Button(root, text="Register!", state=DISABLED)
E=Button(root,text="Enter licence Key", padx=75, pady=20, command=Register, fg="red", bg="grey")
H=LabelFrame(root, text="Please wait Loading . . . . ")
I=Label(root, text="Connecting...")
J=Button(root, text="Cancel", command=message2)
A.pack()
B.pack()
C.pack()
D.pack()
E.pack()
H.pack()
I.pack()
J.pack()
root.mainloop()
# this is the bas8ic gui program for python 


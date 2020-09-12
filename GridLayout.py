from tkinter import *

root = Tk()

label1 = Label(root, text="Name")
label2 = Label(root, text="Password")

#when you want to allow the user to enter a number/name/password, use Entry (input fields)
entry1 = Entry(root)
entry2 = Entry(root)

#column is default
label1.grid(row=0,sticky=E) #align with sticky; North, East, South, West
label2.grid(row=1,sticky=E)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)

c = Checkbutton(root, text="Keep me signed in")
c.grid(columnspan=2)

root.mainloop()

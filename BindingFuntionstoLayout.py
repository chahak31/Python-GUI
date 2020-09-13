from tkinter import *

root = Tk()

#Method 1
"""
def printName():
    print("Hello my name is python")

button1 = Button(root, text="Print my name", command=printName)
button1.pack()
"""

#Method 2
def printName(event):
    print("Hello my name is python")

button1 = Button(root, text="Print my name")
button1.bind("<Button-1>",printName) #parameters: event name(<Button-1> for left clicking your mouse button), function to be called 
button1.pack()
root.mainloop()

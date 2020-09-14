from tkinter import *
import tkinter.messagebox

root = Tk()

tkinter.messagebox.showinfo("Window Title", "This is an important information.")

answer = tkinter.messagebox.askquestion("Question 1", "Do you like silly faces?")

if answer == "yes":
    print("== ))")

root.mainloop()

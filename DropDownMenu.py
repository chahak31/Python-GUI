from tkinter import *

def NewProject():
    print("New Project is created")

def Neww():
    print("New file is created")

def Exit():
    print("Exited...")

def Redo():
    print("Redo...")

def Insert1():
    print("inserting...")

root = Tk()

# ************ Menu Bar ************

menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="file", menu=subMenu) #add_cascade is used for dropdown
subMenu.add_command(label="New Project", command=NewProject)
subMenu.add_command(label="New", command=Neww)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=Exit)

menu2 = Menu(menu)
menu.add_cascade(label="edit", menu=menu2)
menu2.add_command(label="Redo", command=Redo)

# ************ Toolbar ************

toolbar = Frame(root, bg="blue")
insertButt = Button(toolbar, text ="Insert Image", command=Insert1)
insertButt.pack(side=LEFT, padx=2, pady=2)
printButton = Button(toolbar, text ="Print", command=Insert1)
printButton.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

# ********** Status Bar ************

status = Label(root, text="Preparing to do nothing...", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()



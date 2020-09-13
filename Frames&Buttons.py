from tkinter import *

root = Tk()

#invisible frame/container at top
topFrame = Frame(root)
topFrame.pack()

#invisible frame at bottom
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

#Buttons
button1 = Button(topFrame, text="Button 1", fg="red")
button2 = Button(topFrame, text="Button 2", fg="blue")
button3 = Button(topFrame, text="Button 3", fg="yellow")
button4 = Button(bottomFrame, text="Button 4", fg="black")

button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=LEFT)
button4.pack(side=BOTTOM)

root.mainloop()

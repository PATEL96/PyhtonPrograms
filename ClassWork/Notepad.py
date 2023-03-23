from tkinter import *

root = Tk()
root.title("Notepad")

def DoNothing():
	fileWin = Toplevel(root)
	button = Button(fileWin)
	return button

root.geometry("500x400")

menubar = Menu(root)
fileMenu = Menu(menubar, tearoff=0)
fileMenu.add_command(label="New", command=DoNothing)
fileMenu.add_command(label="Open", command=DoNothing)
fileMenu.add_command(label="Save", command=DoNothing)
fileMenu.add_command(label="Save As..", command=DoNothing)
fileMenu.add_command(label="Close", command=DoNothing)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=fileMenu)
root.config(menu=menubar)

# def testKey(event):
#     label.config(text="Key: " + event.keysym)
#     label.pack()

# def testMouse(event):
#     label.config(text="Mouse: " + str(event.x) + " " + str(event.y))
#     label.pack()

# root.bind('<Button>', testMouse)
# label = Label(root)
# label.pack()

# Exit = Button(root, text="Close", command=root.quit)
# Exit.pack()

maintext = Text(root, bd=0)
maintext.pack()

root.mainloop()
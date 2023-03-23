from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Tkinter Testing")

def show():
    messagebox.showinfo("Yoo!!", "This is Hiii!!")

popup = Button(root, text="click me!!", command=show)
popup.pack(padx=20, pady=20)

pop = Button(root, text="close", command=root.destroy)
pop.pack(padx=20, pady=20)

root.mainloop()
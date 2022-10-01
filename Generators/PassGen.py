from tkinter import *
from random import randint
import pyqrcode

root = Tk()
root.title("PASSWORD GENERATOR")
root.geometry("950x530+200+50")

def qr_wifi():
    pswd_out.delete(0, END)
    pswd = ''
    if int(my_entry.get()) >= 6 and  int(my_entry.get()) <= 30:
        for i in range(0, int(my_entry.get())):
            pswd += chr(randint(33,126))
        pswd_out.insert(0, pswd)
        qr_label.configure(passqr())

    elif int(my_entry.get()) > 30:
        error1 = "Password Too Long!!"
        pswd_out.insert(0, error1)

    elif int(my_entry.get()) < 6:
        error2 = "Password Too Short!!"
        pswd_out.insert(0, error2)

def passqr():
    global qr, photo
    qr = pyqrcode.create(pswd_out.get())
    photo = BitmapImage(data=qr.xbm(scale=8))
    qr_label.configure(image=photo)

def copy_pass():
    root.clipboard_clear()
    root.clipboard_append(pswd_out.get())

def save_qr():
    qr = pyqrcode.create(pswd_out.get())
    qr.png('Password.png')

password_frame = Frame(root, bd=2, relief=RIDGE, background='#373738')
password_frame.place(x=50, y=50, width=500, height=430)

qr_frame = Frame(root, relief=RIDGE, background='#373738')
qr_frame.place(x=600, y=50, width=300, height=430)

lf = LabelFrame(password_frame, text="CHARACTERS REQUIRED")
lf.config(bg='#373738', foreground='White')
lf.pack(pady=20)

my_entry = Entry(lf, font=("Arial", 26))
my_entry.config(bg='#373738', foreground='White')
my_entry.pack(pady=20, padx=20)

pswd_out = Entry(password_frame, font=("Arial", 26))
pswd_out.config(bg='#373738', foreground='White')
pswd_out.pack(pady=40, padx=20)

but_frame = Frame(password_frame, bd=2, relief=RIDGE, background='#373738', border= 0)
but_frame.pack(pady=20)

gen_button = Button(but_frame, text="Genrate QR", command=qr_wifi)
gen_button.grid(row=0, column=0, pady=20, padx=20)

copy_button = Button(but_frame, text="Copy To Clipboard", command=copy_pass)
copy_button.grid(row=0, column=1, pady=20, padx=20)

save_button = Button(but_frame, text="Save QR", command=save_qr)
save_button.grid(row=1, column=0, pady=20, padx=20)

exit_button = Button(but_frame, text="Close", command=root.destroy)
exit_button.grid(row=1, column=1, pady=20, padx=20)

qr_label = Label(qr_frame, bg='#FFFFFF', height=300, width=300)
qr_label.pack(pady=65)

root.config(bg='#373738')
root.mainloop()
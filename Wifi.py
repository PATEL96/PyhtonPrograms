from tkinter import *
import pyqrcode

root = Tk()
root.title("WIFI QR CODE GENERATOR")
root.geometry("950x530+200+50")

#Commands For Buttons
def qr_wifi():
    #Generating QR Code
    global qr, photo
    ssid = str(my_entry.get())
    security = 'WPA'
    password = str(my_entry_chr.get())
    qr = pyqrcode.create(f'WIFI:S:{ssid};T:{security};P:{password};;')
    photo = BitmapImage(data=qr.xbm(scale=8))
    
    #Representing QR Code
    qr_label.configure(qr_img())
    
def qr_img():
    #Configuring QR Code
    global photo
    qr_label.config(image=photo)

#Frames for Placements
password_frame = Frame(root, bd=2, relief=RIDGE, background='#373738')
password_frame.place(x=50, y=50, width=500, height=430)

qr_frame = Frame(root, relief=RIDGE, background='#373738')
qr_frame.place(x=600, y=50, width=300, height=430)

lf = LabelFrame(password_frame, text="NAME OF WIFI or SSID")
lf.config(bg='#373738', foreground='White')
lf.pack(pady=20)

cf = LabelFrame(password_frame, text="Password Of Your Network")
cf.config(bg='#373738', foreground='White')
cf.pack(pady=20)

# InputBox For Data
my_entry = Entry(lf, font=("Arial", 26))
my_entry.config(bg='#373738', foreground='White')
my_entry.pack(pady=20, padx=20)

my_entry_chr = Entry(cf, font=("Arial", 26))
my_entry_chr.config(bg='#373738', foreground='White')
my_entry_chr.pack(pady=20, padx=20)

# Buttons For Actions
gen_button = Button(password_frame, text="Genrate QR", command=qr_wifi)
gen_button.pack(pady=20)

exit_button = Button(password_frame, text="Close", command=root.destroy)
exit_button.pack(pady=20)

qr_label = Label(qr_frame, bg='#FFFFFF', height=300, width=300)
qr_label.pack(pady=65)

root.config(bg='#373738')
root.mainloop()
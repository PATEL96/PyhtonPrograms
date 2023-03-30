from smtplib import *
from tkinter import *
from dotenv.main import load_dotenv
from email.mime.text import *
from email.mime.multipart import *
import os

root = Tk()
root.title("Email With Subject")

def Send():
    
    load_dotenv()
    password = os.environ["EmailPass"]
    
    mess = MIMEMultipart()
    mess['From'] = 'patel.raj.official.96@gmail.com'
    mess['To'] = str(receiver_address.get())
    mess['Subject'] = str(mail_subject.get())
    
    body = mail_message.get("1.0","end-1c")
        
    mess.attach(MIMEText(body,'plain'))
    
    server = SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('patel.raj.official.96@gmail.com', password)
    
    text = mess.as_string()
    server.sendmail('patel.raj.official.96@gmail.com', str(receiver_address.get()), text)
    server.quit()

label_main = LabelFrame(root,bd=0)
label_main.pack(padx=20,pady=20)

receiver_mail = LabelFrame(label_main, text="To: ")
receiver_mail.grid(column=0, row=0,padx=20, pady=20)

receiver_address = Entry(receiver_mail, bd=2, font=("Arial", 16))
receiver_address.pack(padx=20,pady=20)

mail_subject_label = LabelFrame(label_main, text="Subject: ")
mail_subject_label.grid(column=1, row=0,padx=20, pady=20)

mail_subject = Entry(mail_subject_label, bd=2, font=("Arial", 16))
mail_subject.pack(padx=20, pady=20)

mail_message_label = LabelFrame(label_main, text="Mesage: ")
mail_message_label.grid(row=1,column=0, columnspan=2, padx=20,pady=20)

mail_message = Text(mail_message_label, bd=2, font=("Arial", 16), height=10, width=50)
mail_message.pack(padx=20,pady=20)

send_button = Button(label_main, text="Send", font=("Arial", 16), command=Send)
send_button.grid(row=2,column=0, padx=20, pady=20)

close_button = Button(label_main, text="Close", font=("Arial", 16), command=root.quit)
close_button.grid(row=2,column=1, padx=20,pady=20)

root.mainloop()
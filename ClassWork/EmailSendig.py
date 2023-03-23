from smtplib import *
from tkinter import *
from dotenv.main import load_dotenv
import os

root = Tk()
root.title("Email Sender")

def Send():

	load_dotenv()
	password = os.environ["EmailPass"]

	server = SMTP("smtp.gmail.com", 587)
	server.starttls()
	server.login("patel.raj.official.96@gmail.com", password)

	server.sendmail("patel.raj.official.96@gmail.com", str(sender_id.get()), message.get())
	server.quit()


sender_mail = LabelFrame(root, text="To:")
sender_mail.pack()

sender_id = Entry(sender_mail, bd=2)
sender_id.pack(padx=20, pady=20)

sender_message = LabelFrame(root, text="Message")
sender_message.pack(padx=20, pady=20)

message = Entry(sender_message, bd=2)
message.pack(padx=20, pady=20)

button_label = LabelFrame(root, bd=0)
button_label.pack(padx=20,pady=20)

send_button = Button(button_label, text="Send", command=Send)
send_button.grid(row=0, column=0, padx=20)

close_button = Button(button_label, text="Close", command=root.quit)
close_button.grid(row=0, column=1, padx=20)


root.mainloop()
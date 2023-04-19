from socket import *
from tkinter import *

root = Tk()
root.title("Chat App")


def Send():
	s = socket()
	Server_Address = ('192.168.0.101', 8080)
	s.connect(Server_Address)
	print(s.recv(1024).decode())
	data = message.get("1.0","end-1c")
	s.send(data.encode())
	s.close()
    

message = Text(root)
message.pack(padx=20,pady=20)

buttons = Frame(root)
buttons.pack(padx=20, pady=20)

send_button = Button(buttons, text="Send", command=Send)
send_button.grid(row=0, column=0, padx=20, pady=20)

close_button = Button(buttons, text="Close", command=root.quit)
close_button.grid(row=0,column=1, padx=20, pady=20)

root.mainloop()
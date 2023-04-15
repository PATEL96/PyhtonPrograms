import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        self.master.resizable(False, False)
        self.entry_value = tk.StringVar()
        self.entry_value.set("")
        
        self.entry = tk.Entry(self.master, width=30, font=('Arial', 14), textvariable=self.entry_value, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        
        self.create_button('7', 1, 0)
        self.create_button('8', 1, 1)
        self.create_button('9', 1, 2)
        self.create_button('/', 1, 3)
        
        self.create_button('4', 2, 0)
        self.create_button('5', 2, 1)
        self.create_button('6', 2, 2)
        self.create_button('*', 2, 3)
        
        self.create_button('1', 3, 0)
        self.create_button('2', 3, 1)
        self.create_button('3', 3, 2)
        self.create_button('-', 3, 3)
        
        self.create_button('0', 4, 0)
        self.create_button('C', 4, 1)
        self.create_button('=', 4, 2)
        self.create_button('+', 4, 3)
        
    def create_button(self, text, row, column):
        button = tk.Button(self.master, text=text, width=7, height=3, font=('Arial', 14),
                           command=lambda:self.button_click(text))
        button.grid(row=row, column=column, padx=5, pady=5)
        
    def button_click(self, text):
        if text == 'C':
            self.entry_value.set("")
        elif text == '=':
            try:
                result = str(eval(self.entry_value.get()))
                self.entry_value.set(result)
            except:
                self.entry_value.set("Error")
        else:
            self.entry_value.set(self.entry_value.get() + text)
        
if __name__ == '__main__':
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()

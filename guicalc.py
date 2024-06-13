import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        
        # Entry widget to display the expression
        self.expression = ""
        self.entry = tk.Entry(root, width=40, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4)
        
        # Creating buttons
        button_texts = [
            '7', '8', '9', '/', 
            '4', '5', '6', '*', 
            '1', '2', '3', '-', 
            '0', '.', '=', '+'
        ]
        
        # Adding buttons to the grid
        row_val = 1
        col_val = 0
        for text in button_texts:
            button = tk.Button(root, text=text, padx=20, pady=20, command=lambda t=text: self.button_click(t))
            button.grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Clear button
        clear_button = tk.Button(root, text='C', padx=20, pady=20, command=self.clear)
        clear_button.grid(row=row_val, column=col_val)
    
    def button_click(self, button_text):
        """Handles button click events."""
        if button_text == '=':
            try:
                result = eval(self.expression)
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
                self.expression = str(result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Expression")
                self.entry.delete(0, tk.END)
                self.expression = ""
        else:
            self.expression += str(button_text)
            self.entry.delete(0, tk.END)
            self.entry.insert(0, self.expression)
    
    def clear(self):
        """Clears the entry widget."""
        self.entry.delete(0, tk.END)
        self.expression = ""

def main():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import messagebox, filedialog
import math

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Scientific Calculator")
        self.root.geometry("600x600")
        self.root.resizable(False, False)

        self.expression = ""
        self.input_text = tk.StringVar()

        # --- Main UI Layout ---
        # Main Calculator (Left side)
        calc_frame = tk.Frame(self.root, width=400, height=600)
        calc_frame.pack(side=tk.LEFT, fill=tk.BOTH)

        # History Panel (Right side)
        history_frame = tk.Frame(self.root, width=200, bg="#f4f4f4", bd=2, relief=tk.SUNKEN)
        history_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # --- Calculator Display ---
        display_field = tk.Entry(calc_frame, font=('arial', 24, 'bold'), textvariable=self.input_text, 
                                 width=15, bg="#eee", bd=10, justify=tk.RIGHT)
        display_field.grid(row=0, column=0, columnspan=4, ipady=20)

        # --- History UI ---
        tk.Label(history_frame, text="History", font=("arial", 12, "bold"), bg="#f4f4f4").pack(pady=5)
        self.history_listbox = tk.Listbox(history_frame, font=("arial", 10), width=25, height=25)
        self.history_listbox.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
        
        tk.Button(history_frame, text="Save to .txt", command=self.save_history, bg="#4CAF50", fg="white").pack(pady=10)

        # --- Buttons Layout ---
        buttons = [
            'C', 'Del', 'sqrt', '/',
            'sin', 'cos', 'tan', '*',
            '7', '8', '9', '-',
            '4', '5', '6', '+',
            '1', '2', '3', 'log',
            '0', '.', 'pi', '='
        ]

        row, col = 1, 0
        for button in buttons:
            action = lambda x=button: self.on_button_click(x)
            tk.Button(calc_frame, text=button, width=10, height=4, bd=1, bg="#fff", 
                      command=action).grid(row=row, column=col, sticky="nsew")
            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
        elif char == "Del":
            self.expression = self.expression[:-1]
        elif char == "=":
            try:
                # Prepare expression for evaluation
                original_expr = self.expression
                temp_expr = self.expression.replace('sqrt', 'math.sqrt').replace('sin', 'math.sin')\
                                           .replace('cos', 'math.cos').replace('tan', 'math.tan')\
                                           .replace('log', 'math.log10').replace('pi', 'math.pi')
                
                result = str(eval(temp_expr))
                
                # Update history
                self.history_listbox.insert(tk.END, f"{original_expr} = {result}")
                self.expression = result
            except Exception:
                messagebox.showerror("Error", "Invalid Input")
                self.expression = ""
        else:
            if char in ['sin', 'cos', 'tan', 'sqrt', 'log']:
                self.expression += char + "("
            else:
                self.expression += str(char)
        
        self.input_text.set(self.expression)

    def save_history(self):
        history_data = self.history_listbox.get(0, tk.END)
        if not history_data:
            messagebox.showwarning("Empty", "No history to save!")
            return
        
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "w") as f:
                for line in history_data:
                    f.write(line + "\n")
            messagebox.showinfo("Success", "History saved successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    app = ScientificCalculator(root)
    root.mainloop()
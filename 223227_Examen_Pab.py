import tkinter as tk
from tkinter import ttk

class PalindromeValidator:
    def __init__(self):
        self.valid_chars = {'a', 'b'}
        
    def is_palindrome(self, input_string):
        if not set(input_string).issubset(self.valid_chars):
            return "Error: solo se permiten caracteres 'a' y 'b'"
        
        return "Es un palíndromo" if input_string == input_string[::-1] else "No es un palíndromo"

class ExpandingPalindromeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Validador de Palíndromos")
        self.root.geometry("400x300")
        
        self.validator = PalindromeValidator()
        self.create_widgets()
        
    def create_widgets(self):
        title_label = tk.Label(self.root, text="Validador de Palíndromos (a,b)", font=('Helvetica', 14))
        title_label.pack(pady=10)
        
        self.input_text = tk.Text(self.root, font=('Helvetica', 12), width=30, height=5)
        self.input_text.pack(pady=5)
        
        validate_button = tk.Button(self.root, text="Validar", command=self.validate_palindromes, font=('Helvetica', 12))
        validate_button.pack(pady=10)
        
        self.results_label = tk.Label(self.root, text="Resultados:", font=('Helvetica', 12, 'bold'))
        self.results_label.pack(pady=5)
        
        self.result_text = tk.Text(self.root, font=('Helvetica', 10), width=40, height=1, state=tk.DISABLED)
        self.result_text.pack(pady=5, fill=tk.X)
        
    def validate_palindromes(self):
        input_lines = self.input_text.get("1.0", tk.END).strip().splitlines()
        
        self.result_text.config(state=tk.NORMAL)
        self.result_text.delete("1.0", tk.END)
        
        for line_number, line in enumerate(input_lines, start=1):
            result = self.validator.is_palindrome(line.lower())
            self.result_text.insert(tk.END, f"Línea {line_number}: {result}\n")
        
        new_height = len(input_lines)
        self.result_text.config(height=new_height)
        
        self.result_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpandingPalindromeGUI(root)
    root.mainloop()

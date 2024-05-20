import tkinter as tk
import random
import string

class PasswordGenerator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Password Generator")
        self.geometry("400x250")

        self.lowercase_chars = string.ascii_lowercase
        self.uppercase_chars = string.ascii_uppercase
        self.digits = string.digits
        self.symbols = string.punctuation

        main_frame = tk.Frame(self)
        main_frame.pack(pady=20)
        
        self.length_label = tk.Label(main_frame, text="Password Length:")
        self.length_label.pack(side=tk.LEFT)
        self.length_entry = tk.Entry(main_frame, width=5)
        self.length_entry.pack(side=tk.LEFT, padx=10)

        self.generate_button = tk.Button(main_frame, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(side=tk.LEFT, padx=10)

        self.password_text = tk.Text(self, height=5, width=40, font=("Arial", 12))
        self.password_text.pack(pady=20)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            password = self.create_password(length)
            self.password_text.delete("1.0", tk.END)
            self.password_text.insert(tk.END, password)
        except ValueError:
            self.password_text.delete("1.0", tk.END)
            self.password_text.insert(tk.END, "Invalid password length!")

    def create_password(self, length):
        alphabet_count = int(length * 0.8)
        non_alphabet_count = length - alphabet_count

        alphabet_chars = self.lowercase_chars + self.uppercase_chars
        non_alphabet_chars = self.digits + self.symbols

        password_chars = random.sample(alphabet_chars, alphabet_count) + random.sample(non_alphabet_chars, non_alphabet_count)
        random.shuffle(password_chars)

        password = "".join(password_chars)
        return password

if __name__ == "__main__":
    app = PasswordGenerator()
    app.mainloop()

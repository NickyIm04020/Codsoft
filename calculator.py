import tkinter as tk

def calculate(operation):
    try:
        num1 = float(num1_entry.get())
        num2 = float(num2_entry.get())

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                result = "Error: Division by zero!"
            else:
                result = num1 / num2
        else:
            result = "Invalid operation!"

        result_label.config(text=f"Result: {result}")

    except ValueError:
        result_label.config(text="Error: Invalid input!")

def clear_all():
    num1_entry.delete(0, tk.END)
    num2_entry.delete(0, tk.END)
    result_label.config(text="")

window = tk.Tk()
window.title("Simple Calculator by Yaswanth")
window.geometry("300x300")
window.configure(bg="#D2B48C")

num1_label = tk.Label(window, text="First Number:", bg="#D2B48C", fg="black")
num1_label.pack(pady=10)
num1_entry = tk.Entry(window, font=("Arial", 14))
num1_entry.pack()

num2_label = tk.Label(window, text="Second Number:", bg="#D2B48C", fg="black")
num2_label.pack(pady=10)
num2_entry = tk.Entry(window, font=("Arial", 14))
num2_entry.pack()

button_frame = tk.Frame(window, bg="#D2B48C")
button_frame.pack(pady=20)

add_button = tk.Button(button_frame, text="+", command=lambda: calculate('+'), width=5, font=("Arial", 14), bg="#A0522D", fg="white")
add_button.pack(side=tk.LEFT, padx=5)

subtract_button = tk.Button(button_frame, text="-", command=lambda: calculate('-'), width=5, font=("Arial", 14), bg="#A0522D", fg="white")
subtract_button.pack(side=tk.LEFT, padx=5)

multiply_button = tk.Button(button_frame, text="*", command=lambda: calculate('*'), width=5, font=("Arial", 14), bg="#A0522D", fg="white")
multiply_button.pack(side=tk.LEFT, padx=5)

divide_button = tk.Button(button_frame, text="/", command=lambda: calculate('/'), width=5, font=("Arial", 14), bg="#A0522D", fg="white")
divide_button.pack(side=tk.LEFT, padx=5)

reset_button = tk.Button(button_frame, text="Clear", command=clear_all, width=5, font=("Arial", 14), bg="#A0522D", fg="white")
reset_button.pack(side=tk.LEFT, padx=5)

result_label = tk.Label(window, text="", font=("Arial", 16), bg="#D2B48C", fg="black")
result_label.pack(pady=20)

window.mainloop()

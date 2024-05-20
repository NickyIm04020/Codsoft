import tkinter as tk
from tkinter import ttk

class ToDoList(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("To-Do List")
        self.geometry("400x400")

        style = ttk.Style()
        style.theme_use("clam")

        self.task_frame = ttk.Frame(self)
        self.task_frame.pack(padx=10, pady=10)

        self.task_treeview = ttk.Treeview(self.task_frame, columns=("Task", "Status"), show="headings")
        self.task_treeview.heading("Task", text="Task")
        self.task_treeview.heading("Status", text="Status")
        self.task_treeview.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = ttk.Scrollbar(self.task_frame, orient=tk.VERTICAL, command=self.task_treeview.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_treeview.configure(yscrollcommand=self.scrollbar.set)

        self.entry_frame = ttk.Frame(self)
        self.entry_frame.pack(padx=10, pady=10)

        self.task_entry = ttk.Entry(self.entry_frame, font=("Arial", 12))
        self.task_entry.pack(side=tk.LEFT, padx=5)

        self.add_button = ttk.Button(self.entry_frame, text="Add Task", command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=5)

        self.complete_button = ttk.Button(self.entry_frame, text="Mark as Complete", command=self.mark_as_complete)
        self.complete_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = ttk.Button(self.entry_frame, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=5)

        self.clear_button = ttk.Button(self.entry_frame, text="Clear Tasks", command=self.clear_tasks)
        self.clear_button.pack(side=tk.LEFT, padx=5)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_treeview.insert("", tk.END, values=(task, "Incomplete"))
            self.task_entry.delete(0, tk.END)

    def mark_as_complete(self):
        selected_item = self.task_treeview.focus()
        if selected_item:
            self.task_treeview.item(selected_item, values=(self.task_treeview.item(selected_item, "values")[0], "Complete"))

    def delete_task(self):
        selected_item = self.task_treeview.focus()
        if selected_item:
            self.task_treeview.delete(selected_item)

    def clear_tasks(self):
        self.task_treeview.delete(*self.task_treeview.get_children())

if __name__ == "__main__":
    app = ToDoList()
    app.mainloop()

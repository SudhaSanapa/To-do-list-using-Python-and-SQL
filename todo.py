import tkinter as tk
from tkinter import messagebox
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",  # Change this to your MySQL username
    password="password",  # Change this to your MySQL password
    database="todolist"
)
cursor = conn.cursor()

def fetch_items():
    listbox.delete(0, tk.END)
    cursor.execute("SELECT id, task_name FROM tasks")
    for row in cursor.fetchall():
        listbox.insert(tk.END, f"{row[0]} - {row[1]}")  # Display ID and Task Name


def add_item():
    task = entry.get()
    if task:
        cursor.execute("INSERT INTO tasks (task_name) VALUES (%s)", (task,))
        conn.commit()
        entry.delete(0, tk.END)
        fetch_items()
    else:
        messagebox.showwarning("Warning", "Please enter a task.")


def update_item():
    try:
        selected = listbox.get(listbox.curselection())
        task_id = selected.split(" - ")[0]  # Extract ID
        new_task = entry.get()
        if new_task:
            cursor.execute("UPDATE tasks SET task_name = %s WHERE id = %s", (new_task, task_id))
            conn.commit()
            entry.delete(0, tk.END)
            fetch_items()
        else:
            messagebox.showwarning("Warning", "Please enter a new task.")
    except:
        messagebox.showerror("Error", "Please select a task to update.")


def delete_item():
    try:
        selected = listbox.get(listbox.curselection())
        task_id = selected.split(" - ")[0]  # Extract ID
        cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
        conn.commit()
        fetch_items()
    except:
        messagebox.showerror("Error", "Please select a task to delete.")


def show_items():
    cursor.execute("SELECT task_name FROM tasks")
    items = cursor.fetchall()
    if items:
        messagebox.showinfo("Task List", "\n".join([item[0] for item in items]))
    else:
        messagebox.showinfo("Task List", "The list is empty.")


root = tk.Tk()
root.title("To-Do List Manager with MySQL")
root.geometry("450x400")

entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=10)


btn_frame = tk.Frame(root)
btn_frame.pack()

add_btn = tk.Button(btn_frame, text="Add", command=add_item, width=10)
add_btn.grid(row=0, column=0, padx=5)

update_btn = tk.Button(btn_frame, text="Update", command=update_item, width=10)
update_btn.grid(row=0, column=1, padx=5)

delete_btn = tk.Button(btn_frame, text="Delete", command=delete_item, width=10)
delete_btn.grid(row=0, column=2, padx=5)

show_btn = tk.Button(root, text="Show List", command=show_items, width=30)
show_btn.pack(pady=5)

# Listbox to display tasks
listbox = tk.Listbox(root, font=("Arial", 12), width=40, height=10)
listbox.pack(pady=10)


fetch_items()

# Run the application
root.mainloop()

# Close MySQL connection when the program exits
conn.close()

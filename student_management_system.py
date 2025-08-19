import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# --- Database Setup ---
conn = sqlite3.connect("students.db")
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT, contact TEXT, email TEXT,
    gender TEXT, dob TEXT, stream TEXT
)
""")
conn.commit()

# --- Functions ---
def add_record():
    data = (name_var.get(), contact_var.get(), email_var.get(),
            gender_var.get(), dob_var.get(), stream_var.get())

    if "" in data:
        messagebox.showerror("Error", "All fields are required")
        return

    cur.execute("INSERT INTO students (name, contact, email, gender, dob, stream) VALUES (?, ?, ?, ?, ?, ?)", data)
    conn.commit()
    messagebox.showinfo("Added", "Record added successfully")
    clear_fields()
    view_records()

def view_records():
    tree.delete(*tree.get_children())   # clear table
    cur.execute("SELECT * FROM students")
    for row in cur.fetchall():
        tree.insert("", tk.END, values=row)

def delete_record():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Warning", "Select a record to delete")
        return
    record_id = tree.item(selected[0])["values"][0]
    cur.execute("DELETE FROM students WHERE id=?", (record_id,))
    conn.commit()
    view_records()
    messagebox.showinfo("Deleted", "Record deleted successfully")

def clear_fields():
    for var in (name_var, contact_var, email_var, gender_var, dob_var, stream_var):
        var.set("")

def remove_all_records():
    cur.execute("DELETE FROM students")
    conn.commit()
    view_records()
    messagebox.showinfo("Cleared", "All records deleted")

# GUI Setup
root = tk.Tk()
root.title("Student Management System")
root.geometry("900x500")
root.config(bg="lightblue")

# Variables
name_var, contact_var, email_var = tk.StringVar(), tk.StringVar(), tk.StringVar()
gender_var, dob_var, stream_var = tk.StringVar(), tk.StringVar(), tk.StringVar()

# Labels & Inputs
fields = [("Name", name_var), ("Contact No", contact_var), ("Email", email_var),
          ("Gender", gender_var), ("DOB", dob_var), ("Stream", stream_var)]
y = 30
for label, var in fields:
    tk.Label(root, text=label).place(x=30, y=y)
    if label == "Gender":
        ttk.Combobox(root, textvariable=var, values=["Male", "Female"]).place(x=150, y=y)
    else:
        tk.Entry(root, textvariable=var).place(x=150, y=y)
    y += 40

# Buttons
tk.Button(root, text="Add", command=add_record, bg="green", fg="white").place(x=30, y=280)
tk.Button(root, text="View", command=view_records, bg="blue", fg="white").place(x=100, y=280)
tk.Button(root, text="Delete", command=delete_record, bg="red", fg="white").place(x=170, y=280)
tk.Button(root, text="Clear Fields", command=clear_fields, bg="orange", fg="white").place(x=240, y=280)
tk.Button(root, text="Clear All Records", command=remove_all_records, bg="black", fg="white").place(x=350, y=280)

# Table
cols = ("ID", "Name", "Contact", "Email", "Gender", "DOB", "Stream")
tree = ttk.Treeview(root, columns=cols, show="headings")
for col in cols:
    tree.heading(col, text=col)
tree.place(x=350, y=30, width=520, height=230)

# Show existing records on startup
view_records()

root.mainloop()

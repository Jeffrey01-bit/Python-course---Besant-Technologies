"""
Simple Student Registration - Tkinter + SQLAlchemy
====================================================
Install: pip install sqlalchemy pymysql
"""

import tkinter as tk
from tkinter import ttk, messagebox
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import DeclarativeBase, Session

# ── Database Setup ─────────────────────────────────────────────────────────
# Change credentials below
DB_URL = "mysql+pymysql://root:Goldenjef8@localhost/pythonclass"

try:
    engine = create_engine(DB_URL)
except Exception as e:
    print(e)

class Base(DeclarativeBase):
    pass

class Student(Base):
    __tablename__ = "students"
    id      = Column(Integer, primary_key=True, autoincrement=True)
    name    = Column(String(100), nullable=False)
    email   = Column(String(100), unique=True, nullable=False)
    phone   = Column(String(15))
    course  = Column(String(100))

Base.metadata.create_all(engine)   # creates table if not exists

# ── Main Window ────────────────────────────────────────────────────────────
root = tk.Tk()
root.title("Student Registration")
root.geometry("750x500")
root.resizable(False, False)

selected_id = None  # tracks which row is being edited

# ── Form Variables ─────────────────────────────────────────────────────────
var_name   = tk.StringVar()
var_email  = tk.StringVar()
var_phone  = tk.StringVar()
var_course = tk.StringVar()

# ── Form Frame ─────────────────────────────────────────────────────────────
form = tk.LabelFrame(root, text="Student Details", padx=10, pady=10)
form.pack(padx=20, pady=10, fill=tk.X)

fields = [("Name",   var_name),
          ("Email",  var_email),
          ("Phone",  var_phone),
          ("Course", var_course)]

for i, (label, var) in enumerate(fields):
    tk.Label(form, text=label, width=10, anchor=tk.W).grid(row=i, column=0, pady=4)
    tk.Entry(form, textvariable=var, width=40).grid(row=i, column=1, pady=4, padx=8)

# ── CRUD Functions ─────────────────────────────────────────────────────────
def get_form():
    name  = var_name.get().strip()
    email = var_email.get().strip()
    if not name or not email:
        messagebox.showwarning("Validation", "Name and Email are required.")
        return None
    return {"name": name, "email": email,
            "phone": var_phone.get().strip(),
            "course": var_course.get().strip()}

def clear_form():
    global selected_id
    selected_id = None
    for v in [var_name, var_email, var_phone, var_course]:
        v.set("")
    btn_update.config(state=tk.DISABLED)
    btn_save.config(state=tk.NORMAL)

def load_table():
    for row in tree.get_children():
        tree.delete(row)
    with Session(engine) as s:
        for st in s.query(Student).all():
            tree.insert("", tk.END, values=(st.id, st.name, st.email, st.phone, st.course))

def save():
    data = get_form()
    if not data:
        return
    try:
        with Session(engine) as s:
            s.add(Student(**data))
            s.commit()
        messagebox.showinfo("Saved", "Student added successfully.")

    except Exception as e:
        messagebox.showerror("Database Error", str(e))
    clear_form()
    load_table()
    messagebox.showinfo("Saved", "Student added successfully.")

def on_select(event):
    global selected_id
    sel = tree.selection()
    if not sel:
        return
    vals = tree.item(sel[0])["values"]
    selected_id = vals[0]
    var_name.set(vals[1])
    var_email.set(vals[2])
    var_phone.set(vals[3] if vals[3] else "")
    var_course.set(vals[4] if vals[4] else "")
    btn_update.config(state=tk.NORMAL)
    btn_save.config(state=tk.DISABLED)

def update():
    if not selected_id:
        return
    data = get_form()
    if not data:
        return
    with Session(engine) as s:
        st = s.get(Student, selected_id)
        if st:
            st.name   = data["name"]
            st.email  = data["email"]
            st.phone  = data["phone"]
            st.course = data["course"]
            s.commit()
    clear_form()
    load_table()
    messagebox.showinfo("Updated", "Record updated.")

def delete():
    sel = tree.selection()
    print(tree.item(sel[0])["values"][0])
    if not sel:
        messagebox.showwarning("Select", "Please select a row to delete.")
        return
    sid = tree.item(sel[0])["values"][0]
    if messagebox.askyesno("Confirm", "Delete this student?"):
        with Session(engine) as s:
            st = s.get(Student, sid)
            if st:
                s.delete(st)
                s.commit()
        clear_form()
        load_table()

# ── Buttons ────────────────────────────────────────────────────────────────
btn_frame = tk.Frame(root)
btn_frame.pack(pady=6)

btn_save   = tk.Button(btn_frame, text="Save",   width=12, bg="#4CAF50", fg="white", command=save)
btn_update = tk.Button(btn_frame, text="Update", width=12, bg="#FF9800", fg="white", command=update, state=tk.DISABLED)
btn_delete = tk.Button(btn_frame, text="Delete", width=12, bg="#F44336", fg="white", command=delete)
btn_clear  = tk.Button(btn_frame, text="Clear",  width=12,               command=clear_form)

for btn in (btn_save, btn_update, btn_delete, btn_clear):
    btn.pack(side=tk.LEFT, padx=6)

# ── Table ──────────────────────────────────────────────────────────────────
cols = ("ID", "Name", "Email", "Phone", "Course")
tree = ttk.Treeview(root, columns=cols, show="headings", height=12)

for col in cols:
    tree.heading(col, text=col)
    tree.column(col, width=130, anchor=tk.CENTER)
tree.column("ID", width=40)

tree.pack(padx=20, pady=8, fill=tk.X)
tree.bind("<<TreeviewSelect>>", on_select)

# ── Load & Run ─────────────────────────────────────────────────────────────
load_table()
root.mainloop()
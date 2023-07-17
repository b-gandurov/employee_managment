import tkinter as tk
from tkinter import messagebox
from crud_operations import add_employee, get_employee, update_employee, delete_employee, generate_report, \
    add_department, get_departments, get_conn, get_roles, view_employee

def handle_add():
    name = name_entry.get()
    contact = contact_entry.get()
    department_id = departments[department_var.get()]
    role_id = roles[role_var.get()]

    try:
        department_id = int(department_id)
        role_id = int(role_id)
    except ValueError:
        messagebox.showerror("Invalid Input", "Department ID and Role ID must be integers")
        return

    add_employee(name, contact, department_id, role_id)
    name_entry.delete(0, tk.END)
    contact_entry.delete(0, tk.END)
    messagebox.showinfo("Success", f"Employee {name} added successfully!")

def handle_view():
    name = name_entry.get()
    employee = view_employee(name)
    if employee:
        result = f"ID: {employee[0]}, Name: {employee[1]}, Contact: {employee[2]}, Department: {employee[3]}, Role: {employee[4]}"
        messagebox.showinfo("Employee Details", result)
    else:
        messagebox.showerror("Error", "No such employee")

def handle_update():
    name = name_entry.get()
    employee = view_employee(name)
    if employee:
        name = name_entry.get()
        contact = contact_entry.get()
        department = department_var.get()
        role = role_var.get()
        if all([name, contact, department, role]):
            department_id = departments[department]
            role_id = roles[role]
            try:
                department_id = int(department_id)
                role_id = int(role_id)
            except ValueError:
                messagebox.showerror("Invalid Input", "Department and Role must be valid selections")
                return

            update_employee(employee[0], name, contact, department_id, role_id)
            messagebox.showinfo("Success", "Employee updated successfully")
        else:
            messagebox.showerror('Error', "Please fill all the fields")
    else:
        messagebox.showerror('Error', "No such employee")

def handle_delete():
    name = name_entry.get()
    employee = get_employee(name)
    if employee:
        delete_employee(employee[0])
        messagebox.showinfo("Success", "Employee deleted successfully")
    else:
        messagebox.showerror('Error',"No such employee")

def handle_report():
    report = generate_report()
    print(f"Report data: {report}")
    report_text = ""
    for employee in report:
        report_text += f"ID: {employee[0]}, Name: {employee[1]}, Contact: {employee[2]}, Department: {employee[3]}, Role: {employee[4]}\n"
    messagebox.showinfo("Employee Report", report_text)

def handle_add_department():
    name = department_name_entry.get()
    if name:
        add_department(name)
        messagebox.showinfo("Success", "Department added successfully")
        start_gui()
    else:
        messagebox.showerror('Error', "Please fill the field")

# UI Component Definitions
base = tk.Tk()
conn = get_conn()
departments_db = get_departments()
departments = {name: id for id, name in departments_db}
department_var = tk.StringVar(base)

if departments:
    department_dropdown = tk.OptionMenu(base, department_var, *departments.keys())
else:
    department_dropdown = tk.OptionMenu(base, department_var, "No Departments")

name_label = tk.Label(base, text="Name:")
name_entry = tk.Entry(base)

contact_label = tk.Label(base, text="Contact:")
contact_entry = tk.Entry(base)

department_label = tk.Label(base, text="Department:")

add_department_button = tk.Button(base, text="Add Department", command=handle_add_department, width=15)

department_name_label = tk.Label(base, text="New Department:")
department_name_entry = tk.Entry(base)

add_button = tk.Button(base, text="Add Employee", command=handle_add, width=15)
view_button = tk.Button(base, text="View Employee", command=handle_view, width=15)
update_button = tk.Button(base, text="Update Employee", command=handle_update, width=15)
delete_button = tk.Button(base, text="Delete Employee", command=handle_delete, width=15)
report_button = tk.Button(base, text="Generate Report", command=handle_report, width=15)

roles_db = get_roles()
roles = {name: id for id, name in roles_db}
role_var = tk.StringVar(base)

if roles:
    role_dropdown = tk.OptionMenu(base, role_var, *roles.keys())
else:
    role_dropdown = tk.OptionMenu(base, role_var, "")

role_label = tk.Label(base, text="Role:")

# Grid Placement
name_label.grid(row=1, column=0)
name_entry.grid(row=1, column=1)

contact_label.grid(row=2, column=0)
contact_entry.grid(row=2, column=1)

department_label.grid(row=3, column=0)
department_dropdown.grid(row=3, column=1)

department_name_label.grid(row=5, column=0)
department_name_entry.grid(row=5, column=1)

add_department_button.grid(row=5, column=2)

add_button.grid(row=0, column=2)
view_button.grid(row=1, column=2)
update_button.grid(row=2, column=2)
delete_button.grid(row=3, column=2)
report_button.grid(row=4, column=2)

role_label.grid(row=4, column=0)
role_dropdown.grid(row=4, column=1)

def start_gui():
    base.mainloop()




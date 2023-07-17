import sqlite3


def setup_db():
    conn = sqlite3.connect('employee_management.db')
    conn.execute("PRAGMA foreign_keys = ON")
    cursor = conn.cursor()

    # Create the departments table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS departments(
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE
    )
    """)

    # Create the roles table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS roles(
        id INTEGER PRIMARY KEY,
        name TEXT UNIQUE
    )
    """)

    # Create the employees table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            contact TEXT,
            department_id INTEGER,
            role_id INTEGER,
            FOREIGN KEY(department_id) REFERENCES departments(id),
            FOREIGN KEY(role_id) REFERENCES roles(id)
        )
    """)

    # Adding default roles
    cursor.execute("INSERT OR IGNORE INTO roles (name) VALUES (?)", ('Manager',))
    cursor.execute("INSERT OR IGNORE INTO roles (name) VALUES (?)", ('Developer',))
    cursor.execute("INSERT OR IGNORE INTO roles (name) VALUES (?)", ('HR',))

    # Adding default departments
    cursor.execute("INSERT OR IGNORE INTO departments (name) VALUES (?)", ('Sales',))
    cursor.execute("INSERT OR IGNORE INTO departments (name) VALUES (?)", ('IT',))
    cursor.execute("INSERT OR IGNORE INTO departments (name) VALUES (?)", ('HR Department',))

    conn.commit()
    conn.close()

setup_db()

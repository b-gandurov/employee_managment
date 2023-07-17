import sqlite3

DATABASE_NAME = 'employee_management.db'

def with_connection(func):
    def with_connection_(*args, **kwargs):
        with sqlite3.connect(DATABASE_NAME) as conn:
            return func(conn, *args, **kwargs)
    return with_connection_

def get_conn():
    return with_connection

@with_connection
def add_employee(conn, name, contact, department_id, role_id):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO employees (name, contact, department_id, role_id) VALUES (?, ?, ?, ?)",
        (name, contact, department_id, role_id),
    )

@with_connection
def view_employee(conn, name):
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT employees.id, employees.name, employees.contact, departments.name, roles.name 
        FROM employees 
        INNER JOIN departments ON employees.department_id = departments.id 
        INNER JOIN roles ON employees.role_id = roles.id 
        WHERE employees.name = ?
        """,
        (name,)
    )
    return cursor.fetchone()

@with_connection
def get_departments(conn):
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM departments
    """)
    return cursor.fetchall()

@with_connection
def get_employee(conn, name):
    cursor = conn.cursor()
    cursor.execute(
        '''
        SELECT * FROM employees
        WHERE name = ?
        ''',
        (name,)
    )
    return cursor.fetchone()

@with_connection
def update_employee(conn, id, name, contact, department_id, role_id):
    cursor = conn.cursor()
    cursor.execute(
        '''
        UPDATE employees
        SET name = ?, contact = ?, department_id = ?, role_id = ?
        WHERE id = ?
        ''',
        (name, contact, department_id, role_id, id)
    )
    conn.commit()

@with_connection
def delete_employee(conn, id):
    cursor = conn.cursor()
    cursor.execute(
        '''
        DELETE FROM employees
        WHERE id = ?
        ''',
        (id,)
    )
    conn.commit()

@with_connection
def generate_report(conn):
    cursor = conn.cursor()
    sql_statement = """
        SELECT employees.id, employees.name, employees.contact, departments.name, roles.name
        FROM employees
        INNER JOIN departments ON employees.department_id = departments.id
        INNER JOIN roles ON employees.role_id = roles.id
    """
    cursor.execute(sql_statement)
    result = cursor.fetchall()
    return result

@with_connection
def add_department(conn,name):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO departments(name)
        VALUES(?)
    """, (name,))
    conn.commit()

@with_connection
def get_all_departments(conn):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM departments
    """)
    departments = cursor.fetchall()
    return departments

@with_connection
def get_departments(conn):
    cursor = conn.cursor()
    cursor.execute("""
    SELECT id, name
    FROM departments
    """)
    return cursor.fetchall()

@with_connection
def add_role(conn,role_name):
        cursor = conn.cursor()
        cursor.execute("INSERT INTO roles (role_name) VALUES (?)", (role_name,))
@with_connection
def get_roles(conn):
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM roles")
        return cursor.fetchall()


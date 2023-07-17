import os
from database_setup import setup_db
from gui import start_gui


def main():
    if not os.path.isfile('employee_management.db'):
        setup_db()


if __name__ == '__main__':
    main()
    start_gui()

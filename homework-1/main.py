"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="12345"
)


def function_of_reading(file_name):
    with open(file_name, encoding='utf-8') as file:
        return file.readlines()


def function_of_appending(data, name_table):
    try:
        with conn.cursor() as cur:
            if name_table == 'customers':
                for element in data:
                    id, company, contact = element.split(',')
                    cur.execute(f"INSERT INTO {name_table} VALUES (%s, %s, %s)", (id, company, contact))
            elif name_table == 'employees':
                for element in data:
                    id, name, surname, title, bday, notes = element.split(',')
                    cur.execute(f"INSERT INTO {name_table} VALUES (%s, %s, %s, %s, %s, %s)",
                                (id, name, surname, title, bday, notes))
            elif name_table == 'orders':
                for element in data:
                    order, customer, employee, date, city = element.split(',')
                    cur.execute(f"INSERT INTO {name_table} VALUES (%s, %s, %s, %s, %s)",
                                (order, customer, employee, date, city))
            cur.execute(f"SELECT * FROM {name_table}")
            rows = cur.fetchall()
            for row in rows:
                print(row)

    finally:
        conn.close()

customers = function_of_reading('north_data/customers_data.csv')
employees = function_of_reading('north_data/employees_data.csv')
orders = function_of_reading('north_data/orders_data.csv')

function_of_appending(customers, 'customers')
function_of_appending(employees, 'employees')
function_of_appending(orders, 'orders')

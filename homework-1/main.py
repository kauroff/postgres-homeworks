"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2  # импортируем библиотеку psycopg2


def function_of_reading(file_name):  # решил делать через функции чтения файла и записи в БД
    with open(file_name, encoding='utf-8') as file:
        return file.read()


def function_of_appending(data, name_table):
    conn = psycopg2.connect(  # настраиваем соединение
        host="localhost",
        database="north",
        user="postgres",
        password="12345"
    )
    conn.autocommit = True  # автокоммит, чтобы не коммитить после каждого добавления данных
    try:  # оборачиваем в блок try
        with conn.cursor() as cur:
            list_of_data = data.split('\n')  # беру данные из csv файла и сплитую их, чтобы разбить
            if name_table == 'customers':  # делаю проверку на название таблицы, тк в разных таблицах разное кол-во столбцов
                for element in list_of_data[1:]: # со второго элемента, тк первый - название столбцов
                    element.replace(', ', '~') # тк в БД встречаются запятые, чтобы они не участвовали в разбиении по запятым, заменим их
                    if len(element.split(',')) == 3:  # проверка на последнюю пустую строку
                        element.replace('~', ', ') # возвращаем запятые обратно
                        id, company, contact = element.split(',')  # распаковка строки на данные в кортеж
                        cur.execute(f"INSERT INTO {name_table} VALUES (%s, %s, %s)",
                                    (id, company, contact))  # добавление данных в таблицу
            elif name_table == 'employees':  # такая же функция для каждой БД
                for element in list_of_data[1:]:
                    element.replace(', ', '~')
                    if len(element.split(',')) == 6:
                        element.replace('~', ', ')
                        id_, name, surname, title, bday, notes = element.split(',')
                        cur.execute(f"INSERT INTO {name_table} VALUES (%s, %s, %s, %s, %s, %s)",
                                    (id_, name, surname, title, bday, notes))
            elif name_table == 'orders':
                for element in list_of_data[1:]:
                    element.replace(', ', ', ')
                    if len(element.split(',')) == 5:
                        element.replace('~', '~')
                        order, customer, employee, date, city = element.split(',')
                        cur.execute(f"INSERT INTO {name_table} VALUES (%s, %s, %s, %s, %s)",
                                    (order, customer, employee, date, city))
    finally:
        conn.close()  # закрытие соединения


# работа с тремя БД
customers = function_of_reading('north_data/customers_data.csv')
employees = function_of_reading('north_data/employees_data.csv')
orders = function_of_reading('north_data/orders_data.csv')

function_of_appending(customers, 'customers')
function_of_appending(employees, 'employees')
function_of_appending(orders, 'orders')

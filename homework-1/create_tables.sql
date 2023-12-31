CREATE TABLE employees
(
	employee_id serial PRIMARY KEY,
	first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
	title varchar(100) NOT NULL,
	birth_date date NOT NULL,
	notes text NOT NULL
);

CREATE TABLE customers
(
	customer_id varchar(10) PRIMARY KEY,
	company_name varchar(100) NOT NULL,
	contact_name varchar(100) NOT NULL
);

CREATE TABLE orders
(
	order_id serial PRIMARY KEY,
	customer_id varchar(10) REFERENCES customers(customer_id),
	employee_id smallint NOT NULL REFERENCES employees(employee_id),
	order_date date NOT NULL,
	ship_city varchar(100) NOT NULL
);

DROP TABLE customers
DROP TABLE employees
DROP TABLE orders
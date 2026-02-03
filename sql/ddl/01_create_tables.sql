CREATE SCHEMA analytics;
SET search_path TO analytics;

CREATE TABLE analytics.customers(
	customer_id INT PRIMARY KEY,
	first_order_date DATE,
	city VARCHAR(50)
);

CREATE TABLE analytics.restaurants(
	restaurant_id INT PRIMARY KEY,
	category VARCHAR(50),
	city VARCHAR(50),
	comission_rate NUMERIC(5,4),
	active_flag BOOLEAN
);

CREATE TABLE analytics.cities(
	city VARCHAR(50) PRIMARY KEY,
	region VARCHAR(20),
	courier_cost_index NUMERIC(5,2)
);

CREATE TABLE analytics.fixed_costs(
	month DATE,
	tech_cost NUMERIC(12,2),
	marketing_cost NUMERIC(12,2),
	gna_cost NUMERIC(12,2)
);

CREATE TABLE analytics.orders(
	order_id BIGINT PRIMARY KEY,
	order_date DATE,
	city VARCHAR(50),
	restaurant_id INT,
	customer_id INT,
	order_value NUMERIC(10,2),
	delivery_fee NUMERIC(10,2),
	comission_rate NUMERIC(5,4),
	subsidy_value NUMERIC(10,2),
	delivery_cost NUMERIC(10,2),
	payment_fee NUMERIC(10,2),
	order_status VARCHAR(20)
);

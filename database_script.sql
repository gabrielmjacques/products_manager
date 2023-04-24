CREATE DATABASE products_manager;
USE products_manager;

CREATE TABLE products(
	id INTEGER PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(100) UNIQUE NOT NULL,
    product_stock INTEGER NOT NULL
);
-- ==============================================================================
-- CAPSTONE: AI-Generated Star Schema for E-Commerce Data Warehouse
-- ==============================================================================

-- 1. TIME DIMENSION
CREATE TABLE dim_time (
    time_id INT PRIMARY KEY,
    date_val DATE NOT NULL,
    day_of_week VARCHAR(10),
    month_name VARCHAR(15),
    quarter INT,
    year INT
);

-- 2. USER DIMENSION
CREATE TABLE dim_users (
    user_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email_hash VARCHAR(255) NOT NULL, -- Hashed for PII compliance
    registration_date DATE
);

-- 3. PRODUCT DIMENSION
CREATE TABLE dim_products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50),
    unit_price DECIMAL(10,2)
);

-- 4. SALES FACT TABLE
CREATE TABLE fact_sales (
    sale_id INT PRIMARY KEY,
    time_id INT,
    user_id INT,
    product_id INT,
    quantity_sold INT,
    total_amount DECIMAL(10,2),
    FOREIGN KEY (time_id) REFERENCES dim_time(time_id),
    FOREIGN KEY (user_id) REFERENCES dim_users(user_id),
    FOREIGN KEY (product_id) REFERENCES dim_products(product_id)
);

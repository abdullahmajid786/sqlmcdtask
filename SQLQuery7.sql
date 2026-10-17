USE BikeStores;
GO

/*
================================================================================
SECTION 7 — Window Functions & Window Framing
Database: BikeStores
================================================================================
*/


-- =============================================================================
-- Task 7.1: Assign a sequential row number to each product ordered by list_price
-- descending. Then assign a second row number partitioned by category_id,
-- resetting within each category.
-- =============================================================================
SELECT
    p.product_id,
    p.product_name,
    p.category_id,
    c.category_name,
    p.list_price,
    ROW_NUMBER() OVER (
        ORDER BY p.list_price DESC
    ) AS overall_row_num,
    ROW_NUMBER() OVER (
        PARTITION BY p.category_id 
        ORDER BY p.list_price DESC
    ) AS category_row_num
FROM production.products AS p
INNER JOIN production.categories AS c
    ON p.category_id = c.category_id
ORDER BY p.category_id, category_row_num;
GO


-- =============================================================================
-- Task 7.2: Write a query that returns each product with its RANK() and 
-- DENSE_RANK() by list_price descending within its category. 
-- Show a product where the two rankings differ.
-- =============================================================================

WITH RankedProducts AS (
    SELECT
        p.product_id,
        p.product_name,
        p.category_id,
        c.category_name,
        p.list_price,
        RANK() OVER (
            PARTITION BY p.category_id 
            ORDER BY p.list_price DESC
        ) AS price_rank,
        DENSE_RANK() OVER (
            PARTITION BY p.category_id 
            ORDER BY p.list_price DESC
        ) AS price_dense_rank
    FROM production.products AS p
    INNER JOIN production.categories AS c
        ON p.category_id = c.category_id
)
SELECT
    product_id,
    product_name,
    category_id,
    category_name,
    list_price,
    price_rank,
    price_dense_rank,
    (price_rank - price_dense_rank) AS rank_gap
FROM RankedProducts
WHERE price_rank <> price_dense_rank
ORDER BY category_id, price_rank;
GO


-- =============================================================================
-- Task 7.3: Use LAG() to calculate the month-over-month revenue change for 
-- each store. Show the current month revenue, the previous month revenue, 
-- and the difference.
-- =============================================================================
WITH MonthlyStoreRevenue AS (
    SELECT
        st.store_id,
        st.store_name,
        YEAR(o.order_date) AS order_year,
        MONTH(o.order_date) AS order_month,
        SUM(oi.quantity * oi.list_price * (1.0 - oi.discount)) AS current_month_revenue
    FROM sales.orders AS o
    INNER JOIN sales.order_items AS oi
        ON o.order_id = oi.order_id
    INNER JOIN sales.stores AS st
        ON o.store_id = st.store_id
    GROUP BY st.store_id, st.store_name, YEAR(o.order_date), MONTH(o.order_date)
)
SELECT
    store_id,
    store_name,
    order_year,
    order_month,
    CAST(current_month_revenue AS DECIMAL(14, 2)) AS current_month_revenue,
    CAST(LAG(current_month_revenue, 1) OVER (
        PARTITION BY store_id 
        ORDER BY order_year, order_month
    ) AS DECIMAL(14, 2)) AS previous_month_revenue,
    CAST(current_month_revenue - LAG(current_month_revenue, 1) OVER (
        PARTITION BY store_id 
        ORDER BY order_year, order_month
    ) AS DECIMAL(14, 2)) AS mom_revenue_difference
FROM MonthlyStoreRevenue
ORDER BY store_id, order_year, order_month;
GO


-- =============================================================================
-- Task 7.4: Use NTILE(5) to divide all products into five price bands. 
-- Return the product name, price, and band number.
-- =============================================================================
SELECT
    product_name,
    list_price,
    NTILE(5) OVER (
        ORDER BY list_price ASC
    ) AS price_band
FROM production.products
ORDER BY price_band, list_price, product_name;
GO


-- =============================================================================
-- Task 7.5: Write a query that shows each order with a running total of revenue 
-- ordered by order_date. Use ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW.
-- =============================================================================
WITH OrderTotals AS (
    SELECT
        o.order_id,
        o.order_date,
        o.customer_id,
        SUM(oi.quantity * oi.list_price * (1.0 - oi.discount)) AS order_revenue
    FROM sales.orders AS o
    INNER JOIN sales.order_items AS oi
        ON o.order_id = oi.order_id
    GROUP BY o.order_id, o.order_date, o.customer_id
)
SELECT
    order_id,
    order_date,
    customer_id,
    CAST(order_revenue AS DECIMAL(12, 2)) AS order_revenue,
    CAST(SUM(order_revenue) OVER (
        ORDER BY order_date, order_id
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS DECIMAL(14, 2)) AS running_total_revenue
FROM OrderTotals
ORDER BY order_date, order_id;
GO


-- =============================================================================
-- Task 7.6: Think About It:
-- Question:
-- Why does LAST_VALUE() require RANGE BETWEEN UNBOUNDED PRECEDING AND 
-- UNBOUNDED FOLLOWING to return the actual last value in the partition, 
-- while FIRST_VALUE() works correctly with the default frame? 
-- What is the default window frame when ORDER BY is specified, and how 
-- does that explain the behavior?
-- =============================================================================

-- Demonstration Query for 7.6:
SELECT
    product_id,
    product_name,
    category_id,
    list_price,
    -- FIRST_VALUE works with default frame:
    FIRST_VALUE(list_price) OVER (
        PARTITION BY category_id 
        ORDER BY list_price DESC
    ) AS highest_price_in_cat_first_val,

    -- LAST_VALUE with DEFAULT frame (returns current row's price, NOT the actual last):
    LAST_VALUE(list_price) OVER (
        PARTITION BY category_id 
        ORDER BY list_price DESC
    ) AS default_frame_last_val_unexpected,

    -- LAST_VALUE with EXPLICIT UNBOUNDED FOLLOWING (returns the true lowest price in category):
    LAST_VALUE(list_price) OVER (
        PARTITION BY category_id 
        ORDER BY list_price DESC
        ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
    ) AS actual_last_price_in_cat
FROM production.products
ORDER BY category_id, list_price DESC;
GO

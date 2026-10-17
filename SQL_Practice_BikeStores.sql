

USE bikestore;
GO

-- SECTION 1: JOINS

-- Q1. (Easy) List every order with the customer's full name, store name, 

SELECT
    o.order_id,
    o.order_date,
    c.first_name + ' ' + c.last_name AS customer_full_name,
    st.store_name,
    sf.first_name + ' ' + sf.last_name AS staff_full_name,
    CASE o.order_status
        WHEN 1 THEN 'Pending'
        WHEN 2 THEN 'Processing'
        WHEN 3 THEN 'Rejected'
        WHEN 4 THEN 'Completed'
        ELSE 'Unknown'
    END AS order_status_description
FROM sales.orders AS o
INNER JOIN sales.customers AS c
    ON o.customer_id = c.customer_id
INNER JOIN sales.stores AS st
    ON o.store_id = st.store_id
INNER JOIN sales.staffs AS sf
    ON o.staff_id = sf.staff_id
ORDER BY o.order_id;
GO


-- -----------------------------------------------------------------------------
-- Q2. (Easy) Show each product with its brand name and category name. 
--            Include products even if they have no brand or category assigned.
-- -----------------------------------------------------------------------------
SELECT
    p.product_id,
    p.product_name,
    ISNULL(b.brand_name, 'No Brand') AS brand_name,
    ISNULL(c.category_name, 'No Category') AS category_name,
    p.list_price,
    p.model_year
FROM production.products AS p
LEFT JOIN production.brands AS b
    ON p.brand_id = b.brand_id
LEFT JOIN production.categories AS c
    ON p.category_id = c.category_id
ORDER BY p.product_id;
GO


-- -----------------------------------------------------------------------------
-- Q3. (Medium) Find all customers who have never placed an order. 
--              Return their name, city, and email.
-- -----------------------------------------------------------------------------
SELECT
    c.customer_id,
    c.first_name + ' ' + c.last_name AS customer_name,
    c.city,
    c.email
FROM sales.customers AS c
LEFT JOIN sales.orders AS o
    ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL
ORDER BY c.customer_id;
GO


-- =============================================================================
-- SECTION 2: GROUP BY
-- =============================================================================

-- -----------------------------------------------------------------------------
-- Q4. (Easy) Calculate total revenue per store. 
--            Revenue = quantity * list_price * (1 - discount). 
--            Sort from highest to lowest.
-- -----------------------------------------------------------------------------
SELECT
    st.store_id,
    st.store_name,
    CAST(SUM(oi.quantity * oi.list_price * (1 - oi.discount)) AS DECIMAL(14, 2)) AS total_revenue
FROM sales.stores AS st
INNER JOIN sales.orders AS o
    ON st.store_id = o.store_id
INNER JOIN sales.order_items AS oi
    ON o.order_id = oi.order_id
GROUP BY st.store_id, st.store_name
ORDER BY total_revenue DESC;
GO


-- -----------------------------------------------------------------------------
-- Q5. (Medium) For each brand, show the number of products, the average list price, 
--              and the highest list price. Only include brands with more than 5 products.
-- -----------------------------------------------------------------------------
SELECT
    b.brand_id,
    b.brand_name,
    COUNT(p.product_id) AS total_products,
    CAST(AVG(p.list_price) AS DECIMAL(10, 2)) AS average_list_price,
    MAX(p.list_price) AS highest_list_price
FROM production.brands AS b
INNER JOIN production.products AS p
    ON b.brand_id = p.brand_id
GROUP BY b.brand_id, b.brand_name
HAVING COUNT(p.product_id) > 5
ORDER BY total_products DESC;
GO


-- -----------------------------------------------------------------------------
-- Q6. (Medium) Show the number of orders and total revenue per month for the year 2017, 
--              ordered chronologically.
-- -----------------------------------------------------------------------------
SELECT
    MONTH(o.order_date) AS order_month,
    DATENAME(month, o.order_date) AS month_name,
    COUNT(DISTINCT o.order_id) AS number_of_orders,
    CAST(SUM(oi.quantity * oi.list_price * (1 - oi.discount)) AS DECIMAL(14, 2)) AS total_revenue
FROM sales.orders AS o
INNER JOIN sales.order_items AS oi
    ON o.order_id = oi.order_id
WHERE YEAR(o.order_date) = 2017
GROUP BY MONTH(o.order_date), DATENAME(month, o.order_date)
ORDER BY order_month ASC;
GO


-- =============================================================================
-- SECTION 3: SUBQUERIES
-- =============================================================================

-- -----------------------------------------------------------------------------
-- Q7. (Medium) Find all products priced above the average list price of their 
--              own category. (Correlated Subquery)
-- -----------------------------------------------------------------------------
SELECT
    p.product_id,
    p.product_name,
    p.category_id,
    p.list_price,
    CAST((
        SELECT AVG(p2.list_price)
        FROM production.products AS p2
        WHERE p2.category_id = p.category_id
    ) AS DECIMAL(10, 2)) AS category_avg_price
FROM production.products AS p
WHERE p.list_price > (
    SELECT AVG(p2.list_price)
    FROM production.products AS p2
    WHERE p2.category_id = p.category_id
)
ORDER BY p.category_id, p.list_price DESC;
GO


-- -----------------------------------------------------------------------------
-- Q8. (Medium) List the customers who have placed more orders than the 
--              average number of orders per customer.
-- -----------------------------------------------------------------------------
SELECT
    c.customer_id,
    c.first_name + ' ' + c.last_name AS customer_name,
    c.email,
    COUNT(o.order_id) AS total_orders
FROM sales.customers AS c
INNER JOIN sales.orders AS o
    ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.first_name, c.last_name, c.email
HAVING COUNT(o.order_id) > (
    SELECT AVG(CAST(cust_order_counts.order_count AS FLOAT))
    FROM (
        SELECT COUNT(order_id) AS order_count
        FROM sales.orders
        GROUP BY customer_id
    ) AS cust_order_counts
)
ORDER BY total_orders DESC, customer_name;
GO


-- =============================================================================
-- SECTION 4: CTES (COMMON TABLE EXPRESSIONS)
-- =============================================================================

-- -----------------------------------------------------------------------------
-- Q9. (Hard) Using a CTE, calculate each customer's total spend, then return 
--            the top 10 customers with their spend and rank. Add a second CTE 
--            that labels each customer as "High" (above the overall average spend) 
--            or "Regular".
-- -----------------------------------------------------------------------------
WITH CustomerSpend AS (
    SELECT
        c.customer_id,
        c.first_name + ' ' + c.last_name AS customer_name,
        SUM(oi.quantity * oi.list_price * (1 - oi.discount)) AS total_spend
    FROM sales.customers AS c
    INNER JOIN sales.orders AS o
        ON c.customer_id = o.customer_id
    INNER JOIN sales.order_items AS oi
        ON o.order_id = oi.order_id
    GROUP BY c.customer_id, c.first_name, c.last_name
),
CustomerClassification AS (
    SELECT
        customer_id,
        customer_name,
        total_spend,
        DENSE_RANK() OVER (ORDER BY total_spend DESC) AS spend_rank,
        CASE
            WHEN total_spend > AVG(total_spend) OVER () THEN 'High'
            ELSE 'Regular'
        END AS spend_tier
    FROM CustomerSpend
)
SELECT TOP 10
    customer_id,
    customer_name,
    CAST(total_spend AS DECIMAL(14, 2)) AS total_spend,
    spend_rank,
    spend_tier
FROM CustomerClassification
ORDER BY spend_rank ASC;
GO


-- -----------------------------------------------------------------------------
-- Q10. (Hard) Using CTEs, find the best-selling product (by quantity) in each 
--             category, and show how much of that product's stock is currently 
--             available across all stores.
-- -----------------------------------------------------------------------------
WITH ProductQuantitySold AS (
    SELECT
        p.category_id,
        p.product_id,
        p.product_name,
        SUM(oi.quantity) AS total_qty_sold
    FROM production.products AS p
    INNER JOIN sales.order_items AS oi
        ON p.product_id = oi.product_id
    GROUP BY p.category_id, p.product_id, p.product_name
),
RankedCategoryProducts AS (
    SELECT
        category_id,
        product_id,
        product_name,
        total_qty_sold,
        ROW_NUMBER() OVER (
            PARTITION BY category_id 
            ORDER BY total_qty_sold DESC
        ) AS rank_in_category
    FROM ProductQuantitySold
),
TotalProductStock AS (
    SELECT
        product_id,
        SUM(quantity) AS total_stock_available
    FROM production.stocks
    GROUP BY product_id
)
SELECT
    c.category_id,
    c.category_name,
    r.product_id,
    r.product_name,
    r.total_qty_sold,
    ISNULL(s.total_stock_available, 0) AS total_stock_available
FROM RankedCategoryProducts AS r
INNER JOIN production.categories AS c
    ON r.category_id = c.category_id
LEFT JOIN TotalProductStock AS s
    ON r.product_id = s.product_id
WHERE r.rank_in_category = 1
ORDER BY c.category_id;
GO


-- =============================================================================
-- SECTION 5: BONUS CHALLENGES
-- =============================================================================

-- -----------------------------------------------------------------------------
-- Bonus 1: Rewrite Q8 using a CTE instead of a subquery and compare readability.
--
-- Readability Comparison:
-- 1. Modular Structure: The CTE breaks the logic into two distinct, named steps
--    (CustomerOrderCounts and BenchmarkAvgOrders), making the query self-documenting.
-- 2. Maintainability: The average threshold is calculated once and easily reused
--    without deeply nesting subqueries inside the HAVING clause.
-- 3. Debugging: Each CTE can be tested individually by running SELECT * FROM <CTE>.
-- -----------------------------------------------------------------------------
WITH CustomerOrderCounts AS (
    SELECT
        c.customer_id,
        c.first_name + ' ' + c.last_name AS customer_name,
        c.email,
        COUNT(o.order_id) AS total_orders
    FROM sales.customers AS c
    INNER JOIN sales.orders AS o
        ON c.customer_id = o.customer_id
    GROUP BY c.customer_id, c.first_name, c.last_name, c.email
),
BenchmarkAvgOrders AS (
    SELECT AVG(CAST(total_orders AS FLOAT)) AS avg_orders_per_customer
    FROM CustomerOrderCounts
)
SELECT
    coc.customer_id,
    coc.customer_name,
    coc.email,
    coc.total_orders,
    CAST(bao.avg_orders_per_customer AS DECIMAL(4, 2)) AS overall_avg_orders
FROM CustomerOrderCounts AS coc
CROSS JOIN BenchmarkAvgOrders AS bao
WHERE coc.total_orders > bao.avg_orders_per_customer
ORDER BY coc.total_orders DESC, coc.customer_name;
GO


-- -----------------------------------------------------------------------------
-- Bonus 2: For Q4, add a column showing each store's percentage share 
--          of total company revenue.
-- -----------------------------------------------------------------------------
WITH StoreRevenueCTE AS (
    SELECT
        st.store_id,
        st.store_name,
        SUM(oi.quantity * oi.list_price * (1 - oi.discount)) AS store_revenue
    FROM sales.stores AS st
    INNER JOIN sales.orders AS o
        ON st.store_id = o.store_id
    INNER JOIN sales.order_items AS oi
        ON o.order_id = oi.order_id
    GROUP BY st.store_id, st.store_name
)
SELECT
    store_id,
    store_name,
    CAST(store_revenue AS DECIMAL(14, 2)) AS store_revenue,
    CAST(
        (store_revenue * 100.0) / SUM(store_revenue) OVER () 
        AS DECIMAL(5, 2)
    ) AS revenue_percentage_share
FROM StoreRevenueCTE
ORDER BY store_revenue DESC;
GO

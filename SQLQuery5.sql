
   --SECTION 5 
   

-- Task 29: Find all products whose list price is above the overall average list price.
SELECT
    product_name,
    list_price
FROM production.products
WHERE list_price > (SELECT AVG(list_price) FROM production.products);


-- Task 30: Find customers who have never placed an order.
SELECT
    customer_id,
    first_name,
    last_name
FROM sales.customers
WHERE customer_id NOT IN (
    SELECT customer_id
    FROM sales.orders
    WHERE customer_id IS NOT NULL
);



-- Task 31: List the most expensive product in each category.
WITH ranked_products AS (
    SELECT
        p.product_name,
        p.category_id,
        p.list_price,
        ROW_NUMBER() OVER (PARTITION BY p.category_id ORDER BY p.list_price DESC) AS rn
    FROM production.products AS p
)
SELECT
    c.category_name,
    r.product_name,
    r.list_price
FROM ranked_products AS r
INNER JOIN production.categories AS c
    ON r.category_id = c.category_id
WHERE r.rn = 1;


-- Task 32: Find staff members who work in the store that generated the most revenue.
WITH store_revenue AS (
    SELECT
        o.store_id,
        SUM(oi.quantity * oi.list_price * (1 - oi.discount)) AS total_revenue
    FROM sales.orders AS o
    INNER JOIN sales.order_items AS oi
        ON o.order_id = oi.order_id
    GROUP BY o.store_id
),
top_store AS (
    SELECT TOP (1) store_id
    FROM store_revenue
    ORDER BY total_revenue DESC
)
SELECT
    s.first_name + ' ' + s.last_name AS staff_full_name,
    s.store_id
FROM sales.staffs AS s
WHERE s.store_id = (SELECT store_id FROM top_store);


-- Task 33: Find orders where the total order value exceeds 5000.
SELECT
    order_id,
    order_total
FROM (
    SELECT
        oi.order_id,
        SUM(oi.quantity * oi.list_price * (1 - oi.discount)) AS order_total
    FROM sales.order_items AS oi
    GROUP BY oi.order_id
) AS order_totals
WHERE order_total > 5000
ORDER BY order_total DESC;


-- Task 34: List products that have never been ordered by any customer.
SELECT
    product_id,
    product_name
FROM production.products AS p
WHERE NOT EXISTS (
    SELECT 1
    FROM sales.order_items AS oi
    WHERE oi.product_id = p.product_id
);


-- Task 35: Find the customer who has spent the most money overall.
SELECT TOP (1)
    c.customer_id,
    c.first_name + ' ' + c.last_name AS customer_full_name,
    SUM(oi.quantity * oi.list_price * (1 - oi.discount)) AS total_spent
FROM sales.customers AS c
INNER JOIN sales.orders AS o
    ON c.customer_id = o.customer_id
INNER JOIN sales.order_items AS oi
    ON o.order_id = oi.order_id
GROUP BY c.customer_id, c.first_name, c.last_name
ORDER BY total_spent DESC;


/* =============================================================================
   SECTION 5 — Subqueries & APPLY (Tasks 5.1 - 5.7)
   ============================================================================= */

-- 5.1 - Products with list_price above average price in their brand (Correlated)
SELECT
    p.product_id,
    p.product_name,
    p.brand_id,
    p.list_price
FROM production.products AS p
WHERE p.list_price > (
    SELECT AVG(p2.list_price)
    FROM production.products AS p2
    WHERE p2.brand_id = p.brand_id
)
ORDER BY p.brand_id, p.list_price DESC;
GO


-- 5.2 - Orders placed by customers in NY or CA using IN
SELECT order_id, customer_id, order_date, store_id
FROM sales.orders
WHERE customer_id IN (
    SELECT customer_id FROM sales.customers WHERE state IN ('NY', 'CA')
)
ORDER BY order_id;
GO


-- 5.3 - Fix NULL trap in NOT IN
SELECT customer_id
FROM sales.customers
WHERE customer_id NOT IN (
    SELECT customer_id FROM sales.orders WHERE customer_id IS NOT NULL
);
GO


-- 5.4 - Average number of items per order across all orders (Derived table in FROM)
SELECT
    CAST(AVG(CAST(line_item_count AS FLOAT)) AS DECIMAL(6, 2)) AS avg_line_items_per_order,
    CAST(AVG(CAST(total_units AS FLOAT)) AS DECIMAL(6, 2)) AS avg_total_units_per_order
FROM (
    SELECT
        order_id,
        COUNT(item_id) AS line_item_count,
        SUM(quantity) AS total_units
    FROM sales.order_items
    GROUP BY order_id
) AS order_item_counts;
GO


-- 5.5 - Rewrite EXISTS as IN & Comparison
SELECT customer_id, first_name, last_name
FROM sales.customers
WHERE customer_id IN (SELECT customer_id FROM sales.orders);
-- EXISTS is safer because it operates on Boolean logic (True/False) without three-valued NULL pitfalls.
GO


-- 5.6 - Top 3 most recent orders per customer using CROSS APPLY
SELECT
    c.customer_id,
    c.first_name,
    o.order_id,
    o.order_date
FROM sales.customers AS c
CROSS APPLY (
    SELECT TOP (3) ord.order_id, ord.order_date
    FROM sales.orders AS ord
    WHERE ord.customer_id = c.customer_id
    ORDER BY ord.order_date DESC, ord.order_id DESC
) AS o
ORDER BY c.customer_id, o.order_date DESC;
GO


-- 5.7 - Think About It: ANY vs ALL vs IN
-- = ANY is identical to IN. Use ANY for inequalities (> ANY means greater than MIN).
-- Use ALL when a value must exceed EVERY row (> ALL means greater than MAX).
-- Example business question mapping naturally to ALL:
SELECT product_name, list_price
FROM production.products
WHERE list_price > ALL (
    SELECT p.list_price
    FROM production.products AS p
    INNER JOIN production.categories AS c ON p.category_id = c.category_id
    WHERE c.category_name = 'Mountain Bikes'
)
ORDER BY list_price ASC;
GO


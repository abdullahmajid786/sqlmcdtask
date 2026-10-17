USE BikeStores;
GO

/*
================================================================================
SECTION 5 — Subqueries & APPLY (Tasks 5.1 - 5.7)
Database: BikeStores
================================================================================
*/

-- =============================================================================
-- 5.1 - Products with list_price above average price in their brand (Correlated)
-- =============================================================================
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


-- =============================================================================
-- 5.2 - Orders placed by customers living in NY or CA using IN
-- =============================================================================
SELECT
    order_id,
    customer_id,
    order_date,
    store_id
FROM sales.orders
WHERE customer_id IN (
    SELECT customer_id
    FROM sales.customers
    WHERE state IN ('NY', 'CA')
)
ORDER BY order_id;
GO


-- =============================================================================
-- 5.3 - Fix NULL trap in NOT IN
-- Problem: If subquery returns any NULL, NOT IN evaluates to UNKNOWN and returns 0 rows.
-- Fix: Filter out NULLs (or use NOT EXISTS).
-- =============================================================================
SELECT customer_id
FROM sales.customers
WHERE customer_id NOT IN (
    SELECT customer_id
    FROM sales.orders
    WHERE customer_id IS NOT NULL
);
GO


-- =============================================================================
-- 5.4 - Average number of items per order across all orders (Derived table in FROM)
-- =============================================================================
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


-- =============================================================================
-- 5.5 - Rewrite EXISTS as IN & Comparison
-- =============================================================================
-- IN Version:
SELECT customer_id, first_name, last_name
FROM sales.customers
WHERE customer_id IN (
    SELECT customer_id
    FROM sales.orders
);

-- Which is safer & why:
-- EXISTS is safer because it operates on Boolean logic (True/False) and is completely
-- immune to NULL values. NOT IN breaks silently when subquery contains NULLs,
-- while NOT EXISTS handles NULLs predictably and optimizes efficiently.
GO


-- =============================================================================
-- 5.6 - Top 3 most recent orders per customer using CROSS APPLY
-- =============================================================================
SELECT
    c.customer_id,
    c.first_name,
    o.order_id,
    o.order_date
FROM sales.customers AS c
CROSS APPLY (
    SELECT TOP (3)
        ord.order_id,
        ord.order_date
    FROM sales.orders AS ord
    WHERE ord.customer_id = c.customer_id
    ORDER BY ord.order_date DESC, ord.order_id DESC
) AS o
ORDER BY c.customer_id, o.order_date DESC;
GO


-- =============================================================================
-- 5.7 - Think About It: ANY vs ALL vs IN
--
-- 1. When to choose ANY over IN:
--    = ANY is identical to IN, but ANY allows inequality comparisons (> ANY, < ANY).
--    Example: "> ANY" means "greater than at least one" (greater than the minimum).
--
-- 2. When to choose ALL:
--    Use ALL when a value must satisfy the comparison against EVERY row in the subquery.
--    Example: "> ALL" means "greater than all rows" (greater than the maximum).
--
-- 3. Business Question mapping naturally to ALL (cannot be expressed with IN):
--    "Find all products priced higher than EVERY Mountain Bike":
-- =============================================================================
SELECT
    product_name,
    list_price
FROM production.products
WHERE list_price > ALL (
    SELECT p.list_price
    FROM production.products AS p
    INNER JOIN production.categories AS c
        ON p.category_id = c.category_id
    WHERE c.category_name = 'Mountain Bikes'
)
ORDER BY list_price ASC;
GO

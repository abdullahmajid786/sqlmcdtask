USE BikeStores;
GO

/*
================================================================================
SECTION 6 — Common Table Expressions (CTEs)
Database: BikeStores
================================================================================
*/


-- =============================================================================
-- Task 6.1: Rewrite this derived table query as a CTE:
--
-- SELECT AVG(order_count) AS avg_orders
-- FROM (
--     SELECT store_id, COUNT(*) AS order_count
--     FROM sales.orders
--     GROUP BY store_id
-- ) AS store_counts;
-- =============================================================================
WITH StoreCounts AS (
    SELECT 
        store_id, 
        COUNT(*) AS order_count
    FROM sales.orders
    GROUP BY store_id
)
SELECT 
    AVG(CAST(order_count AS FLOAT)) AS avg_orders
FROM StoreCounts;
GO


-- =============================================================================
-- Task 6.2: Write a CTE called cte_high_value_products that returns products 
-- with list_price > 2000. Then query the CTE to return only Mountain Bikes 
-- from that list, joining to production.categories.
-- =============================================================================
WITH cte_high_value_products AS (
    SELECT
        product_id,
        product_name,
        brand_id,
        category_id,
        model_year,
        list_price
    FROM production.products
    WHERE list_price > 2000
)
SELECT
    hvp.product_id,
    hvp.product_name,
    c.category_id,
    c.category_name,
    hvp.list_price
FROM cte_high_value_products AS hvp
INNER JOIN production.categories AS c
    ON hvp.category_id = c.category_id
WHERE c.category_name = 'Mountain Bikes'
ORDER BY hvp.list_price DESC;
GO


-- =============================================================================
-- Task 6.3: Write two CTEs in one WITH clause: one that counts orders per 
-- customer, and one that sums revenue per customer. Join them in the outer query 
-- to return customer_id, order_count, and total_revenue side by side.
-- =============================================================================
WITH CustomerOrderCounts AS (
    SELECT
        customer_id,
        COUNT(order_id) AS order_count
    FROM sales.orders
    GROUP BY customer_id
),
CustomerRevenue AS (
    SELECT
        o.customer_id,
        SUM(oi.quantity * oi.list_price * (1.0 - oi.discount)) AS total_revenue
    FROM sales.orders AS o
    INNER JOIN sales.order_items AS oi
        ON o.order_id = oi.order_id
    GROUP BY o.customer_id
)
SELECT
    coc.customer_id,
    coc.order_count,
    CAST(cr.total_revenue AS DECIMAL(14, 2)) AS total_revenue
FROM CustomerOrderCounts AS coc
INNER JOIN CustomerRevenue AS cr
    ON coc.customer_id = cr.customer_id
ORDER BY total_revenue DESC;
GO


-- =============================================================================
-- Task 6.4: Using a recursive CTE, generate a list of numbers from 1 to 10. 
-- Each row should have the number and its square (n * n).
-- =============================================================================
WITH NumberSequence AS (
    -- Anchor member
    SELECT 
        1 AS n,
        1 * 1 AS square

    UNION ALL

    -- Recursive member
    SELECT 
        n + 1,
        (n + 1) * (n + 1)
    FROM NumberSequence
    WHERE n < 10
)
SELECT 
    n, 
    square
FROM NumberSequence;
GO


-- =============================================================================
-- Task 6.5: Using the recursive CTE org chart from section 9.6.2 as a starting 
-- point, modify it to also show the manager's first_name alongside each 
-- employee. Add a level column (0 for the top manager, 1 for their direct 
-- reports, 2 for the next level down).
-- =============================================================================
WITH StaffOrgChart AS (
    -- Anchor member: Top-level manager (manager_id IS NULL)
    SELECT
        staff_id,
        first_name,
        last_name,
        manager_id,
        CAST(NULL AS VARCHAR(50)) AS manager_first_name,
        0 AS level
    FROM sales.staffs
    WHERE manager_id IS NULL

    UNION ALL

    -- Recursive member: Subordinates joined to their managers
    SELECT
        e.staff_id,
        e.first_name,
        e.last_name,
        e.manager_id,
        CAST(m.first_name AS VARCHAR(50)) AS manager_first_name,
        m.level + 1 AS level
    FROM sales.staffs AS e
    INNER JOIN StaffOrgChart AS m
        ON e.manager_id = m.staff_id
)
SELECT
    staff_id,
    first_name + ' ' + last_name AS employee_name,
    manager_id,
    manager_first_name,
    level
FROM StaffOrgChart
ORDER BY level, staff_id;
GO


-- =============================================================================
-- Task 6.6: Think About It:
-- Question:
-- A CTE is defined once but referenced twice in the same outer query. 
-- A colleague says "CTEs are faster than subqueries because the database 
-- computes the result once and reuses it." Is this claim accurate? 
-- What would you need to do if you genuinely needed the result computed 
-- only once and reused?
--
-- Detailed Explanation:
-- 1. Is the colleague's claim accurate?
--    NO, the claim is inaccurate. In Microsoft SQL Server (and most relational 
--    database engines), a Common Table Expression (CTE) is non-materialized 
--    syntactic sugar. It acts as an inline view or temporary query definition, 
--    NOT a cached temporary table.
--
-- 2. Why does re-execution occur?
--    When a CTE is referenced multiple times in the same outer query (such as 
--    joining a CTE to itself), the SQL Server Query Optimizer substitutes and 
--    evaluates the CTE query definition separately for EACH reference. 
--    The database engine does NOT automatically cache or store intermediate 
--    results of the CTE between references.
--
-- 3. CTEs vs Subqueries:
--    CTEs and subqueries generate identical query execution plans. CTEs provide 
--    superior readability, code organization, and support for recursion, but they 
--    do not offer an inherent caching or performance advantage over subqueries.
--
-- 4. How to genuinely compute once and reuse:
--    If an expensive calculation needs to be evaluated once and reused multiple 
--    times across queries or multiple joins:
--
--    a) Use a Local Temporary Table (#temp):
--       SELECT ... INTO #PrecomputedCTE FROM ...;
--       CREATE CLUSTERED INDEX IX_Temp ON #PrecomputedCTE(...);
--       -- Query #PrecomputedCTE multiple times
--       Temporary tables are materialized physically in tempdb, generate statistics, 
--       and execute strictly once.
--
--    b) Use a Table Variable (@table):
--       For smaller data volumes, insert CTE results into a table variable.
--
--    c) Indexed Views (Materialized Views):
--       If the query result is frequently requested across multiple transactions, 
--       an indexed view physically stores the persisted aggregation on disk.
-- =============================================================================

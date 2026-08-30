
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

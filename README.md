# Python & SQL Practice Solutions

## 📌 Repository Overview
This repository contains complete, verified solutions for both the **Python Data Structures Practice Series (Parts 1 - 5 | Questions 1 - 50)** and the **SQL BikeStores Practice Tasks (Joins, GROUP BY, Subqueries, CTEs & Bonus Challenges)**.

---

## 🗄️ SQL Practice Questions (BikeStores Dataset)
**File**: [`SQL_Practice_BikeStores.sql`](file:///c:/python%20saylani%20project%201/SQL_Practice_BikeStores.sql)

### 📊 Tables Used:
`sales.orders`, `sales.order_items`, `sales.customers`, `sales.stores`, `sales.staffs`, `production.products`, `production.brands`, `production.categories`, `production.stocks`

### 💡 Summary of SQL Solutions:

#### 1. Joins
* **Q1 (Easy)**: Full details for orders with Customer Name, Store Name, and Staff Name (`INNER JOIN` across `orders`, `customers`, `stores`, `staffs`).
* **Q2 (Easy)**: All products with brand and category names, preserving unassigned products (`LEFT JOIN` with `brands` and `categories`).
* **Q3 (Medium)**: Customers with zero orders (`LEFT JOIN sales.orders` with `WHERE o.order_id IS NULL`).

#### 2. GROUP BY
* **Q4 (Easy)**: Total revenue per store sorted descending (`quantity * list_price * (1 - discount)` grouped by `store_id`, `store_name`).
* **Q5 (Medium)**: Brand analysis showing product count, average list price, and max price for brands with `> 5` products (`HAVING COUNT(p.product_id) > 5`).
* **Q6 (Medium)**: Monthly order count and total revenue for 2017 sorted chronologically (`WHERE YEAR(order_date) = 2017`).

#### 3. Subqueries
* **Q7 (Medium)**: Products priced above their own category average using a **correlated subquery** (`WHERE p.list_price > (SELECT AVG(...) WHERE p2.category_id = p.category_id)`).
* **Q8 (Medium)**: Customers placing more orders than the company-wide customer average using an aggregated subquery inside `HAVING`.

#### 4. CTEs (Common Table Expressions)
* **Q9 (Hard)**: Multi-CTE calculation of customer spend, top 10 ranked customers (`DENSE_RANK()`), and tier classification (`High` vs `Regular` based on overall average).
* **Q10 (Hard)**: Multi-CTE identifying the best-selling product by quantity in each category (`ROW_NUMBER() OVER (PARTITION BY category_id ORDER BY total_qty_sold DESC)`), joined with total stock across all stores.

#### 5. Section 5 — Subqueries & APPLY (`SQLQuery5_Subqueries.sql` & `SQLQuery5.sql`)
* **Task 5.1**: Correlated scalar subquery in `WHERE` finding products priced above their brand average.
* **Task 5.2**: `IN` predicate filtering orders placed by customers in NY or CA.
* **Task 5.3**: Resolving the classic `NOT IN` three-valued logic NULL trap (`WHERE customer_id IS NOT NULL`).
* **Task 5.4**: Derived table in `FROM` calculating average line items and total units per order.
* **Task 5.5**: Rewriting `EXISTS` into `IN`, detailing why `EXISTS` is safer against `NULL` semantics.
* **Task 5.6**: `CROSS APPLY` returning top 3 most recent orders per customer.
* **Task 5.7 (Think About It)**: Comparison of `ANY` vs `ALL` vs `IN`, demonstrating queries requiring `> ALL` that cannot be naturally expressed with `IN`.

#### 6. Section 6 — Common Table Expressions (`SQLQuery6_CTEs.sql` & `SQLQuery6.sql`)
* **Task 6.1**: Rewrite derived table query into a clean, reusable CTE for calculating average order count per store.
* **Task 6.2**: `cte_high_value_products` CTE filtering for products priced `> 2000`, joined with categories to isolate 'Mountain Bikes'.
* **Task 6.3**: Two CTEs in a single `WITH` clause combining per-customer order counts and per-customer revenue side by side.
* **Task 6.4**: Recursive CTE generating numbers 1 to 10 with their squares ($n \times n$).
* **Task 6.5**: Recursive CTE org chart navigating staff hierarchy (`manager_id`), displaying manager name and hierarchy level (0, 1, 2...).
* **Task 6.6 (Think About It)**: Comprehensive analysis of CTE execution vs. subqueries, debunking the myth of automatic CTE materialization, and detailing temp table (`#temp`) usage for guaranteed single-evaluation reuse.

#### 7. Section 7 — Window Functions & Window Framing (`SQLQuery7.sql`)
* **Task 7.1**: Sequential row numbering across all products (`ROW_NUMBER() OVER (ORDER BY list_price DESC)`) and partitioned by category (`ROW_NUMBER() OVER (PARTITION BY category_id ORDER BY list_price DESC)`).
* **Task 7.2**: Comparison of `RANK()` vs. `DENSE_RANK()` by price descending within category, showing products where ties cause ranks to diverge.
* **Task 7.3**: Month-over-month (MoM) revenue changes per store using `LAG()`, reporting current revenue, prior month revenue, and net difference.
* **Task 7.4**: Dividing product catalog into 5 price bands using `NTILE(5)`.
* **Task 7.5**: Order running revenue total ordered by `order_date` using frame `ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`.
* **Task 7.6 (Think About It)**: Architectural analysis of default window frame (`RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`), explaining why `FIRST_VALUE()` works out of the box while `LAST_VALUE()` requires `BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING`.

---

## 🐍 Python Data Structures Practice (Parts 1 - 5 | Questions 1 - 50)

### ⚠️ Strict Rules Followed Across All Python Solutions:
- ❌ **No `for` / `while` loops**
- ❌ **No comprehensions** (list, set, dict, generator)
- ❌ **No recursion**
- ❌ **No `map` / `filter` / `reduce`**
- ❌ **No lambda functions**
- ❌ **No hardcoded answers**
- ✅ **Strictly uses**: Indexing, slicing, operators, built-in functions, and data structure methods.

### 📁 Python Files & Test Suites:
- `python_lists_part1.py` & `test_python_lists.py` - Part 1: Lists (Q1 - Q10)
- `python_tuples_part2.py` & `test_python_tuples.py` - Part 2: Tuples (Q11 - Q20)
- `python_sets_part3.py` & `test_python_sets.py` - Part 3: Sets (Q21 - Q30)
- `python_dictionaries_part4.py` & `test_python_dictionaries.py` - Part 4: Dictionaries (Q31 - Q40)
- `python_mixed_part5.py` & `test_python_mixed.py` - Part 5: Mixed Data Structures (Q41 - Q50)

---

## 🚀 How to Run

### Run SQL Queries (SQL Server):
```bash
sqlcmd -S . -E -C -i "SQL_Practice_BikeStores.sql"
```

### Run Python Solutions:
```bash
python python_lists_part1.py
python python_tuples_part2.py
python python_sets_part3.py
python python_dictionaries_part4.py
python python_mixed_part5.py
```

### Run Complete Unit Test Suite (50 Tests):
```bash
python -m unittest discover -p "test_*.py"
```
Ran 50 tests in 0.002s (100% Passing)

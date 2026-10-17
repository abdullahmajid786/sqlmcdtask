# Python Data Structures Practice (Complete Parts 1 - 5 | Questions 1 - 50)

## 📌 Assignment Overview
This repository contains comprehensive solutions to the 5-part Python Data Structures practice series ranging from Beginner to Expert levels.

### ⚠️ Strict Rules Followed Across All Solutions:
- ❌ **No `for` / `while` loops**
- ❌ **No comprehensions** (list, set, dict, generator)
- ❌ **No recursion**
- ❌ **No `map` / `filter` / `reduce`**
- ❌ **No lambda functions**
- ❌ **No hardcoded answers**
- ✅ **Strictly uses**: Indexing, slicing, operators, built-in functions, and data structure methods.

---

## 📁 Repository Structure
- `python_lists_part1.py` - Part 1: Lists (Questions 1 - 10)
- `test_python_lists.py` - Unit tests for Questions 1 - 10
- `python_tuples_part2.py` - Part 2: Tuples (Questions 11 - 20)
- `test_python_tuples.py` - Unit tests for Questions 11 - 20
- `python_sets_part3.py` - Part 3: Sets (Questions 21 - 30)
- `test_python_sets.py` - Unit tests for Questions 21 - 30
- `python_dictionaries_part4.py` - Part 4: Dictionaries (Questions 31 - 40)
- `test_python_dictionaries.py` - Unit tests for Questions 31 - 40
- `python_mixed_part5.py` - Part 5: Mixed Data Structures (Questions 41 - 50)
- `test_python_mixed.py` - Unit tests for Questions 41 - 50

---

## 📋 Part 1: Lists (Questions 1 - 10)
* **Q1. Accessing List Elements**: First (`numbers[0]`), Middle (`numbers[len(numbers) // 2]`), Last (`numbers[-1]`).
* **Q2. List Slicing**: First five (`[:5]`), last four (`[-4:]`), every second reverse (`[::-2]`).
* **Q3. List Modification**: `fruits.index()`, `fruits.insert(2, ...)`, `fruits.remove(...)`.
* **Q4. Reverse Without `reverse()`**: Slicing `numbers[::-1]`.
* **Q5. Second Largest Unique Number**: `sorted(set(numbers))[-2]`.
* **Q6. Rotate a List (Right by `k`)**: `numbers[-(k % len(numbers)):] + numbers[:-(k % len(numbers))]`.
* **Q7. Remove Duplicates, Preserve Order**: `list(dict.fromkeys(numbers))`.
* **Q8. Flatten a Nested List**: `sum(data, [])`.
* **Q9. Extract Data from a Matrix**: Main diagonal, secondary diagonal, and middle column indexing with `sum()`.
* **Q10. List Transformation Challenge**: `sorted(set(data))[-3:] + sorted(set(data))[:2][::-1]`.

---

## 📋 Part 2: Tuples (Questions 11 - 20)
* **Q11. Tuple Indexing**: Second (`colors[1]`), Last (`colors[-1]`), Middle three (`colors[1:4]`).
* **Q12. Tuple Unpacking**: `name, age, designation, salary = employee`.
* **Q13. Tuple Concatenation**: `combined = tuple1 + tuple2`, `reversed = combined[::-1]`.
* **Q14. Count and Locate**: `numbers.count(20)` and `numbers.index(20)`.
* **Q15. Extended Tuple Unpacking**: `first, second, *remaining, last = data`.
* **Q16. Modify an Immutable Tuple**: Slicing replacement `numbers[:idx] + (300,) + numbers[idx+1:]`.
* **Q17. Nested Tuple Access**: `students[1][1][1]`, `sum(students[0][1])/len(...)`, `max(students[2][1])`.
* **Q18. Tuple Sorting (No Loops/Comprehensions/Lambda)**: `tuple(sorted(employees, key=operator.itemgetter(1), reverse=True))`.
* **Q19. Tuple Matrix**: Diagonal extraction, `math.prod(diagonal)`, row sums `(sum(r0), sum(r1), sum(r2))`.
* **Q20. Inventory Tuple Challenge**: Total inventory value sum of products, `max(records, key=itemgetter(1))`, reversed tuple of names.

---

## 📋 Part 3: Sets (Questions 21 - 30)
* **Q21. Unique Values**: `set(numbers)` and `len(set(numbers))`.
* **Q22. Set Operations**: Union (`a | b`), Intersection (`a & b`), Difference (`a - b`), Symmetric Difference (`a ^ b`).
* **Q23. Add and Remove**: `skills.update({"Snowflake", "Databricks"})`, `skills.discard("AWS")`.
* **Q24. Common Students**: Taking both (`python & sql`), exactly one course (`python ^ sql`).
* **Q25. Subset and Superset**: `required.issubset(candidate)`, `candidate.issuperset(required)`.
* **Q26. Missing Numbers**: `set(range(1, 11)) - numbers`.
* **Q27. Three-Set Analysis**: All three (`p & s & a`), exactly Python and SQL (`(p & s) - a`), at least two (`(p & s) | (s & a) | (p & a)`).
* **Q28. Transaction Analysis**: All days (`d1 & d2 & d3`), at least two (`(d1 & d2) | (d2 & d3) | (d1 & d3)`), exactly one (`(d1 | d2 | d3) - at_least_two`).
* **Q29. Access Control**: Missing permissions (`req - user`), extra (`user - req`), authorization (`req.issubset(user)`).
* **Q30. Customer Segmentation**: All three platforms (`w & m & s`), exactly two (`at_least_two - all_three`), exactly one (`all_customers - at_least_two`).

---

## 📋 Part 4: Dictionaries (Questions 31 - 40)
* **Q31. Dictionary Access**: `student["name"]`, `student["marks"]`, `student.get("city", "Karachi")`.
* **Q32. Update Dictionary**: 20% salary increase `employee["salary"] = int(employee["salary"] * 1.20)`, bonus `employee["bonus"] = 15000`, department change.
* **Q33. Dictionary Methods**: `keys()`, `values()`, `items()`, and `product.pop("stock")`.
* **Q34. Merge Dictionaries**: Dict merge operator `dict1 | dict2`.
* **Q35. Student Marks (No Loops/Lambda)**: `max(marks.values())`, `min(...)`, `sum(...)/len(...)`, and `max(marks, key=marks.get)`.
* **Q36. Nested Employee Records**: `employees["E102"]["salary"]`, 15% raise to Ali, total payroll sum.
* **Q37. Dictionary Inversion (No Loops/Comprehensions)**: `dict(zip(data.values(), data.keys()))`.
* **Q38. Order Calculation**: Subtotals dict, grand total with `sum()`, and 10% discount calculation.
* **Q39. Employee Performance**: Averages dict, top performer with `max(averages, key=averages.get)`, and highest SQL score with `max(...)`.
* **Q40. Inventory Management**: Total inventory value, most valuable product with `max(item_values, key=item_values.get)`, and stock decrement after sales.

---

## 📋 Part 5: Mixed Data Structures (Questions 41 - 50)
* **Q41. Student Performance System**: Student averages dict, top student via `max(..., key=averages.get)`, tuple of names, unique marks set.
* **Q42. Employee Skills**: Common skills (`&`), Ali-only skills (`-`), all team skills (`|`), requirements check (`issubset`).
* **Q43. Sales Data**: Product revenue dict, total revenue via `sum()`, top-revenue product, price set.
* **Q44. Customer Orders**: Spending per customer dict, top customer, tuple of totals in customer ID order.
* **Q45. Course Enrollment**: All 3 courses (`&`), exactly 2 courses, exactly 1 course, unique student count.
* **Q46. E-Commerce Transactions**: Multi-transaction revenue, Ali total spend, largest transaction ID, unique product names set.
* **Q47. Pipeline Monitoring**: Total records processed, failed pipelines tuple, largest pipeline, average records per run.
* **Q48. Banking Transactions**: Account final balances, highest balance account, total withdrawals (negative amounts), largest single deposit.
* **Q49. Product Recommendations**: Products purchased by at least two, Ali wishlist minus purchases, shared wishlist products, all products set.
* **Q50. Final Company Analysis**: 10 comprehensive metrics: payroll per department, company payroll, highest-paid employee, shared skills, engineering-only skills, remaining budgets, department with higher average salary, name-to-salary map, all unique skills, combined budget sufficiency check.

---

## 🚀 How to Run

### Run All Solution Scripts:
```bash
python python_lists_part1.py
python python_tuples_part2.py
python python_sets_part3.py
python python_dictionaries_part4.py
python python_mixed_part5.py
```

### Run All 50 Unit Tests:
```bash
python -m unittest discover -p "test_*.py"
```
Ran 50 tests in 0.002s (100% Passing)

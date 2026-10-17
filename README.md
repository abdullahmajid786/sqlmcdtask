# Python Data Structures Practice

## 📌 Assignment Overview
This repository contains solutions to the Python Data Structures practice series ranging from Beginner to Expert levels.

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

---

## 📋 Part 1: Lists (Questions 1 - 10)

### Level: Beginner
* **Q1. Accessing List Elements**: First (`numbers[0]`), Middle (`numbers[len(numbers) // 2]`), Last (`numbers[-1]`).
* **Q2. List Slicing**: First five (`[:5]`), last four (`[-4:]`), every second reverse (`[::-2]`).
* **Q3. List Modification**: `fruits.index()`, `fruits.insert(2, ...)`, `fruits.remove(...)`.

### Level: Intermediate
* **Q4. Reverse Without `reverse()`**: Slicing `numbers[::-1]`.
* **Q5. Second Largest Unique Number**: `sorted(set(numbers))[-2]`.
* **Q6. Rotate a List (Right by `k`)**: `numbers[-(k % len(numbers)):] + numbers[:-(k % len(numbers))]`.
* **Q7. Remove Duplicates, Preserve Order**: `list(dict.fromkeys(numbers))`.

### Level: Advanced
* **Q8. Flatten a Nested List**: `sum(data, [])`.
* **Q9. Extract Data from a Matrix**: Main diagonal, secondary diagonal, and middle column indexing with `sum()`.
* **Q10. List Transformation Challenge**: `sorted(set(data))[-3:] + sorted(set(data))[:2][::-1]`.

---

## 📋 Part 2: Tuples (Questions 11 - 20)

### Level: Beginner
* **Q11. Tuple Indexing**: Second (`colors[1]`), Last (`colors[-1]`), Middle three (`colors[1:4]`).
* **Q12. Tuple Unpacking**: `name, age, designation, salary = employee`.
* **Q13. Tuple Concatenation**: `combined = tuple1 + tuple2`, `reversed = combined[::-1]`.

### Level: Intermediate
* **Q14. Count and Locate**: `numbers.count(20)` and `numbers.index(20)`.
* **Q15. Extended Tuple Unpacking**: `first, second, *remaining, last = data`.
* **Q16. Modify an Immutable Tuple**: Slicing replacement `numbers[:idx] + (300,) + numbers[idx+1:]`.
* **Q17. Nested Tuple Access**: `students[1][1][1]`, `sum(students[0][1])/len(...)`, `max(students[2][1])`.

### Level: Advanced
* **Q18. Tuple Sorting (No Loops/Comprehensions/Lambda)**: `tuple(sorted(employees, key=operator.itemgetter(1), reverse=True))`.
* **Q19. Tuple Matrix**: Diagonal extraction, `math.prod(diagonal)`, row sums `(sum(r0), sum(r1), sum(r2))`.
* **Q20. Inventory Tuple Challenge**: Total inventory value sum of products, `max(records, key=itemgetter(1))`, reversed tuple of names.

---

## 📋 Part 3: Sets (Questions 21 - 30)

### Level: Beginner
* **Q21. Unique Values**: `set(numbers)` and `len(set(numbers))`.
* **Q22. Set Operations**: Union (`a | b`), Intersection (`a & b`), Difference (`a - b`), Symmetric Difference (`a ^ b`).
* **Q23. Add and Remove**: `skills.update({"Snowflake", "Databricks"})`, `skills.discard("AWS")`.

### Level: Intermediate
* **Q24. Common Students**: Taking both (`python & sql`), exactly one course (`python ^ sql`).
* **Q25. Subset and Superset**: `required.issubset(candidate)`, `candidate.issuperset(required)`.
* **Q26. Missing Numbers**: `set(range(1, 11)) - numbers`.
* **Q27. Three-Set Analysis**: All three (`p & s & a`), exactly Python and SQL (`(p & s) - a`), at least two (`(p & s) | (s & a) | (p & a)`).

### Level: Advanced
* **Q28. Transaction Analysis**: All days (`d1 & d2 & d3`), at least two (`(d1 & d2) | (d2 & d3) | (d1 & d3)`), exactly one (`(d1 | d2 | d3) - at_least_two`).
* **Q29. Access Control**: Missing permissions (`req - user`), extra (`user - req`), authorization (`req.issubset(user)`).
* **Q30. Customer Segmentation**: All three platforms (`w & m & s`), exactly two (`at_least_two - all_three`), exactly one (`all_customers - at_least_two`).

---

## 🚀 How to Run

### Run Solution Scripts:
```bash
python python_lists_part1.py
python python_tuples_part2.py
python python_sets_part3.py
```

### Run All Unit Tests:
```bash
python -m unittest discover -p "test_*.py"
```

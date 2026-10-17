# Python Data Structures | Lists (Part 1 of 5)

## 📌 Assignment Overview
This repository contains solutions to **Python Practice: Lists (Questions 1 - 10)** ranging from Beginner to Expert levels.

### ⚠️ Rules Followed:
- ❌ **No for/while loops**
- ❌ **No comprehensions** (list, set, dict, generator)
- ❌ **No recursion**
- ❌ **No map / filter / reduce**
- ❌ **No hardcoded answers**
- ✅ **Strictly uses**: Indexing, slicing, operators, built-in functions, and data structure methods.

---

## 📋 Solutions Summary

### Level: Beginner
* **Q1. Accessing List Elements**
  - First: `numbers[0]`
  - Middle: `numbers[len(numbers) // 2]`
  - Last: `numbers[-1]`
* **Q2. List Slicing**
  - First five: `numbers[:5]`
  - Last four: `numbers[-4:]`
  - Every second reversed: `numbers[::-2]`
* **Q3. List Modification**
  - Replace banana with orange: `fruits[fruits.index("banana")] = "orange"`
  - Add grapes at index 2: `fruits.insert(2, "grapes")`
  - Remove cherry: `fruits.remove("cherry")`

### Level: Intermediate
* **Q4. Reverse Without `reverse()`**
  - Reversed using slicing: `numbers[::-1]`
* **Q5. Second Largest Unique Number**
  - `sorted(set(numbers))[-2]` (Expected: `67`)
* **Q6. Rotate a List**
  - Right rotation by `k`: `numbers[-(k % len(numbers)):] + numbers[:-(k % len(numbers))]`
* **Q7. Remove Duplicates, Preserve Order**
  - `list(dict.fromkeys(numbers))`

### Level: Advanced
* **Q8. Flatten a Nested List**
  - `sum(data, [])` (List concatenation via built-in `sum`)
* **Q9. Extract Data from a Matrix**
  - Main diagonal: `[matrix[0][0], matrix[1][1], matrix[2][2]]`
  - Secondary diagonal: `[matrix[0][2], matrix[1][1], matrix[2][0]]`
  - Middle column: `[matrix[0][1], matrix[1][1], matrix[2][1]]`
  - Sums calculated via `sum()`
* **Q10. List Transformation Challenge**
  - 3 largest unique ascending: `sorted(set(data))[-3:]`
  - 2 smallest unique descending: `sorted(set(data))[:2][::-1]`
  - Combined: `sorted(set(data))[-3:] + sorted(set(data))[:2][::-1]` (Expected: `[25, 30, 35, 10, 5]`)

---

## 🚀 How to Run

Run the main solution file:
```bash
python python_lists_part1.py
```

Run the unit tests:
```bash
python test_python_lists.py
```

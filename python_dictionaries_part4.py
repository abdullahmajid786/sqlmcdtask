"""
Python Data Structures | Dictionaries | Questions 31-40
Part 4 of 5 | 10 questions | Beginner to Expert

RULES COMPLIANCE:
- No for/while loops
- No comprehensions (list, dict, set, generator)
- No recursion
- No map / filter / reduce
- No lambda (specifically in Q35)
- No hardcoded answers
- Using indexing, slicing, operators, built-in functions, and data structure methods only.
"""

def main():
    print("=" * 60)
    print("PYTHON PRACTICE: DICTIONARIES (PART 4 OF 5 - QUESTIONS 31 TO 40)")
    print("=" * 60)

    # ==========================================================================
    # LEVEL: BEGINNER
    # ==========================================================================

    # --------------------------------------------------------------------------
    # Q31. Dictionary Access
    # student = {"name": "Ali", "age": 22, "course": "Python", "marks": 85}
    # Extract name and marks; retrieve missing city with default Karachi.
    # --------------------------------------------------------------------------
    print("\n--- Q31: Dictionary Access ---")
    student = {"name": "Ali", "age": 22, "course": "Python", "marks": 85}
    name = student["name"]
    marks = student["marks"]
    city = student.get("city", "Karachi")

    print(f"Student dict: {student}")
    print(f"Name: {name}")
    print(f"Marks: {marks}")
    print(f"City (with default 'Karachi'): {city}")

    # --------------------------------------------------------------------------
    # Q32. Update Dictionary
    # employee = {"name": "Sara", "salary": 100000, "department": "IT"}
    # Raise salary by 20%, add bonus 15000, change department to Data Engineering.
    # --------------------------------------------------------------------------
    print("\n--- Q32: Update Dictionary ---")
    employee = {"name": "Sara", "salary": 100000, "department": "IT"}
    print(f"Initial employee: {employee}")

    # Raise salary by 20%
    employee["salary"] = int(employee["salary"] * 1.20)
    # Add bonus 15000
    employee["bonus"] = 15000
    # Change department to Data Engineering
    employee["department"] = "Data Engineering"

    print(f"Updated employee: {employee}")

    # --------------------------------------------------------------------------
    # Q33. Dictionary Methods
    # product = {"id": 101, "name": "Laptop", "price": 120000, "stock": 5}
    # Extract keys, values, items; remove stock and retain its value.
    # --------------------------------------------------------------------------
    print("\n--- Q33: Dictionary Methods ---")
    product = {"id": 101, "name": "Laptop", "price": 120000, "stock": 5}
    print(f"Initial product: {product}")

    # Extract keys, values, items
    extracted_keys = list(product.keys())
    extracted_values = list(product.values())
    extracted_items = list(product.items())

    # Remove stock and retain its value using pop()
    removed_stock_value = product.pop("stock")

    print(f"Keys: {extracted_keys}")
    print(f"Values: {extracted_values}")
    print(f"Items: {extracted_items}")
    print(f"Removed stock value: {removed_stock_value}")
    print(f"Product after pop('stock'): {product}")

    # ==========================================================================
    # LEVEL: INTERMEDIATE
    # ==========================================================================

    # --------------------------------------------------------------------------
    # Q34. Merge Dictionaries
    # dict1 = {"a": 10, "b": 20, "c": 30}
    # dict2 = {"b": 50, "d": 40}
    # Merge so dict2 overrides overlapping keys.
    # --------------------------------------------------------------------------
    print("\n--- Q34: Merge Dictionaries ---")
    dict1 = {"a": 10, "b": 20, "c": 30}
    dict2 = {"b": 50, "d": 40}

    # Using the dictionary union/merge operator '|' introduced in Python 3.9
    merged_dict = dict1 | dict2

    print(f"Dict 1: {dict1}")
    print(f"Dict 2: {dict2}")
    print(f"Merged dict (dict2 overriding dict1): {merged_dict}")

    # --------------------------------------------------------------------------
    # Q35. Student Marks
    # marks = {"Ali": 85, "Sara": 92, "Ahmed": 78, "Zain": 88}
    # Find highest, lowest, average, and top-scoring student without loops or lambda.
    # --------------------------------------------------------------------------
    print("\n--- Q35: Student Marks (No Loops or Lambda) ---")
    marks = {"Ali": 85, "Sara": 92, "Ahmed": 78, "Zain": 88}

    highest_score = max(marks.values())
    lowest_score = min(marks.values())
    average_score = sum(marks.values()) / len(marks)
    # Using built-in dict method marks.get directly as the key function
    top_scoring_student = max(marks, key=marks.get)

    print(f"Marks: {marks}")
    print(f"Highest score: {highest_score}")
    print(f"Lowest score: {lowest_score}")
    print(f"Average score: {average_score}")
    print(f"Top-scoring student: {top_scoring_student} ({marks[top_scoring_student]})")

    # --------------------------------------------------------------------------
    # Q36. Nested Employee Records
    # employees = {
    #  "E101": {"name": "Ali", "salary": 80000},
    #  "E102": {"name": "Sara", "salary": 120000},
    #  "E103": {"name": "Ahmed", "salary": 95000}
    # }
    # Extract Sara salary, increase Ali salary 15%, and calculate total payroll.
    # --------------------------------------------------------------------------
    print("\n--- Q36: Nested Employee Records ---")
    employees = {
        "E101": {"name": "Ali", "salary": 80000},
        "E102": {"name": "Sara", "salary": 120000},
        "E103": {"name": "Ahmed", "salary": 95000}
    }

    sara_salary = employees["E102"]["salary"]
    # Increase Ali's salary by 15%
    employees["E101"]["salary"] = int(employees["E101"]["salary"] * 1.15)
    # Total payroll sum
    total_payroll = (
        employees["E101"]["salary"] +
        employees["E102"]["salary"] +
        employees["E103"]["salary"]
    )

    print(f"Sara's salary: {sara_salary}")
    print(f"Ali's updated salary (+15%): {employees['E101']['salary']}")
    print(f"Total payroll: {total_payroll}")

    # --------------------------------------------------------------------------
    # Q37. Dictionary Inversion
    # data = {"Python": "Ali", "SQL": "Sara", "AWS": "Ahmed"}
    # Create inverse dictionary without loops or comprehensions.
    # --------------------------------------------------------------------------
    print("\n--- Q37: Dictionary Inversion (No Loops or Comprehensions) ---")
    data = {"Python": "Ali", "SQL": "Sara", "AWS": "Ahmed"}
    # Using zip(values, keys) and built-in dict() constructor
    inverted_dict = dict(zip(data.values(), data.keys()))

    print(f"Original dictionary: {data}")
    print(f"Inverted dictionary: {inverted_dict}")

    # ==========================================================================
    # LEVEL: ADVANCED
    # ==========================================================================

    # --------------------------------------------------------------------------
    # Q38. Order Calculation
    # order = {
    #  "laptop": {"price": 120000, "quantity": 2},
    #  "mouse": {"price": 1500, "quantity": 5},
    #  "keyboard": {"price": 3500, "quantity": 3}
    # }
    # Calculate subtotals, grand total, and amount after 10% discount.
    # --------------------------------------------------------------------------
    print("\n--- Q38: Order Calculation ---")
    order = {
        "laptop": {"price": 120000, "quantity": 2},
        "mouse": {"price": 1500, "quantity": 5},
        "keyboard": {"price": 3500, "quantity": 3}
    }

    subtotals = {
        "laptop": order["laptop"]["price"] * order["laptop"]["quantity"],
        "mouse": order["mouse"]["price"] * order["mouse"]["quantity"],
        "keyboard": order["keyboard"]["price"] * order["keyboard"]["quantity"]
    }
    grand_total = sum(subtotals.values())
    discounted_amount = grand_total * 0.90  # 10% discount

    print(f"Order: {order}")
    print(f"Subtotals: {subtotals}")
    print(f"Grand total: {grand_total}")
    print(f"Amount after 10% discount: {discounted_amount}")

    # --------------------------------------------------------------------------
    # Q39. Employee Performance
    # employees = {
    #  "Ali": {"python": 90, "sql": 85, "aws": 88},
    #  "Sara": {"python": 95, "sql": 92, "aws": 90},
    #  "Ahmed": {"python": 80, "sql": 87, "aws": 84}
    # }
    # Calculate each average, top performer, and highest SQL score.
    # --------------------------------------------------------------------------
    print("\n--- Q39: Employee Performance ---")
    employees_perf = {
        "Ali": {"python": 90, "sql": 85, "aws": 88},
        "Sara": {"python": 95, "sql": 92, "aws": 90},
        "Ahmed": {"python": 80, "sql": 87, "aws": 84}
    }

    averages = {
        "Ali": sum(employees_perf["Ali"].values()) / len(employees_perf["Ali"]),
        "Sara": sum(employees_perf["Sara"].values()) / len(employees_perf["Sara"]),
        "Ahmed": sum(employees_perf["Ahmed"].values()) / len(employees_perf["Ahmed"])
    }
    top_performer = max(averages, key=averages.get)
    highest_sql_score = max(
        employees_perf["Ali"]["sql"],
        employees_perf["Sara"]["sql"],
        employees_perf["Ahmed"]["sql"]
    )

    print(f"Performance data: {employees_perf}")
    print(f"Averages: {averages}")
    print(f"Top performer: {top_performer} (Average: {averages[top_performer]:.2f})")
    print(f"Highest SQL score: {highest_sql_score}")

    # --------------------------------------------------------------------------
    # Q40. Inventory Management
    # inventory = {
    #  "P101": {"name": "Laptop", "price": 120000, "stock": 5},
    #  "P102": {"name": "Mouse", "price": 1500, "stock": 20},
    #  "P103": {"name": "Keyboard", "price": 3500, "stock": 10}
    # }
    # Calculate total value, most valuable item by price x stock, and update stock after selling two laptops and five mice.
    # --------------------------------------------------------------------------
    print("\n--- Q40: Inventory Management ---")
    inventory = {
        "P101": {"name": "Laptop", "price": 120000, "stock": 5},
        "P102": {"name": "Mouse", "price": 1500, "stock": 20},
        "P103": {"name": "Keyboard", "price": 3500, "stock": 10}
    }
    print(f"Initial inventory: {inventory}")

    item_values = {
        "P101": inventory["P101"]["price"] * inventory["P101"]["stock"],
        "P102": inventory["P102"]["price"] * inventory["P102"]["stock"],
        "P103": inventory["P103"]["price"] * inventory["P103"]["stock"]
    }
    total_inventory_value = sum(item_values.values())
    most_valuable_key = max(item_values, key=item_values.get)
    most_valuable_item_name = inventory[most_valuable_key]["name"]
    most_valuable_item_val = item_values[most_valuable_key]

    # Update stock after selling two laptops (P101) and five mice (P102)
    inventory["P101"]["stock"] -= 2
    inventory["P102"]["stock"] -= 5

    print(f"Total inventory value: {total_inventory_value}")
    print(f"Most valuable item (price x stock): {most_valuable_item_name} ({most_valuable_key}) with value {most_valuable_item_val}")
    print(f"Updated inventory after sales: {inventory}")
    print("=" * 60)

if __name__ == "__main__":
    main()

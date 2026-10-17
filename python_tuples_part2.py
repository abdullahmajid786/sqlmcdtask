"""
Python Data Structures | Tuples | Questions 11-20
Part 2 of 5 | 10 questions | Beginner to Expert

RULES COMPLIANCE:
- No for/while loops
- No comprehensions (list, dict, set, generator)
- No recursion
- No map / filter / reduce
- No lambda (specifically in Q18)
- No hardcoded answers
- Using indexing, slicing, operators, built-in functions, and data structure methods only.
"""

from operator import itemgetter
import math

def main():
    print("=" * 60)
    print("PYTHON PRACTICE: TUPLES (PART 2 OF 5 - QUESTIONS 11 TO 20)")
    print("=" * 60)

    # ==========================================================================
    # LEVEL: BEGINNER
    # ==========================================================================

    # --------------------------------------------------------------------------
    # Q11. Tuple Indexing
    # colors = ("red", "green", "blue", "yellow", "purple")
    # Extract second, last, and middle three elements.
    # --------------------------------------------------------------------------
    print("\n--- Q11: Tuple Indexing ---")
    colors = ("red", "green", "blue", "yellow", "purple")
    second_element = colors[1]
    last_element = colors[-1]
    middle_three = colors[1:4]

    print(f"Colors tuple: {colors}")
    print(f"Second element: {second_element}")
    print(f"Last element: {last_element}")
    print(f"Middle three elements: {middle_three}")

    # --------------------------------------------------------------------------
    # Q12. Tuple Unpacking
    # employee = ("Ali", 28, "Data Engineer", 150000)
    # Unpack into four variables and display name and salary.
    # --------------------------------------------------------------------------
    print("\n--- Q12: Tuple Unpacking ---")
    employee = ("Ali", 28, "Data Engineer", 150000)
    name, age, designation, salary = employee

    print(f"Employee tuple: {employee}")
    print(f"Name: {name}")
    print(f"Salary: {salary}")

    # --------------------------------------------------------------------------
    # Q13. Tuple Concatenation
    # tuple1 = (10, 20, 30)
    # tuple2 = (40, 50, 60)
    # Combine tuples, then create another tuple in reverse order.
    # --------------------------------------------------------------------------
    print("\n--- Q13: Tuple Concatenation ---")
    tuple1 = (10, 20, 30)
    tuple2 = (40, 50, 60)
    combined_tuple = tuple1 + tuple2
    reversed_tuple = combined_tuple[::-1]

    print(f"Tuple 1: {tuple1}")
    print(f"Tuple 2: {tuple2}")
    print(f"Combined tuple: {combined_tuple}")
    print(f"Reversed tuple: {reversed_tuple}")

    # ==========================================================================
    # LEVEL: INTERMEDIATE
    # ==========================================================================

    # --------------------------------------------------------------------------
    # Q14. Count and Locate
    # numbers = (10, 20, 30, 20, 40, 20, 50)
    # Count occurrences of 20 and find the first index.
    # --------------------------------------------------------------------------
    print("\n--- Q14: Count and Locate ---")
    numbers_q14 = (10, 20, 30, 20, 40, 20, 50)
    count_20 = numbers_q14.count(20)
    first_index_20 = numbers_q14.index(20)

    print(f"Tuple: {numbers_q14}")
    print(f"Occurrences of 20: {count_20}")
    print(f"First index of 20: {first_index_20}")

    # --------------------------------------------------------------------------
    # Q15. Extended Tuple Unpacking
    # data = (100, 200, 300, 400, 500, 600)
    # Unpack first two and last into variables; put all remaining elements into a list.
    # --------------------------------------------------------------------------
    print("\n--- Q15: Extended Tuple Unpacking ---")
    data_q15 = (100, 200, 300, 400, 500, 600)
    first_val, second_val, *remaining_list, last_val = data_q15

    print(f"Original tuple: {data_q15}")
    print(f"First variable: {first_val}")
    print(f"Second variable: {second_val}")
    print(f"Remaining elements (as list): {remaining_list}")
    print(f"Last variable: {last_val}")

    # --------------------------------------------------------------------------
    # Q16. Modify an Immutable Tuple
    # numbers = (10, 20, 30, 40, 50)
    # Create a new tuple replacing 30 with 300.
    # --------------------------------------------------------------------------
    print("\n--- Q16: Modify an Immutable Tuple ---")
    numbers_q16 = (10, 20, 30, 40, 50)
    target_idx = numbers_q16.index(30)
    modified_tuple = numbers_q16[:target_idx] + (300,) + numbers_q16[target_idx + 1:]

    print(f"Original tuple: {numbers_q16}")
    print(f"Modified tuple (30 replaced with 300): {modified_tuple}")

    # --------------------------------------------------------------------------
    # Q17. Nested Tuple Access
    # students = (
    #  ("Ali", (85, 90, 88)),
    #  ("Sara", (92, 87, 95)),
    #  ("Ahmed", (78, 84, 80))
    # )
    # Extract Sara second score, Ali average, and Ahmed highest score.
    # --------------------------------------------------------------------------
    print("\n--- Q17: Nested Tuple Access ---")
    students = (
        ("Ali", (85, 90, 88)),
        ("Sara", (92, 87, 95)),
        ("Ahmed", (78, 84, 80))
    )

    sara_second_score = students[1][1][1]
    ali_average_score = sum(students[0][1]) / len(students[0][1])
    ahmed_highest_score = max(students[2][1])

    print(f"Students data: {students}")
    print(f"Sara's second score: {sara_second_score}")
    print(f"Ali's average score: {ali_average_score:.2f}")
    print(f"Ahmed's highest score: {ahmed_highest_score}")

    # ==========================================================================
    # LEVEL: ADVANCED
    # ==========================================================================

    # --------------------------------------------------------------------------
    # Q18. Tuple Sorting
    # employees = (
    #  ("Ali", 80000),
    #  ("Sara", 120000),
    #  ("Ahmed", 95000)
    # )
    # Sort by salary descending without loops, comprehensions, or lambda.
    # --------------------------------------------------------------------------
    print("\n--- Q18: Tuple Sorting (Without Loops, Comprehensions, or Lambda) ---")
    employees = (
        ("Ali", 80000),
        ("Sara", 120000),
        ("Ahmed", 95000)
    )
    # Using operator.itemgetter(1) to avoid lambda/loops/comprehensions
    sorted_employees = tuple(sorted(employees, key=itemgetter(1), reverse=True))

    print(f"Original employees: {employees}")
    print(f"Sorted by salary (descending): {sorted_employees}")

    # --------------------------------------------------------------------------
    # Q19. Tuple Matrix
    # matrix = ((2, 4, 6), (8, 10, 12), (14, 16, 18))
    # Extract diagonal, calculate its product, and build a tuple of row sums.
    # --------------------------------------------------------------------------
    print("\n--- Q19: Tuple Matrix ---")
    matrix = (
        (2, 4, 6),
        (8, 10, 12),
        (14, 16, 18)
    )

    diagonal = (matrix[0][0], matrix[1][1], matrix[2][2])
    diagonal_product = math.prod(diagonal)
    row_sums = (sum(matrix[0]), sum(matrix[1]), sum(matrix[2]))

    print(f"Matrix:\n  {matrix[0]}\n  {matrix[1]}\n  {matrix[2]}")
    print(f"Diagonal: {diagonal}")
    print(f"Diagonal product: {diagonal_product}")
    print(f"Row sums: {row_sums}")

    # --------------------------------------------------------------------------
    # Q20. Inventory Tuple Challenge
    # records = (
    #  ("Laptop", 120000, 5),
    #  ("Mouse", 1500, 20),
    #  ("Keyboard", 3500, 10)
    # )
    # Calculate inventory value, find most expensive product, and build reversed tuple of names.
    # --------------------------------------------------------------------------
    print("\n--- Q20: Inventory Tuple Challenge ---")
    records = (
        ("Laptop", 120000, 5),
        ("Mouse", 1500, 20),
        ("Keyboard", 3500, 10)
    )

    # Total inventory value: sum of (price * quantity) for all items
    total_inventory_value = (
        records[0][1] * records[0][2] +
        records[1][1] * records[1][2] +
        records[2][1] * records[2][2]
    )

    # Most expensive product (by unit price at index 1)
    most_expensive_record = max(records, key=itemgetter(1))
    most_expensive_product_name = most_expensive_record[0]

    # Reversed tuple of product names
    reversed_names = (records[0][0], records[1][0], records[2][0])[::-1]

    print(f"Records: {records}")
    print(f"Total inventory value: {total_inventory_value}")
    print(f"Most expensive product: {most_expensive_product_name} ({most_expensive_record[1]})")
    print(f"Reversed tuple of names: {reversed_names}")
    print("=" * 60)

if __name__ == "__main__":
    main()

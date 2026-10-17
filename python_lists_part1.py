"""
Python Data Structures | Lists | Questions 1-10
Part 1 of 5 | 10 questions | Beginner to Expert

RULES COMPLIANCE:
- No for/while loops
- No comprehensions (list, dict, set, generator)
- No recursion
- No map / filter / reduce
- No hardcoded answers
- Using indexing, slicing, operators, built-in functions, and data structure methods only.
"""

def main():
    print("=" * 60)
    print("PYTHON PRACTICE: LISTS (PART 1 OF 5 - QUESTIONS 1 TO 10)")
    print("=" * 60)

    # ==========================================================================
    # LEVEL: BEGINNER
    # ==========================================================================

    # --------------------------------------------------------------------------
    # Q1. Accessing List Elements
    # numbers = [10, 20, 30, 40, 50, 60, 70]
    # Extract the first, middle, and last elements without modifying the original list.
    # --------------------------------------------------------------------------
    print("\n--- Q1: Accessing List Elements ---")
    numbers_q1 = [10, 20, 30, 40, 50, 60, 70]
    first_element = numbers_q1[0]
    middle_element = numbers_q1[len(numbers_q1) // 2]
    last_element = numbers_q1[-1]

    print(f"Original list: {numbers_q1}")
    print(f"First element: {first_element}")
    print(f"Middle element: {middle_element}")
    print(f"Last element: {last_element}")

    # --------------------------------------------------------------------------
    # Q2. List Slicing
    # numbers = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    # Create three new lists: first five elements, last four elements, and every second element in reverse order.
    # --------------------------------------------------------------------------
    print("\n--- Q2: List Slicing ---")
    numbers_q2 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    first_five = numbers_q2[:5]
    last_four = numbers_q2[-4:]
    every_second_reversed = numbers_q2[::-2]

    print(f"Original list: {numbers_q2}")
    print(f"First five elements: {first_five}")
    print(f"Last four elements: {last_four}")
    print(f"Every second element in reverse order: {every_second_reversed}")

    # --------------------------------------------------------------------------
    # Q3. List Modification
    # fruits = ["apple", "banana", "cherry", "mango"]
    # Replace banana with orange, add grapes at index 2, and remove cherry.
    # --------------------------------------------------------------------------
    print("\n--- Q3: List Modification ---")
    fruits = ["apple", "banana", "cherry", "mango"]
    print(f"Initial list: {fruits}")

    # Replace banana with orange using index() and item assignment
    fruits[fruits.index("banana")] = "orange"
    # Add grapes at index 2 using insert()
    fruits.insert(2, "grapes")
    # Remove cherry using remove()
    fruits.remove("cherry")

    print(f"Modified list: {fruits}")

    # ==========================================================================
    # LEVEL: INTERMEDIATE
    # ==========================================================================

    # --------------------------------------------------------------------------
    # Q4. Reverse Without reverse()
    # numbers = [12, 45, 23, 67, 89, 34]
    # Reverse using slicing only; preserve the original list.
    # --------------------------------------------------------------------------
    print("\n--- Q4: Reverse Without reverse() ---")
    numbers_q4 = [12, 45, 23, 67, 89, 34]
    reversed_numbers = numbers_q4[::-1]

    print(f"Original list (preserved): {numbers_q4}")
    print(f"Reversed list (via slicing): {reversed_numbers}")

    # --------------------------------------------------------------------------
    # Q5. Second Largest Unique Number
    # numbers = [45, 12, 89, 34, 89, 67, 45, 23]
    # Find the second-largest unique number. Expected: 67.
    # --------------------------------------------------------------------------
    print("\n--- Q5: Second Largest Unique Number ---")
    numbers_q5 = [45, 12, 89, 34, 89, 67, 45, 23]
    # set() removes duplicates, sorted() orders elements, [-2] selects 2nd largest
    second_largest = sorted(set(numbers_q5))[-2]

    print(f"Original list: {numbers_q5}")
    print(f"Unique sorted: {sorted(set(numbers_q5))}")
    print(f"Second largest unique number: {second_largest} (Expected: 67)")

    # --------------------------------------------------------------------------
    # Q6. Rotate a List
    # numbers = [10, 20, 30, 40, 50, 60]
    # k = 2
    # Rotate the list right by k using slicing. Expected: [50, 60, 10, 20, 30, 40].
    # --------------------------------------------------------------------------
    print("\n--- Q6: Rotate a List ---")
    numbers_q6 = [10, 20, 30, 40, 50, 60]
    k = 2
    effective_k = k % len(numbers_q6)
    rotated_list = numbers_q6[-effective_k:] + numbers_q6[:-effective_k]

    print(f"Original list: {numbers_q6}, k={k}")
    print(f"Rotated list: {rotated_list} (Expected: [50, 60, 10, 20, 30, 40])")

    # --------------------------------------------------------------------------
    # Q7. Remove Duplicates, Preserve Order
    # numbers = [10, 20, 10, 30, 20, 40, 30, 50]
    # Remove duplicates while preserving first-occurrence order.
    # --------------------------------------------------------------------------
    print("\n--- Q7: Remove Duplicates, Preserve Order ---")
    numbers_q7 = [10, 20, 10, 30, 20, 40, 30, 50]
    # dict.fromkeys() preserves insertion order of first occurrences in Python 3.7+
    unique_ordered = list(dict.fromkeys(numbers_q7))

    print(f"Original list: {numbers_q7}")
    print(f"Unique list (order preserved): {unique_ordered}")

    # ==========================================================================
    # LEVEL: ADVANCED
    # ==========================================================================

    # --------------------------------------------------------------------------
    # Q8. Flatten a Nested List
    # data = [[10, 20], [30, 40], [50, 60]]
    # Flatten into [10, 20, 30, 40, 50, 60] using list operations.
    # --------------------------------------------------------------------------
    print("\n--- Q8: Flatten a Nested List ---")
    data_q8 = [[10, 20], [30, 40], [50, 60]]
    # sum(list_of_lists, []) concatenates nested sublists using built-in sum and list '+'
    flattened_list = sum(data_q8, [])

    print(f"Nested list: {data_q8}")
    print(f"Flattened list: {flattened_list} (Expected: [10, 20, 30, 40, 50, 60])")

    # --------------------------------------------------------------------------
    # Q9. Extract Data from a Matrix
    # matrix = [
    #  [10, 20, 30],
    #  [40, 50, 60],
    #  [70, 80, 90]
    # ]
    # Extract main diagonal, secondary diagonal, and middle column; calculate the sum of each.
    # --------------------------------------------------------------------------
    print("\n--- Q9: Extract Data from a Matrix ---")
    matrix = [
        [10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]
    ]

    main_diagonal = [matrix[0][0], matrix[1][1], matrix[2][2]]
    sum_main = sum(main_diagonal)

    secondary_diagonal = [matrix[0][2], matrix[1][1], matrix[2][0]]
    sum_secondary = sum(secondary_diagonal)

    middle_column = [matrix[0][1], matrix[1][1], matrix[2][1]]
    sum_middle = sum(middle_column)

    print(f"Matrix:\n  {matrix[0]}\n  {matrix[1]}\n  {matrix[2]}")
    print(f"Main diagonal: {main_diagonal}, Sum: {sum_main}")
    print(f"Secondary diagonal: {secondary_diagonal}, Sum: {sum_secondary}")
    print(f"Middle column: {middle_column}, Sum: {sum_middle}")

    # --------------------------------------------------------------------------
    # Q10. List Transformation Challenge
    # data = [15, 5, 25, 10, 35, 20, 30]
    # Build a list of the three largest unique values ascending, then two smallest unique values descending. Expected: [25, 30, 35, 10, 5].
    # --------------------------------------------------------------------------
    print("\n--- Q10: List Transformation Challenge ---")
    data_q10 = [15, 5, 25, 10, 35, 20, 30]
    unique_sorted = sorted(set(data_q10))
    three_largest_asc = unique_sorted[-3:]
    two_smallest_desc = unique_sorted[:2][::-1]
    transformed_list = three_largest_asc + two_smallest_desc

    print(f"Original data: {data_q10}")
    print(f"Unique sorted: {unique_sorted}")
    print(f"Three largest unique (ascending): {three_largest_asc}")
    print(f"Two smallest unique (descending): {two_smallest_desc}")
    print(f"Transformed list: {transformed_list} (Expected: [25, 30, 35, 10, 5])")
    print("=" * 60)

if __name__ == "__main__":
    main()

"""
Python Data Structures | Sets | Questions 21-30
Part 3 of 5 | 10 questions | Beginner to Expert

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
    print("PYTHON PRACTICE: SETS (PART 3 OF 5 - QUESTIONS 21 TO 30)")
    print("=" * 60)

    # ==========================================================================
    # LEVEL: BEGINNER
    # ==========================================================================

    # --------------------------------------------------------------------------
    # Q21. Unique Values
    # numbers = [10, 20, 10, 30, 40, 20, 50]
    # Convert to a set and count unique elements.
    # --------------------------------------------------------------------------
    print("\n--- Q21: Unique Values ---")
    numbers_q21 = [10, 20, 10, 30, 40, 20, 50]
    unique_numbers_set = set(numbers_q21)
    unique_count = len(unique_numbers_set)

    print(f"Original list: {numbers_q21}")
    print(f"Unique set: {unique_numbers_set}")
    print(f"Count of unique elements: {unique_count}")

    # --------------------------------------------------------------------------
    # Q22. Set Operations
    # a = {1, 2, 3, 4, 5}
    # b = {4, 5, 6, 7, 8}
    # Find union, intersection, a - b, and symmetric difference.
    # --------------------------------------------------------------------------
    print("\n--- Q22: Set Operations ---")
    a = {1, 2, 3, 4, 5}
    b = {4, 5, 6, 7, 8}

    union_set = a | b
    intersection_set = a & b
    diff_a_b = a - b
    sym_diff = a ^ b

    print(f"Set a: {a}")
    print(f"Set b: {b}")
    print(f"Union (a | b): {union_set}")
    print(f"Intersection (a & b): {intersection_set}")
    print(f"Difference (a - b): {diff_a_b}")
    print(f"Symmetric Difference (a ^ b): {sym_diff}")

    # --------------------------------------------------------------------------
    # Q23. Add and Remove
    # skills = {"Python", "SQL", "AWS"}
    # Add Snowflake and Databricks; safely remove AWS.
    # --------------------------------------------------------------------------
    print("\n--- Q23: Add and Remove ---")
    skills = {"Python", "SQL", "AWS"}
    print(f"Initial skills: {skills}")

    # Add Snowflake and Databricks using update() or individual add()
    skills.update({"Snowflake", "Databricks"})
    # Safely remove AWS using discard() which never raises KeyError if absent
    skills.discard("AWS")

    print(f"Updated skills: {skills}")

    # ==========================================================================
    # LEVEL: INTERMEDIATE
    # ==========================================================================

    # --------------------------------------------------------------------------
    # Q24. Common Students
    # python_students = {"Ali", "Sara", "Ahmed", "Zain"}
    # sql_students = {"Sara", "Ahmed", "Hamza", "Usman"}
    # Find students taking both and exactly one course.
    # --------------------------------------------------------------------------
    print("\n--- Q24: Common Students ---")
    python_students = {"Ali", "Sara", "Ahmed", "Zain"}
    sql_students = {"Sara", "Ahmed", "Hamza", "Usman"}

    taking_both = python_students & sql_students
    exactly_one_course = python_students ^ sql_students

    print(f"Python students: {python_students}")
    print(f"SQL students: {sql_students}")
    print(f"Students taking both courses: {taking_both}")
    print(f"Students taking exactly one course: {exactly_one_course}")

    # --------------------------------------------------------------------------
    # Q25. Subset and Superset
    # required_skills = {"Python", "SQL"}
    # candidate_skills = {"Python", "SQL", "AWS", "Snowflake"}
    # Check required skills are a subset and candidate skills a superset.
    # --------------------------------------------------------------------------
    print("\n--- Q25: Subset and Superset ---")
    required_skills = {"Python", "SQL"}
    candidate_skills = {"Python", "SQL", "AWS", "Snowflake"}

    is_subset = required_skills.issubset(candidate_skills)
    is_superset = candidate_skills.issuperset(required_skills)

    print(f"Required skills: {required_skills}")
    print(f"Candidate skills: {candidate_skills}")
    print(f"Are required skills a subset of candidate skills? {is_subset}")
    print(f"Are candidate skills a superset of required skills? {is_superset}")

    # --------------------------------------------------------------------------
    # Q26. Missing Numbers
    # numbers = {1, 2, 4, 6, 8, 10}
    # Find missing integers from 1 through 10 using set operations.
    # --------------------------------------------------------------------------
    print("\n--- Q26: Missing Numbers ---")
    numbers_q26 = {1, 2, 4, 6, 8, 10}
    full_range_set = set(range(1, 11))
    missing_numbers = full_range_set - numbers_q26

    print(f"Given numbers: {numbers_q26}")
    print(f"Expected range: {full_range_set}")
    print(f"Missing numbers (1 through 10): {missing_numbers}")

    # --------------------------------------------------------------------------
    # Q27. Three-Set Analysis
    # python = {"Ali", "Sara", "Ahmed", "Zain"}
    # sql = {"Sara", "Ahmed", "Hamza"}
    # aws = {"Ahmed", "Zain", "Hamza"}
    # Find students in all three, exactly Python and SQL (not AWS), and at least two.
    # --------------------------------------------------------------------------
    print("\n--- Q27: Three-Set Analysis ---")
    python = {"Ali", "Sara", "Ahmed", "Zain"}
    sql = {"Sara", "Ahmed", "Hamza"}
    aws = {"Ahmed", "Zain", "Hamza"}

    all_three_courses = python & sql & aws
    exactly_python_and_sql = (python & sql) - aws
    at_least_two_courses = (python & sql) | (sql & aws) | (python & aws)

    print(f"Python: {python}")
    print(f"SQL: {sql}")
    print(f"AWS: {aws}")
    print(f"Students in all three courses: {all_three_courses}")
    print(f"Students in exactly Python and SQL (not AWS): {exactly_python_and_sql}")
    print(f"Students in at least two courses: {at_least_two_courses}")

    # ==========================================================================
    # LEVEL: ADVANCED
    # ==========================================================================

    # --------------------------------------------------------------------------
    # Q28. Transaction Analysis
    # day1 = {101, 102, 103, 104}
    # day2 = {103, 104, 105, 106}
    # day3 = {104, 106, 107, 108}
    # Find IDs appearing on all days, exactly one day, and at least two days.
    # --------------------------------------------------------------------------
    print("\n--- Q28: Transaction Analysis ---")
    day1 = {101, 102, 103, 104}
    day2 = {103, 104, 105, 106}
    day3 = {104, 106, 107, 108}

    all_three_days = day1 & day2 & day3
    at_least_two_days = (day1 & day2) | (day2 & day3) | (day1 & day3)
    total_unique_transactions = day1 | day2 | day3
    exactly_one_day = total_unique_transactions - at_least_two_days

    print(f"Day 1: {day1}")
    print(f"Day 2: {day2}")
    print(f"Day 3: {day3}")
    print(f"IDs on all days: {all_three_days}")
    print(f"IDs on at least two days: {at_least_two_days}")
    print(f"IDs on exactly one day: {exactly_one_day}")

    # --------------------------------------------------------------------------
    # Q29. Access Control
    # required_permissions = {"read", "write", "execute"}
    # user_permissions = {"read", "write", "delete"}
    # Find missing and extra permissions and test full authorization.
    # --------------------------------------------------------------------------
    print("\n--- Q29: Access Control ---")
    required_permissions = {"read", "write", "execute"}
    user_permissions = {"read", "write", "delete"}

    missing_permissions = required_permissions - user_permissions
    extra_permissions = user_permissions - required_permissions
    is_fully_authorized = required_permissions.issubset(user_permissions)

    print(f"Required permissions: {required_permissions}")
    print(f"User permissions: {user_permissions}")
    print(f"Missing permissions: {missing_permissions}")
    print(f"Extra permissions: {extra_permissions}")
    print(f"Is user fully authorized? {is_fully_authorized}")

    # --------------------------------------------------------------------------
    # Q30. Customer Segmentation
    # website = {"C1", "C2", "C3", "C4", "C5"}
    # mobile = {"C3", "C4", "C6", "C7"}
    # store = {"C2", "C4", "C7", "C8"}
    # Find customers on exactly one, exactly two, and all three platforms.
    # --------------------------------------------------------------------------
    print("\n--- Q30: Customer Segmentation ---")
    website = {"C1", "C2", "C3", "C4", "C5"}
    mobile = {"C3", "C4", "C6", "C7"}
    store = {"C2", "C4", "C7", "C8"}

    all_three_platforms = website & mobile & store
    at_least_two_platforms = (website & mobile) | (mobile & store) | (website & store)
    exactly_two_platforms = at_least_two_platforms - all_three_platforms
    all_customers = website | mobile | store
    exactly_one_platform = all_customers - at_least_two_platforms

    print(f"Website customers: {website}")
    print(f"Mobile customers: {mobile}")
    print(f"Store customers: {store}")
    print(f"Customers on all three platforms: {all_three_platforms}")
    print(f"Customers on exactly two platforms: {exactly_two_platforms}")
    print(f"Customers on exactly one platform: {exactly_one_platform}")
    print("=" * 60)

if __name__ == "__main__":
    main()

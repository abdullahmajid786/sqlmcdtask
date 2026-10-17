"""
Python Data Structures | Mixed Data Structures | Questions 41-50
Part 5 of 5 | 10 questions | Beginner to Expert

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
    print("PYTHON PRACTICE: MIXED DATA STRUCTURES (PART 5 OF 5 - Q41 TO Q50)")
    print("=" * 60)

    # ==========================================================================
    # LEVEL: ADVANCED
    # ==========================================================================

    # --------------------------------------------------------------------------
    # Q41. Student Performance System
    # students = [
    #  {"id": 1, "name": "Ali", "marks": (85, 90, 88)},
    #  {"id": 2, "name": "Sara", "marks": (92, 95, 91)},
    #  {"id": 3, "name": "Ahmed", "marks": (78, 84, 80)}
    # ]
    # Calculate each average, top student, tuple of names, and set of unique marks.
    # --------------------------------------------------------------------------
    print("\n--- Q41: Student Performance System ---")
    students = [
        {"id": 1, "name": "Ali", "marks": (85, 90, 88)},
        {"id": 2, "name": "Sara", "marks": (92, 95, 91)},
        {"id": 3, "name": "Ahmed", "marks": (78, 84, 80)}
    ]

    # Calculate average for each student
    averages = {
        students[0]["name"]: sum(students[0]["marks"]) / len(students[0]["marks"]),
        students[1]["name"]: sum(students[1]["marks"]) / len(students[1]["marks"]),
        students[2]["name"]: sum(students[2]["marks"]) / len(students[2]["marks"])
    }
    # Top student
    top_student = max(averages, key=averages.get)
    # Tuple of names
    names_tuple = (students[0]["name"], students[1]["name"], students[2]["name"])
    # Set of unique marks
    unique_marks = set(students[0]["marks"] + students[1]["marks"] + students[2]["marks"])

    print(f"Student Averages: {averages}")
    print(f"Top Student: {top_student} (Average: {averages[top_student]:.2f})")
    print(f"Names Tuple: {names_tuple}")
    print(f"Unique Marks Set: {unique_marks}")

    # --------------------------------------------------------------------------
    # Q42. Employee Skills
    # employees = {
    #  "Ali": {"Python", "SQL", "AWS"},
    #  "Sara": {"Python", "Databricks", "SQL"},
    #  "Ahmed": {"AWS", "Snowflake", "SQL"}
    # }
    # Find common skills, Ali-only skills, all team skills, and employees meeting Python + SQL requirements.
    # --------------------------------------------------------------------------
    print("\n--- Q42: Employee Skills ---")
    employees = {
        "Ali": {"Python", "SQL", "AWS"},
        "Sara": {"Python", "Databricks", "SQL"},
        "Ahmed": {"AWS", "Snowflake", "SQL"}
    }

    common_skills = employees["Ali"] & employees["Sara"] & employees["Ahmed"]
    ali_only_skills = employees["Ali"] - employees["Sara"] - employees["Ahmed"]
    all_team_skills = employees["Ali"] | employees["Sara"] | employees["Ahmed"]

    required_skills = {"Python", "SQL"}
    # Check employees meeting requirement without loops
    meeting_req = (
        (("Ali",) if required_skills.issubset(employees["Ali"]) else ()) +
        (("Sara",) if required_skills.issubset(employees["Sara"]) else ()) +
        (("Ahmed",) if required_skills.issubset(employees["Ahmed"]) else ())
    )

    print(f"Common Skills (all employees): {common_skills}")
    print(f"Ali-only Skills: {ali_only_skills}")
    print(f"All Team Skills: {all_team_skills}")
    print(f"Employees meeting Python + SQL requirements: {meeting_req}")

    # --------------------------------------------------------------------------
    # Q43. Sales Data
    # sales = [
    #  ("Laptop", 120000, 2),
    #  ("Mouse", 1500, 5),
    #  ("Keyboard", 3500, 3)
    # ]
    # Calculate revenue, top-revenue product, name-to-revenue dictionary, and set of prices.
    # --------------------------------------------------------------------------
    print("\n--- Q43: Sales Data ---")
    sales = [
        ("Laptop", 120000, 2),
        ("Mouse", 1500, 5),
        ("Keyboard", 3500, 3)
    ]

    name_to_revenue = {
        sales[0][0]: sales[0][1] * sales[0][2],
        sales[1][0]: sales[1][1] * sales[1][2],
        sales[2][0]: sales[2][1] * sales[2][2]
    }
    total_revenue = sum(name_to_revenue.values())
    top_revenue_product = max(name_to_revenue, key=name_to_revenue.get)
    prices_set = {sales[0][1], sales[1][1], sales[2][1]}

    print(f"Name to Revenue: {name_to_revenue}")
    print(f"Total Revenue: {total_revenue}")
    print(f"Top-Revenue Product: {top_revenue_product} ({name_to_revenue[top_revenue_product]})")
    print(f"Set of Prices: {prices_set}")

    # --------------------------------------------------------------------------
    # Q44. Customer Orders
    # customers = {
    #  "C101": {"name": "Ali", "orders": [1200, 2500, 1800]},
    #  "C102": {"name": "Sara", "orders": [3000, 4500]},
    #  "C103": {"name": "Ahmed", "orders": [1500, 2000, 1000]}
    # }
    # Calculate spending per customer, top customer, and tuple of totals in customer ID order.
    # --------------------------------------------------------------------------
    print("\n--- Q44: Customer Orders ---")
    customers = {
        "C101": {"name": "Ali", "orders": [1200, 2500, 1800]},
        "C102": {"name": "Sara", "orders": [3000, 4500]},
        "C103": {"name": "Ahmed", "orders": [1500, 2000, 1000]}
    }

    spending_per_customer = {
        customers["C101"]["name"]: sum(customers["C101"]["orders"]),
        customers["C102"]["name"]: sum(customers["C102"]["orders"]),
        customers["C103"]["name"]: sum(customers["C103"]["orders"])
    }
    top_customer = max(spending_per_customer, key=spending_per_customer.get)
    totals_by_id_order = (
        sum(customers["C101"]["orders"]),
        sum(customers["C102"]["orders"]),
        sum(customers["C103"]["orders"])
    )

    print(f"Spending per Customer: {spending_per_customer}")
    print(f"Top Customer: {top_customer} (Spent: {spending_per_customer[top_customer]})")
    print(f"Totals in Customer ID order: {totals_by_id_order}")

    # --------------------------------------------------------------------------
    # Q45. Course Enrollment
    # courses = {
    #  "Python": {"Ali", "Sara", "Ahmed"},
    #  "SQL": {"Sara", "Ahmed", "Zain"},
    #  "AWS": {"Ali", "Ahmed", "Zain"}
    # }
    # Find students in exactly two, all three, and exactly one course; count unique students.
    # --------------------------------------------------------------------------
    print("\n--- Q45: Course Enrollment ---")
    courses = {
        "Python": {"Ali", "Sara", "Ahmed"},
        "SQL": {"Sara", "Ahmed", "Zain"},
        "AWS": {"Ali", "Ahmed", "Zain"}
    }

    all_three_courses = courses["Python"] & courses["SQL"] & courses["AWS"]
    at_least_two_courses = (
        (courses["Python"] & courses["SQL"]) |
        (courses["SQL"] & courses["AWS"]) |
        (courses["Python"] & courses["AWS"])
    )
    exactly_two_courses = at_least_two_courses - all_three_courses
    all_students_set = courses["Python"] | courses["SQL"] | courses["AWS"]
    exactly_one_course = all_students_set - at_least_two_courses
    unique_students_count = len(all_students_set)

    print(f"Students in all three courses: {all_three_courses}")
    print(f"Students in exactly two courses: {exactly_two_courses}")
    print(f"Students in exactly one course: {exactly_one_course}")
    print(f"Unique students count: {unique_students_count}")

    # ==========================================================================
    # LEVEL: EXPERT
    # ==========================================================================

    # --------------------------------------------------------------------------
    # Q46. E-Commerce Transactions
    # transactions = [
    #  {"id": 101, "customer": "Ali", "items": [("Laptop", 120000, 1), ("Mouse", 1500, 2)]},
    #  {"id": 102, "customer": "Sara", "items": [("Keyboard", 3500, 2), ("Mouse", 1500, 1)]},
    #  {"id": 103, "customer": "Ali", "items": [("Monitor", 45000, 1)]}
    # ]
    # Calculate total revenue, Ali spending, largest transaction, and unique product names.
    # --------------------------------------------------------------------------
    print("\n--- Q46: E-Commerce Transactions ---")
    transactions = [
        {"id": 101, "customer": "Ali", "items": [("Laptop", 120000, 1), ("Mouse", 1500, 2)]},
        {"id": 102, "customer": "Sara", "items": [("Keyboard", 3500, 2), ("Mouse", 1500, 1)]},
        {"id": 103, "customer": "Ali", "items": [("Monitor", 45000, 1)]}
    ]

    t1_amount = (
        transactions[0]["items"][0][1] * transactions[0]["items"][0][2] +
        transactions[0]["items"][1][1] * transactions[0]["items"][1][2]
    )
    t2_amount = (
        transactions[1]["items"][0][1] * transactions[1]["items"][0][2] +
        transactions[1]["items"][1][1] * transactions[1]["items"][1][2]
    )
    t3_amount = (
        transactions[2]["items"][0][1] * transactions[2]["items"][0][2]
    )

    total_revenue_ecom = t1_amount + t2_amount + t3_amount
    ali_spending = t1_amount + t3_amount
    tx_amounts = {
        transactions[0]["id"]: t1_amount,
        transactions[1]["id"]: t2_amount,
        transactions[2]["id"]: t3_amount
    }
    largest_tx_id = max(tx_amounts, key=tx_amounts.get)
    unique_product_names = {
        transactions[0]["items"][0][0],
        transactions[0]["items"][1][0],
        transactions[1]["items"][0][0],
        transactions[1]["items"][1][0],
        transactions[2]["items"][0][0]
    }

    print(f"Total Revenue: {total_revenue_ecom}")
    print(f"Ali Spending: {ali_spending}")
    print(f"Largest Transaction ID: {largest_tx_id} (Amount: {tx_amounts[largest_tx_id]})")
    print(f"Unique Product Names: {unique_product_names}")

    # --------------------------------------------------------------------------
    # Q47. Pipeline Monitoring
    # pipelines = {
    #  "pipeline_1": {"status": "success", "records": (1000, 1200, 1100)},
    #  "pipeline_2": {"status": "failed", "records": (800, 0, 0)},
    #  "pipeline_3": {"status": "success", "records": (1500, 1600, 1700)}
    # }
    # Find total processed records, failed pipelines, largest pipeline total, and average records per run for each.
    # --------------------------------------------------------------------------
    print("\n--- Q47: Pipeline Monitoring ---")
    pipelines = {
        "pipeline_1": {"status": "success", "records": (1000, 1200, 1100)},
        "pipeline_2": {"status": "failed", "records": (800, 0, 0)},
        "pipeline_3": {"status": "success", "records": (1500, 1600, 1700)}
    }

    p1_total = sum(pipelines["pipeline_1"]["records"])
    p2_total = sum(pipelines["pipeline_2"]["records"])
    p3_total = sum(pipelines["pipeline_3"]["records"])

    pipeline_totals = {
        "pipeline_1": p1_total,
        "pipeline_2": p2_total,
        "pipeline_3": p3_total
    }
    total_processed_records = sum(pipeline_totals.values())
    failed_pipelines = (
        (("pipeline_1",) if pipelines["pipeline_1"]["status"] == "failed" else ()) +
        (("pipeline_2",) if pipelines["pipeline_2"]["status"] == "failed" else ()) +
        (("pipeline_3",) if pipelines["pipeline_3"]["status"] == "failed" else ())
    )
    largest_pipeline_name = max(pipeline_totals, key=pipeline_totals.get)
    average_records_per_run = {
        "pipeline_1": p1_total / len(pipelines["pipeline_1"]["records"]),
        "pipeline_2": p2_total / len(pipelines["pipeline_2"]["records"]),
        "pipeline_3": p3_total / len(pipelines["pipeline_3"]["records"])
    }

    print(f"Total Processed Records: {total_processed_records}")
    print(f"Failed Pipelines: {failed_pipelines}")
    print(f"Largest Pipeline Total: {largest_pipeline_name} ({pipeline_totals[largest_pipeline_name]})")
    print(f"Average Records per Run: {average_records_per_run}")

    # --------------------------------------------------------------------------
    # Q48. Banking Transactions
    # accounts = {
    #  "A101": {"holder": "Ali", "transactions": [5000, -2000, 3000, -1000]},
    #  "A102": {"holder": "Sara", "transactions": [10000, -3000, -2000]},
    #  "A103": {"holder": "Ahmed", "transactions": [7000, -1500, 2500]}
    # }
    # Assuming zero starting balances, calculate final balances, highest balance, total withdrawals, and largest single deposit.
    # --------------------------------------------------------------------------
    print("\n--- Q48: Banking Transactions ---")
    accounts = {
        "A101": {"holder": "Ali", "transactions": [5000, -2000, 3000, -1000]},
        "A102": {"holder": "Sara", "transactions": [10000, -3000, -2000]},
        "A103": {"holder": "Ahmed", "transactions": [7000, -1500, 2500]}
    }

    final_balances = {
        "A101": sum(accounts["A101"]["transactions"]),
        "A102": sum(accounts["A102"]["transactions"]),
        "A103": sum(accounts["A103"]["transactions"])
    }
    highest_balance_account = max(final_balances, key=final_balances.get)
    all_transactions = (
        accounts["A101"]["transactions"] +
        accounts["A102"]["transactions"] +
        accounts["A103"]["transactions"]
    )
    # Total withdrawals (negative transactions):
    total_withdrawals = abs(
        accounts["A101"]["transactions"][1] + accounts["A101"]["transactions"][3] +
        accounts["A102"]["transactions"][1] + accounts["A102"]["transactions"][2] +
        accounts["A103"]["transactions"][1]
    )
    largest_single_deposit = max(all_transactions)

    print(f"Final Balances: {final_balances}")
    print(f"Account with Highest Balance: {highest_balance_account} ({final_balances[highest_balance_account]}, Holder: {accounts[highest_balance_account]['holder']})")
    print(f"Total Withdrawals: {total_withdrawals}")
    print(f"Largest Single Deposit: {largest_single_deposit}")

    # --------------------------------------------------------------------------
    # Q49. Product Recommendations
    # users = {
    #  "Ali": {"purchased": {"Laptop", "Mouse"}, "wishlist": {"Keyboard", "Monitor", "Mouse"}},
    #  "Sara": {"purchased": {"Keyboard", "Monitor"}, "wishlist": {"Laptop", "Mouse"}},
    #  "Ahmed": {"purchased": {"Laptop", "Keyboard"}, "wishlist": {"Monitor", "Headphones"}}
    # }
    # Find products bought by at least two users, Ali wishlist minus purchases, shared wishlist products, and all products.
    # --------------------------------------------------------------------------
    print("\n--- Q49: Product Recommendations ---")
    users = {
        "Ali": {"purchased": {"Laptop", "Mouse"}, "wishlist": {"Keyboard", "Monitor", "Mouse"}},
        "Sara": {"purchased": {"Keyboard", "Monitor"}, "wishlist": {"Laptop", "Mouse"}},
        "Ahmed": {"purchased": {"Laptop", "Keyboard"}, "wishlist": {"Monitor", "Headphones"}}
    }

    p_ali = users["Ali"]["purchased"]
    p_sara = users["Sara"]["purchased"]
    p_ahmed = users["Ahmed"]["purchased"]

    bought_at_least_two = (p_ali & p_sara) | (p_sara & p_ahmed) | (p_ali & p_ahmed)
    ali_wishlist_minus_purchases = users["Ali"]["wishlist"] - users["Ali"]["purchased"]

    w_ali = users["Ali"]["wishlist"]
    w_sara = users["Sara"]["wishlist"]
    w_ahmed = users["Ahmed"]["wishlist"]
    shared_wishlist_products = (w_ali & w_sara) | (w_sara & w_ahmed) | (w_ali & w_ahmed)
    all_products = p_ali | w_ali | p_sara | w_sara | p_ahmed | w_ahmed

    print(f"Products bought by at least two users: {bought_at_least_two}")
    print(f"Ali wishlist minus purchases: {ali_wishlist_minus_purchases}")
    print(f"Shared wishlist products (between users): {shared_wishlist_products}")
    print(f"All products: {all_products}")

    # --------------------------------------------------------------------------
    # Q50. Final Company Analysis
    # company = {
    #  "departments": {
    #  "Engineering": {
    #  "employees": [
    #  ("Ali", 120000, {"Python", "AWS", "SQL"}),
    #  ("Sara", 150000, {"Python", "Databricks", "SQL"})
    #  ],
    #  "budget": 500000
    #  },
    #  "Analytics": {
    #  "employees": [
    #  ("Ahmed", 100000, {"SQL", "Power BI"}),
    #  ("Zain", 130000, {"Python", "SQL", "Tableau"})
    #  ],
    #  "budget": 400000
    #  }
    #  }
    # }
    # 1. Payroll per department. 2. Company payroll. 3. Highest-paid employee. 4. Skills shared by all.
    # 5. Engineering-only skills. 6. Remaining budget per department. 7. Department with higher average salary.
    # 8. Name-to-salary dictionary. 9. All unique skills. 10. Is combined budget sufficient?
    # --------------------------------------------------------------------------
    print("\n--- Q50: Final Company Analysis ---")
    company = {
        "departments": {
            "Engineering": {
                "employees": [
                    ("Ali", 120000, {"Python", "AWS", "SQL"}),
                    ("Sara", 150000, {"Python", "Databricks", "SQL"})
                ],
                "budget": 500000
            },
            "Analytics": {
                "employees": [
                    ("Ahmed", 100000, {"SQL", "Power BI"}),
                    ("Zain", 130000, {"Python", "SQL", "Tableau"})
                ],
                "budget": 400000
            }
        }
    }

    # 1. Payroll per department
    eng_emp = company["departments"]["Engineering"]["employees"]
    ana_emp = company["departments"]["Analytics"]["employees"]
    eng_payroll = eng_emp[0][1] + eng_emp[1][1]
    ana_payroll = ana_emp[0][1] + ana_emp[1][1]
    payroll_per_department = {"Engineering": eng_payroll, "Analytics": ana_payroll}

    # 2. Company payroll
    company_payroll = eng_payroll + ana_payroll

    # 3. Highest-paid employee & 8. Name-to-salary dictionary
    name_to_salary = {
        eng_emp[0][0]: eng_emp[0][1],
        eng_emp[1][0]: eng_emp[1][1],
        ana_emp[0][0]: ana_emp[0][1],
        ana_emp[1][0]: ana_emp[1][1]
    }
    highest_paid_employee = max(name_to_salary, key=name_to_salary.get)

    # 4. Skills shared by all
    skills_shared_by_all = (
        eng_emp[0][2] & eng_emp[1][2] & ana_emp[0][2] & ana_emp[1][2]
    )

    # 5. Engineering-only skills
    eng_skills = eng_emp[0][2] | eng_emp[1][2]
    ana_skills = ana_emp[0][2] | ana_emp[1][2]
    engineering_only_skills = eng_skills - ana_skills

    # 6. Remaining budget per department
    remaining_budget_per_dept = {
        "Engineering": company["departments"]["Engineering"]["budget"] - eng_payroll,
        "Analytics": company["departments"]["Analytics"]["budget"] - ana_payroll
    }

    # 7. Department with higher average salary
    dept_averages = {
        "Engineering": eng_payroll / len(eng_emp),
        "Analytics": ana_payroll / len(ana_emp)
    }
    higher_avg_dept = max(dept_averages, key=dept_averages.get)

    # 9. All unique skills
    all_unique_skills = eng_skills | ana_skills

    # 10. Is combined budget sufficient?
    combined_budget = (
        company["departments"]["Engineering"]["budget"] +
        company["departments"]["Analytics"]["budget"]
    )
    is_budget_sufficient = combined_budget >= company_payroll

    print(f"1. Payroll per department: {payroll_per_department}")
    print(f"2. Company payroll: {company_payroll}")
    print(f"3. Highest-paid employee: {highest_paid_employee} ({name_to_salary[highest_paid_employee]})")
    print(f"4. Skills shared by all: {skills_shared_by_all}")
    print(f"5. Engineering-only skills: {engineering_only_skills}")
    print(f"6. Remaining budget per department: {remaining_budget_per_dept}")
    print(f"7. Department with higher average salary: {higher_avg_dept}")
    print(f"8. Name-to-salary dictionary: {name_to_salary}")
    print(f"9. All unique skills: {all_unique_skills}")
    print(f"10. Is combined budget sufficient? {is_budget_sufficient}")
    print("=" * 60)

if __name__ == "__main__":
    main()

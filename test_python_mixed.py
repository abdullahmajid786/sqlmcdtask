import unittest

class TestPythonMixedPart5(unittest.TestCase):
    def test_q41(self):
        students = [
            {"id": 1, "name": "Ali", "marks": (85, 90, 88)},
            {"id": 2, "name": "Sara", "marks": (92, 95, 91)},
            {"id": 3, "name": "Ahmed", "marks": (78, 84, 80)}
        ]
        averages = {
            students[0]["name"]: sum(students[0]["marks"]) / len(students[0]["marks"]),
            students[1]["name"]: sum(students[1]["marks"]) / len(students[1]["marks"]),
            students[2]["name"]: sum(students[2]["marks"]) / len(students[2]["marks"])
        }
        top_student = max(averages, key=averages.get)
        names_tuple = (students[0]["name"], students[1]["name"], students[2]["name"])
        unique_marks = set(students[0]["marks"] + students[1]["marks"] + students[2]["marks"])
        self.assertEqual(top_student, "Sara")
        self.assertEqual(names_tuple, ("Ali", "Sara", "Ahmed"))
        self.assertEqual(unique_marks, {78, 80, 84, 85, 88, 90, 91, 92, 95})

    def test_q42(self):
        employees = {
            "Ali": {"Python", "SQL", "AWS"},
            "Sara": {"Python", "Databricks", "SQL"},
            "Ahmed": {"AWS", "Snowflake", "SQL"}
        }
        common = employees["Ali"] & employees["Sara"] & employees["Ahmed"]
        ali_only = employees["Ali"] - employees["Sara"] - employees["Ahmed"]
        all_skills = employees["Ali"] | employees["Sara"] | employees["Ahmed"]
        req = {"Python", "SQL"}
        meets = (
            (("Ali",) if req.issubset(employees["Ali"]) else ()) +
            (("Sara",) if req.issubset(employees["Sara"]) else ()) +
            (("Ahmed",) if req.issubset(employees["Ahmed"]) else ())
        )
        self.assertEqual(common, {"SQL"})
        self.assertEqual(ali_only, set())
        self.assertEqual(all_skills, {"Python", "SQL", "AWS", "Databricks", "Snowflake"})
        self.assertEqual(meets, ("Ali", "Sara"))

    def test_q43(self):
        sales = [
            ("Laptop", 120000, 2),
            ("Mouse", 1500, 5),
            ("Keyboard", 3500, 3)
        ]
        rev_dict = {
            sales[0][0]: sales[0][1] * sales[0][2],
            sales[1][0]: sales[1][1] * sales[1][2],
            sales[2][0]: sales[2][1] * sales[2][2]
        }
        tot_rev = sum(rev_dict.values())
        top_p = max(rev_dict, key=rev_dict.get)
        prices = {sales[0][1], sales[1][1], sales[2][1]}
        self.assertEqual(tot_rev, 258000)
        self.assertEqual(top_p, "Laptop")
        self.assertEqual(rev_dict, {"Laptop": 240000, "Mouse": 7500, "Keyboard": 10500})
        self.assertEqual(prices, {120000, 1500, 3500})

    def test_q44(self):
        customers = {
            "C101": {"name": "Ali", "orders": [1200, 2500, 1800]},
            "C102": {"name": "Sara", "orders": [3000, 4500]},
            "C103": {"name": "Ahmed", "orders": [1500, 2000, 1000]}
        }
        spending = {
            customers["C101"]["name"]: sum(customers["C101"]["orders"]),
            customers["C102"]["name"]: sum(customers["C102"]["orders"]),
            customers["C103"]["name"]: sum(customers["C103"]["orders"])
        }
        top_c = max(spending, key=spending.get)
        totals_tuple = (
            sum(customers["C101"]["orders"]),
            sum(customers["C102"]["orders"]),
            sum(customers["C103"]["orders"])
        )
        self.assertEqual(spending, {"Ali": 5500, "Sara": 7500, "Ahmed": 4500})
        self.assertEqual(top_c, "Sara")
        self.assertEqual(totals_tuple, (5500, 7500, 4500))

    def test_q45(self):
        courses = {
            "Python": {"Ali", "Sara", "Ahmed"},
            "SQL": {"Sara", "Ahmed", "Zain"},
            "AWS": {"Ali", "Ahmed", "Zain"}
        }
        all_3 = courses["Python"] & courses["SQL"] & courses["AWS"]
        at_least_2 = (
            (courses["Python"] & courses["SQL"]) |
            (courses["SQL"] & courses["AWS"]) |
            (courses["Python"] & courses["AWS"])
        )
        exact_2 = at_least_2 - all_3
        all_st = courses["Python"] | courses["SQL"] | courses["AWS"]
        exact_1 = all_st - at_least_2
        self.assertEqual(exact_2, {"Ali", "Sara", "Zain"})
        self.assertEqual(all_3, {"Ahmed"})
        self.assertEqual(exact_1, set())
        self.assertEqual(len(all_st), 4)

    def test_q46(self):
        transactions = [
            {"id": 101, "customer": "Ali", "items": [("Laptop", 120000, 1), ("Mouse", 1500, 2)]},
            {"id": 102, "customer": "Sara", "items": [("Keyboard", 3500, 2), ("Mouse", 1500, 1)]},
            {"id": 103, "customer": "Ali", "items": [("Monitor", 45000, 1)]}
        ]
        t1 = transactions[0]["items"][0][1] * transactions[0]["items"][0][2] + transactions[0]["items"][1][1] * transactions[0]["items"][1][2]
        t2 = transactions[1]["items"][0][1] * transactions[1]["items"][0][2] + transactions[1]["items"][1][1] * transactions[1]["items"][1][2]
        t3 = transactions[2]["items"][0][1] * transactions[2]["items"][0][2]
        tot = t1 + t2 + t3
        ali = t1 + t3
        tx_dict = {transactions[0]["id"]: t1, transactions[1]["id"]: t2, transactions[2]["id"]: t3}
        largest = max(tx_dict, key=tx_dict.get)
        products = {
            transactions[0]["items"][0][0],
            transactions[0]["items"][1][0],
            transactions[1]["items"][0][0],
            transactions[1]["items"][1][0],
            transactions[2]["items"][0][0]
        }
        self.assertEqual(tot, 176500)
        self.assertEqual(ali, 168000)
        self.assertEqual(largest, 101)
        self.assertEqual(products, {"Laptop", "Mouse", "Keyboard", "Monitor"})

    def test_q47(self):
        pipelines = {
            "pipeline_1": {"status": "success", "records": (1000, 1200, 1100)},
            "pipeline_2": {"status": "failed", "records": (800, 0, 0)},
            "pipeline_3": {"status": "success", "records": (1500, 1600, 1700)}
        }
        p1 = sum(pipelines["pipeline_1"]["records"])
        p2 = sum(pipelines["pipeline_2"]["records"])
        p3 = sum(pipelines["pipeline_3"]["records"])
        p_totals = {"pipeline_1": p1, "pipeline_2": p2, "pipeline_3": p3}
        tot_proc = sum(p_totals.values())
        failed = (
            (("pipeline_1",) if pipelines["pipeline_1"]["status"] == "failed" else ()) +
            (("pipeline_2",) if pipelines["pipeline_2"]["status"] == "failed" else ()) +
            (("pipeline_3",) if pipelines["pipeline_3"]["status"] == "failed" else ())
        )
        largest = max(p_totals, key=p_totals.get)
        self.assertEqual(tot_proc, 8900)
        self.assertEqual(failed, ("pipeline_2",))
        self.assertEqual(largest, "pipeline_3")

    def test_q48(self):
        accounts = {
            "A101": {"holder": "Ali", "transactions": [5000, -2000, 3000, -1000]},
            "A102": {"holder": "Sara", "transactions": [10000, -3000, -2000]},
            "A103": {"holder": "Ahmed", "transactions": [7000, -1500, 2500]}
        }
        bals = {
            "A101": sum(accounts["A101"]["transactions"]),
            "A102": sum(accounts["A102"]["transactions"]),
            "A103": sum(accounts["A103"]["transactions"])
        }
        highest = max(bals, key=bals.get)
        all_tx = accounts["A101"]["transactions"] + accounts["A102"]["transactions"] + accounts["A103"]["transactions"]
        total_w = abs(
            accounts["A101"]["transactions"][1] + accounts["A101"]["transactions"][3] +
            accounts["A102"]["transactions"][1] + accounts["A102"]["transactions"][2] +
            accounts["A103"]["transactions"][1]
        )
        largest_dep = max(all_tx)
        self.assertEqual(bals, {"A101": 5000, "A102": 5000, "A103": 8000})
        self.assertEqual(highest, "A103")
        self.assertEqual(total_w, 9500)
        self.assertEqual(largest_dep, 10000)

    def test_q49(self):
        users = {
            "Ali": {"purchased": {"Laptop", "Mouse"}, "wishlist": {"Keyboard", "Monitor", "Mouse"}},
            "Sara": {"purchased": {"Keyboard", "Monitor"}, "wishlist": {"Laptop", "Mouse"}},
            "Ahmed": {"purchased": {"Laptop", "Keyboard"}, "wishlist": {"Monitor", "Headphones"}}
        }
        p_ali, p_sara, p_ahmed = users["Ali"]["purchased"], users["Sara"]["purchased"], users["Ahmed"]["purchased"]
        at_least_2 = (p_ali & p_sara) | (p_sara & p_ahmed) | (p_ali & p_ahmed)
        ali_diff = users["Ali"]["wishlist"] - users["Ali"]["purchased"]
        w_ali, w_sara, w_ahmed = users["Ali"]["wishlist"], users["Sara"]["wishlist"], users["Ahmed"]["wishlist"]
        shared_w = (w_ali & w_sara) | (w_sara & w_ahmed) | (w_ali & w_ahmed)
        all_p = p_ali | w_ali | p_sara | w_sara | p_ahmed | w_ahmed
        self.assertEqual(at_least_2, {"Keyboard", "Laptop"})
        self.assertEqual(ali_diff, {"Keyboard", "Monitor"})
        self.assertEqual(shared_w, {"Monitor", "Mouse"})
        self.assertEqual(all_p, {"Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"})

    def test_q50(self):
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
        eng_emp = company["departments"]["Engineering"]["employees"]
        ana_emp = company["departments"]["Analytics"]["employees"]
        eng_pay = eng_emp[0][1] + eng_emp[1][1]
        ana_pay = ana_emp[0][1] + ana_emp[1][1]
        dept_pay = {"Engineering": eng_pay, "Analytics": ana_pay}
        comp_pay = eng_pay + ana_pay
        name_sal = {
            eng_emp[0][0]: eng_emp[0][1],
            eng_emp[1][0]: eng_emp[1][1],
            ana_emp[0][0]: ana_emp[0][1],
            ana_emp[1][0]: ana_emp[1][1]
        }
        highest = max(name_sal, key=name_sal.get)
        skills_all = eng_emp[0][2] & eng_emp[1][2] & ana_emp[0][2] & ana_emp[1][2]
        eng_skills = eng_emp[0][2] | eng_emp[1][2]
        ana_skills = ana_emp[0][2] | ana_emp[1][2]
        eng_only = eng_skills - ana_skills
        rem_b = {
            "Engineering": company["departments"]["Engineering"]["budget"] - eng_pay,
            "Analytics": company["departments"]["Analytics"]["budget"] - ana_pay
        }
        dept_avgs = {"Engineering": eng_pay / 2, "Analytics": ana_pay / 2}
        higher_avg = max(dept_avgs, key=dept_avgs.get)
        all_u_skills = eng_skills | ana_skills
        comb_b = company["departments"]["Engineering"]["budget"] + company["departments"]["Analytics"]["budget"]
        is_suff = comb_b >= comp_pay

        self.assertEqual(dept_pay, {"Engineering": 270000, "Analytics": 230000})
        self.assertEqual(comp_pay, 500000)
        self.assertEqual(highest, "Sara")
        self.assertEqual(skills_all, {"SQL"})
        self.assertEqual(eng_only, {"AWS", "Databricks"})
        self.assertEqual(rem_b, {"Engineering": 230000, "Analytics": 170000})
        self.assertEqual(higher_avg, "Engineering")
        self.assertEqual(name_sal, {"Ali": 120000, "Sara": 150000, "Ahmed": 100000, "Zain": 130000})
        self.assertEqual(all_u_skills, {"Python", "AWS", "SQL", "Databricks", "Power BI", "Tableau"})
        self.assertTrue(is_suff)

if __name__ == "__main__":
    unittest.main()

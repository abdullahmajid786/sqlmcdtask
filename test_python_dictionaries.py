import unittest

class TestPythonDictionariesPart4(unittest.TestCase):
    def test_q31(self):
        student = {"name": "Ali", "age": 22, "course": "Python", "marks": 85}
        name = student["name"]
        marks = student["marks"]
        city = student.get("city", "Karachi")
        self.assertEqual(name, "Ali")
        self.assertEqual(marks, 85)
        self.assertEqual(city, "Karachi")

    def test_q32(self):
        employee = {"name": "Sara", "salary": 100000, "department": "IT"}
        employee["salary"] = int(employee["salary"] * 1.20)
        employee["bonus"] = 15000
        employee["department"] = "Data Engineering"
        self.assertEqual(employee["salary"], 120000)
        self.assertEqual(employee["bonus"], 15000)
        self.assertEqual(employee["department"], "Data Engineering")

    def test_q33(self):
        product = {"id": 101, "name": "Laptop", "price": 120000, "stock": 5}
        keys = list(product.keys())
        values = list(product.values())
        items = list(product.items())
        stock_val = product.pop("stock")
        self.assertEqual(keys, ["id", "name", "price", "stock"])
        self.assertEqual(values, [101, "Laptop", 120000, 5])
        self.assertEqual(stock_val, 5)
        self.assertNotIn("stock", product)

    def test_q34(self):
        dict1 = {"a": 10, "b": 20, "c": 30}
        dict2 = {"b": 50, "d": 40}
        merged = dict1 | dict2
        self.assertEqual(merged, {"a": 10, "b": 50, "c": 30, "d": 40})

    def test_q35(self):
        marks = {"Ali": 85, "Sara": 92, "Ahmed": 78, "Zain": 88}
        highest = max(marks.values())
        lowest = min(marks.values())
        avg = sum(marks.values()) / len(marks)
        top_scoring = max(marks, key=marks.get)
        self.assertEqual(highest, 92)
        self.assertEqual(lowest, 78)
        self.assertEqual(avg, 85.75)
        self.assertEqual(top_scoring, "Sara")

    def test_q36(self):
        employees = {
            "E101": {"name": "Ali", "salary": 80000},
            "E102": {"name": "Sara", "salary": 120000},
            "E103": {"name": "Ahmed", "salary": 95000}
        }
        sara_sal = employees["E102"]["salary"]
        employees["E101"]["salary"] = int(employees["E101"]["salary"] * 1.15)
        total_payroll = (
            employees["E101"]["salary"] +
            employees["E102"]["salary"] +
            employees["E103"]["salary"]
        )
        self.assertEqual(sara_sal, 120000)
        self.assertEqual(employees["E101"]["salary"], 92000)
        self.assertEqual(total_payroll, 307000)

    def test_q37(self):
        data = {"Python": "Ali", "SQL": "Sara", "AWS": "Ahmed"}
        inverted = dict(zip(data.values(), data.keys()))
        self.assertEqual(inverted, {"Ali": "Python", "Sara": "SQL", "Ahmed": "AWS"})

    def test_q38(self):
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
        discounted = grand_total * 0.90
        self.assertEqual(subtotals, {"laptop": 240000, "mouse": 7500, "keyboard": 10500})
        self.assertEqual(grand_total, 258000)
        self.assertEqual(discounted, 232200.0)

    def test_q39(self):
        employees = {
            "Ali": {"python": 90, "sql": 85, "aws": 88},
            "Sara": {"python": 95, "sql": 92, "aws": 90},
            "Ahmed": {"python": 80, "sql": 87, "aws": 84}
        }
        averages = {
            "Ali": sum(employees["Ali"].values()) / len(employees["Ali"]),
            "Sara": sum(employees["Sara"].values()) / len(employees["Sara"]),
            "Ahmed": sum(employees["Ahmed"].values()) / len(employees["Ahmed"])
        }
        top_performer = max(averages, key=averages.get)
        highest_sql = max(employees["Ali"]["sql"], employees["Sara"]["sql"], employees["Ahmed"]["sql"])
        self.assertEqual(top_performer, "Sara")
        self.assertEqual(highest_sql, 92)

    def test_q40(self):
        inventory = {
            "P101": {"name": "Laptop", "price": 120000, "stock": 5},
            "P102": {"name": "Mouse", "price": 1500, "stock": 20},
            "P103": {"name": "Keyboard", "price": 3500, "stock": 10}
        }
        item_vals = {
            "P101": inventory["P101"]["price"] * inventory["P101"]["stock"],
            "P102": inventory["P102"]["price"] * inventory["P102"]["stock"],
            "P103": inventory["P103"]["price"] * inventory["P103"]["stock"]
        }
        total_val = sum(item_vals.values())
        most_valuable_key = max(item_vals, key=item_vals.get)
        inventory["P101"]["stock"] -= 2
        inventory["P102"]["stock"] -= 5
        self.assertEqual(total_val, 665000)
        self.assertEqual(most_valuable_key, "P101")
        self.assertEqual(inventory["P101"]["stock"], 3)
        self.assertEqual(inventory["P102"]["stock"], 15)

if __name__ == "__main__":
    unittest.main()

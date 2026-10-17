import unittest

class TestPythonSetsPart3(unittest.TestCase):
    def test_q21(self):
        numbers = [10, 20, 10, 30, 40, 20, 50]
        unique_set = set(numbers)
        count = len(unique_set)
        self.assertEqual(unique_set, {10, 20, 30, 40, 50})
        self.assertEqual(count, 5)

    def test_q22(self):
        a = {1, 2, 3, 4, 5}
        b = {4, 5, 6, 7, 8}
        self.assertEqual(a | b, {1, 2, 3, 4, 5, 6, 7, 8})
        self.assertEqual(a & b, {4, 5})
        self.assertEqual(a - b, {1, 2, 3})
        self.assertEqual(a ^ b, {1, 2, 3, 6, 7, 8})

    def test_q23(self):
        skills = {"Python", "SQL", "AWS"}
        skills.update({"Snowflake", "Databricks"})
        skills.discard("AWS")
        self.assertEqual(skills, {"Python", "SQL", "Snowflake", "Databricks"})

    def test_q24(self):
        python_students = {"Ali", "Sara", "Ahmed", "Zain"}
        sql_students = {"Sara", "Ahmed", "Hamza", "Usman"}
        both = python_students & sql_students
        exactly_one = python_students ^ sql_students
        self.assertEqual(both, {"Sara", "Ahmed"})
        self.assertEqual(exactly_one, {"Ali", "Zain", "Hamza", "Usman"})

    def test_q25(self):
        required_skills = {"Python", "SQL"}
        candidate_skills = {"Python", "SQL", "AWS", "Snowflake"}
        self.assertTrue(required_skills.issubset(candidate_skills))
        self.assertTrue(candidate_skills.issuperset(required_skills))

    def test_q26(self):
        numbers = {1, 2, 4, 6, 8, 10}
        missing = set(range(1, 11)) - numbers
        self.assertEqual(missing, {3, 5, 7, 9})

    def test_q27(self):
        python = {"Ali", "Sara", "Ahmed", "Zain"}
        sql = {"Sara", "Ahmed", "Hamza"}
        aws = {"Ahmed", "Zain", "Hamza"}
        all_three = python & sql & aws
        py_sql_not_aws = (python & sql) - aws
        at_least_two = (python & sql) | (sql & aws) | (python & aws)
        self.assertEqual(all_three, {"Ahmed"})
        self.assertEqual(py_sql_not_aws, {"Sara"})
        self.assertEqual(at_least_two, {"Ahmed", "Sara", "Zain", "Hamza"})

    def test_q28(self):
        day1 = {101, 102, 103, 104}
        day2 = {103, 104, 105, 106}
        day3 = {104, 106, 107, 108}
        all_days = day1 & day2 & day3
        at_least_two = (day1 & day2) | (day2 & day3) | (day1 & day3)
        exactly_one = (day1 | day2 | day3) - at_least_two
        self.assertEqual(all_days, {104})
        self.assertEqual(at_least_two, {103, 104, 106})
        self.assertEqual(exactly_one, {101, 102, 105, 107, 108})

    def test_q29(self):
        required_permissions = {"read", "write", "execute"}
        user_permissions = {"read", "write", "delete"}
        missing = required_permissions - user_permissions
        extra = user_permissions - required_permissions
        authorized = required_permissions.issubset(user_permissions)
        self.assertEqual(missing, {"execute"})
        self.assertEqual(extra, {"delete"})
        self.assertFalse(authorized)

    def test_q30(self):
        website = {"C1", "C2", "C3", "C4", "C5"}
        mobile = {"C3", "C4", "C6", "C7"}
        store = {"C2", "C4", "C7", "C8"}
        all_three = website & mobile & store
        at_least_two = (website & mobile) | (mobile & store) | (website & store)
        exactly_two = at_least_two - all_three
        exactly_one = (website | mobile | store) - at_least_two
        self.assertEqual(all_three, {"C4"})
        self.assertEqual(exactly_two, {"C2", "C3", "C7"})
        self.assertEqual(exactly_one, {"C1", "C5", "C6", "C8"})

if __name__ == "__main__":
    unittest.main()

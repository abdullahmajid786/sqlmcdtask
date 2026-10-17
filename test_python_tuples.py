import unittest
from operator import itemgetter
import math

class TestPythonTuplesPart2(unittest.TestCase):
    def test_q11(self):
        colors = ("red", "green", "blue", "yellow", "purple")
        second = colors[1]
        last = colors[-1]
        middle_three = colors[1:4]
        self.assertEqual(second, "green")
        self.assertEqual(last, "purple")
        self.assertEqual(middle_three, ("green", "blue", "yellow"))

    def test_q12(self):
        employee = ("Ali", 28, "Data Engineer", 150000)
        name, age, designation, salary = employee
        self.assertEqual(name, "Ali")
        self.assertEqual(age, 28)
        self.assertEqual(designation, "Data Engineer")
        self.assertEqual(salary, 150000)

    def test_q13(self):
        tuple1 = (10, 20, 30)
        tuple2 = (40, 50, 60)
        combined = tuple1 + tuple2
        rev = combined[::-1]
        self.assertEqual(combined, (10, 20, 30, 40, 50, 60))
        self.assertEqual(rev, (60, 50, 40, 30, 20, 10))

    def test_q14(self):
        numbers = (10, 20, 30, 20, 40, 20, 50)
        count_20 = numbers.count(20)
        first_index_20 = numbers.index(20)
        self.assertEqual(count_20, 3)
        self.assertEqual(first_index_20, 1)

    def test_q15(self):
        data = (100, 200, 300, 400, 500, 600)
        first, second, *remaining, last = data
        self.assertEqual(first, 100)
        self.assertEqual(second, 200)
        self.assertEqual(remaining, [300, 400, 500])
        self.assertEqual(last, 600)

    def test_q16(self):
        numbers = (10, 20, 30, 40, 50)
        idx = numbers.index(30)
        modified = numbers[:idx] + (300,) + numbers[idx + 1:]
        self.assertEqual(modified, (10, 20, 300, 40, 50))
        self.assertEqual(numbers, (10, 20, 30, 40, 50))

    def test_q17(self):
        students = (
            ("Ali", (85, 90, 88)),
            ("Sara", (92, 87, 95)),
            ("Ahmed", (78, 84, 80))
        )
        sara_second = students[1][1][1]
        ali_avg = sum(students[0][1]) / len(students[0][1])
        ahmed_highest = max(students[2][1])
        self.assertEqual(sara_second, 87)
        self.assertAlmostEqual(ali_avg, 87.66666666666667)
        self.assertEqual(ahmed_highest, 84)

    def test_q18(self):
        employees = (
            ("Ali", 80000),
            ("Sara", 120000),
            ("Ahmed", 95000)
        )
        sorted_emp = tuple(sorted(employees, key=itemgetter(1), reverse=True))
        expected = (
            ("Sara", 120000),
            ("Ahmed", 95000),
            ("Ali", 80000)
        )
        self.assertEqual(sorted_emp, expected)

    def test_q19(self):
        matrix = ((2, 4, 6), (8, 10, 12), (14, 16, 18))
        diagonal = (matrix[0][0], matrix[1][1], matrix[2][2])
        prod = math.prod(diagonal)
        row_sums = (sum(matrix[0]), sum(matrix[1]), sum(matrix[2]))
        self.assertEqual(diagonal, (2, 10, 18))
        self.assertEqual(prod, 360)
        self.assertEqual(row_sums, (12, 30, 48))

    def test_q20(self):
        records = (
            ("Laptop", 120000, 5),
            ("Mouse", 1500, 20),
            ("Keyboard", 3500, 10)
        )
        inv_val = (
            records[0][1] * records[0][2] +
            records[1][1] * records[1][2] +
            records[2][1] * records[2][2]
        )
        most_expensive = max(records, key=itemgetter(1))
        reversed_names = (records[0][0], records[1][0], records[2][0])[::-1]
        self.assertEqual(inv_val, 665000)
        self.assertEqual(most_expensive[0], "Laptop")
        self.assertEqual(reversed_names, ("Keyboard", "Mouse", "Laptop"))

if __name__ == "__main__":
    unittest.main()

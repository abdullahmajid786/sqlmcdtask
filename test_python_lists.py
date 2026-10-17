import unittest

class TestPythonListsPart1(unittest.TestCase):
    def test_q1(self):
        numbers = [10, 20, 30, 40, 50, 60, 70]
        first = numbers[0]
        middle = numbers[len(numbers) // 2]
        last = numbers[-1]
        self.assertEqual(first, 10)
        self.assertEqual(middle, 40)
        self.assertEqual(last, 70)
        self.assertEqual(numbers, [10, 20, 30, 40, 50, 60, 70])

    def test_q2(self):
        numbers = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
        first_five = numbers[:5]
        last_four = numbers[-4:]
        every_second_reversed = numbers[::-2]
        self.assertEqual(first_five, [5, 10, 15, 20, 25])
        self.assertEqual(last_four, [35, 40, 45, 50])
        self.assertEqual(every_second_reversed, [50, 40, 30, 20, 10])

    def test_q3(self):
        fruits = ["apple", "banana", "cherry", "mango"]
        fruits[fruits.index("banana")] = "orange"
        fruits.insert(2, "grapes")
        fruits.remove("cherry")
        self.assertEqual(fruits, ["apple", "orange", "grapes", "mango"])

    def test_q4(self):
        numbers = [12, 45, 23, 67, 89, 34]
        rev = numbers[::-1]
        self.assertEqual(rev, [34, 89, 67, 23, 45, 12])
        self.assertEqual(numbers, [12, 45, 23, 67, 89, 34])

    def test_q5(self):
        numbers = [45, 12, 89, 34, 89, 67, 45, 23]
        second_largest = sorted(set(numbers))[-2]
        self.assertEqual(second_largest, 67)

    def test_q6(self):
        numbers = [10, 20, 30, 40, 50, 60]
        k = 2
        eff_k = k % len(numbers)
        rotated = numbers[-eff_k:] + numbers[:-eff_k]
        self.assertEqual(rotated, [50, 60, 10, 20, 30, 40])

    def test_q7(self):
        numbers = [10, 20, 10, 30, 20, 40, 30, 50]
        unique_ordered = list(dict.fromkeys(numbers))
        self.assertEqual(unique_ordered, [10, 20, 30, 40, 50])

    def test_q8(self):
        data = [[10, 20], [30, 40], [50, 60]]
        flattened = sum(data, [])
        self.assertEqual(flattened, [10, 20, 30, 40, 50, 60])

    def test_q9(self):
        matrix = [
            [10, 20, 30],
            [40, 50, 60],
            [70, 80, 90]
        ]
        main_diag = [matrix[0][0], matrix[1][1], matrix[2][2]]
        sec_diag = [matrix[0][2], matrix[1][1], matrix[2][0]]
        mid_col = [matrix[0][1], matrix[1][1], matrix[2][1]]
        self.assertEqual(main_diag, [10, 50, 90])
        self.assertEqual(sum(main_diag), 150)
        self.assertEqual(sec_diag, [30, 50, 70])
        self.assertEqual(sum(sec_diag), 150)
        self.assertEqual(mid_col, [20, 50, 80])
        self.assertEqual(sum(mid_col), 150)

    def test_q10(self):
        data = [15, 5, 25, 10, 35, 20, 30]
        u = sorted(set(data))
        res = u[-3:] + u[:2][::-1]
        self.assertEqual(res, [25, 30, 35, 10, 5])

if __name__ == "__main__":
    unittest.main()

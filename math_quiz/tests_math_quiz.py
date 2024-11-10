import unittest
from math_quiz import function_A, function_B, function_C


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = function_A(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        # TODO
        valid_operators = ['+', '-', '*']
        for _ in range(1000):
             operator = function_B()
             self.assertIn(operator, valid_operators)
        

    def test_function_C(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (9, 8, '-', '9 - 8', 1),
                (3, 5, '*', '3 * 5', 15),
                (2, 8, '+', '2 + 8', 10),
                (7, 1, '-', '7 - 1', 6),
                (6, 6, '*', '6 * 6', 36)
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                # TODO
                problem, answer = function_C(num1, num2, operator)
                self.assertEqual(problem, expected_problem)
                self.assertEqual(answer,expected_answer)

if __name__ == "__main__":
    unittest.main()

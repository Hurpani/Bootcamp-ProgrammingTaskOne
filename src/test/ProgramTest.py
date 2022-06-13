import unittest
from typing import List, Tuple

from src.main.Program import digit_list_to_value


class DigitToListValueTest(unittest.TestCase):
    def test_empty_list_yields_zero(self):
        val: int = digit_list_to_value([])
        self.assertEqual(val, 0)

    def test_list_validation_raises_exception_for_negatives(self):
        with self.assertRaises(ValueError):
            digit_list_to_value([5, -1, 0])

    def test_list_validation_raises_exception_for_double_digits(self):
        with self.assertRaises(ValueError):
            digit_list_to_value([5, 10, 0])

    def test_lists_yield_expected_values(self):
        test_cases: List[Tuple[List[int], int]] = [
            ([1], 1),
            ([1, 2, 3], 123),
            ([5, 4], 54),
            ([9, 1, 4], 914)
        ]
        for test_case in test_cases:
            self.assertEqual(digit_list_to_value(test_case[0]), test_case[1])


if __name__ == '__main__':
    unittest.main()

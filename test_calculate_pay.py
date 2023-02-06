from unittest import TestCase

from calculate_pay import calculate_pay


class CalculatePay(TestCase):
    def test_positive_value(self):
        self.assertEqual(100, calculate_pay(10, 10))

    def test_overtime(self):
        self.assertEqual(600, calculate_pay(50, 10))

    def test_zero_value(self):
        self.assertEqual(0, calculate_pay(0, 0))

    def test_negative_value(self):
        self.assertEqual(0, calculate_pay(-10, -10))

from unittest import TestCase

from calculate_pay import calculate_pay

class Calculate_Pay(TestCase):
    def test_calculate_pay(self):
        self.assertEqual(100, calculate_pay(10, 10))

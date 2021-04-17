import unittest
from bmi_functions import simplify_height
from bmi_functions import calculate_bmi
from bmi_functions import bmi_category


class BmiTestCase(unittest.TestCase):

    def test_height_conversion1(self):
        height = simplify_height(5, 3)
        self.assertEqual(height, 63)

    def test_height_conversion2(self):
        height = simplify_height(4, 0)
        self.assertEqual(height, 48)

    def test_height_conversion_exception(self):
        with self.assertRaises(ValueError) as exception_context:
            simplify_height(-8, 2)
            self.assertEqual(str(exception_context.exception), "Expecting Non-negative integer values")

    def test_height_conversion_exception2(self):
        with self.assertRaises(ValueError) as exception_context:
            simplify_height("apple", 2)
            self.assertEqual(str(exception_context.exception), "Expecting Non-negative integer values")

    def test_bmi_calculator(self):
        bmi = calculate_bmi(150, 63)
        self.assertEqual(bmi, 27)

    def test_bmi_calculator2(self):
        bmi = calculate_bmi(77, 48)
        self.assertEqual(bmi, 24)

    def test_bmi_calculator_exception(self):
        with self.assertRaises(ValueError) as exception_context:
            calculate_bmi(-5, 87)
            self.assertEqual(str(exception_context.exception), "Expecting Non-negative integer values")

    def test_bmi_calculator_exception2(self):
        with self.assertRaises(ValueError) as exception_context:
            calculate_bmi("three fifty", 84)
            self.assertEqual(str(exception_context.exception), "Expecting Non-negative integer values")

    def test_bmi_category(self):
        output = bmi_category(11)
        self.assertEqual(output, "Underweight")

    def test_bmi_category2(self):
        output = bmi_category(19)
        self.assertEqual(output, "Normal Weight")

    def test_bmi_category3(self):
        output = bmi_category(28)
        self.assertEqual(output, "Overweight")

    def test_bmi_category4(self):
        output = bmi_category(31)
        self.assertEqual(output, "Obese")
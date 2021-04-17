import unittest
from bodyMassIndexClass import *
from retirementSavingsClass import *

class TestClassesCase(unittest.TestCase):

    def test_bodyMassIndexClass(self):
        bmi = BodyMassIndex(250, 5, 7)
        bmi.calculateBMI()
        actualBmi = bmi.getBMI()
        actualCategory = bmi.getCategory()
        self.assertEqual((actualBmi, actualCategory), (40, "Obese"))

    def test_bodyMassIndexClass_exception(self):
        with self.assertRaises(ValueError) as exception_context:
            bmi = BodyMassIndex(250, "five", 7.7)
            self.assertEqual(exception_context.exception, "Expecting Non-negative integer values")

    def test_RetirementClass(self):
        retire = Retirement(50000, 15)
        retire.calculateSavingGoalAge(21, 250000)
        age = retire.getGoalAge()
        self.assertEqual(age, 46)

    def test_RetirementClass_exception(self):
        with self.assertRaises(ValueError) as exception_context:
            retire = Retirement(50000, "15%")
            self.assertEqual(exception_context.exception, "Expecting Non-negative values")

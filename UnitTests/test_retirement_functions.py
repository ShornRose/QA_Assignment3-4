import unittest
from retirement_functions import percent_savings
from retirement_functions import save_goal_met_when

class RetirementTestCase(unittest.TestCase):

    def test_percent_savings(self):
        savings = percent_savings(100, 10)
        self.assertEqual(savings, 13.50)

    def test_percent_savings2(self):
        savings = percent_savings(15000, 25)
        self.assertEqual(savings, 5062.50)

    def test_percent_saving_exception(self):
        with self.assertRaises(ValueError) as exception_context:
            percent_savings(200000, -20)
            self.assertEqual(exception_context.exception, "Expecting Non-negative values")

    def test_percent_saving_exception2(self):
        with self.assertRaises(ValueError) as exception_context:
            percent_savings(200000, "20%")
            self.assertEqual(exception_context.exception, "Expecting Non-negative values")

    def test_save_goal_met_when(self):
        goalAge = save_goal_met_when(21, 100000, 20000)
        self.assertEqual(goalAge, 26)

    def test_save_goal_met_when2(self):
        goalAge = save_goal_met_when(21, 100000, 1000)
        self.assertEqual(goalAge, "Saving Goal is not met.")

    def test_save_goal_met_when3(self):
        goalAge = save_goal_met_when(21, 100000, 2500)
        self.assertEqual(goalAge, 61)

    def test_save_goal_met_when_exception(self):
        with self.assertRaises(ValueError) as exception_context:
            save_goal_met_when(21, -25000, 20000)
            self.assertEqual(exception_context.exception, "Expecting Non-negative values")

    def test_save_goal_met_when_exception2(self):
        with self.assertRaises(ValueError) as exception_context:
            save_goal_met_when(21, "One hundred thousand", 25000)
            self.assertEqual(exception_context.exception, "Expecting Non-negative values")

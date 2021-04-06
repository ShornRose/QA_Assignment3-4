from bmi_functions import *

class BodyMassIndex:

    def __init__(self, weight, feet, inches):
        self.weight = weight
        self.totalHeight = simplify_height(feet, inches)
        self.bmi = 0
        self.bmiCategory = 0

    def calculateBMI(self):
        self.bmi = calculate_bmi(self.weight, self.totalHeight)
        self.bmiCategory = bmi_category(self.bmi)

    def getBMI(self):
        return self.bmi

    def getCategory(self):
        return self.bmiCategory

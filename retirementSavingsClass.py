from retirement_functions import *

class Retirement:
    def __init__(self, salary, percent):
        self.savings = percent_savings(salary, percent)
        self.goalAge = 0

    def calculateSavingGoalAge(self, startAge, savingGoal):
        self.goalAge = save_goal_met_when(startAge, savingGoal, self.savings)

    def getGoalAge(self):
        return self.goalAge


def percent_savings(salary, percentage):
    if (type(salary) == str) or (type(percentage) == str):
        raise ValueError("Expecting Non-negative values")
    if (salary < 0) or (percentage < 0):
        raise ValueError("Expecting Non-negative values")
    else:
        percentOfSalary = percentage / 100
        percentageSaved = salary * percentOfSalary * 1.35
        return round(percentageSaved, 2)

def save_goal_met_when(startAge, savingGoal, yearlySaving):
    if (type(startAge) == str) or (type(savingGoal) == str) or (type(yearlySaving) == str):
        raise ValueError("Expecting Non-negative values")
    if (startAge < 0) or (savingGoal < 0) or (yearlySaving < 0):
        raise ValueError("Expecting Non-negative values")
    else:
        years = round(savingGoal / yearlySaving)
        goalAge = startAge + years
        if goalAge > 100:
            return "Saving Goal is not met."
        else:
            return goalAge

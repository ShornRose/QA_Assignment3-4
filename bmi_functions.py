from math import floor
#def simplify_height(feet, inches):
#    totalInches = inches + (feet * 12)
#    return totalInches
#
# New consideration, what if user enters a negative value

#def simplify_height(feet, inches):
#    if (feet < 0) or (inches < 0):
#        raise ValueError("Expecting Non-negative integer values")
#    else:
#        totalInches = inches + (feet * 12)
#       return totalInches
# New consideration, what if user enters non numbers values

def simplify_height(feet, inches):
    if (type(feet) == str) or (type(inches) == str):
        raise ValueError("Expecting Non-negative integer values")
    if (feet < 0) or (inches < 0):
        raise ValueError("Expecting Non-negative integer values")
    else:
        totalInches = inches + (feet * 12)
        return totalInches

def calculate_bmi(weight, height):
    if (type(weight) == str) or (type(height) == str):
        raise ValueError("Expecting Non-negative integer values")
    if (weight < 0) or (height < 0):
        raise ValueError("Expecting Non-negative integer values")
    else:
        bmi = (weight * 0.45) / (height * 0.025)**2
        bmi = floor(bmi)
        return bmi

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal Weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

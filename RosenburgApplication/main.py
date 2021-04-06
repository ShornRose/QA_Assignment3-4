import bodyMassIndexClass
import retirementSavingsClass

def main():
    app = True
    while app:
        try:
            print("Welcome to the Rosenburg Application.")
            print("Please select the following options.")
            print("1) Calculate BMI")
            print("2) Determine Retirement Age")
            print("3) Close Application")
            option = input("Enter: ")
            print("")

            if option == "1":
                print("We will now calculate your BMI, please enter the following information.")
                weight = input("Enter your weight in pounds: ")
                print("Now enter you height in feet and inches.")
                feet = input("First, feet: ")
                inches = input("Now, inches: ")
                bmi = bodyMassIndexClass.BodyMassIndex(int(weight), int(feet), int(inches))
                bmi.calculateBMI()
                actualBMI = bmi.getBMI()
                bmiCategory = bmi.getCategory()
                print("Your BMI is " + str(actualBMI) + ". Your category is " + str(bmiCategory) +".")
                input("Press Enter to Return to Main Menu.")
                print("")

            elif option == "2":
                print("We will now determine your retirement age, please enter the following information.")
                salary = input("Please enter your yearly salary: ")
                percent = input("What percent of your salary do you save? (ex. 10%): ")
                retire = retirementSavingsClass.Retirement(int(salary), int(percent))
                age = input("What is your current age: ")
                goal = input("What is your retirement goal? (ex. $100,000): ")
                retire.calculateSavingGoalAge(int(age), int(goal))
                ageGoal = retire.getGoalAge()
                if type(ageGoal) == str:
                    print("Your retirement goal is not possible within your lifetime and savings rate.")
                else:
                    print("Your retirement age at your current savings rate is " + str(ageGoal) + ".")
                input("Press Enter to Return to Main Menu")
                print("")

            elif option == "3":
                app = False

            else:
                print("Please enter valid option (1, 2, 3).")
                print("")

        except Exception as err:
            print("An error has occurred: " + err)
            input("Press Enter")
            print()


main()

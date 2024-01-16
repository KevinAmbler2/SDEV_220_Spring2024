"""
@author: Kevin Ambler
@file: honor_roll_test.py
@desc: Accepts student names and GPAs, then tests if the student qualifies for either the Dean's List or the Honor Roll
"""

lastName = input("Enter the student's last name or ZZZ to quit: ")  # Takes the initial value of lastName to start loop

while lastName != "ZZZ":  # Continues to process inputs until "ZZZ" is entered for lastName
    firstName = input("Enter the student's first name: ")  # Records the student's first name

    grade = float(input("Enter the student's GPA as a float: "))  # Records the student's GPA
    if grade >= 3.5:  # Tests if entered student GPA is enough for Dean's List
        print(firstName, lastName, "qualifies for the Dean's List.\n")
    elif grade >= 3.25:  # Tests if entered student GPA is enough for the Honor Roll
        print(firstName, lastName, "qualifies for the Honor Roll.\n")
    else:  # Returns if entered student GPA is not enough for either Dean's List or the Honor Roll
        print(firstName, lastName, "does not qualify for the Dean's List or the Honor Roll.\n")

    # Takes new value of lastName to overwrite initial value and continue while loop for next iteration
    lastName = input("Enter the student's last name or ZZZ to quit: ")

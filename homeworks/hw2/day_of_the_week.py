"""
File: day_of_the_week.py
Author: Ravindu Gunasekara
Date: 09/18/2023
Section: 44
E-mail: rgunase1@umbc.edu
Description:
    Asks for the day of September,
    uses modulus division to determine
    the day of the week.
"""
day = int(input("What day of September 2023 is it? "))

if day < 0 or day > 30:
    print(f"That day {day} is out of range, you must enter a number between 1 and 30.")
else:
    if day % 7 == 0:
        day_name = "Thursday"
    elif day % 7 == 1:
        day_name = "Friday"
    elif day % 7 == 2:
        day_name = "Saturday"
    elif day % 7 == 3:
        day_name = "Sunday"
    elif day % 7 == 4:
        day_name = "Monday"
    elif day % 7 == 5:
        day_name = "Tuesday"
    elif day % 7 == 6:
        day_name = "Wednesday"

    if day == 1 or day == 21:
        print(f"September {day}st is a {day_name}.")
    elif day == 2 or day == 22:
        print(f"September {day}nd is a {day_name}.")
    elif day == 3 or day == 23:
        print(f"September {day}rd is a {day_name}.")
    else:
        print(f"September {day}th is a {day_name}.")

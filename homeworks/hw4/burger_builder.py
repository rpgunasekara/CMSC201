"""
File: burger_builder.py
Author: Ravindu Gunasekara
Date: 10/02/2023
Section: 44
E-mail: rgunase1@umbc.edu
Description:
    Asks user for various inputs to
    build a burger. Building does not
    start till user inputs "bottom bun".
"""
if __name__ == "__main__":
    burger = []
    condiments = []
    type = ""
    burger_count = 0
    start = input("What do you want to add? ").lower()
    end = ""

    while start != "bottom bun":
        print("You must start with the bottom bun!")
        start = input("What do you want to add? ").lower()
    burger.append(start)

    while end != "top bun":
        end = input("What do you want to add? ").lower()

        if end != "top bun":
            burger.append(end)

        if end not in condiments and end != "burger" and end != "top bun":
            condiments.append(end)
        elif end == "burger":
            burger_count += 1

        if "cheese" in condiments:
            type = "cheeseburger"
        else:
            type = "hamburger"

    burger.append(end)
    while "cheese" in condiments:
        condiments.remove("cheese")

    if len(condiments) == 0:
        condiments_to_string = "No Condiments"
    else:
        condiments_to_string = ", ".join(condiments)

    print(f"You have created a {burger_count}-{type} with the condiments: {condiments_to_string}.")

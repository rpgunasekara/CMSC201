"""
File: red_rover.py
Author: Ravindu Gunasekara
Date: 10/02/2023
Section: 44
E-mail: rgunase1@umbc.edu
Description:
    User creates two teams and simulates
    a game of Red Rover till one team is
    left with only one player.
"""
if __name__ == "__main__":
    red_team = []
    blue_team = []
    player = ""
    option = ""

    while player != "begin the game":
        player = input("Who should we add to the Red team? ")
        red_team.append(player)

        if player != "begin the game":
            player = input("Who should we add to the Blue team? ")
            blue_team.append(player)
    red_team.remove("begin the game")

    while len(red_team) > 1 and len(blue_team) > 1:

        player = input("Who should Red team send over? ")

        while player == "display":
            red_team_string = ", ".join(red_team)
            print(f"The Red team is composed of: \n{red_team_string}")
            player = input("Who should Red team send over? ")

        if player != "display":
            while player not in red_team:
              print(f"{player} is not on the Red team.")
              player = input("Who should Red team send over? ")

              while player == "display":
                red_team_string = ", ".join(red_team)
                print(f"The Red team is composed of: \n{red_team_string}")
                player = input("Who should Red team send over? ")

            option = input("Did they make it through the line? ").lower()

            if option == "yes":
                print(f"{player} stays on the Red team.")
                option = "yes"
            elif option == "no":
                print(f"{player} changes to the Blue team.")
                blue_team.append(player)
                red_team.remove(player)
                option = "no"

        player = input("Who should Blue team send over? ")

        while player == "display":
            blue_team_string = ", ".join(blue_team)
            print(f"The Blue team is composed of: \n{blue_team_string}")
            player = input("Who should Blue team send over? ")

        if player != "display":
            while player not in blue_team:
                print(f"{player} is not on the Blue team.")
                player = input("Who should Blue team send over? ")

                while player == "display":
                    blue_team_string = ", ".join(blue_team)
                    print(f"The Blue team is composed of: \n{blue_team_string}")
                    player = input("Who should Blue team send over? ")

            option = input("Did they make it through the line? ").lower()

            if option == "yes":
                print(f"{player} stays on the Blue team.")
                option = "yes"
            elif option == "no":
                print(f"{player} changes to the Red team.")
                red_team.append(player)
                blue_team.remove(player)
                option = "no"
    if len(red_team) == 1:
        print("The Blue team has won.")
    elif len(blue_team) == 1:
        print("The Red team has won.")

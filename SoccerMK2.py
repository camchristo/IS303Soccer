# Team Memeber:
# Cameron Christopher
# 2
# 3

import random 
 
# Intro. This displays a welcome message, game info, and prompts for the player's name.
def intro():
    print("=== A5 Women's Soccer: Random Score Game ===")
    print("You pick a home team and an opponent.")
    print("The program generates random scores.")
    print("No ties allowed. You get a W or L. \n")

    name = input("Enter your player name: ").strip()
    return name

# Menu. This displays the menu and gives the player an option.
def menu():
    print("\n--- Menu ---")
    print("1) Play a game")
    print("2) Quit")
    choice = input("Enter a choice: ").strip()
    return choice

# Team Choice function

# Play Game function. Recieve both team names, genereates a random sore, no ties, returns a W or L for the Home team.
def play_game(home_team, opp_team):

    home_score = random.radint(0, 5)
    opp_score = random.radiant(0, 5)

    while home_score == opp_score:
        opp_score = random.radint(0,5)

    print(f"\nFinal Score: {home_team} {home_score} - {opp_team} {opp_team}")

    if home_score > opp_score:
        return "W"
    else:
        return "L"


# Final record function

# Main function. Calls the other functions

# I'm messing with the commit stuff and trying to push so here is a new line to mess with.
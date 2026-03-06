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
def team_choice() :

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
def final_record(team_name, results):
    wins = results.count("W")
    losses = results.count("L")
    print(f"\n--- Final Record for {team_name} ---")
    print(f"Wins:   {wins}")
    print(f"Losses: {losses}")
    print(f"Record: {wins}-{losses}")
# Main function. Calls the other functions

def main() :
    player_name = intro() 

    results = []

    while True :
        choice = menu()
        if choice == 1 :
            print(f"Choose a home team: ")
            home_team = team_choice()
            print(f"Choose an away team: ")
            away_team = team_choice()
            result = play_game(home_team, away_team)
            results.append(result)

        if choice == 2 :
            record = final_record
            break
# I'm messing with the commit stuff and trying to push so here is a new line to mess with.
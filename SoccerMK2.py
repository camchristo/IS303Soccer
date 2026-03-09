# Team Memeber: 
# Cameron Christopher
# Carter Moser
# Zackery Schaub

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
    choice = int(input("Enter a choice: ").strip())
    return choice

# Team Choice function, default list is Big 12 teams
def team_choice(team_list = None, sHomeTeam = None) :
    #Setting the default
    if team_list is None :
        team_list = ["Arizona State", "Arizona", "BYU", "Baylor", "Cincinnati", "Colorado", "Houston", "Iowa State", "Kansas", 
                 "Kansas State", "Oklahoma State", "TCU", "Texas Tech", "UCF", "Utah", "West Virginia"]
    #Display list of all teams and allow the user to choose a team using a menu. Remove the home team as an option
    if sHomeTeam == None :
        print(team_list)
        sHomeTeam = input("\nChoose a home team from this list: ")
        team_list.remove(sHomeTeam)
    #Choose opponent and only oponent if it is the second time
    print(team_list)
    sOpponent = input("\nNow choose a team to play against: ")
    print("Your opponent will be " + sOpponent)

    return sHomeTeam, sOpponent, team_list

# Play Game function. Recieve both team names, genereates a random sore, no ties, returns a W or L for the Home team.
def play_game(home_team, opp_team):

    home_score = random.randint(0, 5)
    opp_score = random.randint(0, 5)

    while home_score == opp_score:
        opp_score = random.randint(0,5)

    print(f"\nFinal Score: {home_team} {home_score} - {opp_team} {opp_score}")

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

def main():
    player_name = intro()
    results = []
    home_team = None
    team_list = None
    # Create while loop that displays menu and final recored when exited. 
    while True:
        choice = menu()
        if choice == 1:
            home_team, away_team, team_list = team_choice(team_list, home_team)
            result = play_game(home_team, away_team)
            results.append(result)
        elif choice == 2:
            final_record(home_team, results)
            break
        else:
            print("Invalid choice, please enter 1 or 2.")
#Call main function
main()
# I'm messing with the commit stuff and trying to push so here is a new line to mess with.
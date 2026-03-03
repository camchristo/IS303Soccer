# Cameron Christopher
# Soccer Teams

import random

# Enter the name of your home team:
homeTeam = input("Enter the name of your home team: ")

# Enter the number of games that <home team name> will play:
numGames = int(input(f"Enter the number of games that {homeTeam} will play: "))

wins = 0
losses = 0 

results = {
    "Won Against": [],
    "Lost Against": [],
}

# Enter the name of the away team for game <game number>:
for gameNum in range(1, numGames + 1):
    awayTeam = input(f"Enter the name of the away team for game {gameNum}: ")

    # After entering in the away team name, randomly generate scores between 0 and 3 
    # (inclusive) for the home team and the away team.

    homeScore = random.randrange(0,3)
    awayScore = random.randrange(0,3)
    while homeScore == awayScore:
        homeScore = random.randrange (0, 3)
        awayScore = random.randrange(0, 3)

    print(f"{homeTeam}'s score: {homeScore} - {awayTeam}'s score: {awayScore}")

    if homeScore > awayScore:
        wins += 1
        results["Won Against"].append(awayTeam)
    else:
        losses += 1
        results["Lost Against"].append(awayTeam)

# After playing all the games
print("\nTeams won against: ")
for team in results["Won Against"]:
    print(team)

print("\nTeams lost against:")
for team in results["Lost Against"]:
    print(team)

print(f"\nFinal season record: {wins} - {losses}")

winPct = wins / numGames
if winPct >= 0.75:
    print("Qualified for the NCAA Soccer Tournament!")
elif winPct >= 0.50:
    print("You had a good season.")
else:
    print("Your team needs to practice.")


def get_num_teams():
    while True:
        num_teams = int(input("Enter the number of teams in the tournament: "))
        if num_teams < 2:
            print("The minimum number of teams is 2, try again.")
            continue
        else:
            break
    return num_teams


def get_num_games(num_teams):
    while True:
        num_games = int(
            input("Enter the number of games played by each team: "))
        if num_games < num_teams - 1:
            print("Invalid number of games. Each team plays each other at least once in the regular season, try again.")
            continue
        else:
            break
    return num_games


def get_team_names(num_teams):
    teams = []
    for idx in range(num_teams):
        while True:
            team_name = input(f"Enter the name for team #{idx + 1}: ")
            if len(team_name.split()) > 2:
                print("Team names may have at most 2 words, try again.")
                continue
            elif len(team_name) < 2:
                print("Team names must have at least 2 characters, try again.")
            else:
                break
        teams.append(team_name)
    return teams


def get_team_score(teams, games):
    scores = []
    for team in teams:
        while True:
            team_score = int(
                input(f"Enter the number of wins Team {team} had: "))
            if team_score < 0:
                print("The minimum number of wins is 0, try again.")
                continue
            elif team_score > games:
                print(f"The maximum number of wins is {games}, try again.")
            else:
                scores.append(team_score)
                break
    return scores


def main():

    num_teams = get_num_teams()
    team_names = get_team_names(num_teams)

    num_games = get_num_games(num_teams)
    scores = get_team_score(team_names, num_games)
    teams_and_scores = list(zip(team_names, scores))
    start_low = sorted(teams_and_scores, key=lambda x: x[1])
    start_high = sorted(teams_and_scores, key=lambda x: x[1], reverse=True)

    print("Generating the games to be played in the first round of the tournament...")
    for i in range(int(len(teams)/2)):
        print(f"Home: {start_low[i][0]} VS Away: {start_high[i][0]}")


main()

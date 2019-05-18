from cfblogparser import team_extractor

from cfratinghandler import get_ratings
from cfteamrateextractor import team_rate_extractor
from colorprint import CFPrinter
from scoreboardparser import scoreboardextractor

scoreboard = scoreboardextractor(True)
team_rate = team_rate_extractor(True)


def get_rank(name):
    try:
        return str(scoreboard.index(name) + 1)
    except:
        print("ranked manually: " + name)
        if 'damascus' in name:
            return '109'
        return '1'


def get_team_rate_rank(name):
    try:
        return str(team_rate.index(name) + 1)
    except:
        return '-1'


def main():
    print('Start to get teams')
    teams = team_extractor(True)
    return
    # i = 0
    # t = {}
    # for key in teams:
    #     i += 1
    #     if i > 30:
    #         break
    #     t[key] = teams[key]
    # teams = t

    print('Starting to update ratings')
    users = get_ratings(teams.copy(), True)

    teams_data = []
    for name in teams:
        team = teams[name]
        team = sorted(team, key=lambda x: users[x]['rate'], reverse=True)
        teams_data.append(
            [get_rank(name)] + [get_team_rate_rank(name)] + [name] + [[t, users[t]['rate']] for t in team]
        )
    teams_data = sorted(teams_data, key=lambda x: int(x[0]))

    # print(teams_data)
    cfp = CFPrinter(headers=['Rank', 'CF estimated rank', 'Team Name', 'First Person', 'Second Person', 'Third Person'])
    cfp.colored_table_print(teams_data)


if __name__ == '__main__':
    main()

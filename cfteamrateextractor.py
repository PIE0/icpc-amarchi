from normalizer import normalize
from utils import get_html_soup, parse_table

LINK = 'https://codeforces.com/blog/entry/65061'
LOCAL_PATH = 'htmls/cfteamrate.html'


def team_rate_extractor(local=False):
    soup = get_html_soup(LOCAL_PATH, LINK, local)

    con = soup.find(id='pageContent').find(attrs={'class': 'content'})
    tables = con.find_all('table')

    data = []
    for t in tables:
        data.extend(parse_table(t))

    teamrating = []
    for team in data:
        if len(team) > 0:
            if len(team) >= 5:
                teamrating.append([normalize(team[-5]), team[-1]])
            else:
                teamrating.append([normalize(team[-2]), team[-1]])
    teamrating = sorted(teamrating, key=lambda x: float(x[1]), reverse=True)
    teamrating = list(zip(*teamrating))[0]
    return teamrating


if __name__ == '__main__':
    team_rate_extractor(True)

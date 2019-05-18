import requests
from bs4 import BeautifulSoup

from normalizer import normalize
from utils import get_html_soup, parse_table

LINK = 'https://codeforces.com/blog/entry/64909'
LOCAL_PATH = 'htmls/teams.html'


def team_extractor(local=False):
    soup = get_html_soup(LOCAL_PATH, LINK, local)

    con = soup.find(id='pageContent').find(attrs={'class': 'content'})
    tables = con.find_all('table')

    data = []
    for t in tables:
        data.extend(parse_table(t))

    teams = {}
    for team in data:
        if len(team) > 0:
            teams[normalize(team[-4])] = [team[-1], team[-2], team[-3]]
    return teams

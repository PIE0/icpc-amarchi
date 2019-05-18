import requests
from bs4 import BeautifulSoup

from normalizer import normalize
from utils import get_html_soup

LINK = 'https://icpc.baylor.edu/scoreboard/?static=1'
LOCAL_PATH = 'htmls/score_board.html'
REGIONS = {'Northern Eurasia': False, 'North America': False, 'Asia Pacific': False, 'Europe': False,
           'Asia East': False, 'Asia West': False, 'Africa and the Middle East': False, 'Latin America': False}


def scoreboardextractor(local=False):
    soup = get_html_soup(LOCAL_PATH, LINK, local)

    con = soup.find('table')
    rows = con.find('tbody').find_all('td')

    scoreboard = []
    for row in rows:
        if row.text and '1' not in row.text and len(row.text) > 4 and 'tries' not in row.text:
            text = row.text
            for key in REGIONS:
                if text.startswith(key) and not REGIONS[key]:
                    # print(text)
                    text = text[len(key):]
                    REGIONS[key] = True

            scoreboard.append(normalize(text))

    # for i in range(len(scoreboard)):
    #     print(i, scoreboard[i])
    return scoreboard

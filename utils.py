import os.path

import requests
from bs4 import BeautifulSoup


def prRed(skk):
    return "\033[91m{}\033[00m".format(skk)


def prGreen(skk):
    return "\033[92m{}\033[00m".format(skk)


def prYellow(skk):
    return "\033[93m{}\033[00m".format(skk)


def prPurple(skk):
    return "\033[95m{}\033[00m".format(skk)


def prCyan(skk):
    return "\033[96m{}\033[00m".format(skk)


def prBlack(skk):
    return "\033[98m{}\033[00m".format(skk)


def prLightGray(skk):
    return "\033[97m{}\033[00m".format(skk)


def name_rate(name, rate):
    return '{}({})'.format(name, rate)


def get_max_len_each_col(teams):
    max_len = [0 for _ in range(len(teams[0]))]
    for i in range(len(teams[0])):
        for team in teams:
            max_len[i] = max(max_len[i], len(team[i]) if type(team[i]) == str else len(name_rate(*team[i])))
    return list(map(lambda x: x + 1, max_len))


def download_and_save_file(url, file_name):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    with open(file_name, "w") as file:
        file.write(str(soup))


def get_html_soup(local_path, url=None, local=False):
    if local is False or os.path.isfile(local_path) is False:
        download_and_save_file(url, local_path)
    return BeautifulSoup(open(local_path), 'html.parser')


def parse_table(table):
    data = []
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])
    return data

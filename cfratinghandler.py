import ast
import json
import os

import requests
import threading

handle_link = 'https://codeforces.com/api/user.info?handles='
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
local_path = ROOT_DIR + '/users/'


def get_user_rating(handle, local=False):
    if not local:
        res = requests.get(handle_link + handle)
        res = ast.literal_eval(res.text)
    else:
        path = local_path + handle + '.json'
        try:
            file = open(path)
        except:
            print("Downloading {}'s rating...".format(handle))
            url = handle_link + handle
            res = requests.get(url, allow_redirects=True)
            open(path, 'wb').write(res.content)
            file = open(path)
        res = json.loads(file.readline())

    if res['status'] != 'OK' or 'rating' not in res['result'][0]:
        return {handle: {'rate': -1, 'max rate': -1}}
    res = res['result'][0]

    return {handle: {'rate': res['rating'], 'max rate': res['maxRating']}}


threadLock = threading.Lock()
users = {}


class RateThread(threading.Thread):
    def __init__(self, thread_id, team, local=False):
        threading.Thread.__init__(self)
        self.threadID = thread_id
        # print("getting {} team's ratings".format(self.threadID))
        self.team = team
        self.local = local

    def run(self):
        for player in self.team:
            ratings = get_user_rating(player, self.local)
            threadLock.acquire()
            users.update(ratings)
            threadLock.release()


def get_ratings(teams, local=False):
    bucket = 2
    while len(teams):
        threads = []
        cnt = 0
        names = []
        for name in teams:
            names.append(name)
            thread = RateThread(name, teams[name], local)
            thread.start()
            threads.append(thread)
            cnt += 1
            if cnt >= bucket:
                break
        for name in names:
            teams.pop(name)
        for t in threads:
            t.join()
    return users

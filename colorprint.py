from utils import prGreen, prYellow, prRed, prCyan, prPurple, prBlack, prLightGray, name_rate, get_max_len_each_col


class CFPrinter:

    def __init__(self, headers):
        self.COLORS = [[1600, prGreen], [1900, prCyan], [2100, prPurple],
                       [2400, prYellow], [2600, prRed], [3000, prBlack], [4000, prLightGray]]
        self.headers = headers
        self.max_len = []

    def colored_table_print(self, teams):  # format(teams) = [[name, [first, rate], [s, r], [th, r]], ... ]
        self.max_len = get_max_len_each_col(teams)
        for i in range(len(self.headers)):
            self.max_len[i] = max(self.max_len[i], len(self.headers[i]))

        for i in range(len(self.headers)):
            print(self.cons_len_print(i, self.headers[i], 0), end='+')
        print()
        self.print_dash_line()

        for i in range(len(teams)):
            self.print_team(teams[i])
            self.print_dash_line()

    def print_team(self, team):
        for i in range(len(team)):
            val = team[i]
            if type(val) is str:
                print(self.cons_len_print(i, val, 0), end='+')
            elif type(val) is list:
                print(self.cons_len_print(i, self.color_rate(val[1])(name_rate(*val))), end='+')
            else:
                raise
        print()

    def color_rate(self, rate):
        for i in range(len(self.COLORS)):
            if self.COLORS[i][0] > rate:
                return self.COLORS[i][1]

    def cons_len_print(self, i, x, color_overhead=10):
        space = (self.max_len[i] - len(x) + color_overhead)
        return ' ' * ((space + 1) // 2) + x + ' ' * (space // 2)

    def print_dash_line(self):
        for i in range(len(self.max_len)):
            print('-' * self.max_len[i] + '+', end='')
        print()


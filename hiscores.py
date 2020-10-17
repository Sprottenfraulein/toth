class Hiscores:
    def __init__(self, settings):
        self.hiscores = []

    def hiscores_read(self, settings):
        self.hiscores.clear()
        with open(settings.system['scoreboard']) as f:
            score_list = f.read().splitlines()

        for i in range(0, len(score_list)):
            try:
                score, sign = score_list[i].split('=')
            except ValueError:
                continue
            try:
                score = int(score)
            except ValueError:
                score = 0
            if sign == '':
                sign = ' '
            self.hiscores.append((score, sign))
        return self.hiscores

    def hiscore_add(self, hiscore):
        self.hiscores.append([hiscore, ''])
        self.hiscores = sorted(self.hiscores, key=lambda x: x[0], reverse=True)
        for i in range(len(self.hiscores) - 1, -1, -1):
            if self.hiscores[i][0] == hiscore:
                return i

    def hiscores_save(self, settings):
        with open(settings.system['scoreboard'], 'w') as f:
            for item in self.hiscores:
                score_line = str(item[0]) + '=' + item[1]
                f.write("%s\n" % score_line)
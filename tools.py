import asyncio
from datetime import datetime
import random

emojis = {
    'Bear': '🐻',
    'Wolf': '🐺',
    'Boar': '🐗',
    'Knight': '⚔️',
    'Sentinel': '🛡️',
    'Ranger': '🏹',
    'Blacksmith': '⚒️',
    'Alchemist': '⚗️',
    'Collector': '📦',
    'Master': '🐣',
    'Esquire': '🐣'
}

castle_emojis = ['🥔', '🦅', '🦌', '🐉', '🦈', '🐺', '🌑']


def find_emoji(text):
    words = text.split()
    for w in words:
        if w in emojis.keys():
            return emojis[w]
    return '👾'


async def noisy_sleep(t_max, t_min=0):
    rand_seconds = random.randrange(t_min, t_max)
    await asyncio.sleep(rand_seconds)


def bool2emoji(boolean):
    return '✔️' if boolean else '❌'


class ChatWarsCron:
    def __init__(self, server_utc):
        self.utc_delay = server_utc
        self.war_times = [7, 15, 23]

    def hours_before_war(self, h):
        assert h >= 0
        return '00 {},{},{} * * *'.format(*((24 + i + self.utc_delay - h) % 24 for i in self.war_times))

    def minutes_before_war(self, m, h=0):
        assert m >= 0 and h >= 0
        if m >= 60:
            h += m // 60
            m = m % 60
        m = 60 - m
        mstr = str(m)
        vals = [mstr.zfill(2 - len(mstr))] + [(24 + i + self.utc_delay - (h + 1)) % 24 for i in self.war_times]
        return '{} {},{},{} * * *'.format(*vals)

    def hours_after_war(self, h):
        assert h >= 0
        return '00 {},{},{} * * *'.format(*((24 + i + self.utc_delay - h) % 24 for i in self.war_times))

    def minutes_after_war(self, m, h=0):
        assert m >= 0 and h >= 0
        if m >= 60:
            h += m // 60
            m = m % 60
        mstr = str(m)
        vals = [mstr.zfill(2 - len(mstr))] + [(24 + i + self.utc_delay + h) % 24 for i in self.war_times]
        return '{} {},{},{} * * *'.format(*vals)

    def morning(self):
        return self.hours_after_war(0)

    def day(self):
        return self.hours_after_war(2)

    def evening(self):
        return self.hours_after_war(4)

    def night(self):
        return self.hours_after_war(6)

    def reset_time(self):
        return '30 {} * * *'.format(8 + self.utc_delay)

    def get_current_day_time(self, string):
        hour, minute, sec = (int(chunk) for chunk in string.split(':'))
        hour = (24 + hour - self.utc_delay + (8 - self.war_times[0])) % 24
        cw_day_hour = hour % 8
        if cw_day_hour < 2:
            return 'morning'
        elif cw_day_hour < 4:
            return 'day'
        elif cw_day_hour < 6:
            return 'evening'
        else:
            return 'night'

    def get_current_day_third(self, string):
        hour, minute, sec = (int(chunk) for chunk in string.split(':'))
        hour = (24 + hour - self.utc_delay + (8 - self.war_times[0])) % 24
        cw_day_third = hour // 8
        return cw_day_third + 1

    def get_possible_events(self, string):
        hour, minute, sec = (int(chunk) for chunk in string.split(':'))
        hour = (24 + hour - self.utc_delay + (8 - self.war_times[0])) % 24
        cw_day_hour = hour % 8
        cw_time = cw_day_hour % 2

        minute += 60 * cw_time
        return max(int((120 - minute) / 10) - 1, 0)

    def heroku_reset(self):
        time = [datetime.today().minute + 1, datetime.today().hour, datetime.today().day]
        return "{} {} {} * *".format(*time)

    def get_current_time(self):
        time = [datetime.today().hour, datetime.today().minute, datetime.today().second]
        return "{}:{}:{}".format(*time)

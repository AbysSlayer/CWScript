from enums import Items
from time import time
import sqlite3
import emoji
import re

me_compile = re.compile(r"(?:.+\n|\n)+"
                      r"(?P<castle>🌑|🐺|🥔|🦅|🦌|🐉|🦈)(?:(?P<g_emoji>[^[a-zA-Z0-9_]+))?(?:\[(?P<guild>[\w\d]{2,3})\])?(?P<name>.+) "
                      r"(?P<class>Knight|Ranger|Sentinel|Alchemist|Blacksmith|Collector|Esquire|Master) of .+\n"
                      r"\W+Level: (?P<level>\d+)\n"
                      r"\W+Atk: (?P<attack>\d+) \W+Def: (?P<defence>\d+)\n"
                      r"\W+Exp: (?P<exp_current>\d+)\/(?P<exp_needed>\d+)\n"
                      r"\W+Hp: (?P<hp>-?\d+)/(?P<hp_max>\d+)\n"
                      r"\W+Stamina: (?P<stamina_current>\d+)/(?P<stamina_max>\d+)(?: \W+(?P<time_remaining>\d+)min)?\n"
                      r"(?:\W+Mana: (?P<mana>-?\d+)/(?P<mana_max>\d+)\n)?"
                      r"\W+(?P<gold>-?\d+) (?:\W+(?P<pouch>\d+) )?\W+(?P<gem>\d+)\n\n"
                      r"\W+Equipment (?:\[-\]|\+(?P<eq_attack>\d+)\W+\+(?P<eq_defence>\d+)\W+)\n"
                      r"\W+Bag: (?P<bag_current>\d+)/\d+ /inv\n\n"
                      r"(?:\nPet:\n"
                      r"(?P<pet>.+) \((?P<pet_level>\d+) lvl\) \W+ /pet\n\n)?"
                      r"State:\n"
                      r"(?P<state>.+)\n\n"
                      r"More: /hero"
)

iter_materials = r"(?P<cant>\d+) x \W*(?P<item>[a-zA-Z ]+)\n?"


def demoji_to_DB(text: str) -> str:
    return emoji.demojize(text) if text else ''


def update_profile(msg, client):
    if me_compile.match(msg):
        match = me_compile.search(msg)
        conn = sqlite3.connect(f"db/{client}.db")
        punt = conn.cursor()
        punt.executescript('''CREATE TABLE IF NOT EXISTS Profile(last_update REAL,
castle TEXT, g_emoji TEXT, guild TEXT, name TEXT, class TEXT,
level INTEGER, attack INTEGER, defence INTEGER,
exp_current INTEGER, exp_needed INTEGER, hp INTEGER, hp_max INTEGER,
stamina_current INTEGER, stamina_max INTEGER, time_remaining INTEGER,
mana INTEGER, mana_max INTEGER, gold INTEGER, pouch INTEGER, gem INTEGER,
eq_attack INTEGER DEFAULT 0, eq_defence INTEGER DEFAULT 0, bag_current INTEGER DEFAULT 0,
pet TEXT, pet_level INTEGER, state TEXT)''')
        punt.executescript(f'''INSERT OR REPLACE INTO Profile VALUES("{time()}","{demoji_to_DB(match.group(1))}",
"{demoji_to_DB(match.group(2))}", "{match.group(3)}", "{match.group(4)}", "{match.group(5)}", "{match.group(6)}",
"{match.group(7)}", "{match.group(8)}", "{match.group(9)}", "{match.group(10)}", "{match.group(11)}",
"{match.group(12)}", "{match.group(13)}", "{match.group(14)}", "{match.group(15)}", "{match.group(16)}",
"{match.group(17)}", "{match.group(18)}", "{match.group(19)}", "{match.group(20)}", "{match.group(21)}",
"{match.group(22)}", "{match.group(23)}", "{demoji_to_DB(match.group(24))}", 
"{demoji_to_DB(match.group(25))}", "{demoji_to_DB(match.group(26))}")''')
        conn.commit()
        punt.close()
        conn.close()

        
"""
def update_profile(event):
    from regexp import pattern_me
    msg = event.raw_text
    re_me = re.search(pattern_me, msg)
    columns = ["Last_Update", "ID", "Castle", "Emoji", "Guild", "Name", "Class", "Level", "Attack", "Defence",
               "Exp_Current", "Exp_Needed", "Hp", "Hp_Max", "Stamina_Current", "Stamina_Max", "Time_Remaining",
               "Mana", "Mana_Max", "Gold", "Pouches", "Gems", "Eq_Attack", "Eq_Defence", "Bag_Current",
               "Pet", "Pet_Level", "State"]
    try:
        profiles_df = pd.read_csv("data/Profiles.csv")
    except FileNotFoundError:
        profiles_df = pd.DataFrame(columns=columns)
    data = [datetime.now(timezone.utc), event.sender_id] + \
           [i if i not in [re_me.group(j) if re_me.group(j) is not None else '' for j in [1, 2, 26]]
            else demojize(i) for i in re_me.groups()]
    profiles_df = profiles_df.append(pd.DataFrame([data], columns=columns), ignore_index=True)
    profiles_df.to_csv("data/Profiles.csv", index=False)
"""


def exp_state(client :str):
    conn = sqlite3.connect(f"db/{client}.db")
    punt = conn.cursor()
    exp_a = punt.execute(
        'SELECT exp_current, exp_needed, last_update FROM Profile ORDER BY last_update DESC LIMIT 1').fetchall()[0]
    exp_h = punt.execute(
        f'SELECT exp_current, last_update FROM Profile WHERE "{exp_a[2]}" - last_update > 3599 ORDER BY last_update DESC LIMIT 1').fetchall()
    exp_d = punt.execute(
        f'SELECT exp_current, last_update FROM Profile WHERE "{exp_a[2]}" - last_update > 86399 ORDER BY last_update DESC LIMIT 1').fetchall()
    exp_s = punt.execute(
        f'SELECT exp_current, last_update FROM Profile WHERE "{exp_a[2]}" - last_update > 604799 ORDER BY last_update DESC LIMIT 1').fetchall()
    msg = f'''----EXPERIENCIA----
Actual: {exp_a[0]}
Requerida: {exp_a[1]}
Restante: {exp_a[1] - exp_a[0]}'''
    if exp_h:
        msg += f'\nLast hour: {exp_a[0] - exp_h[0][0]}'
    if exp_d:
        msg += f'\nLast day: {exp_a[0] - exp_d[0][0]}'
        if exp_s:
            msg += f'\nLast week: {exp_a[0] - exp_s[0][0]}'
            punt.execute(
                f'DELETE FROM Profile WHERE last_update NOT IN (SELECT last_update FROM Profile WHERE last_update IN ("{exp_a[2]}", "{exp_h[0][1]}", "{exp_d[0][1]}", "{exp_s[0][1]}"))')
    else:
        punt.execute(
            f'DELETE FROM Profile WHERE last_update NOT IN (SELECT last_update FROM Profile WHERE last_update IN ("{exp_a[2]}", "{exp_h[0][1]}", "{exp_d[0][1]}"))')
    
    conn.commit()
    punt.close()
    conn.close()

    return msg


def materials_to_craft(text: str) -> str:
    respond = '<a href=http://t.me/share/url?url=/g_withdraw'
    
    for i in re.finditer(iter_materials, text):
        respond += f'%20{Items.__getattr__(i.group("item").upper().replace(" ", "_")).value}%20{i.group("cant")}'

    return respond + '>Withdraw</a> <--CLICK'

"""
JOBS 
"""


def settings(user):
    jobs_list = [
        ('auto_aren', 'aren_trigger', 'OFF')
    ]
    conn = sqlite3.connect(f"db/{user}.db")
    punt = conn.cursor()
    punt.execute('CREATE TABLE IF NOT EXISTS Jobs(name TEXT PRIMARY KEY UNIQUE, trigger TEXT, status TEXT)')
    punt.executemany('INSERT OR IGNORE INTO Jobs VALUES(?, ?, ?)', jobs_list)
    conn.commit()
    punt.close()
    conn.close()


if __name__ == "__main__":
    pass
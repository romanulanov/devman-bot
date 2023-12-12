import argparse
import requests
import telegram
import time
import os

from dotenv import load_dotenv
from time import sleep


dev_token = os.environ['DEV_TOKEN']
bot_token = os.environ['TG_BOT_TOKEN']
headers = {'Authorization': f'Token {dev_token}'}
url = 'https://dvmn.org/api/long_polling/'


def main():
    parser = argparse.ArgumentParser(
        description='''Бот для отправки результата проверки работ.''')
    parser.add_argument('chat_id',
                        default=1,
                        type=int,
                        help='Введите номер id вашего телеграма.'
                        'Узнать можно здесь: https://telegram.me/userinfobot',
                        )
    args = parser.parse_args()
    bot = telegram.Bot(token=bot_token)
    timestamp = int(time.time())
    chat_id = args.chat_id
    while True:
        try:
            response = requests.get(url,
                                    headers=headers,
                                    params={"timestamp": timestamp},
                                    timeout=90,)
            if response.json()["status"] == "timeout":
                timestamp = response.json()["timestamp_to_request"]
            else:
                timestamp = response.json()["new_attempts"][0]["timestamp"]
                is_negative = response.json()["new_attempts"][0]["is_negative"]
                lesson_title = (
                    response.json()["new_attempts"][0]["lesson_title"]
                )
                lesson_url = response.json()["new_attempts"][0]["lesson_url"]

            if is_negative:
                bot.send_message(
                    text=f'У вас проверили работу «{lesson_title}»\n\nК '
                         f'сожалению в работе нашлись ошибки. '
                         f'Ссылка на урок:{lesson_url}',
                    chat_id=chat_id,
                    )
            else:
                bot.send_message(
                    text=f'У вас проверили работу «{lesson_title}»\n\nП'
                         f'реподаватель одобрил работу, можно приступать'
                         f'к следующему уроку! Ссылка на урок:{lesson_url}',
                    chat_id=chat_id,)
            sleep(5)
        except requests.exceptions.ConnectionError:
            print("Нет интернета. Жду 10 секунд")
            sleep(10)
        except requests.exceptions.ReadTimeout:
            print("Не было получено новых работ. Жду 10 секунд")
            sleep(10)


if __name__ == "__main__":
    load_dotenv()
    main()

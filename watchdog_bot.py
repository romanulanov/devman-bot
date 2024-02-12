import argparse
import logging
import os
import subprocess
import time
import telegram
import traceback

from dotenv import load_dotenv


class TelegramLogsHandler(logging.Handler):
    def __init__(self, tg_bot, chat_id):
        super().__init__()
        self.chat_id = chat_id
        self.tg_bot = tg_bot

    def emit(self, record):
        log_entry = self.format(record)
        self.tg_bot.send_message(chat_id=self.chat_id, text=log_entry)


def start_first_bot(bot, chat_id):
    try:
        subprocess.run(["python", "devbot.py", str(chat_id)])

    except Exception as e:
        error_message = f"Бот упал с ошибкой: {e}\n{traceback.format_exc()}"
        logging.error(error_message)
        bot.send_message(chat_id=chat_id, text=error_message)


def main():
    load_dotenv()
    parser = argparse.ArgumentParser(
        description='''Бот для контроля основного бота.''')
    parser.add_argument('chat_id',
                        default=1,
                        type=int,
                        help='Введите номер id вашего телеграма.'
                        'Узнать можно здесь: https://telegram.me/userinfobot',
                        )
    args = parser.parse_args()
    watchdogbot_token = os.environ['WATCHDOG_BOT_TOKEN']
    bot = telegram.Bot(token=watchdogbot_token)
    chat_id = args.chat_id
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    while True:
        bot.send_message(chat_id=chat_id, text="Бот запущен...")
        start_first_bot(bot, chat_id)
        time.sleep(10)


if __name__ == "__main__":
    main()

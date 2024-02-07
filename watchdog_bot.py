import subprocess
import time
import logging
import telegram
import traceback

bot = telegram.Bot(token="1278285529:AAECtvGkXDaVHtK-hwYEBx_zV9fwCE_Lddc")
chat_id = 138419352


class TelegramLogsHandler(logging.Handler):
    
    def __init__(self, tg_bot, chat_id):
        super().__init__()
        self.chat_id = chat_id
        self.tg_bot = tg_bot

    def emit(self, record):
        log_entry = self.format(record)
        self.tg_bot.send_message(chat_id=self.chat_id, text=log_entry)

def start_first_bot():
    try:
        subprocess.run(["python", "devbot.py", "138419352"])
        
    except Exception as e:
        error_message = f"Error starting the first bot: {e}\n{traceback.format_exc()}"
        logging.error(error_message)
        bot.send_message(chat_id=chat_id, text="Бот упал с ошибкой")
        bot.send_message(chat_id=chat_id, text=error_message)

def main():
    logging.basicConfig(filename='watchdog_bot.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    while True:
        bot.send_message(chat_id=chat_id, text="Бот запущен...")
        start_first_bot()
        print("First bot stopped. Restarting in 10 seconds...")
        time.sleep(10)

if __name__ == "__main__":
    main()
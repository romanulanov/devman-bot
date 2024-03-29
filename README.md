# DVMN Telegram Bot

## Описание

Этот бот предназначен для отправки результата проверки работ с сайта DVMN.org в ваш чат в Telegram. Также к нему прилагается бот, следящий за работой первого и в случае возникновения ошибок, информирующего об этом в телеграме.

## Установка и использование

### Предварительные шаги

1. Убедитесь, что у вас установлен Python (рекомендуется Python 3).
2. Зарегистрируйте бота в Telegram и получите токен.
3. Получите токен разработчика DVMN.org.

### Установка зависимостей

Используйте `pip` (или `pip3`, если есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Инструкция по настройке рабочего окружения
Создайте файл .env и добавьте следующие переменные окружения:

    DEV_TOKEN=ваш_токен_разработчика_DVMN
    TG_BOT_TOKEN=ваш_токен_Telegram_бота

### Пример запуска проекта

Если хотите получать уведомления о проверке работ в телеграм укажите ваш chat_id в окружении:

    python devbot.py 1

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).
# Telegram Voice Transcriber Bot

Бот для Telegram, который расшифровывает голосовые сообщения с помощью Google Speech Recognition API.

## Как запустить

1. Установи зависимости:
```
pip install -r requirements.txt
```

2. Экспортируй переменную окружения:
```
export BOT_TOKEN=your_bot_token_here
```

3. Запусти бота:
```
python bot.py
```

## Развёртывание на Render

1. Зарегистрируйся на https://render.com.
2. Залей проект в GitHub.
3. Создай новый Web Service, подключи репозиторий.
4. Укажи `Start command`:
```
python bot.py
```
5. В секции "Environment" добавь переменную `BOT_TOKEN` с токеном от BotFather.

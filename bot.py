import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import speech_recognition as sr
from pydub import AudioSegment

BOT_TOKEN = os.getenv("BOT_TOKEN")  # токен из переменной окружения

async def voice_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    voice = update.message.voice
    file = await context.bot.get_file(voice.file_id)
    file_path = f"voice.ogg"
    await file.download_to_drive(file_path)

    # Конвертация ogg -> wav
    audio = AudioSegment.from_ogg(file_path)
    wav_path = "voice.wav"
    audio.export(wav_path, format="wav")

    # Распознавание речи
    recognizer = sr.Recognizer()
    with sr.AudioFile(wav_path) as source:
        audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data, language="ru-RU")
            await update.message.reply_text(f"Вы сказали: {text}")
        except sr.UnknownValueError:
            await update.message.reply_text("Не удалось распознать речь.")
        except sr.RequestError:
            await update.message.reply_text("Ошибка соединения с сервисом распознавания.")

    os.remove(file_path)
    os.remove(wav_path)

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.VOICE, voice_handler))
    print("Бот запущен.")
    app.run_polling()

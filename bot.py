import logging
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

def start_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Привет! Я телеграм-бот для преобразования ФИО из кириллицы в латиницу. Отправьте мне ФИО на кириллице, и я верну ФИО на латинице.")

def convert_to_latin(fio: str) -> str:
    translit_rules = {
        'А': 'A', 'Б': 'B', 'В': 'V',
        'Г': 'G', 'Д': 'D', 'Е': 'E',
        'Ё': 'YO', 'Ж': 'ZH', 'З': 'Z',
        'И': 'I', 'Й': 'Y', 'К': 'K',
        'Л': 'L', 'М': 'M', 'Н': 'N',
        'О': 'O', 'П': 'P', 'Р': 'R',
        'С': 'S', 'Т': 'T', 'У': 'U',
        'Ф': 'F', 'Х': 'KH', 'Ц': 'TS',
        'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH',
        'Ъ': '', 'Ы': 'I', 'Ь': '',
        'Э': 'E', 'Ю': 'YU', 'Я': 'YA',
        'а': 'a', 'б': 'b', 'в': 'v',
        'г': 'g', 'д': 'd', 'е': 'e',
        'ё': 'yo', 'ж': 'zh', 'з': 'z',
        'и': 'i', 'й': 'y', 'к': 'k',
        'л': 'l', 'м': 'm', 'н': 'n',
        'о': 'o', 'п': 'p', 'р': 'r',
        'с': 's', 'т': 't', 'у': 'u',
        'ф': 'f', 'х': 'kh', 'ц': 'ts',
        'ч': 'ch', 'ш': 'sh', 'щ': 'shch',
        'ъ': '', 'ы': 'i', 'ь': '',
        'э': 'e', 'ю': 'yu', 'я': 'ya'
    }
    
    converted_fio = ''
    for char in fio:
        if char in translit_rules:
            converted_fio += translit_rules[char]
        else:
            converted_fio += char
    
    return converted_fio

def handle_message(update: Update, context: CallbackContext) -> None:
    fio = update.message.text
    if not fio:
        update.message.reply_text("Пожалуйста, отправьте мне ФИО на кириллице.")
    else:
        converted_fio = convert_to_latin(fio)
        update.message.reply_text(converted_fio)

def main() -> None:
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filename='/home/aleksandr/Aleksandr/New-Telegram/bot.log')
    bot_token = '6002730833:AAHfEIt0JZmILcshHbwiy91HPvEPzR2u_cA'
    bot = Bot(token=bot_token)
    updater = Updater(bot=bot)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

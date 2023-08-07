import logging
     from telegram import Update, Bot
     from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
 def start_command(update: Update, context: CallbackContext) -> None:
         update.message.reply_text("Привет! Я телеграм-бот для преобразования ФИО из кириллицы в латиницу. Отправьте мне ФИО на кириллице, и я верну ФИО на латинице.")
      def convert_fio(update: Update, context: CallbackContext) -> None:
         fio = update.message.text
         converted_fio = convert_to_latin(fio)
         update.message.reply_text(converted_fio)
 def handle_message(update: Update, context: CallbackContext) -> None:
         fio = update.message.text
         if not fio:
             update.message.reply_text("Пожалуйста, отправьте мне ФИО на кириллице.")
         else:
             convert_fio(update, context)
      logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', filename='/home/aleksandr/Aleksandr/New-Telegram/bot.log')
bot = Bot(token='6002730833:AAHfEIt0JZmILcshHbwiy91HPvEPzR2u_cA')
 updater = Updater(bot=bot)
dispatcher = updater.dispatcher
     dispatcher.add_handler(CommandHandler("start", start_command))
     dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), handle_message))

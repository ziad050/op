from telegram.ext import Updater
updater = Updater(token='1654115598:AAFHkI8qvKiilWDmRHTRqRY8ANJPSBJLC1w', use_context=True)
dispatcher = updater.dispatcher
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="you are stupid you didn't understand any thing")

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)




updater.start_polling(clean=True)
updater.idle()
print("wooorking")
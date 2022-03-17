import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from config import BOT_API_KEY


# function to handle the /start command
def start(update, context):
    update.message.reply_text('Hi! Start command received\n/Start: START BOT bot\n/help: For HELP\n/update: UPDATE')


# function to handle the /help command
def help(update, context):
    update.message.reply_text('Help command received')


# function to handle errors occurred in dispatcher
def error(update, context):
    """Log Errors caused by Updates."""
    logging.warning('Update "%s" caused error "%s"', update, context.error)


def text(update, context):
    text_received = update.message.text
    update.message.reply_text(f'did you say that "{text_received}"')


def handler():

    updater = Updater(BOT_API_KEY, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))

    dispatcher.add_handler(MessageHandler(Filters.text, text))

    dispatcher.add_error_handler(error)

    # run til infinity
    updater.start_polling()

    updater.idle()

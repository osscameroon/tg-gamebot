import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from config import BOT_API_KEY


# function to handle the /start command
def start(update, context):
    keyboard = [[InlineKeyboardButton("/Start"),
            InlineKeyboardButton("/Help"),
            InlineKeyboardButton("/Game"),
            ],

            [InlineKeyboardButton("/Whoami"),
            InlineKeyboardButton("/update"),
            InlineKeyboardButton("/sys"),
            ]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Please choose:', reply_markup=reply_markup)

    # update.message.reply_text("Hi")
    # help = {
    #     "Start" : "Start Bot",
    #     "Help" : "Get Help",
    #     "update" : "Get Update",
    #     "game" : "Play Game",
    #     "whoami" : "Get you username",
    #     "sys" : "get your system",
        
    # }
    # reply = ""
    # for key, value in help.items():
    #     reply = reply + "/{key} : value"
    # update.message.reply_text(reply)


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

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram.update import Update
from config import BOT_API_KEY
import platform

# function to greet the user
from models.quiz import test_poll


# function to handle the /start command
def start(update: Update, context: CallbackContext):
    update.message.reply_text('Hi\n'
                              'To start a game, select game type.')


# function to handle the /help command
def help(update: Update, context: CallbackContext):
    commands = {
        'about': 'Displays information about the bot',
        'help': 'displays help comands',
        'games': 'displays a list of available games',
        'leaderboard': 'displays the leaderboard',
        'stop': 'stops game',
        'start': 'Start a game',
        'schedule' : 'schedules games',
        'pause': 'pauses ongoing game',
        'resume': 'resumes paused game',
    }
    reply = 'The following commands are available:\n'
    for option in commands:
        reply += f'/{option} : {commands[option]}\n\n'
    update.message.reply_text(reply)


# function to handle errors occurred in dispatcher
def error(update: Update, context: CallbackContext):
    """Log Errors caused by Updates."""
    logging.warning('Update "%s" caused error "%s"', update, context.error)


def text(update: Update, context: CallbackContext):
    text_received = update.message.text
    update


###############################################################################
# Test commands
def poll(update, context):

    update.message


###############################################################################


def handler():
    updater = Updater(BOT_API_KEY, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(CommandHandler("play_game", play_game))
    dispatcher.add_handler(CommandHandler("whoami", whoami))
    dispatcher.add_handler(CommandHandler("poll", poll))

    dispatcher.add_handler(MessageHandler(Filters.text, text))

    dispatcher.add_error_handler(error)

    # run til infinity
    updater.start_polling()

    updater.idle()

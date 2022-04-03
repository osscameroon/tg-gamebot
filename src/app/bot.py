import logging

from telegram.ext import \
    Updater, \
    CommandHandler, \
    MessageHandler, \
    Filters, \
    CallbackContext
from telegram.update import Update

from src.app.config import BOT_API_KEY
import platform


# function to greet the user
def hello(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello {}'.format(update.message.from_user.first_name))


# function to handle the /start command
def start(update: Update, context: CallbackContext):
    update.message.reply_text('Hi! This is a bot to greet you.\n'
                              'Try sending me a message')


# function to show the information of the computer running this bot
def host(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'Hostname: {platform.node()}\n'
                              f'Platform: {platform.platform()}\n'
                              f'System: {platform.system()}\n'
                              f'Release: {platform.release()}\n'
                              f'Version: {platform.version()}\n'
                              f'Machine: {platform.machine()}')


def play_game(update: Update, context: CallbackContext):
    update.message.reply_text('Select the game you want to play:')


def whoami(update: Update, context: CallbackContext):
    update.message.reply_text(f'You are {update.message.from_user.username}')


# function to handle the /help command
def help(update: Update, context: CallbackContext):
    commands = {
        'start': 'Start the bot',
        'help': 'Get help on how to use the bot',
        'platform': 'Get the platform information of the bot',
        'play_game': 'Play a game'
    }
    reply = 'The following commands are available:\n'
    for command in commands:
        reply += f'/{command} : {commands[command]}\n\n'
    update.message.reply_text(reply)


# function to handle errors occurred in dispatcher
def error(update: Update, context: CallbackContext):
    """Log Errors caused by Updates."""
    logging.warning('Update "%s" caused error "%s"', update, context.error)


def text(update: Update, context: CallbackContext):
    text_received = update.message.text
    update.message.reply_text(f'You said: {text_received}')


def handler():
    updater = Updater(BOT_API_KEY, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(CommandHandler("host", host))
    dispatcher.add_handler(CommandHandler("play_game", play_game))
    dispatcher.add_handler(CommandHandler("whoami", whoami))

    dispatcher.add_handler(MessageHandler(Filters.text, text))

    dispatcher.add_error_handler(error)

    # run til infinity
    updater.start_polling()

    updater.idle()

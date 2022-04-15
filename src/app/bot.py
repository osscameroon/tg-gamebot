import logging
import platform

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
from telegram.update import Update

from constants import BOT_API_KEY
# function to greet the user
from data.quiz import test_poll


# function to handle the /start command
from menus import main_menu_keyboard


def oss_bot_start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hi\nTo start a game, select game type.")


def oss_bot_about(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(f'This is a bot for the {platform.system()} platform')


# show available games
def oss_bot_games(update: Update, context: CallbackContext):
    update.message.reply_text("Games are not implemented yet")


# Display leaderboard
def oss_bot_leaderboard(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Leaderboard is not implemented yet")


# stop ongoing game
def oss_bot_stop(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Stopping game")
    test_poll.stop()


# schedule a game
def oss_bot_schedule(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Scheduling games")


# pause game
def oss_bot_pause(update: Update, context: CallbackContext) -> None:
    test_poll.pause()


# resume game
def oss_bot_resume(update: Update, context: CallbackContext) -> None:
    test_poll.resume()


def oss_bot_menu(update: Update, context: CallbackContext) -> None:
    reply_markup = main_menu_keyboard
    update.message.reply_text('Select Menu', reply_markup=reply_markup)


# function to handle the /help command
def help_cmd(update: Update, context: CallbackContext):
    commands = {
        'about': 'Displays information about the bot',
        'help': 'displays help comands',
        'games': 'displays a list of available games',
        'leaderboard': 'displays the leaderboard',
        'stop': 'stops game',
        'start': 'Start a game',
        'schedule': 'schedules games',
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
    update.message.reply_text(f'You said: {text_received}')


def handler():
    updater = Updater(BOT_API_KEY, use_context=True)
    dispatcher = updater.dispatcher
    # create handlers for all functions above
    dispatcher.add_handler(CommandHandler('menu', menu))
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help_cmd))
    dispatcher.add_handler(CommandHandler('about', about))
    dispatcher.add_handler(CommandHandler('games', games))
    dispatcher.add_handler(CommandHandler('leaderboard', leaderboard))
    dispatcher.add_handler(CommandHandler('stop', stop))
    dispatcher.add_handler(CommandHandler('schedule', schedule))
    dispatcher.add_handler(CommandHandler('pause', pause))
    dispatcher.add_handler(CommandHandler('resume', resume))
    dispatcher.add_handler(CommandHandler('send_keyboard', send_keyboard))
    dispatcher.add_handler(MessageHandler(Filters.text, text))
    dispatcher.add_error_handler(error)
    # run til infinity
    updater.start_polling()

    updater.idle()

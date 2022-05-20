import logging
import platform

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
from telegram.update import Update

from constants import BOT_API_KEY, BOT_NAME
# function to greet the user
from data.quiz import test_poll

# function to handle the /start command
from menus import main_menu_keyboard, start_inline_keyboard, game_inline_keyboard, back_inline_keyboard


def start_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    logging.info('Starting game')
    update.message.reply_text("Hi\nTo start a game, select game type.")


def about_command(update: Update, context: CallbackContext) -> None:
    """Display information about the bot."""
    update.message.reply_text(
        f'BOT NAME: {BOT_NAME} \n BOT VERSION: 1.0 \n BOT PLATFORM: {platform.system()} is a quizbot designed to make the community interactive 😂 have fun while developing your skills')


def list_games_command(update: Update, context: CallbackContext):
    """Display a list of available games."""
    update.message.reply_text("Games are not implemented yet")


# Display leaderboard
def leaderboard_command(update: Update, context: CallbackContext) -> None:
    """Shows the leaderboard."""
    update.message.reply_text("Leaderboard is not implemented yet")


def stop_command(update: Update, context: CallbackContext) -> None:
    """Stop the ongoing game."""
    update.message.reply_text("Stopping game")
    test_poll.stop()


def schedule_games_command(update: Update, context: CallbackContext) -> None:
    """Schedules a game."""
    update.message.reply_text("Scheduling games")


def pause_command(update: Update, context: CallbackContext) -> None:
    """Pause the ongoing game."""
    test_poll.pause()


def resume_command(update: Update, context: CallbackContext) -> None:
    """Resume the paused game."""
    test_poll.resume()


def menu_command(update: Update, context: CallbackContext) -> None:
    """Shows the main menu."""
    reply_markup = main_menu_keyboard
    update.message.reply_text('Select Menu', reply_markup=reply_markup)


def help_command(update: Update, context: CallbackContext):
    """Send a message when the command /help is issued."""
    commands = {
        'About': 'Display information about the bot \nPress',
        'Help': 'display help comands \nPress',
        'Games': 'display a list of available games \nPress',
        'Leaderboard': 'display the leaderboard \nPress',
        'Schedule': 'schedules games \nPress',
        'Start': 'Start a game \nPress',
        'Pause': 'pause ongoing game \nPress',
        'Resume': 'resume paused game \nPress',
        'Stop': 'stop game \nPress',
    }
    reply = 'OSSCAMEROON QUIZBOT HELP!:\n=====================\n'
    # format the help commands as type buttons
    for command in commands:
        reply += f'To {commands[command]} : \t /{command.lower()}\n\n'
    update.message.reply_text(reply)


def oss_bot_error(update: Update, context: CallbackContext):
    """Log Errors caused by Updates."""
    logging.warning('Update "%s" caused error "%s"', update, context.error)


def oss_bot_text(update: Update, context: CallbackContext):
    """Handle text messages."""
    text_received = update.message.text
    update.message.reply_text(f'You said: {text_received}')


def menu_actions(update: Update, context: CallbackContext) -> None:
    """Handle callback queries from the main menu."""
    print("menu_actions")
    query = update.callback_query
    query.answer()

    query.edit_message_text(text='Start Menu', reply_markup=InlineKeyboardMarkup(
        [[InlineKeyboardButton(text='START', callback_data="/start")],
         [InlineKeyboardButton(text='back', callback_data="main_menu")], ]
    ))


def all_callback(update: Update, message_text: str, reply_markup: InlineKeyboardMarkup) -> None:
    query = update.callback_query
    query.answer()
    query.edit_message_text(text=message_text, reply_markup=reply_markup)


def game_callback(update: Update, context: CallbackContext) -> None:
    all_callback(update, "Game Menu", game_inline_keyboard)


def start_callback(update: Update, context: CallbackContext) -> None:
    all_callback(update, "Start Menu", start_inline_keyboard)


def help_callback(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    query.edit_message_text(
        text=f'How to play this game:\n\n'
             f'Open this link: https://github.com/osscameroon/tg-gamebot ',
        reply_markup=back_inline_keyboard
    )


def menu_test(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(text="Menu Test", reply_markup=start_inline_keyboard)


def handler():
    """Entry point for the bot."""
    updater = Updater(BOT_API_KEY, use_context=True)
    dispatcher = updater.dispatcher

    # create handlers for all functions above
    dispatcher.add_handler(CommandHandler('start', start_command))
    dispatcher.add_handler(CommandHandler('about', about_command))
    dispatcher.add_handler(CommandHandler('games', list_games_command))
    dispatcher.add_handler(CommandHandler('leaderboard', leaderboard_command))
    dispatcher.add_handler(CommandHandler('schedule', schedule_games_command))
    dispatcher.add_handler(CommandHandler('stop', stop_command))
    dispatcher.add_handler(CommandHandler('pause', pause_command))
    dispatcher.add_handler(CommandHandler('resume', resume_command))
    dispatcher.add_handler(CommandHandler('help', help_command))
    dispatcher.add_handler(CommandHandler('menu', menu_command))

    # menu test
    dispatcher.add_handler(CommandHandler('menut', menu_test))

    # callback query handlers
    dispatcher.add_handler(CallbackQueryHandler(menu_actions, pattern='menu_actions'))
    dispatcher.add_handler(CallbackQueryHandler(game_callback, pattern='game_callback'))
    dispatcher.add_handler(CallbackQueryHandler(start_callback, pattern='start_callback'))
    dispatcher.add_handler(CallbackQueryHandler(help_callback, pattern='help_callback'))

    dispatcher.add_handler(MessageHandler(Filters.text, oss_bot_text))
    dispatcher.add_error_handler(oss_bot_error)

    # run til infinity
    updater.start_polling()

    updater.idle()

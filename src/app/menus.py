from telegram import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup


main_menu_keyboard = ReplyKeyboardMarkup(
    [
        [  # Start 🏁
            KeyboardButton(text='Start\n🏁', callback_data='start_menu'),
            KeyboardButton(text='Stop\n🛑', callback_data='/stop'),
            KeyboardButton(text='Pause\n⏸️', callback_data='/pause'),
        ],
        [
            KeyboardButton(text='Resume\n🎬', callback_data='/resume'),
            KeyboardButton(text='Games\n🎮', callback_data='/games'),
            KeyboardButton(text='Leaderboard\n🏆', callback_data='/leaderboard'),
        ],
        [
            KeyboardButton(text='About\n🆘️', callback_data='/about'),
            KeyboardButton(text='Help\nℹ', callback_data='/help'),
        ]
    ]
)

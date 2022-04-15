from telegram import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup


main_menu_keyboard = ReplyKeyboardMarkup(
    [
        [  # Start 🏁
            KeyboardButton(text='Start 🏁', callback_data='start_menu'),
            KeyboardButton(text='Stop 🛑', callback_data='/stop'),
            KeyboardButton(text='Pause ⏸️', callback_data='/pause'),
        ],
        [
            KeyboardButton(text='Resume 🎬', callback_data='/resume'),
            KeyboardButton(text='Games 🎮', callback_data='/games'),
            KeyboardButton(text='Leaderboard 🏆', callback_data='/leaderboard'),
        ],
        [
            KeyboardButton(text='About 🆘️', callback_data='/about'),
            KeyboardButton(text='Help ℹ', callback_data='/help'),
        ]
    ]
)

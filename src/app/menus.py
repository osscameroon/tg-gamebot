from telegram import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup

games = [
    {
        'name': "Example Game 1",
        'icon': "😐"
    },{
        'name': "Example Game 1",
        'icon': "🤔"
    },{
        'name': "Example Game 1",
        'icon': "😯"
    },
]

main_menu_keyboard = ReplyKeyboardMarkup(
    [
        [  # Start 🏁
            KeyboardButton(text='Start\n🏁'),
            KeyboardButton(text='Stop\n🛑'),
            KeyboardButton(text='Pause\n⏸️'),
        ],
        [
            KeyboardButton(text='Resume\n🎬'),
            KeyboardButton(text='Games\n🎮'),
            KeyboardButton(text='Leaderboard\n🏆'),
        ],
        [
            KeyboardButton(text='About\n🆘️'),
            KeyboardButton(text='Help\nℹ'),
            KeyboardButton(text='Exit \n❌'),
        ]
    ]
)


start_inline_keyboard = InlineKeyboardMarkup(
    [
        # create inline keyboard buttons with games list using list comprehension
        [
            InlineKeyboardButton(text=game['icon'] + ' ' + game['name'], callback_data='game_callback')
        ] for game in games
    ]
)

game_inline_keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text='▶️\tLaunch', callback_data='launch_callback'),
        ],
        [
            InlineKeyboardButton(text='📘\tHow to play', callback_data='help_callback'),
        ],
        [
            InlineKeyboardButton(text='🔙\tBack', callback_data='start_callback'),
        ]
    ]
)

back_inline_keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text='🔙 Back', callback_data='start_callback'),
        ]
    ]
)


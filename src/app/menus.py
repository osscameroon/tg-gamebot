from telegram import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton, ReplyKeyboardMarkup

games = [
    {
        'name': "Example Game 1",
        'icon': "š"
    },{
        'name': "Example Game 1",
        'icon': "š¤"
    },{
        'name': "Example Game 1",
        'icon': "šÆ"
    },
]

main_menu_keyboard = ReplyKeyboardMarkup(
    [
        [  # Start š
            KeyboardButton(text='Start\nš'),
            KeyboardButton(text='Stop\nš'),
            KeyboardButton(text='Pause\nāøļø'),
        ],
        [
            KeyboardButton(text='Resume\nš¬'),
            KeyboardButton(text='Games\nš®'),
            KeyboardButton(text='Leaderboard\nš'),
        ],
        [
            KeyboardButton(text='About\nšļø'),
            KeyboardButton(text='Help\nā¹'),
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
            InlineKeyboardButton(text='ā¶ļø\tLaunch', callback_data='launch_callback'),
        ],
        [
            InlineKeyboardButton(text='š\tHow to play', callback_data='help_callback'),
        ],
        [
            InlineKeyboardButton(text='š\tBack', callback_data='start_callback'),
        ]
    ]
)

back_inline_keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text='š Back', callback_data='start_callback'),
        ]
    ]
)


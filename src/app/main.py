########################################################################################################################
#
# This project is developed by OSS Cameroon under the mentorship of Ehlmn Boris.
# Authors: Andrew Tatah, Elroy Kanye
# Date: 11/03/2022
# Version: 1.0
# Name: OSS CAMEROON GAME BOT
# Description: This is the main file of the project.
#              This application acts as the data for the telegram bot used for OSS Cameroon games.
#              It communicates with the Telegram servers to perform games, quizzes and challenges in the designated
#              group.
#
########################################################################################################################
from bot import handler


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('OSSCAMEROON')
    print("Running...")
    handler()
    print("Stopped!")

########################################################################################################################
#
# END OF FILE
#
########################################################################################################################

import json


def linkStorage():
    """
    function to link games.son to the quiz object
    """
    with open('src/app/data/db/games.json') as json_file:
        games = json.load(json_file)
    return games

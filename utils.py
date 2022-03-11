import csv, os


def get_api_key(k):
    api_key = ""
    try: # Try to get the API KEY from github secrets
        api_key = os.environ["TELEGRAM_BOT_API_KEY"]
    except KeyError: # If not found, rely on the local storage
        with open("../secrets/API.csv", mode='r') as file:
            for line in csv.reader(file):
                if k == line[0]:
                    api_key = line[1]

    return api_key
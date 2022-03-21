import csv
import os


def get_api_key(k):
    """
    Retrieves the API key from GitHub secret or locally stored file.
    :param k: The identifier of the key to retrieve.
    :return: The API key.
    """
    api_key = ""
    try:  # Try to get the API KEY from GitHub secrets
        api_key = os.environ["TELEGRAM_BOT_API_KEY"]
    except KeyError:  # If not found, rely on the local storage
        with open("/home/andy/.secretes/API.csv", mode='r') as file:
            for line in csv.reader(file):
                if k == line[0]:
                    api_key = line[1]

    return api_key

import csv
import os

andrew = "/home/andy/.secretes/API.csv"
vince = "../secrets/API.csv"


def get_api_key():
    """
    Retrieves the API key from GitHub secret or locally stored file.
    :return: The API key.
    """
    api_key = ""
    try:  # Try to get the API KEY from GitHub secrets
        api_key = os.environ["TELEGRAM_BOT_API_KEY"]
    except KeyError:  # If not found, rely on the local storage
        if os.path.isfile(andrew):
            api_key = read_api(andrew)
        elif os.path.isfile(vince):
            api_key = read_api(vince)
        else:
            print("No API key found.")
            exit(1)  # Exit if no API key is found
    return api_key


def read_api(file_path):
    k = "TELEGRAM"
    with open(file_path, mode='r') as file:
        for line in csv.reader(file):
            if line[0] == k:
                return line[1]

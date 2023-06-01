import requests


def get():
    response = requests.get(
        'https://sportsapicdn-desktop.betking.com/api/feeds/prematch/en/4/5314846/0/0'
    ).json()
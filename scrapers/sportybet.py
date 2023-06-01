import requests


def get():
    response = requests.get(
        'https://www.sportybet.com/api/ng/factsCenter/pcUpcomingEvents?sportId=sr%3Asport%3A117&marketId=186%2C18&pageSize=100&pageNum=1&option=1&_t=1685431333927'
    ).json()
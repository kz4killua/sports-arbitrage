import requests


def get():
    response = requests.get(
        'https://sports.bet9ja.com/desktop/feapi/PalimpsestAjax/GetEventsInGroupV2?GROUPID=3488303&DISP=0&GROUPMARKETID=65&matches=false&v_cache_version=1.232.2.135'
    ).json()
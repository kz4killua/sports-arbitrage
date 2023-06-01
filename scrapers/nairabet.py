import requests


def get():

    # Fetch data
    response = requests.get(
        'https://sports-api.nairabet.com/v2/events?country=NG&locale=en&group=g3&platform=desktop&sportId=MMA&competitionId=UFC&limit=10'
    ).json()

    output = []
    for category in response['data']['categories']:
        for competition in category['competitions']:
            for event in competition['events']:
                for market in event['markets']:
                    outcomes = [
                        {
                            'name': outcome['name'],
                            'value': float(outcome['value']),
                        }
                        for outcome in market['outcomes']
                    ]
                    output.append(outcomes)

    return output
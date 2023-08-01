import requests
from .. import helpers


def fetch_team_standings(series):
    url = f'http://localhost:2020/teamPoints/{series}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()['seriesData']['teamPoints']

        return helpers.classEntries(data)
    else:
        return (response.status_code, None)

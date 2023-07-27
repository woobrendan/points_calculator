import requests
from .. import helpers


def fetch_team_standings(series):
    url = f'http://localhost:2020/teamPoints/{series}'
    response = requests.get(url)

    if response.status_code == 200:
        manuf_val = 'manufPointsList' if series == 'gtwca' or series == 'pgt4a' else 'manufPoints'

        data = response.json()['teamsBySeries']['teamPoints']

        return helpers.classEntries(data)
    else:
        return (response.status_code, None)

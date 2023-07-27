from ast import Gt
import requests
from ..helpers import classEntries


def fetch_team_standings(series):
    url = f'http://localhost:2020/teamPoints/{series}'
    response = requests.get(url)

    GT3_GT4 = True if series == 'gtwca' or series == 'pgt4a' else False

    if response.status_code == 200:
        manuf_val = 'manufPointsList' if GT3_GT4 else 'manufPoints'

        data = response.json()['teamsBySeries'][manuf_val]

        if GT3_GT4:
            pass
        else:
            return classEntries(data)
    else:
        return (response.status_code, None)

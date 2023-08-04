from ast import Gt
import requests
from ..helpers import classEntries
from .manuf_points import convert_manufList_to_dict


def fetch_manuf_standings(series):
    url = f'http://localhost:2020/api/manufPoints/{series}'
    response = requests.get(url)

    GT3_GT4 = True if series == 'gtwca' or series == 'pgt4a' else False

    if response.status_code == 200:
        manuf_val = 'manufPointsList' if GT3_GT4 else 'manufPoints'
        data = response.json()[manuf_val]

        if GT3_GT4:
            return convert_manufList_to_dict(data)
        else:
            return classEntries(data)
    else:
        return (response.status_code, None)

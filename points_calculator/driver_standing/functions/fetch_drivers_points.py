import requests
from ..functions.driver_funcs import sortDriverPoints


def fetch_drivers(series):
    url = f'http://localhost:2020/api/drivers/{series}'
    response = requests.get(url)

    if response.status_code == 201:
        data = response.json()['seriesDrivers']

        entries_by_class = sortDriverPoints(data)

        return entries_by_class

    else:
        return (response.status_code, None)


print('drivers', fetch_drivers('gtwca'))

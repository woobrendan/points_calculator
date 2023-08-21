import requests
from ..functions.driver_funcs import sortDriverPoints


# # Fetch drivers for entries NOT for driver points
def fetch_drivers(series):
    url = f'http://localhost:2020/entries/{series}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()['seriesEntries']['entries']
        print('data', data)

        # entries_by_class = sortDriverPoints(data)

        # return entries_by_class

    else:
        return (response.status_code, None)


def fetch_driver_points(series):
    url = f'http://localhost:2020/api/drivers/{series}'
    response = requests.get(url)

    if response.status_code == 200:

        # returns dict of keys with array vals
        data = response.json()['seriesDrivers']

        entries_by_class = sortDriverPoints(data)

        return entries_by_class

    else:
        return (response.status_code, None)

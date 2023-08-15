import requests
from . import helpers
# import json


def fetch_drivers(series):
    url = f'http://localhost:2020/api/drivers/{series}'
    response = requests.get(url)

    if response.status_code == 201:
        data = response.json()['seriesDrivers']

        entries_by_class = helpers.classEntries(data)

        # Loop through each list for Pro, Pro/Am etc, and alter the list, to be a list of drivers instead of a list of entries. then sort by most points
        for classification in entries_by_class:
            drivers = []
            entry_list = entries_by_class[classification]
            for entry in entry_list:
                driver2 = entry.get('driver2')
                drivers.append(entry['driver1'])

                if driver2:
                    drivers.append(entry['driver2'])

            sorted_drivers = sorted(
                drivers, key=lambda x: x['totalPoints'], reverse=True)

            entries_by_class[classification] = sorted_drivers

        # print(json.dumps(entries_by_class, indent=4))
        return entries_by_class

    else:
        return (response.status_code, None)

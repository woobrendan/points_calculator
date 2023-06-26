from http.client import HTTPResponse
from django.shortcuts import render
import requests
import json


def fetch_drivers():
    response = requests.get('http://localhost:2020/entries')

    if response.status_code == 201:
        data = response.json()['entry']
        # Refactor later for series to be query from front end
        series = 'GT World Challenge America'
        filtered = [entry for entry in data
                    if entry.get('series') == series]

        entries_by_class = {}

        # loop through filtered entries, and sort them into dictionary with keys as the class (pro, Pro/Am or am, etc) and the value as a list of entries
        for entry in filtered:
            classification = entry['classification']

            if classification in entries_by_class:
                entries_by_class[classification].append(entry)
            else:
                entries_by_class[classification] = [entry]

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

        print(json.dumps(entries_by_class, indent=4))

    else:
        return HTTPResponse('Failed to fetch data from API')


if __name__ == "__main__":
    fetch_drivers()

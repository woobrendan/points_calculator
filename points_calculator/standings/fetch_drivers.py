from http.client import HTTPResponse
from django.shortcuts import render
import requests


def fetch_drivers():
    response = requests.get('http://localhost:2020/entries')

    if response.status_code == 201:
        data = response.json()['entry']
        # Refactor later for series to be query from front end
        series = 'GT World Challenge America'
        filtered = [entry for entry in data
                    if entry.get('series') == series]
        drivers = []
        for entry in filtered:
            driver2 = entry.get('driver2')
            drivers.append(entry['driver1'])

            if driver2:
                drivers.append(entry['driver2'])

        sorted_drivers = sorted(
            drivers, key=lambda x: x['totalPoints'], reverse=True)
        print(sorted_drivers)

    else:
        return HTTPResponse('Failed to fetch data from API')

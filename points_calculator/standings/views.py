from http.client import HTTPResponse
from django.shortcuts import render
import requests


def drivers_standing():
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
        print(drivers)

    else:
        return HTTPResponse('Failed to fetch data from API')


if __name__ == "__main__":
    drivers_standing()

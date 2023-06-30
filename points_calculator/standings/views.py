from django.shortcuts import render
from flask import jsonify

from . import fetch_drivers


def drivers_standing(request):
    drivers = fetch_drivers.fetch_drivers()

    # if the value is a tuple, means fetch failed, and we have status code and none value
    if isinstance(drivers, tuple):
        status_code, data = drivers
        error_message = f"Failed to fetch data. Status code: { status_code }"
        return jsonify({"error": error_message}), status_code

    else:
        return render(request, 'standing/drivers_standing.html', {
            'drivers': drivers
        })


def team_standing(request):
    return render(request, 'standing/team_standing.html')


if __name__ == "__main__":
    drivers_standing()

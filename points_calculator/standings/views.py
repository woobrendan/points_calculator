from django.shortcuts import render
from flask import jsonify

from .functions import fetch_drivers, fetch_team_standing


def drivers_standing(request, series):
    drivers = fetch_drivers.fetch_drivers(series)

    # if the value is a tuple, means fetch failed, and we have status code and none value
    if isinstance(drivers, tuple):
        status_code, data = drivers
        error_message = f"Failed to fetch data. Status code: { status_code }"
        return jsonify({"error": error_message}), status_code

    else:
        return render(request, 'standing/drivers_standing.html', {
            'drivers': drivers
        })


def team_standing(request, series):
    team_standing = fetch_team_standing.fetch_team_standings(series)

    # if the value is a tuple, means fetch failed, and we have status code and none value
    if isinstance(team_standing, tuple):
        status_code, data = team_standing
        error_message = f"Failed to fetch data. Status code: { status_code }"
        return jsonify({"error": error_message}), status_code

    else:
        return render(request, 'standing/team_standing.html', {
            'team_standing': team_standing
        })


if __name__ == "__main__":
    drivers_standing()

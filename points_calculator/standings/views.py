from django.shortcuts import render
from flask import jsonify

from .functions import fetch_drivers, fetch_team_standing, helpers


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

    if series != 'gta':
        for _, lists in team_standing.items():
            keys_to_remove = ['R14', 'R15', 'R16', 'R17', 'R18']

            # TC America & GT4 America have 14 rounds
            if series == 'tca' or series == 'pgt4a':
                del keys_to_remove[0]

            # List of TeamEntry
            for team in lists:
                points = team.points
                for key in keys_to_remove:
                    if key in points.__dict__:
                        delattr(points, key)

    _, team_list = list(team_standing.items())[0]
    round_list = helpers.getRounds(team_list[0].points)

    # if the value is a tuple, means fetch failed, and we have status code and none value
    if isinstance(team_standing, tuple):
        status_code, data = team_standing
        error_message = f"Failed to fetch data. Status code: { status_code }"
        return jsonify({"error": error_message}), status_code

    else:
        return render(request, 'standing/team_standing.html', {
            'team_standing': team_standing,
            'round_list': round_list
        })

from django.shortcuts import render, redirect
from flask import jsonify
import json
import requests

from .functions.helpers import getRounds
from .functions.csv_converter import csv_to_clean_keys
from .functions.team_points import team_results_byClass
from .functions.fetch_drivers import fetch_drivers
from .functions.fetch_team_standing import fetch_team_standings


def drivers_standing(request, series):
    if request.method == 'GET':
        drivers = fetch_drivers(series)

        # if the value is a tuple, means fetch failed, and we have status code and none value
        if isinstance(drivers, tuple):
            status_code, data = drivers
            error_message = f"Failed to fetch data. Status code: { status_code }"
            return jsonify({"error": error_message}), status_code

        else:
            return render(request, 'standing/drivers_standing.html', {
                'drivers': drivers
            })
    else:
        pass


def team_standing(request, series):
    team_standing = fetch_team_standings(series)

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
    round_list = getRounds(team_list[0].points)

    button_style = "px-4 py-2 text-sm font-medium text-white bg-red-600 border border-gray-200 rounded-lg hover:bg-black hover:text-red-400 hover:border-red-500"
    anchor_style = "block px-4 py-2"

    # if the value is a tuple, means fetch failed, and we have status code and none value
    if isinstance(team_standing, tuple):
        status_code, data = team_standing
        error_message = f"Failed to fetch data. Status code: { status_code }"
        return jsonify({"error": error_message}), status_code

    else:
        return render(request, 'standing/team_standing.html', {
            'team_standing': team_standing,
            'round_list': round_list,
            'button_style': button_style,
            'anchor_style': anchor_style
        })


def new_result(request):
    if request.method == 'POST':
        result_num = request.POST.get('result_num', '')
        result_csv = request.FILES['result_csv']

        # Take in CSV file and convert to dict, keys as class (pro/am) values as list of result from race
        result_arr = csv_to_clean_keys(result_csv)
        newR = team_results_byClass(result_arr)

        series = result_arr[0]['Series']

        url = f'http://localhost:2020/teamPoints/{series}'
        headers = {'Content-Type': 'application/json'}
        success = False

        for key, result_arr in newR.items():
            for result in result_arr:
                r_num = f"R{result_num}"
                data = {
                    "classification": key,
                    "round": r_num,
                    "points": result['Points'],
                    "teamName": result['Team']
                }
                json_data = json.dumps(data)

                response = requests.post(url, headers=headers, data=json_data)

                if response.status_code == 200:
                    print('POST request successful')
                    sucess = True
                else:
                    print(f'Error: {response.status_code}')
                    sucess = False

        if success:
            redirect("standing:team", series)

    else:
        pass
    return render(request, 'standing/new_result.html')

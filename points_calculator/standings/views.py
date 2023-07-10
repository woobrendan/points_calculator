from django.shortcuts import render
from flask import jsonify
import json
import requests

from .functions import fetch_drivers, fetch_team_standing, helpers
from .functions.csv_converter import csv_to_clean_keys


def drivers_standing(request, series):
    if request.method == 'GET':
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
    else:
        pass


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

        series = result_arr[0]['Series']

        newR = helpers.team_results_byClass(result_arr)
        # returns
        # {'Pro': [{'Pos': '1', 'PIC': '1', '#': '93', 'Class': 'Pro', 'Points': '25', 'Team': 'Racers Edge Motorsports', 'Vehicle': 'Acura NSX GT3 EVO22', 'Series': 'gtwca'}, {'Pos': '2', 'PIC': '2', '#': '28', 'Class': 'Pro', 'Points': '18', 'Team': 'RS1', 'Vehicle': 'Porsche GT3 R 992', 'Series': 'gtwca'}, {'Pos': '5', 'PIC': '3', '#': '53', 'Class': 'Pro', 'Points': '15', 'Team': 'MDK', 'Vehicle': 'Porsche GT3 R 992', 'Series': 'gtwca'}, {'Pos': '13', 'PIC': '4', '#': '94', 'Class': 'Pro', 'Points': '12', 'Team': 'BimmerWorld', 'Vehicle': 'BMW M4 GT3', 'Series': 'gtwca'}],
        #

        url = f'http://localhost:2020/teamPoints/{series}'
        headers = {'Content-Type': 'application/json'}

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
                    # redirect
                else:
                    print(f'Error: {response.status_code}')

    else:
        pass
    return render(request, 'standing/new_result.html')

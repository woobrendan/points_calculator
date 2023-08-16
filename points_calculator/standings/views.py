from django.shortcuts import render, redirect
from flask import jsonify
import json
import requests

from .functions.helpers import getRounds, handle_rounds
from .functions.csv_converter import csv_to_clean_keys
from .functions.team_points.team_points import team_results_byClass
from .functions.driver_points.fetch_drivers_points import fetch_drivers
from .functions.team_points.fetch_team_standing import fetch_team_standings
from .functions.manuf.manuf_points import manuf_results_byClass, manuf_results_list
from .functions.manuf.fetch_manuf_points import fetch_manuf_standings
from .functions.series_buttons import get_series_buttons


def drivers_standing(request, series):
    drivers = fetch_drivers(series)

    buttons = get_series_buttons('drivers', series)

    # if the value is a tuple, means fetch failed, and we have status code and none value
    if isinstance(drivers, tuple):
        status_code, _ = drivers
        error_message = f"Failed to fetch data. Status code: { status_code }"
        return jsonify({"error": error_message}), status_code

    else:
        return render(request, 'standing/drivers_standing.html', {
            'drivers': drivers,
            'buttons': buttons
        })


def team_standing(request, series):
    # fetch all team standing values, sorted as a dict with pro/am as keys and list for team vals, remove rounds not used
    team_standing = handle_rounds(series, fetch_team_standings(series))

    round_list = getRounds(series)

    buttons = get_series_buttons('team', series)

    # if the value is a tuple, means fetch failed, and we have status code and none value
    if isinstance(team_standing, tuple):
        status_code, _ = team_standing
        error_message = f"Failed to fetch data. Status code: { status_code }"
        return jsonify({"error": error_message}), status_code

    else:
        return render(request, 'standing/team_standing.html', {
            'team_standing': team_standing,
            'round_list': round_list,
            'buttons': buttons
        })


def manuf_standing(request, series):
    manuf_standing = handle_rounds(series, fetch_manuf_standings(series))

    round_list = getRounds(series)

    buttons = get_series_buttons('manuf', series)

    # if the value is a tuple, means fetch failed, and we have status code and none value
    if isinstance(team_standing, tuple):
        status_code, _ = team_standing
        error_message = f"Failed to fetch data. Status code: { status_code }"
        return jsonify({"error": error_message}), status_code
    else:
        return render(request, 'standing/manuf_standing.html', {
            'manuf_standing': manuf_standing,
            'round_list': round_list,
            'buttons': buttons
        })


def new_result(request):
    if request.method == 'POST':

        result_num = request.POST.get('result_num', '')
        result_csv = request.FILES['result_csv']

        # Take in CSV file and convert to list of dict
        result_arr = csv_to_clean_keys(result_csv)

        series = result_arr[0]['Series']

        # sort by class, remove dupes, apply points for highest finishing car per team
        team_results = team_results_byClass(result_arr)
        manuf_results = manuf_results_list(
            result_arr) if series == 'gtwca' or series == 'pgt4a' else manuf_results_byClass(result_arr)

        r_num = f"R{result_num}"
        data = {
            "manufResults": manuf_results,
            "teamResults": team_results,
            "roundNum": r_num
        }

        url = f'http://localhost:2020/result/{series}'
        headers = {'Content-Type': 'application/json'}
        json_data = json.dumps(data)

        response = requests.post(url, headers=headers, data=json_data)

        if response.status_code == 200:
            print('POST request successful')
            return redirect("standing:team", series)

        else:
            print(f'Error: {response.status_code}')

    else:
        pass
    return render(request, 'standing/new_result.html')

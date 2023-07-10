from django.shortcuts import render
from flask import jsonify

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

        result_arr = csv_to_clean_keys(result_csv)

        newR = helpers.team_results_byClass(result_arr)
        # returns
        # {'Pro': [{'Pos': '1', 'PIC': '1', '#': '93', 'Class': 'Pro', 'Points': '25', 'Team': 'Racers Edge Motorsports', 'Vehicle': 'Acura NSX GT3 EVO22', 'Series': 'gtwca'}, {'Pos': '2', 'PIC': '2', '#': '28', 'Class': 'Pro', 'Points': '18', 'Team': 'RS1', 'Vehicle': 'Porsche GT3 R 992', 'Series': 'gtwca'}, {'Pos': '5', 'PIC': '3', '#': '53', 'Class': 'Pro', 'Points': '15', 'Team': 'MDK', 'Vehicle': 'Porsche GT3 R 992', 'Series': 'gtwca'}, {'Pos': '13', 'PIC': '4', '#': '94', 'Class': 'Pro', 'Points': '12', 'Team': 'BimmerWorld', 'Vehicle': 'BMW M4 GT3', 'Series': 'gtwca'}],
        #
        # 'Pro-Am': [{'Pos': '3', 'PIC': '1', '#': '120', 'Class': 'Pro-Am', 'Points': '25', 'Team': 'Wright Motorsports', 'Vehicle': 'Porsche 911 GT3-R (991.ii)', 'Series': 'gtwca'}, {'Pos': '4', 'PIC': '2', '#': '007', 'Class': 'Pro-Am', 'Points': '18', 'Team': 'TRG - The Racers Group', 'Vehicle': 'Aston Martin Vantage AMR GT3', 'Series': 'gtwca'}, {'Pos': '6', 'PIC': '3', '#': '45', 'Class': 'Pro-Am', 'Points': '15', 'Team': 'Wright Motorsports', 'Vehicle': 'Porsche GT3 R 992', 'Series': 'gtwca'}, {'Pos': '7', 'PIC': '4', '#': '91', 'Class': 'Pro-Am', 'Points': '12', 'Team': 'DXDT Racing', 'Vehicle': 'Mercedes-AMG GT3', 'Series': 'gtwca'}, {'Pos': '8', 'PIC': '5', '#': '38', 'Class': 'Pro-Am', 'Points': '10', 'Team': 'ST Racing', 'Vehicle': 'BMW M4 GT3', 'Series': 'gtwca'}, {'Pos': '9', 'PIC': '6', '#': '33', 'Class': 'Pro-Am', 'Points': '8', 'Team': 'Triarsi Competizione', 'Vehicle': 'Ferrari 296 GT3', 'Series': 'gtwca'}, {'Pos': '10', 'PIC': '7', '#': '9', 'Class': 'Pro-Am', 'Points': '6', 'Team': 'TR3 Racing', 'Vehicle': 'Mercedes-AMG GT3', 'Series': 'gtwca'}, {'Pos': '11', 'PIC': '8', '#': '19', 'Class': 'Pro-Am', 'Points': '4', 'Team': 'Esses Racing with Mercedes-Benz of Austin', 'Vehicle': 'Mercedes-AMG GT3', 'Series': 'gtwca'}, {'Pos': '12', 'PIC': '9', '#': '08', 'Class': 'Pro-Am', 'Points': '2', 'Team': 'DXDT Racing', 'Vehicle': 'Mercedes-AMG GT3', 'Series': 'gtwca'}, {'Pos': '14', 'PIC': '10', '#': '16', 'Class': 'Pro-Am', 'Points': '1', 'Team': 'ACI Motorsports', 'Vehicle': 'Porsche 911 GT3-R (991.ii)', 'Series': 'gtwca'}, {'Pos': '', 'PIC': '', '#': '04', 'Class': 'Pro-Am', 'Points': '0', 'Team': 'Crowdstrike by Riley', 'Vehicle': 'Mercedes-AMG GT3', 'Series': 'gtwca'}],
        # 'Am': [{'Pos': '15', 'PIC': '1', '#': '43', 'Class': 'Am', 'Points': '25', 'Team': 'RealTime Racing', 'Vehicle': 'Mercedes-AMG GT3', 'Series': 'gtwca'}]}

        # for result in result_arr:
        #     r_num = f"R{result_num}"
        #     data = {
        #         "classification": result['Class'],
        #         "round": r_num
        #         # "points":
        #     }

        # json send should { teamName: "name", classificaiton, round, points}

    else:
        pass
    return render(request, 'standing/new_result.html')

from django.shortcuts import render
from flask import jsonify
from .functions.driver_funcs import fetch_driver_points
from Utility.series_buttons import get_series_buttons
from Utility.helpers import getRounds


def drivers_standing(request, series):
    # Use different function as this gets entries, not driver points
    drivers = fetch_driver_points(series)

    buttons = get_series_buttons('drivers', series)
    round_list = getRounds(series)

    # if the value is a tuple, means fetch failed, and we have status code and none value
    if isinstance(drivers, tuple):
        status_code, _ = drivers
        error_message = f"Failed to fetch data. Status code: { status_code }"
        return jsonify({"error": error_message}), status_code

    else:
        return render(request, 'driver_standing/drivers_standing.html', {
            'drivers': drivers,
            'buttons': buttons,
            'round_list': round_list
        })

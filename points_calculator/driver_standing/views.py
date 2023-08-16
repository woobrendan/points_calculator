from django.shortcuts import render
from flask import jsonify
from .functions.fetch_drivers_points import fetch_drivers
from ..Utility.series_buttons import get_series_buttons


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

series_list = ['gtwca', 'pgt4a', 'gta', 'tca', 'grc']
button_style = "px-4 py-2 text-sm font-medium text-white bg-red-600 border border-gray-200 rounded-lg hover:bg-black hover:text-red-400 hover:border-red-500"
selected_style = "px-4 py-2 text-sm font-medium text-white bg-black-500 border border-red-500 rounded-lg hover:bg-black hover:text-red-400 hover:border-red-500"


def get_series_buttons(points_type, selected_series):
    # GR Cup won't have manuf point standing
    if points_type == 'manuf' and 'grc' in series_list:
        series_list.remove('grc')

    seriesObj = {}

    for series in series_list:
        selected = selected_style if series == selected_series else button_style
        seriesObj[series] = selected

    return seriesObj

button_style = "px-4 py-2 text-sm font-medium text-white bg-red-600 border border-gray-200 rounded-lg hover:bg-black hover:text-red-400 hover:border-red-500"

selected_style = "px-4 py-2 text-sm font-medium text-red-400 bg-black border border-red-500 rounded-lg hover:bg-black hover:text-red-400 hover:border-red-500"

anchor_style = "block px-4 py-2"


def get_series_buttons(points_type, selected_series):
    series_list = ['gtwca', 'pgt4a', 'gta', 'tca', 'grc']

    # GR Cup won't have manuf point standing
    if points_type == 'manuf' and 'grc' in series_list:
        series_list.remove('grc')

    seriesObj = {}

    for series in series_list:
        selected = selected_style if series == selected_series else button_style

        seriesObj[series] = {
            "button": selected,
            "anchor": anchor_style
        }

    return seriesObj

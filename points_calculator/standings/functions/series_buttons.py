series_list = ['gtwca', 'pgt4a', 'gta', 'tca', 'grc']
button_style = "px-4 py-2 text-sm font-medium text-white bg-red-600 border border-gray-200 rounded-lg hover:bg-black hover:text-red-400 hover:border-red-500"
selected_style = "px-4 py-2 text-sm font-medium text-white bg-red-600 border border-gray-200 rounded-lg hover:bg-black hover:text-red-400 hover:border-red-500"


def get_series_buttons(points_type, selected_series):
    # GR Cup won't have manuf point standing
    if points_type == 'manuf':
        series_list.pop()

    seriesObj = {}
    for series in series_list:
        seriesObj[series] = {
            'name': series,
        }

from .team_manuf_entry import Team_Manuf_Entry


def classEntries(data):
    entries_by_class = {}

    # loop through data, getting key and value, creating a new key in entries_by_class for each class, create empty list, then creating instance of team_entry
    for classification, entry_list in data.items():
        entries_by_class[classification] = []

        if entry_list:
            for entry in entry_list:
                teamName, points = entry['teamName'], entry['points']

                entry_obj = Team_Manuf_Entry(
                    teamName, classification, points)

                entries_by_class[classification].append(entry_obj)

    for class_list in entries_by_class.values():
        if class_list:
            class_list.sort(key=lambda x: x.total_points, reverse=True)

    return entries_by_class


def getSeriesName(str):
    if str == "gtwca":
        return "GT World Challenge America"
    if str == "pgt4a":
        return "Pirelli GT4 America"
    if str == "gta":
        return "GT America"
    if str == "tca":
        return "TC America"
    if str == "tgr":
        return "Toyota GR Cup"


def sort_by_val(entry, sort_by):
    key = entry[sort_by]

    if key == '':
        key = 100

    return int(key)

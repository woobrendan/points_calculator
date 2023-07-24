from . import team_entry


def classEntries(data):
    entries_by_class = {}

    for classification, entry_list in data.items():
        entries_by_class[classification] = []

        if entry_list:
            for entry in entry_list:
                teamName, points = entry['teamName'], entry['points']

                entry_obj = team_entry.TeamEntry(
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


def getRounds(points_dict):
    round_list = []
    for roundNum in points_dict.__dict__:
        round_list.append(roundNum)
    return round_list


def handle_rounds(series, class_entries):
    if series != 'gta':
        for _, lists in class_entries.items():
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

    return class_entries


def sort_by_pic(entry):
    pic = entry['PIC']
    if pic == '':
        pic = '100'
    return int(pic)

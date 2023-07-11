from . import team_entry


def classEntries(entry_list):
    entries_by_class = {}

    # loop through filtered entries, and sort them into dictionary with keys as the class (pro, Pro/Am or am, etc) and the value as a list of entries
    for entry in entry_list:
        teamName, classification, points = entry['teamName'], entry['classification'], entry['points']

        entry_obj = team_entry.TeamEntry(teamName, classification, points)

        if entry_obj.classification in entries_by_class:
            entries_by_class[classification].append(entry_obj)
        else:
            entries_by_class[classification] = [entry_obj]

    for class_list in entries_by_class.values():
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


def removeDuplicateTeams(arr):
    unique_teams = set()
    filtered_entries = []

    for entry in arr:
        team_name = entry['Team']

        if team_name not in unique_teams:
            unique_teams.add(team_name)
            filtered_entries.append(entry)

    return arr


def sort_by_pic(entry):
    pic = entry['PIC']
    if pic == '':
        pic = '100'
    return int(pic)


def update_team_points(arr):
    points = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]
    length = len(arr)
    print('arr', arr)

    if length <= 10:
        # update points for the first 10 entries, anything after change to zero
        for i, entry in enumerate(arr[:length]):
            entry['Points'] = points[i]
    else:
        for i, entry in enumerate(arr[:10]):
            entry['Points'] = points[i]

        for entry in arr[10:]:
            entry['Points'] = 0

    return arr


def team_results_byClass(entry_list):
    entries_by_class = {}

    # loop through filtered entries, and sort them into dictionary with keys as the class (pro, Pro/Am or am, etc) and the value as a list of entries
    for entry in entry_list:
        classification = entry['Class']

        if classification in entries_by_class:
            entries_by_class[classification].append(entry)
        else:
            entries_by_class[classification] = [entry]

    for class_list in entries_by_class.values():
        # Take in each class list of result, sort by PIC, then remove duplicate teams
        class_list.sort(key=sort_by_pic)
        class_list[:] = update_team_points(removeDuplicateTeams(class_list))[:]

    return entries_by_class

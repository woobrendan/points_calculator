from . import team_entry


def classEntries(entry_list):
    entries_by_class = {}

    # loop through filtered entries, and sort them into dictionary with keys as the class (pro, Pro/Am or am, etc) and the value as a list of entries
    for entry in entry_list:

        entry_obj = team_entry.TeamEntry(
            entry['teamName'], entry['classification'], entry['points'])

        classification = entry_obj.classification

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

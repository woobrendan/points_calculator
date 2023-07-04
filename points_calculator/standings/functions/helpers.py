def classEntries(entry_list):
    entries_by_class = {}

    # loop through filtered entries, and sort them into dictionary with keys as the class (pro, Pro/Am or am, etc) and the value as a list of entries
    for entry in entry_list:
        classification = entry['classification']

        for roundNum in entry['points']:
            if entry['points'][roundNum] is None:
                entry['points'][roundNum] = ''

        if classification in entries_by_class:
            entries_by_class[classification].append(entry)
        else:
            entries_by_class[classification] = [entry]

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

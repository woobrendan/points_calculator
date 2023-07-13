from .helpers import sort_by_pic


def removeDuplicateManuf(arr):
    unique_manuf = set()
    filtered_entries = []

    for entry in arr:
        vehicle = entry['Manufacturer']

        if vehicle not in unique_manuf:
            unique_manuf.add(vehicle)
            filtered_entries.append(entry)

    return filtered_entries


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
        sorted_list = class_list[:]

        # remove dupe entries, then update points based on team finish
        class_list[:] = update_team_points(
            removeDuplicateManuf(sorted_list))[:]

    return entries_by_class

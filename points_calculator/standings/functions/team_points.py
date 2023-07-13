from .helpers import sort_by_pic
from .points import update_points


def removeDuplicateTeams(arr):
    unique_teams = set()
    filtered_entries = []

    for entry in arr:
        team_name = entry['Team']

        if team_name not in unique_teams:
            unique_teams.add(team_name)
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
        class_list[:] = update_points(
            removeDuplicateTeams(sorted_list))[:]

    return entries_by_class

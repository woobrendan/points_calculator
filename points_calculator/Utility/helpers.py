
# For table header, row values
def getRounds(series):
    round_list = ['R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9',
                  'R10', 'R11', 'R12', 'R13', 'R14', 'R15', 'R16', 'R17', 'R18']

    if series == 'gtwca':
        return round_list[0:13]

    if series == 'tca' or series == 'pgt4a':
        return round_list[0:14]

    return round_list

# Loops through entry values removes key for rounds 14 to 18 depending on series


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

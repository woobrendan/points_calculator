def getRounds(series):
    round_list = ['R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7', 'R8', 'R9',
                  'R10', 'R11', 'R12', 'R13', 'R14', 'R15', 'R16', 'R17', 'R18']

    if series == 'gtwca':
        return round_list[0:13]

    if series == 'tca' or series == 'pgt4a':
        return round_list[0:14]

    return round_list

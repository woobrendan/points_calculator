class Points:
    def __init__(self, points_dict):
        for round_num, value in points_dict.items():
            setattr(self, round_num, value)


def update_points(arr):
    points = [25, 18, 15, 12, 10, 8, 6, 4, 2, 1]

    for i, entry in enumerate(arr):
        if i < 10:
            if entry['PIC'] == '':
                entry['Points'] = 0
            else:
                entry['Points'] = points[i]
        else:
            entry['Points'] = 0

    return arr

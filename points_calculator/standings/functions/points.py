class Points:
    def __init__(self, points_dict):
        for round_num, value in points_dict.items():
            setattr(self, round_num, value or None)

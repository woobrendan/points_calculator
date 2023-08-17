from Utility.points import Points


class Team_Manuf_Entry:
    def __init__(self, name: str, classification: str, points_dict: dict):
        self.name = name
        self.classification = classification
        self.points = Points(points_dict)
        self.total_points = sum(
            value or 0 for value in self.points.__dict__.values())

        for round_num in self.points.__dict__:
            if getattr(self.points, round_num) == 0:
                setattr(self.points, round_num, 0)
            elif getattr(self.points, round_num) is None:
                setattr(self.points, round_num, '')

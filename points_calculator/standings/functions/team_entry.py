from points import Points


class TeamEntry:
    def __init__(self, name: str, classification: str, points_dict: dict, type):
        self.name = name
        self.classifcation = classification
        self.points = Points(points_dict)
        self.total_points = sum(value or 0 for value in self.points.values())

        for round_num in self.points.__dict__:
            if getattr(self.points, round_num) is None:
                setattr(self.points, round_num, '')

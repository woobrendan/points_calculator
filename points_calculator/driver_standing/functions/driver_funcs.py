from Utility.points import Points


def sortDriverPoints(driversArr):
    classDrivers = {}

    for driver in driversArr:
        name, classification, points = driver['name'], driver['classification'], driver['points']

        driver_obj = Driver_Points_Entry(name, classification, points)

        if classDrivers[classification]:
            classDrivers[classification].append(driver_obj)
        else:
            classDrivers[classification] = [driver_obj]

    for class_list in classDrivers.values():
        if class_list:
            class_list.sort(key=lambda x: x.total_points, reverse=True)

    return classDrivers


class Driver_Points_Entry:
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

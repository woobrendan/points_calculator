from Utility.points import Points
# from .fetch_drivers_points import fetch_drivers
import requests


def sortDriverPoints(driversArr):
    classDrivers = {}

    for classification, driver_list in driversArr.items():
        classDrivers[classification] = []

        if driver_list:
            for driver in driversArr:
                name, classification, points = driver['name'], driver['classification'], driver['points']

                driver_obj = Driver_Points_Entry(name, classification, points)

                classDrivers[classification].append(driver_obj)

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


# # Fetch drivers for entries NOT for driver points
def fetch_drivers(series):
    url = f'http://localhost:2020/entries/{series}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()['seriesEntries']['entries']
        print('data', data)

        # entries_by_class = sortDriverPoints(data)

        # return entries_by_class

    else:
        return (response.status_code, None)


def fetch_driver_points(series):
    url = f'http://localhost:2020/api/drivers/{series}'
    response = requests.get(url)

    if response.status_code == 200:

        # returns dict of keys with array vals
        data = response.json()['seriesDrivers']

        entries_by_class = sortDriverPoints(data)

        return entries_by_class

    else:
        return (response.status_code, None)

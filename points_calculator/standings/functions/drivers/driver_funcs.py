from Utility.points import Points
import requests
# from .fetch_drivers_points import fetch_drivers

# # Fetch drivers for entries NOT for driver points


def fetch_drivers(series):
    url = f'http://localhost:2020/entries/{series}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()['seriesEntries']['entries']

        return data

        # entries_by_class = sortDriverPoints(data)

        # return entries_by_class

    else:
        return (response.status_code, None)


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


def getEventNameByNum(round_num, series):
    gtam_events = {
        "1": "St.Petersburg",
        "2": "St.Petersburg",
        "3": "Sonoma",
        "4": "Sonoma",
        "5": "NOLA",
        "6": "NOLA",
        "7": "COTA",
        "8": "COTA",
        "9": "VIR",
        "10": "VIR",
        "11": "Nashville",
        "12": "Nashville",
        "13": "RoadAm",
        "14": "RoadAm",
        "15": "Sebring",
        "16": "Sebring",
        "17": "Indy",
        "18": "Indy",
    }

    sro_events = {
        "1": "Sonoma",
        "2": "Sonoma",
        "3": "NOLA",
        "4": "NOLA",
        "5": "COTA",
        "6": "COTA",
        "7": "VIR",
        "8": "VIR",
        "9": "RoadAm",
        "10": "RoadAm",
        "11": "Sebring",
        "12": "Sebring",
        "13": "Indy",
        "14": "Indy",
    }

    return gtam_events[round_num] if series == 'gtam' else sro_events[round_num]


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


# Take in results arr from CSV, and loop through entries from backend, add driver keys and values to result
def handle_drivers(result_arr, series, round_num):
    drivers = fetch_drivers(series)
    event = getEventNameByNum(round_num, series)

    # Filter out entries that arent racing this event, or if a driver pairing has changed at future events. use the dict as reference
    # key = ("Pro", "21")
    # value = {"driver1": "Manny Franco", "driver2": "Alessandro Balzan"}
    driver_info = {}
    for entry in drivers:
        if entry["events"][event]:
            key = (entry["classification"], entry["number"])
            driver_info[key] = {
                "driver1": entry["driver1"],
                "driver2": entry["driver2"] if series in ('gtwca', 'pgt4a') else None
            }

    for result in result_arr:
        key = (result["Class"], result["#"])
        if key in driver_info:
            result["driver1"] = driver_info[key]["driver1"]
            result["driver2"] = driver_info[key]["driver2"] if series in (
                'gtwca', 'pgt4a') else None

    return result_arr


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

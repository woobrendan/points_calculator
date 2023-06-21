import requests
from csv_converter import csv_to_clean_keys

file_path = '../Results/results.csv'


def get_entries():
    response = requests.get('http://localhost:2020/entries')
    data = response.json()
    return data['entry']


# for row in get_entries():
#     print(row)
result = csv_to_clean_keys(file_path)
entries = get_entries()

if __name__ == "__main__":
    # creates a dictionary, with the key as the number and series, and the value as the entry
    entry_mapping = {(entry['number'], entry['series'])
                      : entry for entry in entries}

    for row in result:
        key = (row['#'], row['Series'])
        if key in entry_mapping:
            entry = entry_mapping[key]
            points = int(row['Points'])
            entry['driver1']['points'] += points

            driver2 = entry.get('driver2')
            if driver2:
                driver2['points'] += points

            update_url = 'http://localhost:2020/entries/' + entry['_id']
            requests.patch(update_url, json=entry)

    # for row in result:
    #     print(row)

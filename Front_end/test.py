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
    for row in result:
        for entry in entries:
            if row['#'] == entry['number']:
                points = int(row['Points'])
                entry['driver1']['points'] += points
                entry['driver1']['points'] += points
                print(entry)
                # Beware of double loop, printed twice
                # hit post route to update points

    # for row in result:
    #     print(row)

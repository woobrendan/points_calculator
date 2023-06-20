import requests


def get_entries():
    response = requests.get('http://localhost:2020/entries')
    data = response.json()
    return data['entry']


for row in get_entries():
    print(row)

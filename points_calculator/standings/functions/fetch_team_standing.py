import requests


def fetch_team_standings(series):
    url = f'http://localhost:2020/teamPoints/{series}'
    response = requests.get(url)

    if response.status_code == 201:
        data = response.json()['teamsBySeries']
        team_points_list = data['teamPoints']

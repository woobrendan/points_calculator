import requests
import helpers


def fetch_team_standings(series):
    url = f'http://localhost:2020/teamPoints/{series}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()['teamsBySeries']
        team_points_list = data['teamPoints']

        return helpers.classEntries(team_points_list)
    else:
        return (response.status_code, None)

import csv
import io

file_path = '../Results/results.csv'

key_list = [
    'Pos',
    'PIC',
    '#',
    'Name',
    'Class',
    'Points',
    'Additional3',
    'Additional4'
]


def csv_to_dict_arr(csv_file):
    csv_reader = csv.reader(io.TextIOWrapper(csv_file, encoding='utf-8'))
    headers = next(csv_reader)  # gets the header row
    results = []
    for row in csv_reader:
        result_dict = dict(zip(headers, row))
        results.append(result_dict)
    return results


def clean_results(arr, key_arr):
    results = []
    for result in arr:
        filtered = {key: result[key] for key in key_arr if key in result}
        results.append(filtered)
    return results


def change_key_name(dict_arr):
    for result in dict_arr:
        if 'Name' in result:
            result['Team'] = result.pop('Name')
        if 'Additional4' in result:
            result['Vehicle'] = result.pop('Additional4')
        if 'Additional3' in result:
            result['Series'] = result.pop('Additional3')
        if 'Additional6' in result:
            result['Manufacturer'] = result.pop('Additional6')

        series = result['Series']

        if series == 'FGTWCA':
            result['Series'] = 'gtwca'
        if series == 'PGT4A':
            result['Series'] = 'pgt4a'
        if series == 'GTA':
            result['Series'] = 'gta'
        if series == 'TCAM':
            result['Series'] = 'tca'

    return dict_arr


# returns cleaned up csv results into list of dictionaries to use to compare to entries
def csv_to_clean_keys(csv_file):
    dict_arr = csv_to_dict_arr(csv_file)
    cleaned = clean_results(dict_arr, key_list)
    return change_key_name(cleaned)


if __name__ == "__main__":
    for row in csv_to_clean_keys(file_path):
        print(row)

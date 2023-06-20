import csv

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


def csv_to_dict_arr(file_path):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        results = []
        for row in csv_reader:
            results.append(row)
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
    return dict_arr


# returns cleaned up csv results into list of dictionaries to use to compare to entries
def csv_to_clean_keys(file_path):
    dict_arr = csv_to_dict_arr(file_path)
    cleaned = clean_results(dict_arr, key_list)
    return change_key_name(cleaned)


if __name__ == "__main__":
    for row in csv_to_clean_keys(file_path):
        print(row)

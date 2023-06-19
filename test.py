import csv

file_path = './Results/results.csv'

def display_data(file_path):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if row['Pos']:
                print(row)

# display_data(file_path)

def csv_to_dict_arr(file_path):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        results = []
        for row in csv_reader:
            results.append(row)
        return results

# csv_to_dict_arr(file_path)

key_list = [
    'Pos',
    'PIC',
    '#',
    'Name',
    'Class',
    'Points',
    'Additional4'
]

def clean_results(arr, key_arr):
    results = []
    for result in arr:
        filtered = {key: result[key] for key in key_arr if key in result}
        results.append(filtered)
    return results

cleaned = clean_results(csv_to_dict_arr(file_path), key_list)

def change_key_name(dict_arr):
    for result in dict_arr: 
        if 'Name' in result:
            result['Team'] = result.pop('Name')
        if 'Additional4' in result:
            result['Vehicle'] = result.pop('Additional4')
    return dict_arr

# print(clean_results(csv_to_dict_arr(file_path), key_list))
for row in change_key_name(cleaned):
    print(row)

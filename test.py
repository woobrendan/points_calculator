import csv

file_path = './Results/results.csv'

def display_data(file_path):
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            if row['Pos']:
                print(row)

display_data(file_path)
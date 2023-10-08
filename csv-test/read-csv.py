import csv

file_path = input("Enter path to a csv file: ")
with open(file_path, 'r') as f:
    f_reader = csv.reader(f, delimiter=";")
    for row in f_reader:
        print(row)

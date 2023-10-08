import csv

file_path = input("Enter path to the countries csv file: ")
country = input("Enter a country to check: ")
with open(file_path, 'r') as f:
    f_reader = csv.reader(f, delimiter=";")
    for row in f_reader:
        if row[1]==country:
            print(country + " is  on position " + row[0] + " on world countries list with the population of " + row[2] + ".")

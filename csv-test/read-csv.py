import csv

with open('countries.csv', 'r') as country_list:
    country_reader = csv.reader(country_list)
    for row in country_reader:
        print(row)

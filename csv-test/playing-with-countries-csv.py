import csv

def get_file_path():
    file_path = ""
    suffix = ".csv"
    while (file_path.endswith(suffix) == False):
        file_path = input("Enter path to the countries csv file: ")
    return file_path

def get_selection():
    user_selection = ""
    user_selection = input("Choose one\n a) Check a country's population\n b) Compare populations\n q) Quit\nYour choise: ")
    return user_selection.lower()

def get_country(csv_file_path):
    inputted_country = ""
    country_found = False
    while (country_found == False):
        inputted_country = input("Choose a country: ")
        with open(csv_file_path, 'r') as fil:
            fil_reader = csv.reader(fil, delimiter=";")
            for row in fil_reader:
                if row[1] == inputted_country:
                    country_found = True
    return inputted_country

def main():
    print("Let's start!\n")
    csv_file = get_file_path()
    selection = ""
    while (selection != "q"):
        selection = get_selection()
        match selection:
            case "a":
                country = get_country(csv_file)
                with open(csv_file, 'r') as f:
                    f_reader = csv.reader(f, delimiter=";")
                    for row in f_reader:
                        if row[1]==country:
                            country_specs = country + " is  on position " + row[0] + " on world countries list with the population of " + row[2] + "."
                            print(country_specs)
            case "b":
                print(selection + " doesn't yet do anything.")
            case "q":
                print("Exiting the program.")
            case _:
                print("Sorry, I didn't understand that, please try again.")

if __name__ == "__main__":
    main()

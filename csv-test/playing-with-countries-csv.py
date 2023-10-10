import csv

def get_file_path():
    file_path = ""
    suffix = ".csv"
    while (file_path.endswith(suffix) == False):
        file_path = input("Enter path to the countries csv file: ")
    return file_path

def main():
    print("Let's start!\n")
    csv_file = get_file_path()
    selection = "c"
    while (selection != "q"):
        selection = input("Choose one\n a) Check a country's population\n q) Quit\nYour choise: ")
        selection = selection.lower()
        match selection:
            case "a":
                country = input("Enter a country to check: ")
                with open(csv_file, 'r') as f:
                    f_reader = csv.reader(f, delimiter=";")
                    for row in f_reader:
                        if row[1]==country:
                            print(country + " is  on position " + row[0] + " on world countries list with the population of " + row[2] + ".")
            case "b":
                print(selection + " doesn't yet do anything.")
            case "q":
                print("Exiting the program.")
            case _:
                print("Sorry, I didn't understand that, please try again.")

if __name__ == "__main__":
    main()

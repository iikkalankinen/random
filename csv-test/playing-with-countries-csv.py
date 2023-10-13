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
def compare_pops(c1pop, c2pop):
    if c1pop > c2pop:
        return 1
    if c1pop < c2pop:
        return 2
    if c1pop == c2pop:
        return 3
    return 4

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
                            country_specs = country + " is on position " + row[0] + " on world countries list with the population of " + row[2] + "."
                            print(country_specs)
            case "b":
                print("Let's compare populations of two countries")
                print("Choose the first country")
                country1 = get_country(csv_file)
                print("Choose another country to compare with " + country1 + ".")
                country2 = get_country(csv_file)
                while (country1 == country2):
                    print("Hey, choose a different country than " + country1 + "!")
                    country2 = get_country(csv_file)
                country1_pop = 0
                country2_pop = 0
                with open(csv_file, 'r') as f:
                    f_reader = csv.reader(f, delimiter=";")
                    for row in f_reader:
                        if row[1]==country1:
                            country1_pop = row[2]
                        if row[1]==country2:
                            country2_pop = row[2]
                country1_pop_int = country1_pop.replace(" ", "")
                country1_pop_int = country1_pop_int.replace(",", "")
                country1_pop_int = int(country1_pop_int)
                country2_pop_int = country2_pop.replace(" ", "")
                country2_pop_int = country2_pop_int.replace(",", "")
                country2_pop_int = int(country2_pop_int)
                print("Population of " + country1 + " is " + country1_pop + ". " + "Population of " + country2 + " is " + country2_pop + ".")
                comparison = compare_pops(country1_pop_int, country2_pop_int)
                print("Comparison result: " + str(comparison))
                match comparison:
                    case 1:
                        print("1")
                    case 2:
                        print("2")
                    case 3:
                        print("3")
                    case _:
                        print("Error")
            case "c":
                print(selection + "doesn't yet do anything.")
            case "q":
                print("Exiting the program.")
            case _:
                print("Sorry, I didn't understand that, please try again.")

if __name__ == "__main__":
    main()

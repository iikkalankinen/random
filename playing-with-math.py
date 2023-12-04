import math

def get_selection():
    features = {
    "a": "Calculate circle's area",
    "b": "Calculate circle's radius",
    "c": "Calculate circle's circumference",
    "q": "Quit"
    }
    user_selection = ""
    for key, value in features.items():
        print(f"{key}: {value}")
    user_selection = input("Choose one: ")
    return user_selection.lower()

def calculate_circle_area():
    radius = get_value_from_user("circle's area", "radius")
    if radius.isnumeric() == False:
        while(radius.isnumeric() == False):
            print("Let's try again")
            radius = get_value_from_user("circle's area", "radius")
    result = math.pi * int(radius) ** 2
    result = math.floor(result * 100)/100.0
    print("The area for a circle with the radius of " + radius + " is " + str(result))

def calculate_circle_radius():
    print("To calculate the circle's radius, I need one of the following values: diameter, area, circumference")
    user_input = ""
    calc_flag = False
    while(user_input != "q"):
        user_input = input("Choose one value that you already know: a) diameter, b) area, c) circumference, q) quit or don't have any of those: ")
        user_input = user_input.lower()
        match user_input:
            case "a":
                diameter = get_value_from_user("circle's radius", "diameter")
                if diameter.isnumeric() == False:
                    while(diameter.isnumeric() == False):
                        print("Let's try again")
                        diameter = get_value_from_user("circle's radius", "diameter")
                result = int(diameter)/2
                result = math.floor(result * 100)/100.0
                calc_flag = True
                print("The radius for a circle with the diameter of " + diameter + " is " + str(result))
            case "b":
                area = get_value_from_user("circle's radius", "area")
                if area.isnumeric() == False:
                    while(area.isnumeric() == False):
                        print("Let's try again")
                        area = get_value_from_user("circle's radius", "area")
                result = math.sqrt(int(area) / math.pi)
                result = math.floor(result * 100)/100.0
                calc_flag = True
                print("The radius for a circle with the area of " + area + " is " + str(result))
            case "c":
                circumference = get_value_from_user("circle's radius", "circumference")
                if circumference.isnumeric() == False:
                    while(circumference.isnumeric() == False):
                        print("Let's try again")
                        circumference = get_value_from_user("circle's radius", "circumference")
                result = int(circumference) / (2 * math.pi)
                result = math.floor(result * 100)/100.0
                calc_flag = True
                print("The radius for a circle with the circumference of " + circumference + " is " + str(result))
            case "q":
                if calc_flag == False:
                    print("Can't calculate circle's radius. Returning to the main menu.")
                else:
                    print("Returning to main menu.")
            case _:
                print("Sorry, I didn't understand that, please try again.")

def calculate_circle_circumference():
    start_values = {
        "a": "Area",
        "b": "Radius",
        "c": "Diameter",
        "x": "Don't have any of the above",
        "q": "Return to main menu"
    }
    user_input = ""
    while(user_input != "q" and user_input != "x"):
        for key, value in start_values.items():
            print(f"{key}: {value}")
        user_input = input("Choose one: ")
        user_input = user_input.lower()
        match user_input:
            case "a":
                print("a")
            case "b":
                print("b")
            case "c":
                print("c")
            case "x":
                print("x")
            case "q":
                print("q")
            case _:
                print("Sorry, I didn't understand that, please try again.")

def get_value_from_user(what_is_calculated, value_to_ask):
    ret_value = input("To calculate " + what_is_calculated + ", I need a value for " + value_to_ask + ". Your input: ")
    return ret_value

if __name__ == "__main__":
    print("Let's start!")
    selection = ""
    while (selection != "q"):
        selection = get_selection()
        match selection:
            case "a":
                calculate_circle_area()
            case "b":
                calculate_circle_radius()
            case "c":
                calculate_circle_circumference()
            case "q":
                print("Exiting the program.")
            case _:
                print("Sorry, I didn't understand that, please try again.")
import math

def get_selection():
    features = {
    "a": "Calculate circle's area",
    "b": "Calculate circle's radius",
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
    print("The area for a cirlce with the radius of " + radius + " is " + str(result))

def get_value_from_user(what_is_calculated, value_to_ask):
    ret_value = input("To calculate " + what_is_calculated + ", I need a value for " + value_to_ask + ". Your input: ")
    return ret_value

if __name__ == "__main__":
    print("Let's start!\n")
    selection = ""
    while (selection != "q"):
        selection = get_selection()
        match selection:
            case "a":
                calculate_circle_area()
            case "b":
                print("b")
            case "c":
                print(selection + "doesn't yet do anything.")
            case "q":
                print("Exiting the program.")
            case _:
                print("Sorry, I didn't understand that, please try again.")
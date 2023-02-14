calculation_to_units = 24
name_of_unit = "hours"

def days_to_unit(num_of_days):

    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"

def validate_and_execute(user_input):
    #checking if input is a number
    if user_input.isdigit():
        user_input_number = int(num_of_days_element)
        #checking if input is a positive number
        if user_input_number > 0:
            calculated_value = days_to_unit(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered 0, please enter a valid positive number")

    else:
        print("your input is not a number, dont ruin my programme")
user_input = ""
#loops
while user_input != "exit":
    user_input = input("hey user, enter s number of days and i will convert it to hours!\n")
    if user_input != "exit":
        list_of_days = user_input.split(",")

        for num_of_days_element in list_of_days:
            validate_and_execute(num_of_days_element.strip())
    """list_of_days = user_input.split(",")
   # for num_of_days_element in set(list_of_days):*/"""


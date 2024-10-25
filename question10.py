def tuples_to_dictionary():
    # Prompt the user to enter tuples in the format string:integer
    user_input = input("Enter tuples in the format string:integer, separated by commas: ")

    # Convert the input string to a list of tuples
    tuples_list = []
    for item in user_input.split(","):
        key, value = item.split(":")
        tuples_list.append((key.strip(), int(value.strip())))

    # Create a dictionary from the list of tuples
    result_dict = {key: value for key, value in tuples_list}

    return result_dict
result = tuples_to_dictionary()
print("Resulting dictionary:", result)

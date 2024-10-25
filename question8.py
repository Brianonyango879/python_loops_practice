def keys_with_values_greater_than_n():
    # Prompt the user to enter dictionary items in the format key:value
    user_input = input("Enter dictionary items in the format key:value, separated by commas: ")
    n = int(input("Enter an integer n: "))

    # Convert the input string to a dictionary
    items = [item.strip() for item in user_input.split(",")]
    dictionary = {}
    for item in items:
        key, value = item.split(":")
        dictionary[key.strip()] = int(value.strip())

    # Find keys with values greater than n
    keys = [key for key, value in dictionary.items() if value > n]

    return keys

print("Keys with values greater than n:", keys_with_values_greater_than_n())

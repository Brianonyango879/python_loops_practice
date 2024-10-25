def reverse_strings():
    # Prompt the user to enter strings separated by commas
    user_input = input("Enter a list of strings separated by commas: ")
    # Split the input into a list of strings
    strings = [s.strip() for s in user_input.split(",")]

    # Reverse each string in the list
    reversed_list = [string[::-1] for string in strings]

    return reversed_list
print("Reversed strings:", reverse_strings())

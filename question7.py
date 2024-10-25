def remove_duplicates():
    # Prompt the user to enter items separated by commas
    user_input = input("Enter items separated by commas: ")
    # Convert the input into a list by splitting the string
    items = [item.strip() for item in user_input.split(",")]

    # Remove duplicates manually
    unique_items = []
    for item in items:
        if item not in unique_items:
            unique_items.append(item)

    return unique_items

print("List without duplicates:", remove_duplicates())

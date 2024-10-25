def find_largest_in_tuple():
    # Prompt the user to enter numbers separated by commas
    user_input = input("Enter numbers separated by commas: ")
    # Convert the input to a tuple of integers
    numbers = tuple(int(num.strip()) for num in user_input.split(","))

    # Find the largest number
    largest = numbers[0]  # Start with the first element as the largest
    for num in numbers:
        if num > largest:
            largest = num
    return largest
print("Largest number:", find_largest_in_tuple())

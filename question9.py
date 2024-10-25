def has_pair_with_sum():
    # Prompt the user to enter a list of integers separated by commas
    user_input = input("Enter a list of integers separated by commas: ")
    numbers = [int(num.strip()) for num in user_input.split(",")]
    target_sum = int(input("Enter the target sum: "))

    # Check for two numbers that add up to the target sum
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target_sum:
                return True
    return False

result = has_pair_with_sum()
print("Result:", result)

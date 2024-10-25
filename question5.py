#prompt the user to enter keys and  values
def even_keys():
    user_dict = {}
    while True:
        key = input("Enter Key: or 'done' when finished:")
        if key.lower() == 'done':
            break
        try:
            value = int(input("Enter value:"))
            user_dict[key] = value
        except ValueError:
            print("Please enter a valid value")
            #validation
    print("Keys with even value:")
    for key, value in user_dict.items():
            if value % 2 == 0:
                print(f"{key}")
even_keys()

# loop to prompt user
def prompt_user():
    while True:
        user_input = input("Enter a word or type 'exit' to quit:")
        if user_input.lower() == "exit":
            print("Exiting...")
            break
        print(f"You typed: {user_input}")
#call the user
prompt_user()
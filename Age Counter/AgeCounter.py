def check_age():
    while True:
        try:
            age_str = input("Please enter your age: ")
            age = int(age_str)

            if age < 0 or age > 120:
                print("Error: Age must be between 0 and 120.")
            else:
                print(f"You entered: {age}")
                if age % 2 == 0:
                    print("Your age is an even number.")
                else:
                    print("Your age is an odd number.")
                break  # Exit the loop if age is valid
        except ValueError:
            print("Error: Invalid input. Please enter a whole number for your age.")
check_age()
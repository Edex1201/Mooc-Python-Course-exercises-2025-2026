def read_input(prompt,number1,number2):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input >= number1 and user_input <= number2:
                return user_input
            else:
                print(f'You must type in an integer between {number1} and {number2}')
        except ValueError:
            print(f'You must type in an integer between {number1} and {number2}')
numbers = read_input("Please type in a number: ",5,10)          
print("You typed in:", numbers)    
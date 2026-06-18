while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    try:
        user_function = int(input("Function: "))
        if user_function == 1:
            with open ("diary.txt", "a") as new_file:
                user_diary_entry = input("Diary entry: ")
                new_file.write(user_diary_entry + "\n")
        elif user_function == 2:
            print("Entries: ")
            with open("diary.txt") as my_file:
                for i in my_file:
                    print(i)
        elif user_function == 0:
            print("Bye now!")
            break
    except ValueError:
        print("No characters allowed, only numbers (1,2,3)")
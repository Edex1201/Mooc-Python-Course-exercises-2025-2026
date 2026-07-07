#PROBLEM: Create a small dictionary - Translator


with open("dictionary.txt") as file:
    saving_values = []
    for i in file:
        parts = i.strip()
        saving_values.append(parts)
#print(saving_values)
    
while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    try:
        user_input = int(input("Function: "))
        if user_input == 3:
            print("Bye!")
            break
        if user_input == 1:
            adding_german_input = input("The word in German: ")
            adding_english_input = input("The word in English: ")
            with open("dictionary.txt", "a") as file:
                file.write(f'{adding_german_input};{adding_english_input}\n')
            print("Dictionary entry added")
        elif user_input == 2:
            searching_term = input("Search term: ")
            dictionary_of_words = {}
            with open("dictionary.txt") as file:
                for terms in file:
                    terms_separated = terms.strip().split(";")
                    dictionary_of_words[terms_separated[0]] = terms_separated[1]
                for german,english in dictionary_of_words.items():
                    if searching_term == german or searching_term == english or searching_term in german or searching_term in english:
                        print(f'{german} - {english}')

        #     searching_tearm
    except ValueError:
        print("You must enter a number, not a character.")


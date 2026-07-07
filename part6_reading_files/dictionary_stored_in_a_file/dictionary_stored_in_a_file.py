# with open("dictionary.txt") as file:
#     saving_values = []
#     for i in file:
#         parts = i.strip()
#         saving_values.append(parts)
# #print(saving_values)
    
# while True:
#     print("1 - Add word, 2 - Search, 3 - Quit")
#     try:
#         user_input = int(input("Function: "))
#         if user_input == 3:
#             print("Bye!")
#             break
#         if user_input == 1:
#             adding_german_input = input("The word in German: ")
#             adding_english_input = input("The word in English: ")
#             with open("dictionary.txt", "a") as file:
#                 file.write(f'{adding_german_input};{adding_english_input}\n')
#             print("Dictionary entry added")
#         elif user_input == 2:
#             searching_term = input("Search term: ")
#             dictionary_of_words = {}
#             with open("dictionary.txt") as file:
#                 for terms in file:
#                     terms_separated = terms.strip().split(";")
#                     dictionary_of_words[terms_separated[0]] = terms_separated[1]
#                 for german,english in dictionary_of_words.items():
#                     if searching_term == german or searching_term == english or searching_term in german or searching_term in english:
#                         print(f'{german} - {english}')

#         #     searching_tearm
#     except ValueError:
#         print("You must enter a number, not a character.")

def read_dictionary():
    # Words are stored in a list. If the translation would always
    # be to same direction (e.g. from English to Finnish),
    # using dictionary as a data structure would be a good idea
    dictionary = []
 
    with open("dictionary.txt") as file:
        # In the example file, word pair is at one line as
        # finnish;english, for example
        # auto;car
        for row in file:
            row = row.replace("\n","")
            dictionary.append(tuple(row.split(";")))
 
    return dictionary
 
def add_word(dictionary: list):
    word_fi = input("The word in Finnish: ")
    word_en = input("The word in English: ")
    # Add to list
    dictionary.append((word_fi, word_en))
 
    # Write to file
    with open("dictionary.txt", "a") as file:
        file.write(word_fi + ";" + word_en + "\n")
        print("Dictionary entry added")
 
def search_word(dictionary: list):
    word = input("Search term: ")
    for word_fi, word_en in dictionary:
        if word in word_fi or word in word_en:
            print(f"{word_fi} - {word_en}")
 
 
dictionary = read_dictionary()
while True:
    print("1 - Add word, 2 - Search, 3 - Quit")
    function = input("Function: ")
    if function == "1":
        add_word(dictionary)
    elif function == "2":
        search_word(dictionary)
    elif function == "3":
        print("Bye!")
        break
 

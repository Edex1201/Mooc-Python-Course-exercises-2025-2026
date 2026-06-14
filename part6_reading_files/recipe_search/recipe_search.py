#Thi programm allows user to search for recipes based on their names, preparation times, or ingredients.

#user_recipes = input("Please enter the name of a file: ")

# Write your solution here
def search_by_name(filename: str, word: str):
    saving_recipes = []
    saving_a_recipes = []
    dictionary_of_names = {}
    names = []
    with open(filename) as recipes_file:
        for i in recipes_file:
            cleaning = i.strip()
            saving_recipes.append(cleaning)
        for searched_word in range(len(saving_recipes)):
            if len(dictionary_of_names) == 0:
                dictionary_of_names[saving_recipes[searched_word]] = []
            elif saving_recipes[searched_word-1] == "":
                dictionary_of_names[saving_recipes[searched_word]] = []
        for key,value in dictionary_of_names.items():
            if word.lower() in key.lower():
                names.append(key)
    return names


def search_by_time(filename: str, prep_time: int):
    results = []
    current_name = ""
    
    with open(filename) as recipes_file:
        for i in recipes_file:
            cleaning = i.strip()
            try:
                time = int(cleaning)
                if time <= prep_time and current_name != "":
                    results.append(f"{current_name}, preparation time {time} min")
            except ValueError:
                current_name = cleaning
    
    return results

def search_by_ingredient(filename: str, ingredient: str):
    x = []
    return x

# def search_by_ingredient(filename: str, ingredient: str):
#     saving_recipes2 = []
#     with open(filename) as recipes_file:
#         for i in recipes_file:
#             cleaning = i.strip()
#             saving_recipes2.append(cleaning)
#     return saving_recipes2

print(search_by_name("recipes2.txt", "oat"))
print(search_by_time("recipes1.txt", 20))
print(search_by_ingredient("recipes.txt", "eggs"))




#IN DIESER FUNKTION DIE ZWEI DATEIN ÖFFNEN!!! (20:48, 05,06,26)









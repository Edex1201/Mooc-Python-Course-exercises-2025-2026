import re

user_input = input("Write text: ")
saving_user_input = [word for word in re.split(r"[ \s.,!?#]+",user_input) if word]
saving_words = [] #In this list I'm saving all words from the worslist file

saving_word_in_a_dictionary = {}
with open ("wordlist.txt") as new_file:
    for word in new_file:
        part = word.strip().split()
        for i in part:
            saving_words.append(i) #In this list i'm saving all words from the wordlist file
#print(saving_user_input)
text_wo_spaces = "" #variable to save each valid_word in a f-string to add that space in between words
for valid_word in saving_user_input:
    if valid_word.lower() in saving_words:
        text_wo_spaces += f"{valid_word} "
    elif valid_word.lower() not in saving_words:
        text_wo_spaces += f"*{valid_word}* "
print(text_wo_spaces)
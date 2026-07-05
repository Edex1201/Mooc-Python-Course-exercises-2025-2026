def find_words(search_term: str):
    with open("words.txt") as file:
        saving_words = [] #saving all the words from the file (words.txt)
        for i in file:
            parts = i.strip()
            saving_words.append(parts)

#===============================================================================================================

    if "." in search_term:
        saving_words_with_dot = []
        #no =  #looking for this word

        for word in saving_words:
            no_n = "" #saving compared character from the zip loop. Then checking if they're in the dicto variable.
            if len(word) == len(search_term):
                for first,second in zip(word,search_term):
                    if second != ".":
                        no_n += second
                    else:
                        no_n += first
                if no_n == word:
                    saving_words_with_dot.append(no_n)
                #print(no)
        return saving_words_with_dot
    
    elif "*" in search_term:
        saving_words_with_asteric = []
        search_term_copy = search_term.replace("*","")
        for w in saving_words:
            if search_term.endswith("*") and w.startswith(search_term_copy):
                saving_words_with_asteric.append(w)
            elif search_term.startswith("*") and w.endswith(search_term_copy):
                saving_words_with_asteric.append(w)
        return saving_words_with_asteric

        # for w in saving_words:
        #     if w.startswith(search_term_copy) or w.endswith(search_term_copy):
        #         saving_words_with_asteric.append(w)
        # return saving_words_with_asteric
    
    elif search_term in saving_words:
        saving_normal_words = []
        saving_normal_words.append(search_term)
        return saving_normal_words


if __name__ == "__main__":
    print(find_words("reson*"))
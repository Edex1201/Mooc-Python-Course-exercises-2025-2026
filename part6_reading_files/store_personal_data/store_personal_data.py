# Write your solution here
#1 Was soll am Ende herauskommen?
#2 Welche Daten brauche ich dafür?
#3 Wie komme ich an diese Daten?
#4 Muss ich alle Elemente prüfen? (Schleife einbauen)
#5 Muss ich jedes Element mit jedem anderen vergleichen?
#6 Habe ich schon eine Funktion, die einen Teil der Arbeit erledigt? -> benutzen
#7 Muss ich mir den besten/grösten/kleinsten Wert merken?

def store_personal_data(person: tuple):
    with open("people.csv", "a") as new_file:
        s_v = ""
        for i in person:
            s_v += f'{i};'
        s_v = s_v[:-1]
        new_file.write(s_v)
    # with open("people.csv", "w") as new_file:
    #     pass

store_personal_data(("Paul Paulson", 37, 175.5))
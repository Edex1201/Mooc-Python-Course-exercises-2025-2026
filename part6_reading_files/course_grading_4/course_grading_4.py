#Zunächst brauche ich eine Datei, die nur Informationen über den Kurs beinhaltet.

# with open("Course information", "w") as file_a:
#     file_a.write("name: Introduction to Programming\n")
#     file_a.write("study credits: 5")

# #Dann brauche ich einen Dictionary, der am besten die Namen und die Noten speichert.
# #Das wird dann in eine (.Txt) Datei eingefügt werden


saving_c = []
s_i = []
s_i_len = 0
saving_number_of_points = 0
with open("Test", "w") as n_f:
    with open("course1.txt") as f:
        for i in f:
            parts = i.strip("name:").strip("\n")
            parts = parts.strip()
            #parts1 = parts.strip("name:")
            s_i.append(parts)
            saving_c.append(len(i))
    first_line = (f'{s_i[0]}, {s_i[-1][-1]} credits')
    n_f.write(first_line)
    n_f.write("\n")
    n_f.write("="*len(first_line))
    
    #n_f.write("="*max(saving_c))
# with open("Test", "w") as o:
#     pass
# with open("Test", "a") as n:
#     n.write("="*max(saving_c))

print(s_i)
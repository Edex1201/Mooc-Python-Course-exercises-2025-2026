#As we left if last time, the program read and processed files containing student information,
#completed exercises and exam results. We'll add a file containing information about the course. An example of the format of the file: (Example in the official page)
#name: Introduction to Programming
#study credits: 5
#The program should then create two files. There should be a file called results.txt with the following contents:
#Introduction to Programming, 5 credits
#======================================
#name                          exec_nbr  exec_pts. exm_pts.  tot_pts.  grade
#pekka peloton                 21        5         9         14        0
#jaana javanainen              27        6         11        17        1
#liisa virtanen                35        8         14        22        3
#The statistics section is identical to the results printed out in part 3 of the project. The only addition here is the header section.
#Additionally, there should be a file called results.csv with the following format:
#12345678;pekka peloton;0
#12345687;jaana javanainen;1
#12345699;liisa virtanen;3
#When the program is executed, it should look like this:
#Student information: students1.csv
#Exercises completed: exercises1.csv
#Exam points: exam_points1.csv
#Course information: course1.txt
#Results written to files results.txt and results.csv

student_info = input("Student information: ")
exercise_data = input("Exercises completed: ")
exam_points =  input("Exam points: ")
course_info = input("Course information: ")

saving_students_names = {} #Diese Variable enthält auch die ID der Stundenten
with open(student_info) as new_file:
    for i in new_file:
        parts = i.strip().split(";")
        if parts[0] == "id":
            continue
        saving_students_names[parts[0]] = parts[1]+" "+parts[2]
#print(saving_students_names)  

saving_exercise_data = {}
with open(exercise_data) as new_file:
    for i in new_file:
        parts_e = i.strip().split(";")
        if parts_e[0] == "id":
            continue
        saving_exercise_data[parts_e[0]] = [int(x) for x in parts_e[1:]]
    for key_1,val_1 in saving_exercise_data.items():
        saving_exercise_data[key_1]= sum(val_1)
#print(f'exercise_data summed: {saving_exercise_data}')

saving_exam_data = {}#in this dictionary i'm saving the summed exam points.
with open(exam_points) as new_file:
    count= 1
    for i in new_file:
        parts = i.strip().split(";")
        if parts[0] == "id":
            continue
        saving_exam_data[parts[0]] = [int(x) for x in parts[1:]]
        #print(f'runs:{count} from saving_exam_data: {saving_exam_data}')
        count +=1
    for key,val in saving_exam_data.items():
        saving_exam_data[key] = sum(val)  #summing the values of saving_exam_data. They values are lists
#print(f'saving_exam_data_check: {saving_exam_data}')
#print(saving_exam_data)

saving_exam_data_copy = {}
for key,value in saving_exam_data.items():
    saving_exam_data_copy[key] = value
#print(f'THIS IS THE COPY OF THE EXAM VARIABLE: {saving_exam_data_copy}')
awarded_points = {}
total_points = 40
listing_points = {15: 1,16: 1, 17:1, 18:2, 19:2, 20:2, 21:3, 22:3, 23:3, 24:4, 25:4, 26:4, 27:4, 28:5}
for key,value in saving_exercise_data.items():
    percentage = value/total_points*100
    awarded_points[key] = int(percentage/10)
    if percentage >= 10:
        saving_exam_data[key] += int(min(percentage//10,10))
    elif percentage < 10:
        saving_exam_data[key] += 0
#print(f'Awarded points: {awarded_points}')
#print(f'Saving_exam after points: {saving_exam_data}')

students_grade = {} #This variable needs to be a dictionary where I can save the name of the students and the grade that they get!!!

with open("results.txt", "w") as new_file_1, open("results.csv", "w") as new_file_2:
    saving_c = [] #list with the len of each iteration thorugh the file. After that I use the max() funktion to determine the lenght of this part "="
    s_i = []
    with open(course_info) as n:
        for i in n:
            parts = i.strip("name:").strip("\n")
            parts = parts.strip()
            s_i.append(parts)
            saving_c.append(len(i))
    first_line = (f'{s_i[0]}, {s_i[-1][-1]} credits')
    new_file_1.write(first_line)
    new_file_1.write("\n")
    new_file_1.write("="*len(first_line))
    new_file_1.write("\n")
    #new_file_1.write(f'Introduction to Programming, 5 credits\n======================================\n')
    new_file_1.write(f'{"name":<30}{"exec_nbr":<10}{"exec_pts.":<10}{"exm_pts.":<10}{"tot_pts.":<10}{"grade":<10}\n')
    count = 0
    for key,value in saving_exam_data.items():
        students_grade[key] = 0
        if value in listing_points:
            students_grade[key] = listing_points[value]
        elif value > 28:
            students_grade[key] = 5
        else:
            students_grade[key] = 0
    
    for id1,names in saving_students_names.items(): #Students names with ID's are saved in this variable (saving_students_names)
        if id1 in students_grade:
            grade = int((students_grade[id1]))
            new_file_1.write(f'{names:30}{saving_exercise_data[id1]:<10}{awarded_points[id1]:<10}{saving_exam_data_copy[id1]:<10}{saving_exam_data[id1]:<10}{grade:<10}\n')
            new_file_2.write(f'{id1};{names};{grade}\n')
        else:
            continue #new_file_1.write(f'{names} doesnt exist\n')

print("Results written to files results.txt and results.csv")
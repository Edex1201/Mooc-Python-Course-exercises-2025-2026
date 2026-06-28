
import operator

def filter_solutions():
    operations = {
        "+" : operator.add,
        "-" : operator.sub,
        "*" : operator.mul,
        "/" : operator.truediv
    }
    saving_values = []
    saving_symbol = ""
    saving_first_numbers = ""
    saving_converted_first_numbers = [] #saving the problem e.g (2-1) and the result e.g (3)
    saving_second_converted_numbers = 0
    saving_good = []
    saving_bad = []

    with open("solutions.csv") as my_file:
        for value in my_file:
            parts = value.strip().split(";")
            saving_values.append(parts)

    with open("correct.csv", "w") as new_good_file, open("incorrect.csv", "w") as new_bad_file:       
        for i in saving_values:
            saving_first_numbers = ""
            saving_converted_first_numbers = []
            for e in i[1]:
                if e != "+" and e != "-":
                    saving_first_numbers += e
                elif e == "+" or e == "-":
                    saving_converted_first_numbers.append(int(saving_first_numbers))
                    saving_converted_first_numbers.append(e)
                    saving_index = i[1].index(e)
                    saving_converted_first_numbers.append(int(i[1][saving_index+1:]))
                    saving_second_converted_numbers = int(i[2])
                    operation_helper = operations[saving_converted_first_numbers[1]](saving_converted_first_numbers[0],saving_converted_first_numbers[2])
                    if operation_helper == saving_second_converted_numbers:
                        new_good_file.write(f'{i[0]};{i[1]};{i[2]}\n')
                    else:
                        new_bad_file.write(f'{i[0]};{i[1]};{i[2]}\n')
    with open("corrects.csv", "w") as new_ho:
        pass
    
        
            
        
    #print(saving_converted_first_numbers, saving_second_converted_numbers)


filter_solutions()
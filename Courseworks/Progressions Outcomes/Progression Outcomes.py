#I declare that my work contains no example of misconduct, such as plagiarism, or collusion.
#Any code taken from other sources is referenced within my code solution.

#Student ID: 18874792
#Date: 24/11/2022

total_of_credits = 0
TOTAL_CREDITS = 120
marks = range(0, 121, 20)
outcomes = []
final_output = [] 
students = []
dictionary = {}

def studentid_format(student_id):
    character_checker = 'w'
    if len(student_id) < 8 or len(student_id) > 8:
        print('\nThe ID entered is more or less than 8 characters.\n')
        return True
    if str.lower(student_id[0]) != character_checker:
        print("\nThe ID entered is missing a 'w'.\n")
        return True

def progression_outcome(x, y ,z):
    if x == 120:
        print('Progress\n')
        outcomes.append('Progress')
    elif x == 100 and y + z == 20:
        print('Progress (module trailer)\n')
        outcomes.append('Progress (module trailer)')
    elif x < 100 and y <= 120 and z <= 60:
        print('Module retriever\n')
        outcomes.append('Module retriever')
    elif x <= 40 and y <= 40 and z >= 80:
        print('Exclude\n')
        outcomes.append('Exclude')
 
def stars_print():
    stars_progress = 0
    stars_trailer = 0
    stars_retriever = 0
    stars_exclude = 0
    for x in range(len(outcomes)):
        if outcomes[x] == 'Progress':
            stars_progress += 1
        elif outcomes[x] == 'Progress (module trailer)':
            stars_trailer += 1
        elif outcomes[x] == 'Module retriever':
            stars_retriever += 1
        elif outcomes[x] == 'Exclude':
            stars_exclude += 1

    print('Progress', stars_progress,':', '*' * stars_progress)
    print('Trailer', stars_trailer,':', '*' * stars_trailer)
    print('Retriever', stars_retriever,':', '*' * stars_retriever)
    print('Exclude', stars_exclude,':', '*' * stars_exclude)

def print_dictionary():
    for i in range(len(students)):
        students_key = str(students[i])
        dictionary[students_key] = final_output[i]
    for key, value in dictionary.items():
        print(key,':', value)

def write_txt_file():
    with open('Part3.txt', 'w') as write_txt:
        for i in range(len(outcomes)):
            data_set = str(outcomes[i]) + ' - ' + str(final_output[i]) + '\n'
            write_txt.write(data_set)

def read_text_file():
    with open('Part3.txt', 'r') as file:
        print(file.read())

def histogram():
    print("\n-----------------------------------------------------------")
    print('Histogram')
    print('\nPart 1')
    stars_print()
    print()
    print(len(outcomes), 'outcomes in total.')
    print('\nPart 2')
    [print(outcomes[i], ' - ', final_output[i]) for i in range(len(outcomes))]
    print('\nPart 3:')
    read_text_file()
    print('\nPart 4:')
    print_dictionary()
    print("-----------------------------------------------------------")
    
while(True):
    student_id = input('Please enter the student ID: ')
    if studentid_format(student_id):
        continue
    students.append(student_id)

    try:              
        pass_credits = int(input('Enter your total PASS credits: '))
        if pass_credits not in marks:
            print('The PASS credits entered is out of range.\n')
            continue
        defer_credits = int(input('Enter your total DEFER credits: '))
        if defer_credits not in marks:
            print('The DEFER credtis entered is out of range.\n')
            continue
        fail_credits = int(input('Enter your total FAIL credits: '))
        if fail_credits not in marks:
            print('The FAIL credits entered is out of range.\n')
            continue
    except ValueError:
        print('Integer required.\n')
        continue

    total_of_credits = pass_credits + defer_credits + fail_credits

    if total_of_credits != TOTAL_CREDITS:
        print('Total incorrect.\n')
        continue

    progression_outcome(pass_credits, defer_credits, fail_credits)
    string_format = f"{pass_credits}, {defer_credits}, {fail_credits}"
    final_output.append(string_format)
    write_txt_file()

    print('Would you like to enter another set of data?')
    go_on = input("Enter 'y' for yes or 'q' to quit and view results: ")
    if str.lower(go_on) == 'y':
        continue
    elif str.lower(go_on) == 'q':
        break

histogram()
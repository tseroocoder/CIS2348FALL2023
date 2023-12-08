#Michelle Oteri
#2252197
import csv


def extract_major_and_gpa(input_text):
    parts = input_text.split()

    for i in range(len(parts) - 1, -1, -1):
        user_gpa = float(parts[i])
        user_major = ' '.join(parts[:i]).lower()
        return user_major, user_gpa


def read_csv(file_path, name):
    data = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data


def print_students_within_gpa_range(student_data, major, gpa, requested_gpa, gpa_tolerance=0.1):
    print("Your student(s):")

    for student in student_data:
        student_id, first_name, last_name, gpa, graduated, disciplinary_action = student

        if not graduated and disciplinary_action is None:
            gpa_difference = abs(requested_gpa - gpa)
            if gpa_difference <= gpa_tolerance:
                print(f"ID: {student_id}, Name: {first_name} {last_name}, GPA: {gpa}")


def main():
    students_data = read_csv('StudentsMajorsList-3.csv', 'major')
    gpa_data = read_csv('GPAList-1.csv', 'gpa')
    graduation_data = read_csv('GraduationDatesList-1.csv', 'graduation')

    Majors = [inner_list[3] for inner_list in students_data]
    GPA = [inner_list[1] for inner_list in gpa_data]
    graduation_date = [inner_list[1] for inner_list in graduation_data]

    user_input = input("Enter your major and GPA ")

    user_major, user_gpa = extract_major_and_gpa(user_input)

    if user_major not in students_data:
        print("No such student")

    merged_data = []
    for student, gpa, graduation in zip(students_data, gpa_data, graduation_data):
        merged_data.append(student + gpa[1:] + graduation[1:])

        user_input = input("Enter your major and GPA: ")

    user_major, user_gpa = extract_major_and_gpa(user_input)

    merged_data = []
    for student, gpa, graduation in zip(students_data, gpa_data, graduation_data):
        merged_data.append(student + gpa[1:] + graduation[1:])

        user_input = input("Enter your major and GPA: ")

    user_major, user_gpa = extract_major_and_gpa(user_input)

    if user_major in merged_data and len(user_major.split()) == 1 and len(user_gpa.split()) == 1:
        print("Valid submission!")
    else:
        print("No such student")

    for student, gpa, graduation in zip(students_data, gpa_data, graduation_data):
        merged_data.append(student + gpa[1:] + graduation[1:])

        user_input = input("Enter your major and GPA: ")

    user_major, user_gpa = extract_major_and_gpa(user_input)

    merged_data = []

    # Check if the user's major is in the roster and if only one major and GPA are submitted
    if user_major in merged_data and len(user_major.split()) == 1 and len(user_gpa.split()) == 1:
        print("Valid submission!")

        print("Your student(s):")
    for student in merged_data:
        student_major = student[0]
        student_gpa = float(student[1])

    if student_major == user_major and student_gpa >= (float(user_gpa) - 0.1) and student_gpa <= (
            float(user_gpa) + 0.1):
        print(f"Student ID: {student[2]}, Name: {student[3]} {student[4]}, GPA: {student[1]}")

        print("You may also consider:")
    for student in merged_data:
        student_major = student[0]
        student_gpa = float(student[1])

    if student_major == user_major and student_gpa >= (float(user_gpa) - 0.25) and student_gpa <= (
            float(user_gpa) + 0.25):
        print(f"Student ID: {student[2]}, Name: {student[3]} {student[4]}, GPA: {student[1]}")
    else:
        print("No such student")

    # Get user input for major and requested GPA
    user_major = input("Enter your major: ")
    user_gpa = float(input("Enter your requested GPA: "))

    # Print header for the student list
    print("Your student(s):")

    # Initialize variables for tracking the closest GPA
    closest_gpa_diff = float('inf')
    closest_student = None

    # Iterate through the merged data to find the closest GPA student within the requested major
    for student in merged_data:
        student_major = student[0]
    student_gpa = float(student[1])

    # Exclude students who have graduated or had disciplinary action
    if student_major == user_major and student[5] != 'Graduated' and student[6] != 'Disciplinary Action':
        gpa_diff = abs(student_gpa - user_gpa)

        # Check if the current student has a closer GPA to the requested GPA
        if gpa_diff < closest_gpa_diff:
            closest_gpa_diff = gpa_diff
            closest_student = student

    # Check if a student with closest GPA was found within the criteria
    if closest_student:
        print(
            f"Student ID: {closest_student[2]}, Name: {closest_student[3]} {closest_student[4]}, GPA: {closest_student[1]}")
    else:
        print("No students found within the requested major who meet the criteria.")


# Function to get user input for major and requested GPA
def get_user_input():
    user_major = input("Enter your major: ")
    user_gpa = float(input("Enter your requested GPA: "))
    return user_major, user_gpa


# Function to check if the user wants to quit
def check_quit(input_str):
    if input_str.lower() == 'q':
        print("Quitting the program. Goodbye!")
        return True
    return False


# Main program loop
while True:
    # Get user input for major and requested GPA
    user_major, user_gpa = get_user_input()

    # Check if the user wants to quit
    if check_quit(user_major) or check_quit(str(user_gpa)):
        break

    # Print header for the student list
    print("Your student(s):")

    merged_data = [
        ['Computer Science', '3.8'],
        ['Business Administration', '3.5'],
        ['Electrical Engineering', '3.2']
    ]
    # Initialize variables for tracking the closest GPA
    closest_gpa_diff = float('inf')
    closest_student = None

    # Iterate through the merged data to find the closest GPA student within the requested major
    for student in merged_data:
        student_major = student[0]
        student_gpa = float(student[1])

        # Exclude students who have graduated or had disciplinary action
        if student_major == user_major and student[5] != 'Graduated' and student[6] != 'Disciplinary Action':
            gpa_diff = abs(student_gpa - user_gpa)

            # Check if the current student has a closer GPA to the requested GPA
            if gpa_diff < closest_gpa_diff:
                closest_gpa_diff = gpa_diff
                closest_student = student

    # Check if a student with closest GPA was found within the criteria
    if closest_student:
        print(
            f"Student ID: {closest_student[2]}, Name: {closest_student[3]} {closest_student[4]}, GPA: {closest_student[1]}")
    else:
        print("No students found within the requested major who meet the criteria.")

main()


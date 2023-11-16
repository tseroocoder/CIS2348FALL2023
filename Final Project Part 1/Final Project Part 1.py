#Michelle Oteri
#2252197
import csv
from collections import defaultdict

def read_csv_file(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data


students_data = read_csv_file('StudentsMajorsList-3.csv')
gpa_data = read_csv_file('GPAList-1.csv')
graduation_data = read_csv_file('GraduationDatesList-1.csv')

students = defaultdict(dict)
majors = set()


def sort_by_last_name(x):
    return x[3]


def sort_by_student_id(x):
    return x[0]


for row in students_data:
    student_id, last_name, first_name, major, disciplinary = row
    students[student_id] = {'last_name': last_name, 'first_name': first_name, 'major': major}
    majors.add(major)
    if disciplinary:
        students[student_id]['disciplinary'] = True

for row in gpa_data:
    student_id, gpa = row
    students[student_id]['gpa'] = float(gpa)

for row in graduation_data:
    student_id, graduation_date = row
    students[student_id]['graduation_date'] = graduation_date


def write_csv_file(filename, data, header):
    with open(filename, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        for row in data:
            writer.writerow(row)

full_roster = sorted([(student_id, student['major'], student['first_name'], student['last_name'],
                       student['gpa'], student['graduation_date'],
                       'Yes' if student.get('disciplinary') else 'No') for student_id, student in students.items()],
                     key=sort_by_last_name)
write_csv_file('FullRoster.csv', full_roster,
               ['Student ID', 'Major', 'First Name', 'Last Name', 'GPA', 'Graduation Date', 'Disciplinary'])

for major in majors:
    major_students = sorted([(student_id, student['last_name'], student['first_name'],
                              student['graduation_date'],
                              'Yes' if student.get('disciplinary') else 'No') for student_id, student in
                             students.items() if student['major'] == major],
                            key=sort_by_student_id)
    filename = f"{major.replace(' ', '')}Students.csv"
    write_csv_file(filename, major_students,
                   ['Student ID', 'Last Name', 'First Name', 'Graduation Date', 'Disciplinary'])

def sort_by_gpa_descending(x):
    return x[4]


scholarship_candidates = sorted([(student_id, student['last_name'], student['first_name'],
                                  student['major'], student['gpa']) for student_id, student in students.items()
                                 if student['gpa'] > 3.8 and not student.get(
        'disciplinary') and 'graduation_date' not in student],
                                key=sort_by_gpa_descending)
write_csv_file('ScholarshipCandidates.csv', scholarship_candidates,
               ['Student ID', 'Last Name', 'First Name', 'Major', 'GPA'])

disciplined_students = sorted([(student_id, student['last_name'], student['first_name'], student['graduation_date'])
                               for student_id, student in students.items() if student.get('disciplinary')],
                              key=sort_by_last_name)
write_csv_file('DisciplinedStudents.csv', disciplined_students,
               ['Student ID', 'Last Name', 'First Name', 'Graduation Date'])

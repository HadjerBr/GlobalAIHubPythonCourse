students = []
studentsByPassingGrades = []
for i in range(2):
    info = input("\n\nEnter the student number:" + str(i+1) + "'s name, midterm grade, project grade and final grade with blanks between them: ").split()
    name = info[0]
    midterm = float(info[1])
    project = float(info[2])
    final = float(info[3])
    student = {"name": name, "midterm": midterm, "project": project, "final": final}
    print("This student's information:\n ", student)
    student["passing grade"] = passingGrade = round((student["midterm"]*0.3 + student["project"]*0.3 + student["final"]*0.4), 2)
    students.append(student)
    studentsByPassingGrades.append({'name': name, 'passing grade': passingGrade})

print("\n\nAll the students' marks and passing grades:\n", students)

studentsByPassingGrades.sort(key=lambda x: x.get('passing grade'), reverse=True)
print('\n\nAll the students from the highest passing grade to the lowest: \n', studentsByPassingGrades, end=' ')

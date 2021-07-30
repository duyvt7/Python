n = int (input('insert student Number: '))

students = []
for a in range(n):
    name = input('student name: ')
    score = int(input('student score: '))
    students.append([name, score])
print(students)
students = sorted(students, key=lambda x: x[1])
# print(students[n-2][0])
secondLowest = sorted(list(set(x[1] for x in students)))[1]
# print(secondLowest)
desireStudent = []
for x in students:
    if x[1]== secondLowest:
        desireStudent.append(x[0])

print(desireStudent)


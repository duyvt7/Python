n = int (input('insert student Number: '))
ans = []
for a in range(n):
    name = input('student name: ')
    score = int(input('student score: '))
    ans.append([name, score])
print(ans)
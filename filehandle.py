# f= open('demofile.txt', 'r')
# print(f.read(5))
# print(f.readline())
# print(f.readline())
# print(f.readline())

# f=open('demofile.txt','r')
# for x in f:
#     print(x)
# f.close()
# f=open('demofile.txt', 'a')
# f.write('\nsome content to the file')
# f=open('demofile.txt', 'r')
# print(f.read())
# f= open('demofile.txt', 'w')
# f.write('i deleted old content')
# f=open('demofile.txt','r')
# print(f.read())
# f.close()
# f=open('newfile.txt','w')
# f.write('new file created')
# f=open('newfile.txt','r')
# print(f.read())

import os
if os.path.exists('newfile.txt'):
    os.remove('newfile.txt')
else:
    print('the file does not exists')
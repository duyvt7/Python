# import os
# f=open('file','r')
# print(f.readline())
# c=open('file','w')
# c.write('\n them vao cho zui')
# c.close()
# f=open('file','r')
# print(f.read())
# f.close()
# os.remove('file')

f= open('file','w')
f.write('something in the file \n another thing')
f=open('file','a')
f.write('\n add a line to the file')
f=open('file','r')
print(f.read())
f.close()
import os
if os.path.exists('file'):
    os.remove('file')
else:
    print('file does not exists')
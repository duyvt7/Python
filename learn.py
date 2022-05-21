from tkinter import Y


print('hello')
#this is a comment
#multi line comment
# secondline
# third line#
'''comment in multiline
dfdsaf
fsagfg
gfasfsd
'''
#error var names
# 2var (numbers at begining of the name)
# My-var (special signals)
# my var (spaces)#
x = int(2)
x=float(3)
y='hello'
print(type(x))
# print(x+y) error command
print(x,y)

x=y=z=5 #assign variables to a value
x,y,z=5,6,7
x,y,z = [6,7,8]
fruits=['apple', 'banana', 'orange']
x,y,z=fruits
print(x,y,z)


def myfunc():
    global x 
    x='awesome'
    print('python is '+x)

myfunc()
print(x)
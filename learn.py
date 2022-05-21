
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
# x = int(2)
# x=float(3)
# y='hello'
# print(type(x))
# print(x+y) error command
# print(x,y)

# x=y=z=5 #assign variables to a value
# x,y,z=5,6,7
# x,y,z = [6,7,8]
# fruits=['apple', 'banana', 'orange']
# x,y,z=fruits
# print(x,y,z)


# def myfunc():
#     global x 
#     x='awesome'
#     print('python is '+x)

# myfunc()
# print(x)

#
# number : int float complex
# string: str
# list, tuple, set, dict, range
# bool
# bytes, bytearray,memoryview
# none#
# x=5
# print(type(x))
#import random library
# import random
# print(random.randrange(10))
# x='''bc'''
# print(type(x))
# print(x[1])
# print(len(x))
# if 'a' not in x:
#     print('yes')
# else:
#     print('no')
# for i in x:
#     print(i)
b = " Hello, World!  "
# print(b[2:5])
# print(b[5:])
# print(b[-7:-1])
print(b.upper())
print(b.lower())
print(b.strip())
x=b.split(',')
print(x) #return x is a list
a= 'python'
print(a+b)
x,y,z=3,4,5
txt='i want to buy {} eggs with price {} total {}'
print(txt.format(x,y,z))


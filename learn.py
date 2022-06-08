# a='a string too long'
# b='''
# this is
# a
# multiline
# string '''
# # for x in a:
# #     print(x)
# print(a[0])
# print(a.split('t'))
# x=5
# y='b \n \t \' \\{}'
# print(a+b)
# print(y.format(x))
# from re import X


list1=['a','b','b','c']
print(list1[-2:-1])
list1[0]='x'
print(list1[0])
list2=['x','y','z']
list1.insert(2,'a')
print(list1)
list1.extend(list2)
print(list1)
print({x for x in list1 if 'x' in x})


tuple1=('a','b','c')
print(type(tuple1))
tuple1=list(tuple1)
print(tuple1[1])
if 'a' in tuple1:
    print('yes')
else:
    print('no')
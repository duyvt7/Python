# # # x=y=z='5'
# # # print(x,y,z)

# # # from turtle import clear


# # x='apple'
# # # for i in x:
# # #     print(i)

# # print(x.upper())
# # print(x.lower())
# # print(x.strip())

# # y='hello, world'
# # z=y.split(',')
# # print(z)
# # z=y.replace('l','L')
# # print(z)
# # # print(x+' '+y)
# # z=x+' '+y
# # txt='i want to buy {2} eggs with {0} milk and {1} coconuts'
# # x,y,z=[3,4,5]
# # print(txt.format(x,y,z))

# # print ('hello world with')

# # mylist=['apple', 'orange','banana', 'apple', 'orange','banana']
# # # mylist=mylist*2
# # mylist[-3:-1]=['orange', 'apple']

# # mylist.append('hello')
# # mylist.insert(2,"pineapple")
# # mylist.extend([2,3,4])

# # mylist.remove('banana')
# # mylist.pop(0)
# # # del mylist
# # # mylist.clear()
# # print(mylist)
# # for x in range(len(mylist)) :
# #     print(mylist[x])
# # i=0
# # print
# # while i< len(mylist):
# #     print(mylist[i])
# #     i=i+1
# # newlist = [x for x in mylist if 'c' in x]
# # print(newlist)

# # mytuple=('apple', 'orange','banana', 'apple', 'orange','banana')
# # def myFunc():
# #     print('hello')
# # myFunc()
# # def person(name, age):
# #     print(name , age)
# # person("duy",17)

# # def myFunction(*kid):
# #     print(kid)
# # myFunction('duy', 'vu', 'hoang')

# # def myFunc2(child1,child2,child3):
# #     print(child3)
# # myFunc2(child1='a',child2='b', child3='c')

# # def myFunc3(**kid):
# #     print('his name is'+kid['lname'])

# # myFunc3(fname='a', lname='b')

# def myFunction(x):
#     print(x)

# def student(age, grade):
#     print(age, grade)

# student(5,6)

# def func2(*kid):
#     print(kid)

# func2('duy','vu','thu')

# def func3(child1, child2, child3):
#     print(child1, child2, child3)

# func3(child1='a', child2='b', child3='3')

from turtle import clear


txt='  hello, world  '
print(txt[-1:])

print(txt.upper())
print(txt.lower())
print(txt.strip())
print(txt.replace('o','O'))
print(txt.split(','))
# x=5
# print (x,txt)

x,y,z=[2,3,4]
txt2='i want to  buy {}eggs, {} orange, {} banana'
print(txt2.format(x,y,z))


class tv:
    def __init__(abc, size, year):
        abc.size=size
        abc.year=year
    
    def buy(self):
        print('i have bought a TV ', self.size, 'inch')

class LG(tv):
    def __init__(abc, size, year):
        super().__init__(size, year)

A=tv(29, 2020)
print(A.size, A.year)
A.buy()

B=LG(32, 2022)
print(B.size)

def myfunc():
    print('Hello')

myfunc()

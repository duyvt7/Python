
# # #this is a comment
# # #multi line comment
# # # secondline
# # # third line#
# # '''comment in multiline
# # dfdsaf
# # fsagfg
# # gfasfsd
# # '''
# # #error var names
# # # 2var (numbers at begining of the name)
# # # My-var (special signals)
# # # my var (spaces)#
# # # x = int(2)
# # # x=float(3)
# # # y='hello'
# # # print(type(x))
# # # print(x+y) error command
# # # print(x,y)

# # # x=y=z=5 #assign variables to a value
# # # x,y,z=5,6,7
# # # x,y,z = [6,7,8]
# # # fruits=['apple', 'banana', 'orange']
# # # x,y,z=fruits
# # # print(x,y,z)


# # # def myfunc():
# # #     global x 
# # #     x='awesome'
# # #     print('python is '+x)

# # # myfunc()
# # # print(x)

# # #
# # # number : int float complex
# # # string: str
# # # list, tuple, set, dict, range
# # # bool
# # # bytes, bytearray,memoryview
# # # none#
# # # x=5
# # # print(type(x))
# # #import random library
# # # import random
# # # print(random.randrange(10))
# # # x='''bc'''
# # # print(type(x))
# # # print(x[1])
# # # print(len(x))
# # # if 'a' not in x:
# # #     print('yes')
# # # else:
# # #     print('no')
# # # for i in x:
# # #     print(i)
# # # b = " Hello, World!  "
# # # print(b[2:5])
# # # print(b[5:])
# # # print(b[-7:-1])
# # # print(b.upper())
# # # print(b.lower())
# # # print(b.strip())
# # # x=b.split(',')
# # # print(x) #return x is a list
# # # a= 'python'
# # # print(a+b)
# # # x,y,z=3,4,5
# # # txt='i want to buy\' {} \'eggs\n with price {} \n\t\btotal {}'
# # # print(txt.format(x,y,z))

# # # class myclass:
# # #   x=5
# # # a=myclass()
# # # print(a.x)
# # # class person:
# # #   def __init__(self,fname,lname):
# # #     self.fname=fname
# # #     self.lname=lname
# # #   def myMed(abc):
# # #     print('Hello, my name is '+abc.fname)

# # # A=person('duy','vu')
# # # print(A.fname, A.lname)
# # # A.myMed()
# # # A.fname='Duy'
# # # print(A.fname)
# # # # del A.lname

# # # class myClass:
# # #   x=5
# # # p1=myClass()
# # # print(p1.x)

# # # class person:
# # #   def __init__(abc, name, age):
# # #     abc.name=name
# # #     abc.age=age
# # #   def hello(abc):
# # #     print('hello, my name is '+ abc.name )

# # # # class student(person):
# # # #   def __init__(abc, name, age):
# # # #     person.__init__(abc, name,age)

# # # class student(person):
# # #   def __init__(abc, name, age, year):
# # #       super().__init__(name, age)
# # #       abc.graduationYear=year
# # #   def welcome(wc):
# # #     print('welcome', wc.name, wc.age, "to the class ", wc.graduationYear)

# # # A=person('Duy',30)
# # # print(A.age, A.name)
      
# # # B=student('Hung',20, 2022)
# # # print(B.name)
# # # print(B.graduationYear)
# # # B.welcome()

# # class car:
# #   def __init__(self,color,year):
# #       self.year=year
# #       self.color=color
# #   def myCar(abc):
# #     print('the car color ', abc.color, ' is mine' )

# # # class toyota(car):
# # #   def __init__(self, color, year, name):
# # #       car.__init__(self, color, year)
# # #       self.name=name

# # class toyota(car):
# #   def __init__(self, color, year, name):
# #       super().__init__( color, year)
# #       self.name=name

# # A=car('red',2019)
# # print(A.color,A.year)
# # A.myCar()
# # B=toyota('grey',2022, 'vios')
# # print(B.name)
# # B.myCar()

# def myfunc():
#   print('hello')

# myfunc()

def myfunc():
  print('Hello')

myfunc()

def myfunc1(name, age):
  print('hello', name ,' im ', age)

myfunc1('duy', 8)

def myfunc2(*key):
  print('i want to buy', key)
myfunc2('apple', "orange", 'banana')

def myfunc3(child1, child2, child3):
  print(child1)
myfunc3(child1='a', child3='b', child2='c')

def myfunc4(**child):
  print('his name is',child['child1'])

myfunc4(child='a', child1='b')



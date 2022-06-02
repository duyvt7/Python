from calendar import c


def myfunc():
  print('hello')
myfunc()
# def myfunc1(a):
#   print('hello',a)

# myfunc1(5)
# def myfunc2(*a):
#   print('hello',a)
# myfunc2(3,4,5)

# def myfunc3(child1,child2,child3):
#   print('welcome',child1,child2,child3)
# myfunc3(child1='a',child2='b',child3='c')
# def myfunc4(**child1):
#   print('welcome',child1)
# myfunc4(child1='a', child2='b',child3='c')

class tv:
  def __init__(abc, year, size):
    abc.size=size
    abc.year=year
  def buy(abc):
    print('i want to buy this tv')
a=tv(2022,32)
a.buy()
a.size=48
print(a.size)
# del a
print(a.size)

class lg(tv):
  def __init__(abc, year, size):
    super().__init__(year, size)
b=lg(2022,56)
b.buy()
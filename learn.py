from calendar import c


def myfunc():
  print('hello')
myfunc()
def myfunc1(a):
  print('hello',a)

myfunc1(5)
def myfunc2(*a):
  print('hello',a)
myfunc2(3,4,5)

def myfunc3(child1,child2,child3):
  print('welcome',child1,child2,child3)
myfunc3(child1='a',child2='b',child3='c')
def myfunc4(**child1):
  print('welcome',child1)
myfunc4(child1='a', child2='b',child3='c')
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

class TV:
  def __init__(self, size, year):
    self.size=size
    self.year=year    

LG=TV(32,2022)
print(LG.size, LG.year)
# x=y=z='5'
# print(x,y,z)

# from turtle import clear


x='apple'
# for i in x:
#     print(i)

print(x.upper())
print(x.lower())
print(x.strip())

y='hello, world'
z=y.split(',')
print(z)
z=y.replace('l','L')
print(z)
# print(x+' '+y)
z=x+' '+y
txt='i want to buy {2} eggs with {0} milk and {1} coconuts'
x,y,z=[3,4,5]
print(txt.format(x,y,z))
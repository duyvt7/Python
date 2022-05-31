
mylist = ["apple", "banana", "cherry"]
mylist[1]
print(mylist[-1])
mylist[1]='haha'
print(mylist)
mylist.append('a')
print(mylist)
mylist.insert(2,'hehe')
print(mylist)
mylist2=['a',32,'b']
mylist.extend(mylist2)
print(mylist)
mylist.remove(32)
print(mylist)
# del mylist
# print(mylist)
# mylist.clear()
# print(mylist)
mylist.pop(2)
print(mylist)
if 'a' not in mylist:
    print('yes')
else:
    print('no')
# for i in range(len(mylist)):
#     print(mylist[i])


i=0

while i < len(mylist):
    print(mylist[i])
    i=i+1

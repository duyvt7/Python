x = int(input('nhap vao so x = '))
y = int(input('nhap vao so y = '))
z = int(input('nhap vao so z = '))
n = int(input('nhap vao so n = '))

for a in range(x+1):
    for b in range (y+1):
        for c in range (z+1):
            if (a+b+c)!= n:
                print([a,b,c])
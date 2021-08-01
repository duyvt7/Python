a = 'this is a string'
txt1 = a.split(' ')
print (txt1) 
txt2 = '-'.join(txt1)



def split_and_join(line):
    return ('-'.join(line.split(' ')))
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
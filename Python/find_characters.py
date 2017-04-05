def find_char(x,y):
    n = [] #our new list to add strings to
    for each in x:
        if y in each:
            n.append(each)
    print n

l = ['hello','world','my','name','is','Anna']
char = 'a'

find_char(l, char)

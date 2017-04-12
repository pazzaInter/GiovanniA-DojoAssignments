#Odd/Even

def odd_even():
    for each in range(2001):
        if each%2 == 0:
            print "Number is", str(each) + ".", "This is an even number."
        else:
            print "Number is", str(each) + ".", "This is an odd number."

odd_even()

#Multiply

def multiply(l,b):
    for each in range(len(l)):
        l[each] *= b
    return l

a = [2,4,10,16]

print multiply(a,5)

#Hacker Challenge

def layered_multiples(m_fun):
    new_list = []
    for each in m_fun:
        temp_list = []
        for num in range(each):
            temp_list.append(1)
        new_list.append(temp_list)
    return new_list

x = layered_multiples(multiply([2,4,5],3))

print x

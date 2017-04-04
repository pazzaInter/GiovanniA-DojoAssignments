#Multiples
#Part 1
def odd_numbers():
    #this function will odd numbers
    for each in range(1000):
        if each % 2 != 0:
            print each

#Part 2
def multiples5():
    #this function will only print multiples of 5
    for each in range(5,1000001):
        if each % 5 == 0:
            print each

#Sum list
a = [1, 2, 5, 10, 255, 3]

print sum(a) #easy way

def calc_sum(x):
    #this will total the values for a given list
    total = 0
    for each in a:
        total += each
    return total

print calc_sum(a)

#Average list
a = [1, 2, 5, 10, 255, 3]

def average(x):
    #This will return the average of a given list
    average = 0
    total = 0
    for each in x:
        total += each
    average = total / len(x)
    return average

print average(a)

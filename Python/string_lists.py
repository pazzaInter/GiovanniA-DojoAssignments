//Find and replace
str = "It's thanksgiving day. It's my birthday, too!"

first_idx = str.find('day')

postion = first_idx, first_idx + (len('day') - 1)

print "Position of the word day in", str, "is", postion

new_str = str.replace(' day', ' month')

print new_str

//Min and Max
x = [2,54,-2,7,12,98]

minimum = min(x)
maximum = max(x)

print "The minimum and maximum of", x, "is", minimum, "and", maximum

//First and Last
x = ["hello",2,54,-2,7,12,98,"world"]

first = x[0]
last = x[len(x)-1]

print "First value in list:", first
print "Last value in list:", last

new_list = [first, last]

print new_list

//New List
x = [19,2,54,-2,7,12,98,32,10,-3,6]

x.sort()

first_half = x[:len(x)/2]
second_half = x[len(x)/2:]

new_x = []

new_x.append(first_half)

for each in second_half:
    new_x.append(each)

print new_x

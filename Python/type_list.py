def type_list(x):
    total = 0
    final_word = ''
    mixed = 0 #this should not be greater than 0 if the type is the same
    first_type = type(x[0])
    for each in x:
        if isinstance(each, int):
            total += each
        elif isinstance(each, str):
            final_word += " " + each
        if type(each) != first_type:
            mixed += 1
    if mixed > 0:
        print "The array you entered is of a mixed type"
        print "Sum: " + str(total)
        print "String:" + final_word
        print mixed
    elif first_type == int:
        print "The array you entered is an integer type."
        print "Sum: " + str(total)
    elif first_type == str:
        print "The array you entered is a string type."
        print "String:" + final_word

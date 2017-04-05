def comparison(x,y):
    if len(x) != len(y):
        #This will immediately eliminate lists that are different sizes
        print "The lists are not the same."
    else:
        counter = 0 #This counter will increment for each matchching value between lists
        for each in x:
            if each == y[counter]:
                #for each match in lists we will increment the counter to check the next index of the second list, no match and we break the loop
                counter += 1
            else:
                break
        if counter == len(x):
            print "The lists are the same!"
        else:
            print "The lists are not the same."

list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]

# list_one = [1,2,5,6,5]
# list_two = [1,2,5,6,5,3]
#
# list_one = [1,2,5,6,5,16]
# list_two = [1,2,5,6,5]
#
# list_one = ['celery','carrots','bread','milk']
# list_two = ['celery','carrots','bread','cream']

comparison(list_one, list_two)

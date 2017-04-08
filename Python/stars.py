#Create a function called draw_stars() that takes a list of numbers and prints out *.

def return_stars(x):
    for each in x:
        #check if the item is a string
        if isinstance(each, str):
            #if string then print the first letter for the length of the string
            print each[0].lower() * len(each)
        else:
            #just pring out * the number of times the value in the list is
            print "*" * each

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

return_stars(x)

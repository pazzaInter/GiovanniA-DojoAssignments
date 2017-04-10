name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(list1,list2):
    new_dict = zip(list1,list2)
    new_dict = dict(new_dict)
    print new_dict

make_dict(name, favorite_animal)


#Hacker Challenge

def make_dict2(list1, list2):
    #whichever list is larger will be used as the keys
    if list1 >= list2:
        new_dict = zip(list1,list2)
        new_dict = dict(new_dict)
        print new_dict
    else:
        new_dict = zip(list2,list1)
        new_dict = dict(new_dict)
        print new_dict

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

make_dict2(name, favorite_animal)

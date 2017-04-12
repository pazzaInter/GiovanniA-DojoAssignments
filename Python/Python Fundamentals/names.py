#Part 1

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def print_students(x):
    counter = 0 #will be used to count index in list
    for each in x:
        print x[counter]["first_name"], x[counter]["last_name"]
        counter += 1 #move onto next index


print_students(students)


print '' #separate print out of code above and below
#Part 2

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def print_users(x):
    for each in users:
        print each
        counter = 0 #will be used to count index in list
        for first, last in users[each]:
            fname = users[each][counter][first]
            lname = users[each][counter][last]
            print counter + 1, "-", fname, lname, "-", len(fname) + len(lname)
            counter += 1 #move onto next index

print_users(users)

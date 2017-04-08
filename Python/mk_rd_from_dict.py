#Create a dictionary containing some information about yourself. The keys should include name, age, country of birth, favorite language.

bio = {"name": "Me", "age": 99, "birth country": "USA", "favorite language": "Python"}

def print_bio(x):
   print "My name is", bio["name"]
   print "My age is", bio["age"]
   print "My country of birth is", bio["birth country"]
   print "My favorite programming language is", bio["favorite language"]

print_bio(bio)

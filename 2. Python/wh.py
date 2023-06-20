# while loop : a statement that will execute it's block code,
#              as long as it's condition remain true

#while 1 == 1:
#    print("oh, i'm stuck in a loop!")

name = ""

while len(name) == 0:
    name = input("Enter your name: ")

print("Hello " + name)


age = None

while not age:
    age = input("Enter your age: ")

print("Oh, it's you again, and you're age is " + age)

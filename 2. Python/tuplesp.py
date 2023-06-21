# tuple = collection which isordered and unchangeable
#         used to group together related data

student = ("Newt",18,"Male")

print(student.count("Newt")) # how many times value appears

print(student.index("Male")) # find the index of the value, the position

for x in student: # for to print all the values in students
    print(x)      

if "Newt" in student:       # if the value "" is in the var student then print that
    print("Newt is here!")

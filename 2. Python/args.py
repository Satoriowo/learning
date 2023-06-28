# *args = parameter that will pack all arguments into a tuple

#def sum(num1,num2):
#    sum_ = num1 + num2
#    return sum_
#print(sum(2,5))

def add(*args):
    sum = 0 
    for i in args:
        sum +=i
    return sum

print(add(2,3,4))

def add2(*stuff):
    sum = 0
    stuff = list(stuff)
#   stuff[0] = 0 # to change an element of stuff
    for i in stuff:
        sum += i
    return sum

print(add2(1,2,4,5,6))

# *kwargs = parameter that will pack all arguments into a directionary
#           useful so that a function can accept a varying amount of keyword arguments

def hi(**kwargs): #there kwargs is like 'dictionary' where var first, middle and last are saved here
   # print('Hi ' +kwargs['first'] + ' ' + kwargs['last'])
    print('Hello', end=' ')
    for key,value in kwargs.items():
        print(value, end=' ')

hi(first='Newt',middle="Owo",last='Study')

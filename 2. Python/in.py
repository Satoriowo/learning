name = (input("What's your name?: ")) #solo usamos input pq automaticamente es un valor str
age = int(input("What's your age?: ")) #we use int(input()) para que el valor que reciba sea un int y es lo que ocupamos
height = float(input("What's your height?: ")) # float(input()) para que el valor recibido sea el de float

print("So your name is " +name)
print("You are " + str(age) + " years old")
print("and then ,your height is " + str(height) + " cm")

# logical operators (and, or, not) = used to check if 2 or more conditional statements is true!

temp = int( input("Whats the temperature outside?: "))

if temp >= 0 and temp <= 30: # es un "y"
    print("The temperature is good for today")
    print("so, go outside dude!!")
elif temp < 0 or temp > 30: # es un "o"
    print("The temperature is bad today :c")
    print("Stay inside!, is for your health")

# scope = Region that a variable is recognized
#         Variable that is only avaible from i nside the region it's created.
#         Global and locally scoped versions of a variable can be created

#name = 'Newt' and if we uncomment this line and line 12, then there isn't error, because variable name is now out of the function and is now a global variable
def display_name():
    name = "Newt" # its a local scope, only avaible inside this function
    print(name)

display_name()

#print(name) if we uncomment this line, there will be an error, because variable name is only avaible in function 'display_name'

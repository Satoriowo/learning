# index operator [] = gives access to a sequence's element (str, list, tuples)

name = 'newt Study'

#if(name[0].islower()): # if the first letter in name is lower, then
#    name = name.capitalize() # if that's true, capitalize the first letter

first_name = name[0:4].upper()
last_name = name[5:].lower()
last_character = name[-1]

print(first_name) 
print(last_name)
print(last_character)

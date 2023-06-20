# slicing = create a substring by extracting elements from another string
#           indexing[] or slice ()
#           [start:stop:step]

name = "Newt Study"

first_name = name[:4] #[start:stop] it starts on 0*
last_name = name[5:] #start:stop
funky_name = name[0:10:1] #start : stop : step/cada cuantas letras se registra
# tmb en la var anterior se imprime todo el "name"

reversed_name = name[::-1]

print(reversed_name)
print(funky_name)
print(first_name)
print(last_name)

#ejercicio

website = "https://google.com"

slice = slice(8,-4)

print(website[slice])

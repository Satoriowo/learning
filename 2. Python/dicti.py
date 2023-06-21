# dictionary = A changeable, unordered collection of unique key: value pairs
#              Fast because they use hashing, allow us to acces a value quickly

capitals = {'USA':'Washington DC',
            'Mexico':'CDMX',
            'China':'Beijing',
            'Russia':'Moscow'}

capitals.update({'Germany':'Berlin'}) # update/put another key,value
capitals.update({'USA':'New York'}) #update key,value
capitals.pop('China') # remove the pair of key you selected
#capitals.clear()

#print(capitals['Mexico'])
#print(capitals.get('Germany')) in this form it doesn't give us an error just 'error'

#print(capitals.keys()) print just keys
#print(capitals.values()) print just values
#print(capitals.values()) print all

for key,value in capitals.items():
    print(key,value)

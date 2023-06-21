# set = collection which is unordered, unindexed. NO duplicate values!

utensils = {'fork','spoon','knife'}
dishes = {'bowl','plate','cup','knife'}
# don't print duplicate values, just print it 1 time
# is more 'faster' if u need to check items, than list

#utensils.add('napkin')
#utensils.remove('knife')
#utensils.update(dishes) put both together and then print it out
# for x in utensils:
#       print(x)

#if u want to print it but u have a single variable:
dinner_table = utensils.union(dishes)

for x in dinner_table:
    print(x)

print(dishes.difference(utensils))
print(utensils.intersection(dishes))

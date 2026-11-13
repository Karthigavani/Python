#SET:
##a={'a','app','1'}
##print(type(a))

#To add in a set-add, update.
##a={'a','app','1'}
##a.add('look')
##print(a)

##a.update('2345')#it adds as a single element
##print(a)

#Delete-Remove, discard, pop.
##a={'a','app','1'}
##a.remove('a') 
##print(a)
##a.remove('b') #if elements not present in the set it gives error
##print(a)

##a.discard('a')
##print(a)
##a.discard('b') #if elements not present in the set doesnt gives error
##print(a)

#pop- it deletes one element randomnly & doesnt able to give any index value.
##a.pop()
##print(a)

#SET operations-union, intersection, difference,
#symmetric difference, disjoint, superset, subset.
a={'a','b','c'}
b={'a','d'}
print(a.union(b)) #combines two set, dont allow the duplicate values.
print(a.intersection(b)) #shows the common elements.
print(a.difference(b)) #shows the remaining elements other than common.
print(a.symmetric_difference(b)) #shows the remaining elements in both the sets.
print(a.isdisjoint(b)) #checks whether there is no common elements between two.
print(a.issuperset(b)) 
print(b.issubset(a))





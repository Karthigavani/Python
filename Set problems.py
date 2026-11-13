#SET:
#1.Write a Python program to remove item(s) from a given set.
##a={3,'hi',1.5,4,'hello'}
##a.discard(3)
##print(a)
##
##a.pop()
##print(a)

#2.Write a Python program to remove an item from a set if it is present in 
#the set.
##a={3,'hi',1.5,4,'hello'}
##if 'hi' in a:
##    a.remove('hi')
##    print(a)
##else:
##    print('not found')

#3.Write a Python program to create set difference.
##a={'a','b','c','d'}
##b={'a','e','f','d'}
##print(a.difference(b))
##print(a.symmetric_difference(b))

##4.Write a Python program to remove all elements from a given set.
##a={'a','b','c','d'}
##a.clear()
##print(a)

##5.Write a Python program to find the maximum and minimum values in 
##a set
##a={30,5,10,40,50}
##print(max(a))
##print(min(a))
##print(sum(a))

##method: 2
##a=[30,5,100,40,50]
##b=a[0]
##for i in a:
##    if i>b:
##        b=i
##print(b)

##6.Find union, intersection, and difference between two sets.






##7.Check if two sets are disjoint.
##8. Remove all elements divisible by 2 from a set of numbers.
##a={30,5,11,40,57}
##a=list(a)
##for i in a:
##    if i%2==0:
##        a.remove(i)
##print(a)
        
##9.Find elements present in only one of two sets (symmetric difference).

#LIST:
##a=[1,2,3,'app',5.2,None,True,4]
##print(a)
##print(type(a))

#length-starts from 1,2..but ends in before the end value.
#index-starts from 0,1..but ends in before the end value.
##print(len(a))
##a=[1,2,['jan','feb,'mar'],'app',5.2,None,True,4]
##print(len(a))

#slicing-based on index value.
##print(a[1:5])
##a=[1,2,['jan','feb,'mar'],'app',5.2,None,True,4]
##a[1:3]='rose','welcome'
##print(a)
##a[2:2]=['sunflower']
##print(a)


#Replace-based on index value-can replace a word and a list.
##a[1]='computer' 
##print(a)
##a[2]=['jan','feb,'mar']
##print(a)

#Adding in list - append, extend, insert.
#Append- add at the end of the list.
#1. Append as a element at the end.
##k=['a','b','c','d']
##k.append('lily')
##print(k)

#2. Append a list at the end,shows it as a single element.
##m=['e','f']
##k.append(m)
##print(k)
##k.extend(m)
##print(k)

#Extend- it adds a element at the end, by separting each word into a single string.
##k=['a','b','c','d']
##k.extend('lily')
##print(k)

#insert - takes index value 0,1.. and inserts the given value in the index position.
##k.insert(1,'22')
##print(k)

#Deleting in list-pop, remove.
#pop - removes based on index value.
##k=['a','b','c','d']
##k.pop()
##print(k)

##k=['a','b','c','d']
##k.pop(1)
##print(k)

#reverse pop- takes the index value but starts from -1, -2,..
##k=['a','b','c','d']
##k.pop(-1)
##print(k)

#To get the index value.
##k=['a','b','c','d']
##z=k.index('b')
##print(z)

#to get index value of a element, starts from the index 2.
##k=['a','b','c','d','b']
##z=k.index('b',2)
##print(z)

#To get the count value.
#count-it counts the total times the element presents in a set.
##a=[1,2,3,'app',5.2,None,True,4]
##b=a.count('app')
##print(b)
##a=[1,2,3,'app',5.2,None,['new','app'],True,4,['a','b',['new','app']]]
##print(len(a))
##b=a.count(['new','app'])
##print(b)

##li=['new,app']
##print(len(li))
##li=['new','app']
##print(len(li))

#To reverse a list:
##a=[1,2,3,'app',5.2,None,True,4]
##a.reverse()
##print(a)

#to reverse using slicing:
##r=a[::-1]
##print(r)

#Number sort:
##a=[1,2,3,4,5]
#ascending order
##a.sort()
##print(a)

#descending order
##a=[1,2,3,4,5]
##a.sort(reverse=True)
##print(a)

#letters sort:
##a=['a','b','c','d','e']
##b=['a','1','b','2','c','3']
##c=['c','e','a','d','b']
##c.sort()
##print(c)

#sort first numbers & then sorts the alphabets
##b.sort()
##print(b)

#to get an empty list:
##a.clear()
##print(a)

#to copy a list:
##n=a.copy()
##print(n)
##a.extend('app')
##print(a)
##print(n)

#to join list without extend:
##print(a+b)

#method:2 for loop:
##a=['a','b','c','d','e']
##m=['','2']
##for i in a:  
##    m=m+list(i)
##print(m)







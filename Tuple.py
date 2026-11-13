#Tuple:
##a= 'a','b','c','d','e'
##b=('a','b','c','d','e')
#while tuple(), give all the characters as 1 arguments.
##c=tuple('a,b,c,d,e')
##print(type(a))
##print(type(b))
##print(type(c))

#membership operator:(in, not in-used in string, list, tuple, dictionary)
##a= 'a','b','c','d','e'
##d=['hello','world']
##print('e' in a )
##print('world'not in d)
##print('world'in d)
##print('so' in d)
##print('so'not in d)

#Identity operator:(is, is not-compare the memory location of two objects)
##a=10
##b=20
##c=a
##print(a is c)
##print(a is not c)
##print(a is b)
##print(id(a))

#To count in tuple: it counts total times the character present in a tuple.
##a= 'a','b','c','d','e','c'
##b=a.count('c')
##print(b)

#To get index value in tuple:
##a= 'a','b','c','d','e','c'
##print(a.index('c'))

#To change in tuple:
a='a','b','c','d','e','c'
#to change into list:
b=list(a)
print(b)
#to change into tuple:
c=tuple(b)
print(c)



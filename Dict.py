#Dictionary:
##a={'name':'karthiga'}
##b={'name':'karthiga','age':'20','course':'python','year':'2026'}
##print(a)
##print(b)
##c={}
##d=set()
##print(type(c))
##print(type(d))

###Replace:
##print(b['year'])
##print(b['name'])
##
##b['age']=22
##print(b)
##
###Add as new if not exist
##b['year']=2027
##print(b)


#Delete-pop,popitem,clear.
##a={'name':'karthiga'}
##b={'name':'karthiga','age':'20','course':'python','year':'2026'}
##b.pop('age') #must give key & remove both key and value.
##print(b)
##b.popitem() #remove last key and value.
##print(b)
##a.clear()
##print(a)

#To Add-update, setdefault.
##b={'eng':70,'tam':80}
##a.update(b) #to join/add two dictoionary
##print(a)

##b.setdefault('age','20') #If the key already present-no change
##print(b)
##b.setdefault('math',90) #If key not present add as new value
##print(b)

#Key and values
##a={'name':'karthiga'}
##b={'name':'karthiga','age':'20','course':'python','year':'2026'}
##print(b.keys()) #Keys in dictionary
##print(b.values()) #Values in dictionary
##print(b.items()) #give keys and values as list in tuple
##print(b['age'])
##print(b.get('age'))

#adding values to list and changing as dictionary:
##a=['name','age','course']
##b=dict.fromkeys(a,20)
##print(b)

#two list runs simultaneously:
##a=['n1','n2','n3','n4','n5']
##b=[5,10,15,20,25]
##for i,j in zip(a,b):
##    print(i,j)
    
#List to dictionary:
##a={'name':'karthiga'}
##b={'name':'karthiga','age':'20','course':'python','year':'2026'}
##d=dict(zip(a,b))
##print(d)
##print(type(d))


##a=[1,2,3,4]
s={'name':"karthiga",'age':20,'course':'python','name':'abc','num':20}
##for i in s:
##    print(i)
##     print(i,s[i]) # i=name, s[i]=malini

##for i,j in s.items():
##    print(i,j)


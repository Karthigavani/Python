#List:
#Converting two list to a dictionary without using zip.
##a=['1','2','3']
##b=['4','5','6']
##c={} #Empty dictionary.
##for i in range(len(a)):
##    print(a[i],'=',b[i])

##for i in range(len(a)):
##   c[a[i]]=b[i] #a[i]-key & b[i]-value.
##print(c)

#1..Write a Python program to insert items into a list in sorted order.
##a=[25, 45, 36, 47, 69, 48, 68, 78, 14, 36]
##print('original list',':', a)
##a.sort()
##print('Sorted list:', a)


##2.Write a Python program to sum all the items in a list.
##a=[10, 20, 30, 40, 50]
##b=0
##for i in a:
##    b=b+i
##print(b)

#method:2
##print(max(a))
##print(min(a))
##print(sum(a))

#3.Write a Python program to get the largest number from a list.
a=[10, 20, 30, 40, 50]
for i in a:
    
##a.sort(reverse=True)
##print(a)
##b=a[0]
##print(b)

#4.Write a Python program to remove duplicates from a list.
##a=[10, 20, 10, 30, 20, 40, 30,20]
##b=[]
##for i in a: #10,
##    if i not in b: #10, 20, 10(xx checks already present, if present it adds.), 30, 20(xx),40,30(xx)
##        b.append(i)
##    else:
##        c=a.count(i)
##        print(i,'=',c)
##print(b)

#5.Write a Python program to clone or copy a list.
##a=[10, 20, 10, 30, 20, 40, 30,20]
##b=a.copy()
##print(b)

#6.Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
##a=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
###using pop:
##a.pop(0)
##print(a)
##a.pop(3)
##print(a)
##
###method:2 using remove
##a.remove('Red')
##a.remove('Pink')
##a.remove('Yellow')
##print(a)

##7.Write a Python program to print the numbers of a specified list after 
##removing even numbers from it.
##a=[25, 45, 36, 47, 69, 48, 68, 78, 14, 36]
##b=[]
##c=[]
##for i in a:
##    if i%2==1:
##        b.append(i)
##    else:
##        c.append(i)
##print('Odd number:', b)
##print('Even number:', c)

#8.Write a Python program to access the index of a list.
##a=['25','45', '36', '47', '69', '48', '68', '78', '14', '36']
##b=a.index(47)
##print(b)

##print(a)
##b=input('enter a number:')
##c=a.index(b)
##print(c)

##9.Write a Python program to append a list to the second list.
##a=['1','2','3']
##b=['4','5','6']
##for i in b:
##    a.append(i)
##print(a)

##10.Find common elements between two lists
##a=[10, 20, 30]
##b=[40, 10, 20]
##for i in a: 
##    if i in b: 
##        print(i)

#11. Find elements present in one list but not in another.
##a=[10, 20, 30]
##b=[40, 10, 20]
##for i in a:
##    if i not in b:
##        print(i)
##for i in b:
##    if i not in a:
##        print(i)

#12. Count how many even and odd numbers are in a list.
##a=[25, 45, 36, 47, 69, 48, 68, 78, 14, 36]
##b=[]
##c=[]
##for i in a:
##    if i%2==1:
##        b.append(i)
##    else:
##        c.append(i)
##print('Odd number:', b)
##print('Even number:', c)
##print('Odd number len:',len(b))
##print('Even number len:',len(c))

##13.Separate positive and negative numbers into two lists.
##a=[1,2,3,-4,-5,-6]
##b=[]
##c=[]
##for i in a:
##    if i>=0:
##        b.append(i)
##    else:
##        c.append(i)
##print('Positive numbers:',b)
##print('negative numbers:',c)

    



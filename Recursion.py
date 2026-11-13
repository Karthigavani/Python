#Recursion-----

##def fun():
##    a=1
##    while a<=10:
##        print(a)
##        a=a+1
##    fun()
##fun()

#1.Print numbers from 1 to n using recursion.
##n=int(input('Enter a no:'))
##def num_ber():
##    k=1
##    while k<=n:
##        print(k)
##        k=k+1
##    num_ber()
##num_ber()

#2.Print numbers from n to 1.
##n=int(input('Enter a no:'))
##def num_ber():
##    k=n
##    while k>0:
##        print(k)
##        k=k-1
##    num_ber()
##num_ber()

#3.Find factorial of a number.
##def factorial(n):
##    m=1
##    for i in range(1,n+1):
##        m=m*i
##        print(m)
##    factorial(n)
##factorial(5)

#4.Find sum of first n natural numbers.
##def natural(a):
##    s=0 #to store sum values
##    i=1 #for range one by one.
##    while i<=a: #0,1,2,3,4,5
##        s=s+i 
##        i=i+1  
##    print(s)
##    natural(a)
##natural(5)

#5.Count the number of digits in a number.
##def count(a):
##    if a<10:
##        print('Single digit')
##    else:
##        print('double digit')
##    count(a)
##count(6)

#6.Find sum of digits of a number.
##def sum(a):
##    k=a%10
##    print(k)
##    l=k%10
##    print(l)
##    v=k+l
##    print(v)
##sum()
        
        

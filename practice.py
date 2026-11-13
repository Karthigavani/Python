#if condition:
#syntax:
#if <condition>:
    #statement
##a=25
##b=45
##c=15
##if a>b and a>c:
##    print('a=25 is greater')
##if b>a and b>c:
##    print('b=45 is greater')
##if c>a and c>b:
##    print('c=15 is greater')

##a=int(input('enter the year:'))
##if a%4==0:
##    print(a,'is a leap year')

##a=int(input('Enter a number:'))
##if a%3==0 and a%5==0:
##    print(a,'is divisible by both 3 and 5')

##ch=input('Enter a character:')
##if ch>='A' and ch<='Z':
##    print(ch, 'is uppercase.')

##a=int(input('Enter a number:'))
##if a>0:
##    print(a,'is a positive number')
##if a==0:
##    print(a,'is zero integer')
##if a<0:
##    print(a,'is negative number')

##a=10
##b=55
##c=100
##if a>b and a<c:
##    print(a,'is the middle no')
##if b>a and b<c:
##    print(b,'is the middle no')
##if c>a and c<b:
##    print(c,'is the middle no')
##if a<b and a>c:
##    print(a,'is the middle no')
##if b<a and b>c:
##    print(b,'is the middle no')
##if c<a and c>b:
##    print(c,'is the middle no')

##a=int(input('Enter the no:'))
##b=int(input('Enter the no:'))
##c=int(input('Enter the no:'))
##
##if a+b>c:
##    print('valid traingle')
##if a+c>b:
##    print('valid triangle')
##if b+c>a:
##    print('valid triangle')

##a=int(input('Enter the units:'))
##if a<=100:
##    print('Total bill:', a*2)
##if a>100 and a<= 200:
##    print('Total bill:', a*3)
##if a>200 and a<=300:
##    print('Total bill:', a*5)
##if a>300:
##    print('Total bill:', a*7)

##a=int(input('Enter the marks:'))
##if a>=90 and a<=100:
##    print('Grade A')
##elif a>=80 and a<=89:
##    print('Grade B')
##elif a>=70 and a<=79:
##    print('Grade c')
##elif a>=60 and a<=69:
##    print('Grade D')
##else:
##    print('Grade F')

##a=int(input('Enter the number:'))
##if a>=100 and a<=999:
##    if a%7==0:
##        print('Its 3 digit and div by 7')
##    else:
##        print('not divisible by 7')
##else:
##    print('Not a 3 digit number')

##a=int(input('Enter the number:'))
##b=int(input('Enter the number:'))
##c=int(input('Enter the number:'))
##d=int(input('Enter the number:'))
##if a>b and a>c and a>d:
##    print('a is the largest number')
##elif b>a and b>c and b>d:
##    print('b is the largest number')
##elif c>a and c>b and c>d:
##    print('c is the largest number')
##else:
##    print('d is the largest number')

##a=int(input('Enter the DATE:'))
##a=int(input('Enter the MONTH:'))
##a=int(input('Enter the YEAR:'))

##li=[60,20,40,10,50,30]
##for i in range(len(li)): #0,6 ----- 0, 1, 2 3
##    for j in range(i + 1, len(li)): #-----(0+1,6) (2) (3) (4)
##        if li[i]>li[j]: #60>60, 20>40, 40>10, 
##            li[i],li[j]=li[j],li[i] 2,3=3,2(40,10=10,40)
##print(li)


#For loop :(syntax)
##for i in range(11):
##    print(i)

##for reverse in range(10,0,-1):
##    print(reverse)

##for even in range(1,11):
##       if even%2==0:(checks the condition is true or false, it goes to the next step only if its true.)
##        print(even)
        
##for even in range(2,11,2):
##    print(even)

##for even in range(1,10,2):
##    print(even+1)

##k=2
##while k <= 20:
##    print(k)
##    k=k+2

##numbers = list(range(2, 21, 2))
##for i in numbers:
##    print(i)

##for odd in range(1,20,2):
##    print(odd)

##for i in range(1,20):
##    if i%2==1:
##        print(i)

##for a in range(1,51):
##    print(a)

##for nat_num in range(1,11):
##    print(nat_num)

##for who_num in range(0,10):
##    print(who_num)

#ques: num btw 20 & 40.
##for a in range(21,40):
##    print(a)

##m=0
##for a in range(1,11):
##    m=m+a
##print(m)

##m=0
##for a in range(1,21):
##    if a%2==1:
##        m=m+a
##print(m)
        
##m=0
##for a in range(1,21):
##    if a%2!=0:
##        m=m+a
##print(m)

##m=1        
##for i in range(1,6):
##    m=m*i
##print(m)

##n=int(input('Enter no:'))
##m=0
##for i in range(1,n+1):
##    m=m+i
##print(m)
    
##for i in range(1,11):
##    print('5','x',i,'=',5*i)

##n=int(input('Enter no:'))
##for i in range(1,11):
##    print(n,'x',i,'=',n*i)

##for i in range(1,6):
##    for j in range(1,11):
##        print(i, "x", j, "=", i * j)
##    print()

##for i in range(1,11):
##    for j in range(1,11):
##        print(i,'x',j,'=',i*j)
##    print()













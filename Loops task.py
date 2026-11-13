##1. Loop syntax.
'''for <variable>in range(start, stop, increment/decreament):
    statement

2. print numbers in terms of 5.
for i in range(5,101,5):
    print(i)

3. python program from user and reverses it.
##a='karthiga'
a=input('Enter the word: ')
#01234567
 print(a[::-1])

4.output in a vertical order.
b=a[1:5:1]
for i in b:
    print(i)

##5. python program that accepts a strings and calculate the numbers and letters.
##print(a.isalpha())
##for i in range(1,5,1): #i=1 2 3 4 
##    print(i) #1 2 3 4
a='app26'
alpha=0
digit=0
for c in a:
    if c.isalpha():
        alpha+=1
    if c.isdigit():
        digit+=1
print(alpha)
print(digit)

##6.display odd numbers between  1 to 50.
for i in range(1,50,2):
    print(i)

##7.python program to find average and sum of n integer numbers.
a=int(input('Enter the no: '))
b=0
for i in range(1,a+1,1): #i= 1 2 3 4 5
    b+=i #b=b+i #0+1 #1+2 #3+3 #6+4 #10+5
print('sum:',b) #1 3 6 10 15
print('average:', b/a)

##8.multiplication table from  1 to 10.
a=int(input('Enter the number: '))
for i in range(1,11,1):
    print(i,'x',a,'=',i*a)

##9.print middle letter of a string.
a=input('Enter the string: ')
length=len(a)
centre=length//2
if length%2==0:
    slicing=a[centre-1:centre+1]
    print('The middle two letter: ',slicing)
else:
    slicing1=a[centre]
    print('The middle letter: ',slicing1)
    
##10.python program to get a fibonacci series from 0 to 50.

11.

##12.display numbers from -10 to -1 using for loop.
for i in range(-10,0,1):
    print(i)

##13.print first 10 natural numbers using while loop.
k=1
while k<11: #1<11 #2<11 #3<11 #4<11 #5<11 #6<11 #7<11 #8<11 #9<11 #10<11 #11<11
    print(k) #1 #2 #3 #4 #5 #6 #7 #8 #9 #10
    k=k+1 #11

k=10
while k>=0: #10>0 #
     print(k) #10
     k=k-1 #9

14. factorial of a given number.
a=int(input('Enter the number: '))
z=1
for i in range(1,a+1,1): #1, 2, 3
    z*=i #1*1=1,#1*2=2, #2*3=6
print(z) #1,2,6

15. calculate the cube of all numbers from 1 to given numbers
a=int(input('enter the number: '))
for i in range(1,a+1,1): 
    print('The cube of',i,'=',i**3)

16. reverse a given integer number.
a=int(input('Enter the num: '))
b=str(a)
print(b[::-1])

b=str(a)
c=b[::-1]
for d in c:
    print(d)

17. while loop statement to print the following series.
k=105
while k>=7:
    print(k)
    k=k-7
    
18.for loop statement to print the following series.
for i in range(10,301,10):
    print(i)

19.sum of digits of a number accepted from user.'''
a=int(input('Enter the no: '))
s=0
i=1
while i<=a:
    s=s+i
    print('s=',s)
    i=i+1
    print('i=',i)
print('The sum of numbers:', s)

















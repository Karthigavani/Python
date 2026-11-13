#1.Create a function to check whether a number is positive, negative, or zero.
##def inp_no(a):
##    if a>0:
##        print(a,'is positive')
##    elif a<0:
##        print(a,'is negative')
##    else:
##        print(a,' is zero')
##inp_no(5)

#2.Develop a function to determine whether a given year is a leap year.
##def leap_year(a):
##    if a//4==0:
##        print(a,'is leap year')
##    else:
##        print(a,'is not a leap year')
##leap_year(1996)

#3.Implement a function to find the largest among three numbers.
##def largest(a,b,c):
##    if a>b and a>c:
##        print(a,'is the largest')
##    elif b>a and b>c:
##        print(b, 'is the largest')
##    else:
##        print(c, 'is the largest')
##largest(10,20,30)

#4.Write a function to check whether a number is even or odd.
##def even_odd(a):
##    if a//2==0:
##        print(a,'is even')
##    else:
##        print(a,'is odd')
##even_odd(5)    

#5.Design a function to assign grades based on student marks.
##def student_marks(a):
##    if a>=90:
##        print(a,'= GRADE A')
##    elif a>=80:
##        print(a,'=GRADE B')
##    elif a>=70:
##        print(a,'=GRADE C')
##    else:
##        print(a,'=GRADE D')
##student_marks(74)

#6.Create a function to print the multiplication table of a given number.
##def multiplication(a):
##    for i in range(1,11):
##        print(a,'x',i,'=',a*i)
##multiplication(2)

#7.Create a function to check whether a number is zero.
##def zero(a):
##    if a==0:
##        print(a,'is zero')
##    else:
##        print(a,'is not zero')
##zero(5)

#8.Create a function to check if number is prime.
##def prime(a):

#9.Create a function to return factorial of a number.
##for i in range(2,16):
##    if i%2==0 or i%3==0:
##        print(i)
        
#10.Develop a function to calculate the factorial of a number using loops.
##m=1
##def factorial(a):
##    for i in range(1,a+1):
##        global m
##        m=m*i
##    print(m)
##factorial(5)
        
#11.Implement a function to generate the Fibonacci series up to N terms.

#12.Write a function to find the sum of all natural numbers up to N.
##def sum_num(n):
##    m=0
##    for i in range(n+1):
##        m=m+i
##    print(m)
##sum_num(3)

#13.Create a function to count the digits in a given number.
##def count_num(n):
##    if n<10:
##        print('single digit')
##    elif n>=10 and n<100:
##        print('two digit')
##    elif n>=100 and n<=999:
##        print('three digit')
##    else:
##        print('more than 4 digit')
##a=int(input('enter the num:'))
##count_num(a)

#method:2
##n=int(input('Enter the no:'))
##c=0
##while n>0:
##    n=n//10
##    c+=1
##print(c)
        
#14.Implement a function to reverse a string.
##def reverse_str(a):
##    b=a[::-1]
##    print(b)
##reverse_str('python')

#15.Create a function to check whether a string is a palindrome.
##def palindrome(a):
##    b=a[::-1]
##    if b==a:
##        print(a,'is a palindrome')
##palindrome('mom')

#16.Develop a function to count vowels in a string.
##def vowels(a):
##    m=0
##    for i in a:
##        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
##            m=m+1
##    print(m)
##            
##vowels('string')

#17.Write a function to find the frequency of characters in a string.
##def frequency(a):
##    m=0
##    for i in a:
##        m=m+1
##    print(m)
##frequency('discoveries')

#18.Create a function to count the number of words in a sentence.
##def count_words(a):
##
##    for i in a:
##        b=a.split()
##        c=len(b)
##    print(c)
##count_words("I'm a good girl")


#method:2
##def count_words(a):
##    c=1
##    for i in a:
##        if i==' ':
##            c=c+1
##    print(c)
##count_words("I'm a good girl")


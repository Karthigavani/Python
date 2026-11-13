'''#24.10.2026 FUNCTIONS TYPES
1. Build in functions.
2. User defined function
Based on how arguments are passed to a function.
i). Positional
Values are assigned based on their position.
add(10, 20)
ii). Keyword arguments
Values are assigned using parameter names.
add(a=10, b=20)
iii). Default arguments
A parameter has a predefined default value.
def greet(name="User"):
iv). Variable-length positional arguments
Accepts any number of positional arguments.
def add(*args):
v). Variable-length keyword arguments
Accepts any number of keyword arguments.
def info(**kwargs)
Based on arguments and return values.
i)No arguments, no return value -
ii)Arguments, no return value	
iii)No arguments, with return value	
iv)Arguments, with return value
3.Lamda function
4.Recursive function
'''
##a=int(input('enter a value:'))
##b=int(input('enter a value:'))
##c=a+b
##print(c)

##def add(a, b):
##    return a + b
####print(add(10, 20))
####print(add(5, 15))
####print(add(2, 3))
##
##c=add(30,20)
##print(c)
'''
def add(a, b):
    return a + b
def multiply(a, b):
    return a * b
print(add(10, 5))
print(multiply(10, 5))

#modularity:
m1 = 80
m2 = 90
m3 = 70
total = m1 + m2 + m3
print("Total:", total)

average = total / 3
print("Average:", average)

if average >= 90:
    print("Grade A")
elif average >= 75:
    print("Grade B")
else:
    print("Grade C")
    '''
'''
def check():
    n=int(input ("enter a number:"))

    if n % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

check()
'''
'''
def add(a, b):
	c=(a+b)
	return c
d=(add(10,20))
print(d)
'''
'''
def add(a, b):
    c = a + b
    return c
print(add(a=20,b=10))
'''
'''
def add(*z):
        t=0
        for i in z:
                T=t+i
        return(T)
a=add(20,30)
print(a)

'''
'''
def check():
	n=int (input ("enter a number:"))
	if n % 2 == 0:
		print("Even number")
	else:
		print("Odd number")
check()
'''
def add(**numbers):
    total = 0

    for i in numbers.values():
        total = total + i

    return total

print(add(10, 20, 30, 40))

import math*
math.sqrt







#if & if else problems:
#1.
a=int (input('Enter the no.: '))
if a>100:
    print('a is greater than 100')
#2.
a=int (input('Enter the no.: '))
if a<0:
    print('a is less than 0')
#3.
a=input('Enter a character: ')
if a=='A':
    print('its A')
#4.
a=int (input('Enter the no.: '))
if a%7==0:
    print('Divisible by 7')
#5.
a=int (input('Enter the no.: '))
if a==100:
    print('Its exactly 100')
#6.
a=input('Enter a string value: ')
b=len(a)
print('It has',b,'characters')
if b>5:
    print('True')

if a%10==5:
    print('It ends with 5')

if a==25000:
    print('true')

#7.
b=1234
if a==b:
    print('the passcode is correct')


#if else tasks:
#1. number is greater than 50.
a=int(input('Enter the no: '))

if a>50:
    print('greater than 50')
else:
    print('condition not satisfied')

#2. number is divisible by 9 or not.
a=int(input('Enter the no: '))
if a%9==0:
    print(a, 'is divisible by 9')
else:
    print(a, 'Not divisible by 9')

#3. compare two strings.
a=input('Enter str A: ')
b=input('Enter str B: ')
if a==b:
    print('two strings are equal')
else:
    print('two strings are not equal')

#4. check if age is above 60 or not.
a=int(input('Enter the age: '))
if a>60:
    print('above 60 years old')
else:
    print('below 60 years old')

#5. check if number is two digit or not.
a=int(input('Enter a num: '))
if a>9 and a<100:
    print('its a two digit number')
else:
    print('its not a two digit number')

#6. check if character is alphabet or not.
a=input('Enter a character: ')
b=a.isalpha()
c=a.isdigit()
if b==a.isalpha():
    print(b ,'is a character')
    if c==a.isdigit():
            print(c,'is a number')
else:
    print('invalid')

#7. check if total purchase >1000 for free delivery.
a=int(input('Enter the total purchase: '))
if a>1000:
    print('Eligible for free delivery')
else:
    print('not eligible for free delivery')

#8. check if students attendance >=75% or not.
a=int(input('Enter the attendance percentage: '))
if a>=75:
    print('Its greater than 75%')
else:
    print('Its less than 75%')

#9. check if username matches the stored username.
username=1234
a=int(input('Enter the username: '))
if a==username:
    print('it matches')
else:
    print('it doesnt matches')

#10. check if number is multiple of 4 or not.
a=int(input('Enter the number: '))
if a%4==0:
    print('it divisible by 4')
else:
    print('its not divisible by 4')

#11. check if passcode equals 'admin123
passcode='admin123'
a=input('Enter the passcode: ')
if a==passcode:
    print('it equals to the passcode')
else:
    print('its not equal to the passcode')

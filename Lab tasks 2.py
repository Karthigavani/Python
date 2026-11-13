'''1. single digit:
a=int(input('Enter the no.: '))
if a>0 and a<10:
    if a==1:
        print('one')
    elif a==2:
        print('two')
    elif a==3:
        print('three')
    elif a==4:
        print('four')
    elif a==5:
        print('five')
    elif a==6:
        print('six')
    elif a==7:
        print('seven')
    elif a==8:
        print('eight')
    elif a==9:
        print('nine')
else:
    print('its not a single digit no.')
   '''
'''##2. Subject marks of a single students.
a=int(input('English: '))
b=int(input('Language: '))
c=int(input('Maths: '))
d=int(input('Science: '))
e=int(input('Social: '))
f=a+b+c+d+e
g=f/5
h=(f/500)*100
print('Total: ',f)
print('Average: ',g)
print('percentage: ',h)'''

'''##3.calculate the energy bill.
a=int(input('Enter the power consumed: '))
if a<300 and a>200:
    b=a*3.50
    print('Bill= ',b)
elif a<200 and a>100:
    c=a*2.50
    print('Bill= ',c)
else:
    d=a*1.50
    print('Bill= ',d)'''

'''##4. print the digits of number separately.
a=int(input('Enter the two digit no.: '))
b=a//10
c=a%10
print(b)
print(c)'''

'''##three digits of number separately.
a=int(input('Enter the three digit no.: '))
b=a//100
c=a%100
d=c//10
e=c%10
print(b)
print(d)
print(e)'''

'''##5.theory & practical score.
a=int(input('Theory: '))
b=int(input('Practical: '))
if a>20 and b>20:
    print('You are pass')
else:
    print('Better luck next time')
c=a+b
print('Total: ',c)'''

##6.
for a in range(1,6):
    b=input('Enter the name: ')
    c=int(input('Language: '))
    d=int(input('English: '))
    e=int(input('Maths: '))
    f=int(input('social: '))
    g=int(input('Sci Th.: '))
    h=int(input('Sci Prc.: '))
    Total=c+d+e+f+g+h
    print(b,':','Total: ',Total)
    percentage=(Total/500)*100
    print(b,':','percentage: ',percentage )
    if c>=40 and d>=40 and e>=40 and f>=40 and g>=20 and h>=20:
        print()
        if percentage>80 and percentage<100:
            print(b,'you are secured A+')
        elif percentage<80 and percentage>60:
            print(b,'you are secured A')
        elif percentage<60 and percentage>40:
            print(b,'you are secured B+')
    else:
        print(b,'Better luck next time')









































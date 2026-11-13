'''a=input("enter data")
print(len(a)>5)'''
'''a=int(input('Enter the no.: '))
if a>0:
    print('positive no.')
    if a%2==0:
        print('its even no.')
    else:
        print('its odd no.')
else:
    print('negative no.')'''
'''a=int(input('Enter the age: '))
if a>=18:
    b=input('Do u have drivers license: ')
    if b=='yes':
        print('You can drive')
    else:
       print('you are not eligible to drive') 
else:
    print('You are not eligible to drive')'''
##for i in range(5,101,5):
##    print(i)

a='app45'
##print(a.isalpha())
##print(a[1:5:2])
##print(a[::-1])
alpha_count=0
digit_count=0
for i in a:
    if i.isalpha():
        alpha_count+=1
    if i.isdigit():
        digit_count+=1
    
print(alpha_count)
print(digit_count)

for i in range(0,101,2):
    print(i)






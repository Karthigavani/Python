###lambda functions:
###1.Lambda to find square of a number.
##square=lambda a:a**2
##print(square(2))
##
###2.Lambda to check even or odd.
##check=lambda a:'even' if a%2==0 else 'odd'
##print(check(2))
##
###3.Lambda to find maximum of two numbers.
##max_mum=lambda a,b:'a is max' if a>b else 'b is max'
##print(max_mum(8,9))

#4.Lambda to calculate cube.
##cube=lambda a:a**3
##print(cube(2))

###5.Lambda to check positive or negative.
##check=lambda a:'positive' if a>0 else 'negative'
##print(check(5))
##
###6.Lambda to add two numbers.
##add=lambda a,b:a+b
##print(add(2,3))

#7.Lambda to sort list of tuples by second value.

#8.Lambda with filter() to get even numbers.
##a=[2,3,4,5,6,7,8]
##even=list(filter(lambda x:(x%2==0),a ))
##print(even)

#9.Lambda with filter() to get vowels from string.
##a='cadd centre live wire'
##string=list(filter(lambda x:x in "aeiouAEIOU",a))
##print(string)

#10.Lambda with map() to square list elements.
##a=[1,2,3]
##square=list(map(lambda x: x**2,a))
##print(square)

#11.Lambda with map() to convert lowercase to uppercase.
##string="hi", "hello", "hey"
##result=list(map(lambda x: x.upper(),string))
##print(result)

#12.Lambda with reduce() to find sum of list.

#13.Lambda with reduce() to find product of list.

#14.Lambda to check string length > 5.

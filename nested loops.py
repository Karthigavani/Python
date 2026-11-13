##Nested loop:
##SYNTAX:
##    for<variable>in range():   #outerloop-row
##        for<variable>in range():  #innerloop-column
##            statement
##examples:
##1.
##for a in range(1,4):
##    for b in range(5,9):
##        print(b)

##for a in range(1,4):
##    for b in range(5,9):
##        print(b,end='')
##    print()

##2.
##for a in range(1,6):
##    for b in range(0,3):
##        print(a,end='')
##    print()

##3.
##for a in range(0,4):
##    for b in range(1,4):
##        print('*',end='')
##    print()
##(empty print statement moves to the next line)

##4.
##for a in range(1,6):   #1, 2, 3, 
##    for b in range(1,a+1):   #(1, 1+1=2---1)(1, 2+1=3---1,2), (1, 3+1=4---1,2,3)
##        print(b,end='')
##    print()

##5.
##for a in range(1,4):
##    for b in range(3,a-1,-1):
##        print(b,end='')
##    print()

##Problems:
##1.
##for a in range(1,6):
##    for b in range(1,a+1):
##        print(a, end='')
##    print()

##2.
##for a in range(1,6):
##    for b in range(5,a-1,-1):
##        print(b, end='')
##    print()

##for a in range(5,0,-1):
##    for b in range(a,0,-1):
##        print(b, end='')
##    print()

##3.
##for a in range(1,6):
##    for b in range(5,a-1,-1):
##        print(b,end='')
##    print()

#4. fibonacci series.
##for a in range():
##    for b in range():
##        print()
##    print()

##5.
##for a in range (1,6): 
##    for b in range(1,a+1): 
##        print('*',end='')
##    print()

#6.
##c=0
##for a in range(1,6): #1, 2, 3, 4, 5
##    for b in range(a): #1, (2,3) (4,5,6) (7,8,9,10)(11,12,13,14,15)
##        c=c+1
##        print(c,end=' ')
##    print()

#7.
for a in range(6,1,-1):
    for b in range(a,-1,-1):
        print(' ',end='')
    for c in range(1,a): 
        print(c,end='')
    print()

###8.
##for a in range():
##    for b in range():
##        print()
##    print()
    
####9.
##for a in range(1,6):
##    for b in range(1,6):
##        print('*',end='')
##    print()

###10.
##for a in range():
##    for b in range():
##        print()
##    print()

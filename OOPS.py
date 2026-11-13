'''
#OOPS- object oriented programming system.
Feautures:
1.clear organized structure for program.
2.resuable
3.secured
4.maintainable code
5.reduce the complexity of code.
6.In func only a action is done vs in oops we can group data
and more functions together.
7.It organizes code using classes and objects.
'''
##class student:
##    def study(self):
##        a=10 #attribute
##        print('student is studying')
##s1=student()
##s1.study()
'''
what happens here?
class student-->defines a class named student.
def study(self)-->defines a method inside the class.
s1=student()-->creates an object of the student class.
s1.study()-->calls the method using the object.

order of the syntax-------
class-->
constructor-->
attributes-->
methods-->
assign an object-->
call methods-->
'''
##class home():
##    def n(self):
##        self.name=input("enter the name:")
##        print("welcome home",self.name)
##home1=home()
##home1.n()
'''what happens here?
Here self is used in methods(self)->to transfer the memory address of the object.
self.name is used in attribute->so that the name attribute can be used as global variable,
if self is used. without using self it is considered as local variable.'''
'''
class home():
    name=input("enter the name:")
    side=int(input('enter the hall side:'))
    a=side**2
    def n(self):
        print("welcome home",self.name)
    def hall_dimensions(self):
        print(self.name,"The hall dimensions will be:",self.a)
    def room(self):
        print(self.name,"the room is ready with the dimensions",self.a)
home1=home()
home1.n()
home1.hall_dimensions()
home1.room()
'''
'''
what happens here?
1.get all the inputs before calls the methods.
2.write self in all print or it shows error.
3.self -->memory location transfer, global attribute when defines inside a method

#constructor--->
1. A constructor runs automatically when we call a class.
2. purpose - construct an object and assign a value to the object.
3. self keyword use is a must.
4. syntax---
__init__():
'''
##class salem():
##    def __init__(self):
##        self.name="karthiga"
##        self.address="kitchipalayam"
##        print(self.name)
##        print(self.address)
##s1=salem()
'''
what happens here?
here only object is assigned for a class.
function is not called here, instead constructor runs without calling.

Default constructor/zero arguments constructors:
1.A default constructor is a constructor that initializes an object
with default values without requiring the programmer to provide arguments.
2.Initializes with predefined or default values	
syntax: def __init__(self):

parameterized constructor:
1.Accepts arguments from the user.
2.Initializes with supplied values
syntax: def __init__(self, name):
'''
##class chat_app:
####    def __init__(self):
####        print("welcome to the world of magic")
##    def __init__(self,a):
##        print(a,"welcome to the world of magic")
####a=chat_app()      #default
##a=chat_app("karthiga") #parameterized
'''
Destructor:
A default constructor is a constructor that
initializes an object with default values without requiring
the programmer to provide arguments.
'''
##class operators:
##    def add(self):
##        self.a=int(input("Enter the number:"))
##        self.b=int(input("Enter the number:"))
##        self.c=self.a+self.b
##        print(self.c)
##    def sub(self):
##        self.d=self.a-self.b
##        print(self.d+self.c)
##    def multiply(self):
##        self.e=self.a*self.b
##        print(self.e)
##    def divide(self):
##        self.f=self.a/self.b
##        print(self.f)
##    def __del__(self):
##        print("obj deleted")
##operations=operators()
####operations.add()
####operations.sub()
####operations.multiply()
####operations.divide()
##del operations
'''
#Single level inheritance:
Single-level inheritance is a type of
inheritance in which one child class inherits the properties
and methods of one parent class.

#multi level inheritance:
a child class inherits from a parent class, and another child class
inherits from that child class.

#multiple inheritance:
Multiple inheritance is a type of inheritance in which a
single child class inherits properties and methods from two or more parent classes.

#hierarchical inheritance:
Two or more child classes inherit from a single parent class.
In simple words, one parent class shares its properties and methods with multiple child class.

'''
'''
#single level inheritance:
class operators:
    def value(self):
        self.a=int(input("Enter the number:"))
        self.b=int(input("Enter the number:"))
    def add(self):
        self.c=self.a+self.b
        print(self.c)
    def sub(self):
        self.d=self.a-self.b
        print(self.d+self.c)
    def multiply(self):
        self.e=self.a*self.b
        print(self.e)
    def division(self):
        self.f=self.a/self.b
        print(self.f)

class arithmetic(operators):
    def floor_division(self):
        self.g=self.a//self.b
        print(self.g)

operations=arithmetic()
operations.value()
operations.add()
operations.sub()
operations.multiply()
operations.division()
operations.floor_division()
'''
'''
what happens here?
here class operators-->parent class.
class arithmetic-->child class where parent class(operators)is inherited.
therefore, object operations is assigned only to child class arithmetic.
and call the methods from both the parent and child class.
no need to assign object for parent class also.
this is single level inheritance.
'''
'''
#multi level inheritance:
class tickets:
    def value(self):
        self.Total=100
        self.window=20
        self.three_seater=20
        self.two_seater=5
        self.single_seater=10
class bus(tickets):
    def intro(self):
        print("Welcome!")
class book(bus):
    def book(self):
        a=int(input("select the tickets:"))
        unsold=self.Total-a
        print("The Available tickets are:",unsold)
bus=book()
bus.value()
bus.intro()
bus.book()
'''
        
        
        










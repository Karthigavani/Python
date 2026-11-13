#24.10.2026---FUNCTIONS, SYNTAX, FEAUTURES.
'''
1. Named, reusable block of code designed to perform specific tasks.
2. Input values through parameters.
3. Process the datas-performing the operations on the input data
(Add, sub, sorting, calculating an average, etc...)
4. Display the results of the operations.
5. sends back the results to the place where functions was called.
Eg:
'''
def add(a, b):
    return a + b
result = add(10, 20)
print(result)
'''
6.
Step:1 Function call
result = add(10, 20)
The program calls the add() function with the arguments 10 and 20.
Step:2 Function execution
return a + b
Python calculates 10 + 20, giving 30.
Step:3 Return to the caller
The value 30 goes back to the statement result = add(10, 20),
where the function was called. The variable result stores 30.
Step:4 Display the result
print(result) displays 30.

7.The function calculates the answer, and return sends that
answer back to the code that called the function.

8.In Python, the value returned by a function can be stored
in a variable and retrieved or reused later.
i)Store the returned value in a variable:
'''
def add(a, b):
    return a + b
result = add(10, 20)
print(result)
'''
What happens here?
add(10, 20) calls the function.
return a + b calculates and returns 30.
result = 30 stores the returned value in result.
print(result) retrieves and displays the value.
Here, the variable result allows you to access
the returned value later.

ii)Retrieve and reuse the value.
'''
def add(a, b):
    return a + b
result = add(10, 20)
print(result)
print(result * 2)
print(result + 5)
'''
what happens here?
The function runs once, and the
returned value 30 is stored in result. You can reuse
that value without calling the function again.

iii)What happens if you don't store the value?
The function calculates and returns 30, but the program doesn't store
it in a variable or display it. Once that returned value is no longer
referenced, you cannot retrieve it through a variable later.
To display the result directly, you can write:
'''
print(add(10, 20))
#-------------------------------------------------------#
##def add(a, b):
##    return a + b
##add(10, 20)
'''
9. Syntax of function.
'''
##def add(a, b):
##    return a + b
##add(10, 20)
'''
-->def — Keyword used to define a function.
--> add — Function name.
--> a, b — Parameters that receive input values.
--> return — Statement that sends the result back to the caller.
-->add(10, 20) — Function call that passes arguments to the function.

10.Function is a bottom to top approach.
11.Code Reusability - writing a block of code once and
using it multiple times without rewriting the same logic.
'''
def add(a, b):
    return a + b
print(add(10, 20))
print(add(5, 15))
print(add(2, 3))
'''
what happens here?
We define the add() function once and call it three times with different arguments.
This saves time and avoids rewriting the addition logic.

12.Modularity - dividing a large program into smaller,independent functions,
each responsible for a specific task.
'''
def add(a, b):
    return a + b
def multiply(a, b):
    return a * b
print(add(10, 5))
print(multiply(10, 5))
'''
what happens here?
The program has two separate functions. add() performs addition, while multiply()
performs multiplication.Each function handles a specific task,
making the program easier to organize.

13.Maintainability - making code easier to understand, modify, debugging,test,
and fix when requirements change or errors occur.
'''
def calculate_price(price):
    return price * 1.10
print(calculate_price(100))
print(calculate_price(200))
'''
what happens here?
i)Suppose the tax or price multiplier changes. We can update the calculation in one function
instead of modifying multiple places in the program.
ii)For example, changing 1.10 to 1.15 updates the calculation for every call.
iii)Centralizing shared logic makes updates easier and reduces the risk of
inconsistent calculations

14.Reduction of Code Duplication - avoiding repeated copies of the same or
similar code by placing common logic in a reusable function.
'''
print(10 + 20)
print(30 + 40)
print(50 + 60)
#---------------------------------#
def add(a, b):
    print(a + b)
add(10, 20)
add(30, 40)
add(50, 60)
'''
15.Parameters and arguments-Transfer of input values to functions-
Parameters are names declared in a function definition to receive input values.
Arguments are the actual values or expressions supplied when the function is called.
'''
def multiply(a, b):
    return a * b
result = multiply(5, 4)
print(result)
'''
what happens here?
i)a and b are parameters.
ii)5 and 4 are arguments.
iii)When the function is called, the argument values are bound to the
corresponding parameter names.
iv)The function multiplies the values and returns 20.
v)Python supports several argument-passing forms, including positional arguments,
keyword arguments,default parameter values, and variable-length arguments
using *args and **kwargs.
EG: Default arguments
'''
def greet(name, message="Hello"):
    return message + " " + name
print(greet("Karthiga"))
print(greet("Karthiga", "Welcome"))
'''
what happens here?

17.Return values-Transfer of results to the caller.
A return value is the value a function sends back to its caller using the return statement.
The returned value can be assigned to a variable,used in an expression,
passed to another function, or displayed.
A function without an explicit return statement returns None by default.

18.Abstraction-Hides implementation details behind a function interface.
Abstraction allows users to access a function's functionality through its interface without
needing to know its internal implementation details.
'''
def calculate_area(length, width):
    return length * width
area = calculate_area(10, 5)
print(area)
'''
what happens here?
i)The function name: calculate_area
ii)The required inputs: length and width
iii)The returned result: the area
iv)The caller does not need to repeat or manage the multiplication logic.
v)Abstraction reduces complexity and separates how a task is used from how it is implemented.

19.Scope-Controls variable accessibility.
Scope determines where a variable name can be accessed within a program. Variables
assigned inside a function are generally local to that function unless other scope rules apply.
'''
def calculate():
    result = 10 + 20
    print(result)
calculate()
'''
what happens here?
The variable result is local to calculate().
It cannot normally be accessed directly outside the function.
'''
def calculate():
    result = 10 + 20
calculate()
print(result)
'''
what happens here?
This raises a NameError because result is not defined in the outer scope.
To make the value available to the caller, return it:
'''
def calculate():
    result = 10 + 20
    return result
answer = calculate()
print(answer)
'''
what happens here?
Local scope helps isolate variables, reducing unintended
interference between different parts of a program.

20.First-class functions-Allows functions to be manipulated as objects.
Python treats functions as first-class objects. This means functions can be
assigned to variables,passed as arguments to other functions,
returned from functions, and stored in data structures.
'''
def greet():
    return "Hello"
message_function = greet
print(message_function())
'''
what happens here?
i)greet refers to the function object.
ii)message_function = greet assigns that function object to another name.
iii)message_function() calls the same function.
iv)First-class functions enable flexible programming techniques such as
callbacks, decorators, and higher-order functions.

21.Higher-order functions-A higher-order function is a function that
accepts another function as an argument, returns a function, or does both.
'''
def square(n):
    return n * n
def apply_function(func, value):
    return func(value)
print(apply_function(square, 5))
'''
what happens here?
i)square defines the operation.
ii)apply_function() accepts a function through its func parameter.
iii)func(value) invokes the supplied function with the given value.
iv)The final result is returned to the caller.
v)Built-in functions such as map(), filter(), and
sorting with a key function use this programming capability.

22.Recursion-Solves problems through repeated self-invocation.
Recursion is a programming technique in which a function calls itself
to solve a problem by reducing it to smaller instances of the same problem.
'''
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(4))
'''
what happens here?
i)The function calculates the factorial
using smaller function calls:
- factorial(4) returns 4 * factorial(3).
- factorial(3) returns 3 * factorial(2).
- factorial(2) returns 2 * factorial(1).
- factorial(1) returns 1, stopping the recursion.
Therefore,(4X3X2X1 = 24).
ii)Recursive functions need a base case to terminate.
This example assumes n is a positive integer.

23.Flexible arguments-Supports variable numbers and forms of inputs.
Python functions support flexible argument-passing mechanisms,
allowing them to accept different numbers and forms of arguments.
i)EG: using *args.
'''
def add_all(*args):
    return sum(args)
print(add_all(10, 20))
print(add_all(10, 20, 30, 40))
'''
what happens here?
Here, *args collects positional arguments into a tuple,
allowing the function to accept a variable number of inputs.
ii)EG: using **kwargs.
'''
def display_details(**kwargs):
    print(kwargs)
display_details(name="Karthiga", role="Data Analyst")
'''
what happens here?
**kwargs collects keyword arguments into a dictionary.
iii)Flexible argument handling makes functions
useful when the number or names of inputs may vary.

24.Exception handling-Manages runtime errors with function execution.
Functions can use structured exception handling to detect and
manage runtime errors, helping programs respond to invalid inputs or failed operations.
EG:
'''
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
print(divide(10, 2))
print(divide(10, 0))
'''
what happens here?
i)The try block contains the division operation.
ii)If the denominator is zero, Python raises ZeroDivisionError.
iii)The except block handles that specific error.
iv)The function returns a message instead of allowing that exception to
terminate the normal execution flow.
v)Exception handling improves the robustness of functions when
errors are anticipated and handled appropriately.




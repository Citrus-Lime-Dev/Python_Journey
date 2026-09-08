Function -> Function is a reusable block of code that executes only when it is explicitly called.

Defining a Function:
  def greet(value):
    print("Welcome to Python!!!")
  greet()

Calling a Function: greet()

parameters -> values mentioned in () when defining a function 
arguments -> values passed in () while calling a function
return values -> values expected to return from function using "return" keyword

local variables -> These are defined inside a specific block, such as a function or a method. 
                   They only exist while that block is executing and are completely invisible to the rest of the program.
global variables -> These are defined at the top level of a script or module, outside of any functions or classes.
                    They are alive for the entire duration of the program and can be accessed from anywhere within that file.

default arguments -> Uses a fallback value if the argument is omitted. Eg: def func(a=10)
keyword arguments -> Matched explicitly by using the parameter name. Eg: func(b=20, a=10)
positional arguments -> Matched strictly by the order they are passed. Eg: func(10, 20)
Arbitrary arguments -> Accepts a flexible, unknown number of variables. Eg: func(*list, **dict) 

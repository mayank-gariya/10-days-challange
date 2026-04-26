# Q1: Custom Map Function

# Write a function that behaves like map() without using built-in map.

# func = lambda x: x * 2
# lst = [1, 2, 3]

# def map_replica(func , lst):
#     return list((func )(num) for num in lst)


# print(map_replica(func,lst))

# Q2: Function Composition

# Create a function compose(f, g) such that:

# compose(f, g)(x) = f(g(x))

# def add_five(x): return x + 5
# def double(x): return x * 2

# # Manually composing: double(add_five(10))
# result = double(add_five(10)) # (10 + 5) * 2 = 30

# def compose(f, g):
#     return lambda x: f(g(x))

# pipeline = compose(double, add_five)
# print(pipeline(10)) # 30

# Q3: Variable Arguments Analyzer

# Write a function that takes any number of arguments and returns:

# count of numbers
# count of strings

# def encounter(*args):
#     str_count = 0
#     num_count = 0
    
#     for x in args:
#         if isinstance(x,(int ,float)):
#             num_count += 1
#         elif isinstance(x,str):
#             str_count += 1
        
#     return str_count , num_count


# number , strings = encounter('hello',65,77,65,'mayank')

# print('count of numeric arguments is ' ,number,'count of str is ', strings)    
    
# Q4: Decorator (Core Concept)

# Write a decorator that:

# prints "Function Started" before execution
# prints "Function Ended" after execution

# def deco(func):
#     def wrapper():
#         print('printing before starting the function')
#         func().upper()
#         print('printing after ending the function')
#     return wrapper

# @deco
# def my_func(*args):
#     return 'mayank is my name'

# print(my_func())



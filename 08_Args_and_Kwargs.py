"""
🔍 Summary of what you learned here:
- *args collects extra positional arguments into a tuple.
- **kwargs collects extra keyword arguments into a dictionary.
- You can mix them, but the order in the function definition must be: def func(normal_args, *args, **kwargs)
"""


# This function accepts any number of positional arguments using *args
def add_all(*args):
    # args is a tuple containing all the passed values
    return sum(args)  # sum() adds all elements in the tuple

# Calling the function with 3 numbers
print(add_all(1, 2, 3))         
# Output: 6
# Explanation: 1 + 2 + 3 = 6

# Calling the function with 4 numbers
print(add_all(10, 20, 30, 40))  
# Output: 100
# Explanation: 10 + 20 + 30 + 40 = 100



# This function accepts any number of keyword arguments using **kwargs
def print_info(**kwargs):
    # kwargs is a dictionary containing all key=value pairs
    for key, value in kwargs.items():
        print(f"{key}: {value}")  # Print each key and its value

# Calling the function with 3 keyword arguments
print_info(name="Siam", age=22, country="Bangladesh")
# Output:
# name: Siam
# age: 22
# country: Bangladesh
# Explanation: kwargs = {'name': 'Siam', 'age': 22, 'country': 'Bangladesh'}



# This function accepts normal arguments (a, b),
# any extra positional arguments (*args),
# and any extra keyword arguments (**kwargs)
def demo_function(a, b, *args, **kwargs):
    print("a =", a)          # First positional argument
    print("b =", b)          # Second positional argument
    print("args =", args)    # All remaining positional arguments as a tuple
    print("kwargs =", kwargs)  # All remaining keyword arguments as a dict

# Calling the function with:
# - 2 normal positional args: 1 and 2 → a=1, b=2
# - 3 extra positional args: 3, 4, 5 → args = (3, 4, 5)
# - 2 keyword args: x=10, y=20 → kwargs = {'x': 10, 'y': 20}
demo_function(1, 2, 3, 4, 5, x=10, y=20)

# Output:
# a = 1
# b = 2
# args = (3, 4, 5)
# kwargs = {'x': 10, 'y': 20}
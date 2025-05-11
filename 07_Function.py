# Learn Python Functions - 20 Examples with Comments and Explanations

# 1️⃣ Basic Function
# Simple function that prints a message
def greet():
    print("1. Hello, Sishir!")

greet()

# 2️⃣ Function with one parameter
def greet_user(name):
    print("2. Hello,", name)

greet_user("Siam")

# 3️⃣ Function with return value
def add(a, b):
    return a + b

print("3. Sum:", add(5, 10))

# 4️⃣ Function with default argument
def greet(name="Guest"):
    print("4. Welcome", name)

greet()
greet("Tushar")

# 5️⃣ Keyword arguments
def user_info(name, age):
    print(f"5. {name} is {age} years old.")

user_info(age=20, name="Sishir")

# 6️⃣ Arbitrary arguments (*args)
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print("6. Total:", sum_all(1, 2, 3, 4, 5))

# 7️⃣ Arbitrary keyword arguments (**kwargs)
def print_info(**data):
    for key, value in data.items():
        print(f"7. {key} = {value}")

print_info(name="Siam", country="BD")

# 8️⃣ Return multiple values
def calculate(a, b):
    return a + b, a - b, a * b

add, sub, mul = calculate(10, 5)
print("8. Add:", add, "Sub:", sub, "Mul:", mul)

# 9️⃣ Check even or odd
def is_even(n):
    return n % 2 == 0

print("9. Is 6 even?", is_even(6))

# 🔟 Function with loop inside
def print_table(n):
    print(f"10. Table of {n}:")
    for i in range(1, 11):
        print(n, "x", i, "=", n*i)

print_table(5)

# 1️⃣1️⃣ Function calling another function
def double(n):
    return n * 2

def triple_double(n):
    return double(n) * 3

print("11. Triple of double:", triple_double(2))

# 1️⃣2️⃣ Function with condition
def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    else:
        return "C"

print("12. Grade:", grade(85))

# 1️⃣3️⃣ Recursive function
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print("13. Factorial of 5:", factorial(5))

# 1️⃣4️⃣ Lambda (anonymous) function
square = lambda x: x * x
print("14. Square:", square(4))

# 1️⃣5️⃣ Function with list

def get_even(numbers):
    return [n for n in numbers if n % 2 == 0]

print("15. Even numbers:", get_even([1, 2, 3, 4, 5]))

# 1️⃣6️⃣ Global variable usage
x = 10

def modify_global():
    global x
    x = 20

modify_global()
print("16. Global x:", x)

# 1️⃣7️⃣ Function with nested function
def outer():
    def inner():
        return "Inner Function"
    return inner()

print("17. Result:", outer())

# 1️⃣8️⃣ Function with pass (empty function)
def to_do():
    pass

print("18. Defined empty function to_do() with pass")

# 1️⃣9️⃣ Function with type hints
def add_numbers(a: int, b: int) -> int:
    return a + b

print("19. Type hint result:", add_numbers(7, 3))

# 2️⃣0️⃣ Function using f-string
def welcome(name):
    return f"20. Welcome, {name}!"

print(welcome("Shishir"))
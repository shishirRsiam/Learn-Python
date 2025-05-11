# Simple Python Program by Sishir Siam

# Printing some basic output
print("Hello World")
print("Sishir Siam")

# Taking user name as input
name = input("Enter your name: ")
print("Hello, " + name)

# Taking age as input and converting to integer
age = int(input("Enter your age: "))
print("Your Age -> " + str(age))

# Taking two numbers as input
a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

# Performing basic arithmetic operations
print("\n--- Arithmetic Operations ---")
print(f"Sum: {a} + {b} = {a + b}")
print(f"Difference: {a} - {b} = {a - b}")
print(f"Product: {a} * {b} = {a * b}")
# Checking division by zero
if b != 0:
    print(f"Quotient: {a} / {b} = {a / b:.2f}")  # rounded to 2 decimal places
else:
    print("Division by zero is not allowed.")

# Summary
print("\n--- Summary ---")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"You entered numbers {a} and {b}")
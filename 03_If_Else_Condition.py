# A Biye Age Checker with User Input
age = int(input("Enter Your Age: "))
# Multiline if-elif ladder checking different ranges
if age >= 21 and age <= 40:
    print("21. Biyer Boyos Hoiche")
    print("21. Biye Diye Daw")
elif age >= 18 and age <= 20:
    print("21. Ar Kichudin Wait Koro")
elif age < 18:
    print("21. Tumi Baccha")
else:
    print("21. Tomake Biye Korte Hobe Na")

# -------------------------------------------------------------------- #

# 1️⃣ Basic if statement
x = 10
# Checks if x is greater than 5
if x > 5:
    print("1. x is greater than 5")

# 2️⃣ if-else example
x = 3
# Checks if x > 5; else runs fallback
if x > 5:
    print("2. Greater than 5")
else:
    print("2. Not greater than 5")

# 3️⃣ if-elif-else chain
marks = 85
# Grading logic
if marks >= 90:
    print("3. Grade: A+")
elif marks >= 80:
    print("3. Grade: A")
elif marks >= 70:
    print("3. Grade: B")
elif marks >= 60:
    print("3. Grade: C")
else:
    print("Fail")                       # Grade is based on value

# 4️⃣ Age check
age = 17
# Adult check based on age
if age >= 18:
    print("4. Adult")
else:
    print("4. Minor")

# 5️⃣ Even or odd
n = 6
# Checks if number is even
if n % 2 == 0:
    print("5. Even")
else:
    print("5. Odd")

# 6️⃣ Positive, negative or zero
num = -5
# Number type check
if num > 0:
    print("6. Positive")
elif num < 0:
    print("6. Negative")
else:
    print("6. Zero")

# 7️⃣ Check if number is in range
n = 15
# Using Python's range comparison
if 10 <= n <= 20:
    print("7. Number is in range 10-20")
else:
    print("7. Number not in range")

# 8️⃣ Nested if
age = 25
# Inner check only runs if outer is True
if age > 18:
    if age < 30:
        print("8. Young adult")

# 9️⃣ Using and
a, b = 15, 25
# Logical AND usage
if a > 10 and b > 20:
    print("9. Both conditions are True")

# 🔟 Using or
temp = 35
# Logical OR usage
if temp < 0 or temp > 30:
    print("10. Extreme temperature")

# 1️⃣1️⃣ Using not
is_raining = False
# NOT operator reverses the boolean
if not is_raining:
    print("11. Go outside")

# 1️⃣2️⃣ Check string case
text = "Hello"
# Check if all characters are uppercase
if text.isupper():
    print("12. Uppercase")
else:
    print("12. Not Uppercase")

# 1️⃣3️⃣ Check if element in list
fruits = ['apple', 'banana', 'mango']
# Membership test
if 'banana' in fruits:
    print("13. Banana is in list")

# 1️⃣4️⃣ Multiple elifs
day = "Wednesday"
# Check what day it is
if day == "Monday":
    print("14. Start of week")
elif day == "Friday":
    print("14. Weekend is near")
elif day == "Sunday":
    print("14. Weekend")
else:
    print("14. Midweek")

# 1️⃣5️⃣ Shorthand if
a = 8
# One-line if statement
if a > 5: print("15. Shorthand if: a > 5")

# 1️⃣6️⃣ Shorthand if-else (ternary)
x = 9
# Ternary operator (single-line if-else)
print("16. Even" if x % 2 == 0 else "16. Odd")

# 1️⃣7️⃣ Compare two numbers
a, b = 50, 70
# Simple number comparison
if a > b:
    print("17. a is greater")
else:
    print("17. b is greater or equal")

# 1️⃣8️⃣ Check password match
password = "admin"
confirm = "admin"
# Simple equality check
if password == confirm:
    print("18. Password matched")
else:
    print("18. Password mismatch")

# 1️⃣9️⃣ Voting eligibility
age = 16
# Legal voting age check
if age >= 18:
    print("19. Eligible to vote")
else:
    print("19. Not eligible to vote")

# 2️⃣0️⃣ Check divisible by 3 and 5
num = 15
# Modulo check for both 3 and 5
if num % 3 == 0 and num % 5 == 0:
    print("20. Divisible by both 3 and 5")
else:
    print("20. Not divisible by 3 and 5")
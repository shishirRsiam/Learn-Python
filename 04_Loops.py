# 1️️ Basic for loop using range()
for i in range(1, 6):
    # Prints numbers from 1 to 5
    print(f"1️⃣ Value of i: {i}")


# 2️⃣ for loop with spaces and number pattern
for i in range(1, 6):
    # Prints space pattern followed by the number
    print(i * ' ' + str(i))


# 3️⃣ while loop basic usage
i = 1
while i <= 5:
    # Will print i stars and increase i by 1 each time
    print(i * '*')
    i += 1


# 4️⃣ while loop with step increase
i = 1
while i <= 30:
    # Increases by 3 each time, prints that many stars
    print(i * '*')
    i += 3


# 5️⃣ Loop through a list
fruits = ['apple', 'banana', 'mango']
for fruit in fruits:
    # Each fruit printed in a new line
    print(f"5️⃣ Fruit: {fruit}")


# 6️⃣ Using break in a loop
for i in range(1, 10):
    if i == 5:
        break  # Exits the loop when i is 5
    print(f"6️⃣ i before break: {i}")


# 7️⃣ Using continue in a loop
for i in range(1, 6):
    if i == 3:
        continue  # Skips number 3
    print(f"7️⃣ i after continue check: {i}")


# 8️⃣ Nested for loop for pattern printing
for i in range(1, 6):
    for j in range(i):
        print("*", end="")  # Prints stars on the same line
    print()  # Moves to the next line


# 9️⃣ While loop with user input and break
# Uncomment below code to test it interactively
# while True:
#     name = input("Enter your name (type 'exit' to stop): ")
#     if name == 'exit':
#         break
#     print("Hello", name)


# 🔹 More Advanced Examples

# 1️0⃣ For loop with index and value using enumerate
colors = ['red', 'green', 'blue']
for index, color in enumerate(colors):
    print(f"10⃣ Index {index}: {color}")


# 1️1⃣ Looping over dictionary
person = {"name": "Siam", "age": 22, "country": "Bangladesh"}
for key, value in person.items():
    print(f"11⃣ {key}: {value}")


# 1️2⃣ Reverse loop
for i in range(5, 0, -1):
    print(f"12⃣ Reverse i: {i}")


# 1️3⃣ Loop with condition inside
numbers = [2, 5, 8, 11, 14]
for n in numbers:
    if n % 2 == 0:
        print(f"13⃣ Even number: {n}")


# 1️4⃣ Loop over characters in a string
text = "Siam"
for ch in text:
    print(f"14⃣ Letter: {ch}")


# 1️5⃣ While loop countdown
count = 5
while count > 0:
    print(f"15⃣ Countdown: {count}")
    count -= 1


# 1️6⃣ Loop with else in for
for i in range(3):
    print(f"16⃣ Loop i: {i}")
else:
    print("16⃣ Finished loop without break")


# 1️7⃣ Loop with else in while
x = 3
while x > 0:
    print(f"17⃣ x: {x}")
    x -= 1
else:
    print("17⃣ Done counting down")


# 1️8⃣ Nested while loop for multiplication table
i = 1
while i <= 3:
    j = 1
    while j <= 3:
        print(f"18⃣ {i} * {j} = {i*j}")
        j += 1
    i += 1


# 1️9⃣ For loop to sum a list
numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(f"19⃣ Total sum: {total}")


# 20⃣ Find max number in list using loop
nums = [10, 50, 30, 70, 20]
max_num = nums[0]
for n in nums:
    if n > max_num:
        max_num = n
print(f"20⃣ Max number: {max_num}")
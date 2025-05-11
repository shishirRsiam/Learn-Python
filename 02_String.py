# 📌 Full String Operations Example in Python

# Define the name
name = "Md. Sishir Rahman Siam"

# 1️⃣ Accessing characters
print("First two characters:", name[0] + name[1])  # M + d

# 2️⃣ Count occurrences (case-sensitive)
print("Count of 's':", name.count('s'))  # Only lowercase 's'

# 3️⃣ Length of the string
print("Total length:", len(name))

# 4️⃣ Case conversions
print("Original:", name)
print("Lowercase:", name.lower())
print("Uppercase:", name.upper())
print("Title case:", name.title())  # Capitalizes every word
print("Swap case:", name.swapcase())  # Swaps upper/lower

# 5️⃣ Substring search
print("Find 'Siam':", name.find('Siam'))    # Returns starting index or -1
print("Find 'siam':", name.find('siam'))    # Case-sensitive

# 6️⃣ Replace text
new_name = name.replace("Rahman", "Mandal")
print("After replace:", new_name)

# 7️⃣ Check substring existence
print("Is 'Siam' in name?", "Siam" in name)

# 8️⃣ Conditional check
if "Siam" in name:
    print("✅ Found")
else:
    print("❌ Not Found")

# 9️⃣ Start and end checks
print("Starts with 'Md.':", name.startswith("Md."))
print("Ends with 'Siam':", name.endswith("Siam"))

# 🔟 Character type checks
print("Is alphabetic only?:", name.replace(" ", "").replace(".", "").isalpha())
print("Is alphanumeric?:", name.isalnum())  # Spaces/dots => False
print("Is all lowercase?:", name.islower())
print("Is all uppercase?:", name.isupper())

# 1️⃣1️⃣ String splitting and joining
split_name = name.split()  # Splits by space
print("Split into words:", split_name)
joined_name = "-".join(split_name)  # Join using '-'
print("Joined with hyphen:", joined_name)

# 1️⃣2️⃣ Whitespace trimming
name_with_spaces = "   Md. Sishir Rahman Siam   "
print("Before strip:", repr(name_with_spaces))
print("After strip:", repr(name_with_spaces.strip()))

# 1️⃣3️⃣ Count uppercase and lowercase letters
upper_count = sum(1 for c in name if c.isupper())
lower_count = sum(1 for c in name if c.islower())
print("Uppercase letters:", upper_count)
print("Lowercase letters:", lower_count)

# 1️⃣4️⃣ Reverse the name
print("Reversed name:", name[::-1])

# 1️⃣5️⃣ Looping through characters
print("Characters in name:")
for char in name:
    print(char, end=" | ")
print()

# 1️⃣6️⃣ Using format()
formatted = "My name is {} and I am learning Python.".format(name)
print("Formatted:", formatted)

# 1️⃣7️⃣ Using f-string (more modern)
print(f"My name is {name} and I love coding.")

# 1️⃣8️⃣ Check if string is numeric
year = "2025"
print("Is year numeric?", year.isnumeric())  # True

# 1️⃣9️⃣ Multiline string
about = """This is Sishir Siam.
Learning Python.
Practicing string operations."""
print("Multiline string:\n", about)


"""

✅ Output Preview (Truncated for Brevity)
First two characters: Md
Count of 's': 1
Total length: 23
Original: Md. Sishir Rahman Siam
Lowercase: md. sishir rahman siam
Uppercase: MD. SISHIR RAHMAN SIAM
Title case: Md. Sishir Rahman Siam
...
Reversed name: maiS namhaR rihsiS .dM
...

"""
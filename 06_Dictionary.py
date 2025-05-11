# 1️⃣ Creating a basic dictionary
info = {
    "Name": "Sishir Siam",
    "age": 20,
    "is_Adult": True
}
print("1️⃣ Name:", info["Name"])     # Access by key
print("2️⃣ Age:", info["age"])       # Access by key

# 3️⃣ Update an existing key's value
info["Name"] = "Sishir"
print("3️⃣ Updated Name:", info["Name"])

# 4️⃣ Add a new key-value pair
info["Lastname"] = "Siam"
print("4️⃣ Added Lastname:", info["Lastname"])

# 5️⃣ Print the full dictionary
print("5️⃣ Full Dictionary:", info)

# 6️⃣ Nested dictionary example
Sishir = {
    "Name": "Sishir Siam",
    "Sub and Marks": {
        "Eng": 60,
        "Bangla": 90,
        "Math": 70
    }
}
# 7️⃣ Accessing nested values
print("6️⃣ Math Marks:", Sishir["Sub and Marks"]["Math"])

# 8️⃣ Using get() method (returns None if key not found)
print("7️⃣ Using get():", info.get("age"))
print("8️⃣ Using get() with invalid key:", info.get("phone"))  # None, not error

# 9️⃣ Check if a key exists
print("9️⃣ 'age' in info?", "age" in info)
print("🔟 'phone' in info?", "phone" in info)

# 1️⃣1️⃣ Delete a key-value pair
del info["is_Adult"]
print("1️⃣1️⃣ After deleting 'is_Adult':", info)

# 1️⃣2️⃣ Use pop() to remove and return value
age_value = info.pop("age")
print("1️⃣2️⃣ Removed age:", age_value)
print("1️⃣3️⃣ Dictionary now:", info)

# 1️⃣4️⃣ Add multiple items with update()
info.update({"Country": "Bangladesh", "Age": 21})
print("1️⃣4️⃣ After update:", info)

# 1️⃣5️⃣ Get all keys
print("1️⃣5️⃣ Keys:", list(info.keys()))

# 1️⃣6️⃣ Get all values
print("1️⃣6️⃣ Values:", list(info.values()))

# 1️⃣7️⃣ Get all items (key-value pairs)
print("1️⃣7️⃣ Items:", list(info.items()))

# 1️⃣8️⃣ Loop through dictionary keys
print("1️⃣8️⃣ Looping keys:")
for key in info:
    print(f"  {key} => {info[key]}")

# 1️⃣9️⃣ Loop through key-value pairs
print("1️⃣9️⃣ Looping with items():")
for k, v in info.items():
    print(f"  {k}: {v}")

# 2️⃣0️⃣ Dictionary inside a list (useful for JSON-like structure)
people = [
    {"name": "Sishir", "age": 20},
    {"name": "Siam", "age": 22},
]
print("2️⃣0️⃣ Accessing from list of dicts:", people[1]["name"])  # Output: Siam
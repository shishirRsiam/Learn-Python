# 1️⃣ Create a list
names = ['Sishir', 'Siam', 'Santo', 'Tushar', 'Raj', 20]  # A list can contain strings and numbers
print("1️⃣ Initial list:", names)

# 2️⃣ Append a new item at the end of the list
names.append('Hello')
print("2️⃣ After append:", names)

# 3️⃣ Access last and second last item using negative indexing
print("3️⃣ Last item:", names[-1])     # 'Hello'
print("4️⃣ Second last item:", names[-2])  # 20

# 5️⃣ Remove an item by value
names.remove(20)  # Removes the first occurrence of 20
print("5️⃣ After removing 20:", names)

# 6️⃣ Insert a new item at index 0 (beginning)
names.insert(0, "Haha")
print("6️⃣ After insert at beginning:", names)

# 7️⃣ Check if a value is in the list
print("7️⃣ Is 'Sishir' in the list?", "Sishir" in names)

# 8️⃣ Modify an item at a specific index
names[-1] = 500  # Replaces 'Hello' with 500
print("8️⃣ After modifying last item:", names)

# 9️⃣ Count how many times an item appears
print("9️⃣ Count of 'Siam':", names.count("Siam"))

# 🔟 Get length of the list
n = len(names)
print("🔟 Length of list:", n)

# 1️⃣1️⃣ Print full list using slicing
print("1️⃣1️⃣ Full list with slicing [0:n]:", names[0:n])

# 1️⃣2️⃣ Print first 3 elements using slicing
print("1️⃣2️⃣ First 3 items [0:3]:", names[0:3])

# 1️⃣3️⃣ Loop through list using index
print("1️⃣3️⃣ Loop using range and index:")
for i in range(n):
    print(f"Index {i} = {names[i]}")

# 1️⃣4️⃣ Loop directly through each item (more pythonic)
print("1️⃣4️⃣ Loop directly through items:")
for name in names:
    print(name)

# 1️⃣5️⃣ Slice from index 2 to 4 (not including 4)
print("1️⃣5️⃣ Slice [2:4]:", names[2:4])

# 1️⃣6️⃣ Reverse the list (using slicing)
print("1️⃣6️⃣ Reversed list:", names[::-1])

# 1️⃣7️⃣ Sort list (if all elements are same type)
string_names = ['Zara', 'Aman', 'Siam']
string_names.sort()
print("1️⃣7️⃣ Sorted string list:", string_names)

# 1️⃣8️⃣ Copy a list
copy_names = names.copy()
print("1️⃣8️⃣ Copied list:", copy_names)

# 1️⃣9️⃣ Extend a list with another list
names.extend(['New1', 'New2'])
print("1️⃣9️⃣ Extended list:", names)

# 2️⃣0️⃣ Clear all items from list
empty_list = ['A', 'B', 'C']
empty_list.clear()
print("2️⃣0️⃣ Cleared list:", empty_list)  # []
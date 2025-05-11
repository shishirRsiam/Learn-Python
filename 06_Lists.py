

names = ['Sishir', 'Siam', 'Santo', 'Tushar', 'Raj', 20]
names.append('Hello')

print(names[-1])
print(names[-2])

names.remove(20)
names.insert(0,"Haha")

print("Sishir" in names)

names[-1] = 500

print(names)

print(names.count("Siam"))

n = len(names)
print(names[0:n])
print(names[0:3])


'''
for i in range(n):
    print(names[i])
for name in names:
    print(name)
'''

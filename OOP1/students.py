class Students:
    def __init__(self, name, age, cls):
        self.name = name
        self.age = age
        self.cls = cls
    def __str__(self):
        return f"{self.name} {self.age} {self.cls}"

s1 = Students("Sishir", 20, 12)
s2 = Students("Siam", 19, 11)

print(s1.name + " " + str(s1.age) + " " + str(s1.cls))

student_list = []

print(type(student_list))


n = int(input("Enter Your Student Number: "))
for i in range(n):
    value = input().split()
    student_list.append(Students(value[0], int(value[1]), int(value[2])))

for student in student_list:
    print(student)




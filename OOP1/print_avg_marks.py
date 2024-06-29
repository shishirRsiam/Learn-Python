class Students:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def print_avarage_marks(self):
        total = sum(self.marks)
        print("Hi,", self.name, "your avarage marks is:", total/int(len(self.marks)))

s1 = Students("Sishir Siam", [99,92, 95])
s1.print_avarage_marks()
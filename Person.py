class Person:
    def __init__(self, fname, lname, age):
        self.fname=fname
        self.lname=lname
        self.age=age

    def printname(self):
        print("Hello my name is :", self.fname, " ", self.lname)

p1=Person('John', 'Smith', 26)
p1.printname()
print(p1.age)

del p1.age

p2=Person('Adam', 'Eve', 100)
print(p2.fname)
print(p2.age)

print(p1.age)

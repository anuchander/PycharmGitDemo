class Person:
    def __init__(self, fname, lname, age):
        self.fname=fname
        self.lname=lname
        self.age=age

    def printname(self):
        print("Hello my name is :", self.fname, " ", self.lname)

class Student(Person):
    def __init__(self, fname, lname, age, year):
        super().__init__(fname, lname, age)
        self.graduationyear=year

    def welcome(self):
        print("Welcome", self.fname, self.lname,"to the class of ", self.graduationyear)


x=Student("Mike", "Olson", 15, 2019)
x.printname()
x.welcome()
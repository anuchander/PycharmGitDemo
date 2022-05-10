import datetime
class Employee:

    num_of_emp=0
    raise_amount=1.04

    def __init__(self, first, last, pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first + "."+last+"@company.com"
        Employee.num_of_emp+=1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amount)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{}' - '{}'.format(self.fullname(), self.email)


    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount=amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True


emp_str_1='John-Doe-70000'
emp_str_2='Steve-Smith-30000'
emp_str_3='Jane-Doe-90000'

print("Printing str1")
print(emp_str_1)
print("*********")
print("Printing str(emp_str_1)")
print(emp_str_1.__str__())
print("*********")
new_emp_1=Employee.from_string(emp_str_1)
print(new_emp_1.first)
print(new_emp_1.email)
print(new_emp_1.pay)

emp1=Employee('Aarthi', 'Palaniswamy', 250000)
emp2=Employee('Golda', 'Arulappan', 400000)

print("*******************")
print("Printing if its work day")
my_date=datetime.date(2016,7,10)
print(Employee.is_workday(my_date))

print("*****************")
print("Employee.fullname(emp2) and emp1.fullnmae() values ")
print(emp1.fullname())
print(Employee.fullname(emp2))
print("*****************")

''' both are same '''
Employee.raise_amount=1.05
Employee.set_raise_amount(1.05)

print("printing instance variable values ")
emp1.raise_amount=1.05
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
print("*****************")
print("Printing emp1 instance dictionary")
print(emp1.__dict__)
print("*****************")
print("Printing Employee class dictionary")
print(Employee.__dict__)
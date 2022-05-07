class Employee:
    raise_amt=1.04
    def __init__(self, fname, lname, pay):
        self.fname=fname
        self.lname=lname
        self.pay=pay
        self.email=self.fname+"."+self.lname+"@email.com"

    def fullname(self):
        return '{} {}'.format(self.fname, self.lname)

    def applyraise(self):
        self.pay=self.pay*self.raise_amt


class Developer(Employee):

    raise_amt = 1.10
    def __init__(self, fname, lname,pay, prog_lang):
        super().__init__(fname, lname, pay)
        self.prog_lang=prog_lang


class Manager(Employee):
    def __init__(self, fname, lname, pay, employees=None):
        super().__init__(fname, lname,pay)
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def del_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_employee(self):
        for emp in self.employees:
            print("-->", emp.fullname())


dev1=Developer('Aarthi', 'Palaniswamy', 50000, 'Python')
dev2=Developer("Golda", "Arulappan", 60000, 'Java')

print(dev1.email)
print(dev1.prog_lang)
print(dev1.pay)
dev1.applyraise()
print("Apply raise ")
print(dev1.pay)
print("****************")
print("****************")
print("Dev2 details")
print(dev2.email)
print(dev2.prog_lang)
print(dev2.pay)
dev2.applyraise()
print("Apply raise for dev2")
print(dev2.pay)

print(help(Developer))


mgr1 = Manager('Cory','Smith', 50000, [dev1])
print(mgr1.email)
mgr1.fullname()
mgr1.print_employee()

print("****Isinstance check *********")
print(isinstance(mgr1, Manager))
print(isinstance(mgr1, Developer))

print("******Is subclass check *******")
print(issubclass(Developer, Employee))
print(issubclass(Manager, Developer))

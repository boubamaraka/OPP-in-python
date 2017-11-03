# class is blue print for instance
class Employee:
    raise_amout = 1.04
    number_employee = 0
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.number_employee += 1

    def get_fullname(self):
        return ("{} {} ".format(self.first, self.last))

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amout)

class Developer(Employee):
    raise_amout = 1.10
    def __init__(self, first, last, pay, prog_lang):
        super(Developer,self).__init__(first, last, pay)
        #or use Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super(Manager,self).__init__(first, last, pay)
        #or use Employee.__init__(self, first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_employee(self):
        for emp in self.employees:
            print("-->", emp.get_fullname())

emp_1 = Developer("Ibrahima", "Fofana", 3000, "Python")
emp_2 = Developer("Salimou", "Fofana", 2000, "C++")
emp_3 = Developer("Mohamed", "Fofana", 2000, "C++")
'''emp_1 = Developer("Ibrahima", "Fofana", 3000, "Python")
emp_2 = Developer("Salimou", "Fofana", 2000, "C++")
print(emp_1.get_fullname(),emp_1.pay)
print(emp_2.get_fullname(),emp_2.pay)
print("---------raise method -----------")
emp_1.apply_raise()
emp_2.apply_raise()
print(emp_1.get_fullname(),emp_1.pay, emp_1.prog_lang)
print(emp_2.get_fullname(),emp_2.pay, emp_2.prog_lang)'''
mgr_1 = Manager("Aly", "Djiguine", 9000, [emp_1,emp_2])
mgr_1.print_employee()
print("---- add employee -----------")
mgr_1.add_employee(emp_3)
mgr_1.print_employee()
print("---- remove employee -----------")
mgr_1.remove_employee(emp_2)
mgr_1.print_employee()

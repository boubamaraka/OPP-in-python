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

    def get_employee(self):
        return ("First Name: {} Last Name: {} Email: {} Salary: {}".format(self.first, self.last, self.email, self.pay))

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amout)

    def __repr__(self):
        return "Employee ('{}', '{}', '{}', '{}')"  .format(self.first, self.last, self.email, self.pay)

    def __str__(self):
        return "Employee ('{}' - '{}')"  .format(self.first, self.last)
emp_1 = Employee("Ibrahima", "Fofana", 3000)
emp_2 = Employee("Salimou", "Fofana", 2000)
print(emp_1)
print("-------------------------")
print(emp_1.get_fullname())
print(emp_2.get_fullname())
print("-------------------------")
print(emp_1.get_employee())
print(emp_2.get_employee())
print("------------------------- Raise Salary --------------")
emp_1.raise_amout = 1.05
emp_1.apply_raise()
emp_2.apply_raise()
print(emp_1.get_employee())
print(emp_2.get_employee())
print(Employee.number_employee)

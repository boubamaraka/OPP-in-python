# class is blue print for instance
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    def get_fullname(self):
        return ("{} {} ".format(self.first, self.last))
    def get_employee(self):
        return ("First Name: {} Last Name: {} Email: {} Salary: {}".format(self.first, self.last, self.email, self.pay))

emp_1 = Employee("Ibrahima", "Fofana", 3000)
emp_2 = Employee("Salimou", "Fofana", 2000)
print("-------------------------")
print(emp_1.get_fullname())
print(emp_2.get_fullname())
print("-------------------------")
print(emp_1.get_employee())
print(emp_2.get_employee())

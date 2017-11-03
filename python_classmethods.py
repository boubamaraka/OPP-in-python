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

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amout = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)



emp_1 = Employee("Ibrahima", "Fofana", 3000)
emp_2 = Employee("Salimou", "Fofana", 2000)
emp_1.set_raise_amount(1.05)
emp_str_1 = 'Ibrahima-Fofana-3000'
emp_str_2 = 'Aicha-Fofana-3200'
emp_str_3 = 'Diaria-Djiguine-5200'

new_emp1 = Employee.from_string(emp_str_1)
new_emp2 = Employee.from_string(emp_str_2)
new_emp3 = Employee.from_string(emp_str_3)
print(new_emp1.get_fullname())
print(new_emp2.get_fullname())
print(new_emp3.get_fullname())

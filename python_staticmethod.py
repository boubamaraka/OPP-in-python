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
    @staticmethod
    def is_workday(day):
        if day.weekday() ==5 or day.weekday() == 6:
            return False
        return True

import datetime
mydate = datetime.date(2016, 7, 10)
mydate2 = datetime.date(2016, 7, 11)
print(Employee.is_workday(mydate))
print(Employee.is_workday(mydate2))

emp_1 = Employee("Ibrahima", "Fofana", 3000)
emp_2 = Employee("Salimou", "Fofana", 2000)

class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours=None, rest_days=0, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, hours=None, rest_days=0):
        if hours is not None:
            return hours
        else:
            return (7 - rest_days) * 8

    @classmethod
    def get_email(cls, name, email=None):
        if email is not None:
            return email
        else:
            return f"{name}@email.com"

    @classmethod
    def set_hourly_payment(cls, new_payment):
        cls.hourly_payment = new_payment

    def salary(self):
        hours = self.get_hours(self.name, self.hours, self.rest_days)
        return hours * self.hourly_payment

employee1 = EmployeeSalary("Ivan", rest_days=2)
print(employee1.salary())

EmployeeSalary.set_hourly_payment(500)
print(employee1.salary())

employee2 = EmployeeSalary("Anna", hours=40, email="anna@example.com")
print(employee2.salary())
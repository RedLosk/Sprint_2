class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours=None, rest_days=0, email=None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, hours, rest_days):
        if hours is None:
            hours = (7 - rest_days) * 8
        return cls(hours=hours, rest_days=rest_days)

    @classmethod
    def get_email(cls, name, email):
        if email is None:
            email = f"{name}@email.com"
        return cls(name=name, email=email)

    @classmethod
    def set_hourly_payment(cls, new_payment):
        cls.hourly_payment = new_payment

    def salary(self):
        hours = self.hours if self.hours is not None else (7 - self.rest_days) * 8
        return hours * self.__class__.hourly_payment

employee = EmployeeSalary("Иван", rest_days=2)
print(employee.salary())

EmployeeSalary.set_hourly_payment(500)
print(employee.salary())

employee2 = EmployeeSalary("Анна", hours=40, email="anna@example.com")
print(employee2.salary())
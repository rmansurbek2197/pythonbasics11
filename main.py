class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self, bonus_percentage):
        return self.salary * bonus_percentage / 100

    def calculate_total_salary(self, bonus_percentage):
        return self.salary + self.calculate_bonus(bonus_percentage)


class PayrollSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def calculate_total_payroll(self, bonus_percentage):
        total_payroll = 0
        for employee in self.employees:
            total_payroll += employee.calculate_total_salary(bonus_percentage)
        return total_payroll


class Manager(Employee):
    def __init__(self, name, salary, bonus_percentage):
        super().__init__(name, salary)
        self.bonus_percentage = bonus_percentage

    def calculate_bonus(self, bonus_percentage):
        return super().calculate_bonus(self.bonus_percentage)


class Developer(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)


payroll_system = PayrollSystem()
payroll_system.add_employee(Manager("John Doe", 5000, 10))
payroll_system.add_employee(Developer("Jane Doe", 4000))
payroll_system.add_employee(Manager("Bob Smith", 6000, 15))
print(payroll_system.calculate_total_payroll(10))
print(payroll_system.employees[0].calculate_bonus(10))
print(payroll_system.employees[1].calculate_bonus(10))
print(payroll_system.employees[2].calculate_bonus(15))
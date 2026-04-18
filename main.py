class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_bonus(self, bonus_percentage):
        return self.salary * bonus_percentage / 100

    def calculate_payroll(self, bonus_percentage):
        bonus = self.calculate_bonus(bonus_percentage)
        return self.salary + bonus

class PayrollSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def calculate_total_payroll(self, bonus_percentage):
        total_payroll = 0
        for employee in self.employees:
            total_payroll += employee.calculate_payroll(bonus_percentage)
        return total_payroll

payroll_system = PayrollSystem()
employee1 = Employee("John Doe", 5000)
employee2 = Employee("Jane Doe", 6000)
payroll_system.add_employee(employee1)
payroll_system.add_employee(employee2)
print(payroll_system.calculate_total_payroll(10))
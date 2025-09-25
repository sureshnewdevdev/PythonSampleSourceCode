import csv

class Employee:
    def __init__(self, id, name, age, department, salary):
        self.id = int(id)
        self.name = name
        self.age = int(age)
        self.department = department
        self.salary = int(salary)

    def display_info(self):
        return f"ID: {self.id}, Name: {self.name}, Age: {self.age}, Department: {self.department}, Salary: {self.salary}"   

employees = []
with open('employees.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        emp = Employee(row['id'], row['name'], row['age'], row['department'], row['salary'])
        employees.append(emp)

        for emp in employees:
            print(emp.id, emp.name, emp.age, emp.department, emp.salary)
            print(f"ID: {emp.id}, Name: {emp.name}, Age: {emp.age}, Department: {emp.department}, Salary: {emp.salary}")
            print('DDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD')
            print(emp.display_info())
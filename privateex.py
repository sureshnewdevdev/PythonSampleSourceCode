class Employee:
    def __init__(self, name, salary, department):
        self.name = name           # Public attribute
        self._department = department  # Protected attribute
        self.__salary = salary     # Private attribute (name mangling)
    
    # Public method to access private attribute
    def get_salary(self):
        return self.__salary
    
    # Public method to modify private attribute with validation
    def set_salary(self, new_salary):
        if new_salary >= 0:
            self.__salary = new_salary
            print(f"Salary updated to ${new_salary}")
        else:
            print("Salary cannot be negative.")
    
    # Protected method for internal use
    def _calculate_bonus(self):
        return self.__salary * 0.1
    
    # Public method that uses protected method
    def get_bonus(self):
        bonus = self._calculate_bonus()
        return f"Bonus: ${bonus:.2f}"

# Usage
emp = Employee("Alice", 50000, "Engineering")
emp.__salary
print(emp.name)           # Accessible
print(emp._department)    # Accessible but should be treated as protected
# print(emp.__salary)     # Error: AttributeError
print(emp.get_salary())   # Correct way to access salary
emp.set_salary(55000)     # Correct way to modify salary
print(emp.get_bonus())    # Access bonus through public interface
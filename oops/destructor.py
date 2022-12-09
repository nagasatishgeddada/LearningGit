class Employee: #creating a class
    def __init__(self):
        print("Employee created")
    def __del__(self):
        print("Destructor called Employee deleted")
emp = Employee() #emp is object Employee is class
del emp
emp=Employee()
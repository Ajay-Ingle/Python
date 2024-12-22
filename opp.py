
"""
Create a sample class named Employee with two attributes id and name
employee :
    id
    name
object initializes id and name dynamically for every Employee object created.

emp = Employee(1, "coder")
Use del property to first delete id attribute and then the entire object
"""
class employee:
    def __init__(self,i,name):
        self.id = i
        self.name = name

    def display(self):
        print(f"The id of employee:{self.id} \nName: {self.name}")


emp = employee(1, "Ajay")


del emp

try:
    print(emp.id)
except NameError:
    print("The employee id not found")
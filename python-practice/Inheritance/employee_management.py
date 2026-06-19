class Employee:
    def __init__(self, name):
        self.name = name

    def show(self):
        print("Employee:", self.name)

class Manager(Employee):
    def manage(self):
        print("Managing Team")

m = Manager("Sathwika")

m.show()
m.manage()
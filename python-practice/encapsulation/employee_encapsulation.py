class Employee:

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

e = Employee("Sathwika")

print(e.get_name())
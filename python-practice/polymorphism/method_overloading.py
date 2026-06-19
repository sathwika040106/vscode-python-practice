class Calculator:
    def add(self, a, b=0):
        return a + b

c = Calculator()

print(c.add(10))
print(c.add(10, 20))
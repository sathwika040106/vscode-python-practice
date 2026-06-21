class Product:

    def __init__(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

p = Product(999)

print(p.get_price())
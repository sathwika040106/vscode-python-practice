class Grandparent:
    def show_grandparent(self):
        print("I am Grandparent")

class Parent(Grandparent):
    def show_parent(self):
        print("I am Parent")

class Child(Parent):
    def show_child(self):
        print("I am Child")

c = Child()

c.show_grandparent()
c.show_parent()
c.show_child()
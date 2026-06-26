class Book:

    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Book: {self.title}"


book = Book("Python Mastery")

print(book)
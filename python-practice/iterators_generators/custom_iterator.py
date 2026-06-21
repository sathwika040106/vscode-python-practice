class Count:
    def __init__(self, limit):
        self.limit = limit
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= self.limit:
            value = self.num
            self.num += 1
            return value
        raise StopIteration

c = Count(5)

for i in c:
    print(i)
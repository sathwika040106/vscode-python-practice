def numbers():
    yield 1
    yield 2
    yield 3

for num in numbers():
    print(num)
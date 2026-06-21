import logging

logging.basicConfig(
    filename="calculator.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))

result = a + b

logging.info(f"Addition Performed: {a} + {b} = {result}")

print("Result =", result)
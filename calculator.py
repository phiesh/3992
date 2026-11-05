import sys


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Деление на ноль запрещено")
    return a / b


def main(args):
    if len(args) != 4:
        print("Использование: calculator.py <операция> <a> <b>")
        return 1
    operation, a, b = args[1], float(args[2]), float(args[3])
    if operation == "add":
        result = add(a, b)
    elif operation == "subtract":
        result = subtract(a, b)
    elif operation == "multiply":
        result = multiply(a, b)
    elif operation == "divide":
        result = divide(a, b)
    else:
        print("Неизвестная операция")
        return 1
    print(result)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
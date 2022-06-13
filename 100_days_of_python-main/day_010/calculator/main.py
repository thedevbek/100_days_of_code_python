from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)
    num1 = float(input("What is the first number?: "))

    for symbol in operations:
        print(symbol)

    continue_calculations = True
    while continue_calculations:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))

        operation = operations[operation_symbol]
        answer = operation(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            continue_calculations = False
            calculator()

calculator()
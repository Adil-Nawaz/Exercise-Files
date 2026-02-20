def add(n1, n2):
    """takes 2 int variables as input and returns sum of them"""
    return n1+n2
def subtract(n1, n2):
    """takes 2 int variables as input and returns subtraction of them"""
    return n1-n2
def divide(n1, n2):
    """takes 2 int variables as input and returns division of them"""
    return n1/n2
def multiply(n1, n2):
    """takes 2 int variables as input and returns multiplication of them"""
    return n1*n2
#Operations
operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}
#Inputs
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
for keys in operations:
    print(keys)
operation_Symbol = input("What operation you want to perform? ")
for keys, values in operations.items():
    if operation_Symbol == operations[keys]:
        values(num1, num2)
print(values)
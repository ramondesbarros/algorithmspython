#
def addition(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2

def multiplication(n1, n2):
    return n1 * n2

def division(n1, n2):
    return n1 / n2

new_operation = True

while(new_operation == True):

    n1 = int(input("Enter the first number -> "))
    n2 = int(input("Enter the second number -> "))

    print("1- addition")
    print("2- subtraction")
    print("3- multiplication")
    print("4- division")

    operation = int(input("Enter the transaction number: -> "))

    if operation == 1:
        result = addition(n1, n2)

        print(result)

    if operation == 2:
        result = subtraction(n1, n2)
        print(result)

    if operation == 3:
        result = multiplication(n1, n2)
        print(result)

    if operation == 4:
        if n2 == 0:
            print("The second number cannot be 0. Try again!")
            continue
        else:
            result = division(n1, n2)
            print(result)
    new_operation = bool(int(input("Continue? 1 for yes, 0 for no: ")))





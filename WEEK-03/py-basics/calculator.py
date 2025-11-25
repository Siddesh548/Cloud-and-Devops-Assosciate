def calculator():
    try:
        n1 = float(input("Enter first number: "))
        n2 = float(input("Enter second number: "))

        if n2 == 0:
            print("Error: Second number cannot be ZERO for /, //, or % operations.")
            return

        print("Choose operation: +  -  *  /  //  %  **")
        op = input("Enter operator: ")

        if op == '+':
            print("Result:", n1 + n2)
        elif op == '-':
            print("Result:", n1 - n2)
        elif op == '*':
            print("Result:", n1 * n2)
        elif op == '/':
            print("Result:", n1 / n2)
        elif op == '//':
            print("Result:", n1 // n2)
        elif op == '%':
            print("Result:", n1 % n2)
        elif op == '**':
            print("Result:", n1 ** n2)
        else:
            print("Invalid operator!")

    except ValueError:
        print("Error: Please enter valid numbers.")

calculator()

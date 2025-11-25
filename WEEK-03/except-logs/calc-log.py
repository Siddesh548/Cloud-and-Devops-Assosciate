import logging

logging.basicConfig(
    filename="calculator.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def calculator(): 
    try:
        n1 = int(input("Enter first number: "))
        n2 = int(input("Enter second number: "))

        print("Choose operation: +  -  *  /  //  %  **")
        op = input("Enter operator: ")

        if op == '+':
            result = n1 + n2
            print("Result:", result)
            
            return

        elif op == '-':
            result = n1 - n2
            print("Result:", result)
            logging.warning(f"Subtraction performed: {n1} - {n2} = {result}")
            return

        elif op in ['/', '//', '%']:
            if n2 == 0:
                print("Error: Cannot divide by ZERO")
                logging.error(f"Zero division error: {n1} {op} {n2}")
                return

            if op == '/':
                result = n1 / n2
            elif op == '//':
                result = n1 // n2
            else:
                result = n1 % n2

            print("Result:", result)
            logging.info(f"Division op performed: {n1} {op} {n2} = {result}")

        elif op == '*':
            result = n1 * n2
            print("Result:", result)
            logging.info(f"Multiplication: {n1} * {n2} = {result}")
            return

        elif op == '**':
            result = n1 ** n2
            print("Result:", result)
            logging.info(f"Power: {n1} ** {n2} = {result}")
            return

        else:
            print("Error: Invalid operator!")
            logging.error(f"Unknown operator used: {op}")
            return

    except ValueError:
        print("Error: Enter valid numbers.")
        logging.error("Invalid numeric input.")

calculator()


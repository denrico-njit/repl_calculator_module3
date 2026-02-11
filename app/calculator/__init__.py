from app.operations import Operations

def calculator():
    """Basic REPL Calculator -- Not particularly useful, but instructive!"""
    print("Still the World's Most Mediocre REPL Calculator\n")
    
    # main loop for the calculator
    while True:
        print("Enter an operation (add/subtract/multiply/divide) and two numbers, separated by spaces.")
        print("e.g. add 1 2")
        print("or type 'quit' to quit")

        expression = input("Expression: ")

        if expression.lower() == 'quit':
            print('Quitting')
            break

        try:
            #split user input on whitespace
            operation, n1, n2 = expression.split()
            #Input validation:
            #ensure operation exists - raise error if not
            if operation not in ['add', 'subtract', 'multiply', 'divide']:
                raise ValueError
            #convert to floats if possible
            n1, n2 = float(n1), float(n2)
        except ValueError:
            print("Invalid input. Please follow the format: <operation> <num1> <num2>\n")
            continue


        if operation == 'add':
            result = Operations.addition(n1, n2)
        elif operation == 'subtract':
            result = Operations.subtraction(n1, n2)
        elif operation == 'multiply':
            result = Operations.multiplication(n1, n2)
        elif operation == 'divide':
            try:
                result = Operations.division(n1, n2)
            except ValueError as e:
                # Handle division by zero errors
                print(e)
                continue
        
        print(f"Result: {result}\n")

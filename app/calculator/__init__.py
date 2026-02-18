from app.operation import Operation
from app.calculation import Calculation, CalculationFactory
from typing import List


def display_help() -> None:
    """
    Displays the help message with usage instructions and supported operations.
    """
    help_message = """
Calculator Help
--------------------
Usage:
    <operation> <number1> <number2>
    - Perform a calculation with the specified operation and two numbers.
    - Supported operations:
        add       : Adds two numbers.
        subtract  : Subtracts the second number from the first.
        multiply  : Multiplies two numbers.
        divide    : Divides the first number by the second.
        power     : Exponentiates the first number by the second.

Special Commands:
    help      : Display this help message.
    history   : Show the history of calculations.
    exit      : Exit the calculator.

Examples:
    add 5 1
    subtract 4.1 2.2
    multiply 7 8
    divide 20 4
    power 2 3
    """
    print(help_message)

def display_history(history: List[Calculation]) -> None:
    """
    Displays the history of calculations performed during the session.

    Parameters:
        history (List[Calculation]): A list of Calculation objects representing past calculations.
    """
    if not history:
        print("Nothing to see here yet.")
    else:
        print("Previous Calculations:")
        for idx, calculation in enumerate(history, start=1):
            print(f"{idx}. {calculation}")

def calculator():
    """Basic REPL Calculator -- Not particularly useful (yet), but instructive!"""

    # initialize history - a list of calculations.
    # neat type hinting from exemplar code. didn't know you could do that
    # for variables as well as functions!
    history: List[Calculation] = []

    print("Still the World's Most Mediocre REPL Calculator")
    print("Type 'help' for instructions, 'history' to see previous calculation, or 'exit' to quit.\n")

    # main loop for the calculator
    while True:
        try:
            # take input and strip extra whitespace from ends
            user_input = input(">> ").strip()

            if not user_input:
                continue # pragma: no cover
            
            if user_input == 'help':
                display_help()
                continue
            
            elif user_input == 'history':
                display_history(history)
                continue

            elif user_input.lower() in ['quit', 'exit', 'q']:
                print('Quitting')
                break
            
            # Ensure formatting of the calculation is correct - operation number number
            try:
                operation, str_num1, str_num2 = user_input.split()
                num1 = float(str_num1)
                num2 = float(str_num2)
            except ValueError:
                # catch botched split on user input
                # either due to poor formatting or invalid conversion
                print("Invalid input. Use the format <operation> <num1> <num2>")
                print("or type 'help' for more information.")
                continue
            
            # Attempt to use factory to create calculation object
            try:
                calculation = CalculationFactory.create_calculation(operation, num1, num2)
            except ValueError as e:
                # catch nonexistent operations
                print(e)
                print("Invalid input. Type 'help' to see the list of valid operations")
                continue

            # Attempt to run the calculation
            try:
                result = calculation.execute()
            except ZeroDivisionError:
                # catch div/0
                print("Cannot divide by zero.")
                print("Please enter a non-zero divisor.")
                continue
            except Exception as e:
                print(f"Something unforseen has happened: {e}")
                print("Please try again.")
                continue
            
            # Kludge(?) to make the output readable. History still stores full calculation
            result = str(calculation).split()[-1]
            print(f"Result: {result}")
            history.append(calculation)




                

                
        except KeyboardInterrupt:
            # catches ctrl + C
            print("KeyboardInterrupt detected. Exiting.")
            break
        except EOFError:
            # catches ctrl + D
            print("EOF Detected. Exiting")
            break


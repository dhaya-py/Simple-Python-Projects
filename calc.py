while True:
    print("Options :")
    print("Enter 'add' for Addition")
    print("Enter 'sub' for Subtraction")
    print("Enter 'mul' for Multiplication")
    print("Enter 'div' for Division")
    print("Enter 'Quit' to end the program")

    user_input = input("Enter the option :")

    if user_input == "Quit":
        break

    elif user_input in ('add', 'sub', 'mul', 'div'):
        num1 = float(input("Enter first number :"))
        num2 = float(input("Enter second number :"))

        if user_input == 'add':
            print(f"Result: {num1 + num2}")
        elif user_input == 'sub':
            print(f"Result: {num1 - num2}")
        elif user_input == 'mul':
            print(f"Result: {num1 * num2}")
        elif user_input == 'div':
            if num2 != 0:
                print(f"Result: {num1 / num2}")
            else:
                print("Can't divide by zero.")
    else:
        print("Invalid input. Please enter the Valid Option.")

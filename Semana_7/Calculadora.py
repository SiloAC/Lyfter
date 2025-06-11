current_number = 0

def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b 


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


while True:
    print(f"Current number: {current_number}")

    while True:
        try:
            operation = int(input("Select an operation to perform:" 
                            "\n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Erase\n"))
            break
        except:
            print("Enter a valid number")
            print(f"Current number: {current_number}")

    if operation == 1:
        num1 = float(input("Choose a number to add to the current number: "))
        result = addition(current_number, num1)
    elif operation == 2:
        num1 = float(input("Choose a number to subtract to the current number: "))
        result = subtraction(current_number, num1)
    elif operation == 3:
        num1 = float(input("Choose a number to multiply by the current number: "))
        result = multiplication(current_number, num1)
    elif operation == 4:
        num1 = float(input("Choose a number to divide by the current number: "))
        if num1 == 0:
            print("You cannot divide by 0")
            break
        else:    
            result = division(current_number, num1)
    elif operation == 5:
        current_number = 0
        result = current_number
    else:
        print("Invalid operation type")
        break

    current_number = result

    print(f"Current number: {current_number}")

    again = int(input("Type 1 to continue, and 2 to Finish "))
    
    if again == 1:
        print("Thank you")
    elif again == 2:
        print("Goodbye")
        break
    elif again != 1 or 2:
        print("Nice try")
        break
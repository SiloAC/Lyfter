def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


def calculator():
    current_number = 0
    while True:
        print(f"Current number: {current_number}")

        while True:
            try:
                operation = int(input("Select an operation to perform:"
                    "\n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Erase\n"))
                break
            except:
                print("Enter a valid number")

        if operation == 1:
            num1 = float(input("Choose a number to add to the current number: "))
            result = addition(current_number, num1)
        elif operation == 2:
            num1 = float(input("Choose a number to subtract from the current number: "))
            result = subtraction(current_number, num1)
        elif operation == 3:
            num1 = float(input("Choose a number to multiply by the current number: "))
            result = multiplication(current_number, num1)
        elif operation == 4:
            num1 = float(input("Choose a number to divide by the current number: "))
            if num1 == 0:
                print("You cannot divide by 0")
                continue 
            else:
                result = division(current_number, num1)
        elif operation == 5:
            current_number = 0
            continue 
        else:
            print("Invalid operation type")
            break

        current_number = result #updates the current number so it wont be 0
        print(f"Current number: {current_number}")

        again = int(input("Type 1 to continue, and 2 to Finish "))
        if again == 1:
            continue  
        elif again == 2:
            print("Goodbye")
            break
        else:
            print("Nice try")
            break

def main():
    try:
        calculator()
    except ValueError:
        print("Please enter a valid number")

main()
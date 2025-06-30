numbers = []

print("Enter 10 numbers: ")

for i in range(10):
    while True:
        number = int(input(f"Number {i + 1}: "))
        numbers.append(number)
        break

max_number = max(numbers)
numbers.remove(max_number)
numbers.insert(1, max_number)

print(f"New organized list: {numbers}. The highest number was: {max_number}")
print("Choose 3 numbers, I will tell you which is the highest one")
first_number = int(input("Choose your first number:"))
second_number = int(input("Choose your second number:"))
third_number =int(input("Choose your third number:"))

highest = max(first_number, second_number, third_number)
print(f"The highest number is: {highest}") 
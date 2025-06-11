def sum_list (numbers):
    total = 0
    for number in numbers:
        total += number
    return total

numbers_list = [1, 2, 3, 4, 5]
result = sum_list(numbers_list)
print("The total addition is:", result)
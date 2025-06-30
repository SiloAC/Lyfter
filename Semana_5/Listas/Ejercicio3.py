def exchange_ends(list):
    if len(list) < 2:
        return list #nothing to exchange
    list[0], list[-1] = list[-1], list[0]
    return list
    

first_list = [1, 2, 3, 4, 5]
second_list = [6]
first_result = exchange_ends(first_list)
second_result = exchange_ends(second_list)

print(f"More than one number:", first_result)
print(f"Only one number:", second_result)

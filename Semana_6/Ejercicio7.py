def is_prime (n): #Checks if number is odd
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1): #Found this online. Not really sure how it works, but it did
        if n % i == 0:
            return False
    return True


def filter_primes(numbers_list): #Goes through the list checking primes
    primes = []
    for number in numbers_list:
        if is_prime(number):
            primes.append(number)
    return primes


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 17, 19, 23, 25, 27, 50, 59, 60, 71]
result = filter_primes(numbers)
print(result)
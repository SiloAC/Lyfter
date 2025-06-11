import random

secret = random.randint(1, 10)

print("Try to find the secret number between 1 and 10")

while True:
    user_number = int(input("Choose a number: "))

    if user_number == secret:
        print("Congratulations!")
        break
    else:
        print("Try again")
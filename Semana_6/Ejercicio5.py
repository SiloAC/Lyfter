def count_uppercase_lowercase (words):
    uppercase = 0
    lowercase = 0

    for character in words:
        if character.isupper():
            uppercase += 1
        elif character.islower():
            lowercase += 1

    print(f"Number of uppercase letters: {uppercase}")
    print(f"Number of lowercase letters: {lowercase}")

count_uppercase_lowercase("Hello World!")


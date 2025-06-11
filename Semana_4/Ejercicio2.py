name = input("What is your name?")
last_name = input("What is your last name?")
age = int(input("What is your age?"))

if (age <= 3):
    print (f"You are a baby named {name} {last_name}")
elif (age <= 10):
    print (f"You are a child named {name} {last_name}")
elif (age <= 12):
    print (f"You are a preadolescent named {name} {last_name}")
elif (age <= 30):
    print (f"You are a young adult named {name} {last_name}")
elif (age <=59):
    print (f"You are a adult named {name} {last_name}")
else:
    print (f"You are a senior named {name} {last_name}")
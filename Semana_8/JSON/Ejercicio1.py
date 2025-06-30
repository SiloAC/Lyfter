import json

pokemon_data = [
    {
        "name": {"english": "Pikachu"},
        "type": ["Electric"],
        "base": {
            "HP": 35,
            "Attack": 55,
            "Defense": 40,
            "SP. Attack": 50,
            "Sp. Defense": 50,
            "Speed": 90
        }
    },
    {
        "name": {"english": "Charmander"},
        "type": ["Fire"],
        "base": {
            "HP": 39,
            "Attack": 52,
            "Defense": 43,
            "SP. Attack": 60,
            "Sp. Defense": 50,
            "Speed": 65
        }
    },
    {
        "name": {"english": "Squirtle"},
        "type": ["Water"],
        "base": {
            "HP": 44,
            "Attack": 48,
            "Defense": 65,
            "SP. Attack": 50,
            "Sp. Defense": 64,
            "Speed": 43
        }
    }
]

def add_pokemon():
    name = input("Enter Pokémon name: ")

    print("Enter Pokémon types (one at a time). Type 'done' exactly to finish:")
    types = []
    while True:
        t = input("Type: ")
        if t == "done":  # case-sensitive / to fix this we can use .lower / not seen yet
            break
        types.append(t)

    print("Enter base stats:")
    hp = int(input("HP: "))
    attack = int(input("Attack: "))
    defense = int(input("Defense: "))
    sp_attack = int(input("SP. Attack: "))
    sp_defense = int(input("Sp. Defense: "))
    speed = int(input("Speed: "))

    new_pokemon = {
        "name": {"english": name},
        "type": types,
        "base": {
            "HP": hp,
            "Attack": attack,
            "Defense": defense,
            "SP. Attack": sp_attack,
            "Sp. Defense": sp_defense,
            "Speed": speed
        }
    }

    pokemon_data.append(new_pokemon)
    print(f"Pokémon '{name}' added successfully!")

# Main loop
while True:
    print("1. Add a new Pokémon")
    print("2. View all Pokémon")
    print("3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_pokemon()
    elif choice == "2":
        print(json.dumps(pokemon_data, indent=4))
    elif choice == "3":
        break
    else:
        print("Invalid option. Try again.")
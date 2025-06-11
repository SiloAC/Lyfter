import csv

def save_games_on_svc():
    file = 'games.csv'
    headers = ['Name', 'Genre', 'Developer', 'ESRB Rating']
    games = []

    try:
        number_of_games = int(input("How many games would you like to add?"))
    except ValueError:
        print("Please enter a valid number")

    for i in range(number_of_games):
        print(f"\n--- Game {i+1} ---")
        name = input("Name: ")
        genre = input("Genre: ")
        developer = input("Developer: ")
        esrb = input("ESRB Rating: ")
        games.append([name, genre, developer, esrb])

    with open(file, 'w', newline='', encoding='utf-8') as new_file:
        writer = csv.writer(new_file)
        writer.writerow(headers)
        writer.writerows(games)
    
    print(f"{number_of_games} games have been saved to file {file}")

save_games_on_svc()
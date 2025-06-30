def order_songs(entry, output):
	try:
		#saving song names on variable
		with open(entry, 'r', encoding='utf-8') as entry_songs:
			songs = entry_songs.readlines()

		#Ordering songs alphabetically
		n = len(songs)
		for i in range(n):
			for j in range(0, n - i - 1):
				if songs[j] > songs[j + 1]:  
					songs[j], songs[j + 1] = songs[j + 1], songs[j]
		
		#Overriding new file
		with open(output, 'w', encoding='utf-8') as output_songs:
			output_songs.writelines(songs)
		
		print(f"{len(songs)} songs have been saved on file {output}")

	except FileNotFoundError:
		print(f"The file '{entry}' was not found.")

order_songs('songs.txt', 'new_songs.txt')
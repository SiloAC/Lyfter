def order_words (new_words):
    words = []
    current_word = ""

    for character in new_words: # Converting to list
        if character == "-": 
            words.append(current_word) 
            current_word = "" # Resets the variable
        else:
            current_word += character 
    
    words.append(current_word) 

    for i in range(len(words)): #Bubble algorithm - sorting the words alphabetically 
        for j in range(0, len(words) - i - 1):
            if words[j] > words[j + 1]:
                words[j], words[j + 1] = words[j + 1], words[j]

    result = "" 
    for word in range(len(words)): #Converting to string again
        result += words[word]
        if word < len(words) - 1:
            result += "-" #Re-adding the dash

    return result 

result = order_words("zebra-mouse-dog-cat")
print(result)
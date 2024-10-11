def character_counter(sentence):
    sentence = sentence.lower()  # Convert the sentence to lowercase to ignore case differences
    counter = {}  # Initialize an empty dictionary to store the character counts

    # Loop through each character in the sentence
    for character in sentence:  
        if character.isalpha():  # Check if the character is a letter (ignore other characters)
            if character in counter:  # If the character is already in the dictionary, increase its count
                counter[character] += 1
            else:
                counter[character] = 1  # If the character is not in the dictionary, add it with count 1

    # Print the count of each character
    for letter, count in counter.items():
        print(f"'{letter}' appears {count} times")

sentence = input("Enter a sentence: ")
character_counter(sentence)


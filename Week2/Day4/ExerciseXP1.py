 # 🌟 Exercise 1: Random Sentence Generator

# Goal: Create a program that generates a random 
# sentence of a specified length from a word list.

# Key Python Topics:
#     File handling (open(), read())
#     Lists
#     Random number generation (random.choice())
#     String manipulation (split(), join(), lower())
#     Error handling (try, except)
#     Input validation

# Instructions:
#     Download the provided word list and save it in 
#       your development directory.
#     Create a function to read the words from the 
#       file.
#     Create a function to generate a random sentence 
#       of a given length.
#     Create a main function to handle user input and 
#       program flow.

# Step 1: Create the get_words_from_file function
#     Create a function named get_words_from_file 
#       that takes the file path as an argument.
#     Open the file in read mode ("r").
#     Read the file content.
#     Split the content into a list of words.
#     Return the list of words.


def get_words_from_file(file_path):
        with open(file_path, "r") as file:
            content = file.read()

        words = content.split()
        return words

# Step 2: Create the get_random_sentence function
#     Create a function named get_random_sentence 
#       that takes the sentence length as an argument.
#     Call get_words_from_file to get the list of 
#       words.
#     Select a random word from the list length times.
#     Create a sentence with the selected words.
#     Convert the sentence to lowercase.
#     Return the sentence.

import random

def get_random_sentence(length):
    words = get_words_from_file("words.txt")

    random_words = []

    for _ in range(length):
        random_word = random.choice(words)
        random_words.append(random_word)

    sentence = " ".join(random_words).lower()
    return sentence

# Step 3: Create the main function

#     Create a function named main.
#     Print a message explaining the program’s purpose.
#     Ask the user for the desired sentence length.
#     Validate the user input:
#         Check if it is an integer.
#         Check if it is between 2 and 20 (inclusive).
#     If the input is invalid, print an error message and exit.
#     If the input is valid, call get_random_sentence with the length and print the generated sentence.

def main():
    print("This program generates a random sentence from a word list.")
    user_input = input("Enter sentence length (between 2 and 20): ")

    try:
        length = int(user_input)

        if length < 2 or length > 20:
            print("Error: Length must be between 2 and 20.")
            return

    except ValueError:
        print("Error: Please enter a valid integer.")
        return

    sentence = get_random_sentence(length)
    print("Generated sentence:")
    print(sentence)

if __name__ == "__main__":
    main()
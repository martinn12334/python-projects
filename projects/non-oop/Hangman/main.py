#Step 1

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random

word = random.choice(word_list)
print(word)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
user_answer = input("Enter your guess: ").lower()
# print(user_answer)

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for letter in word:
    if letter == user_answer:
        print("Right")
    else:
        print("Wrong")
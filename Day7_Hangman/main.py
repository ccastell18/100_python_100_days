# imported for use of random function
import random
import os
import words
import art


# models for the hangman

print(art.logo)
# used to keep the game going in the while loop until it is switched to true
end_of_game = False
# words chosen for game
word_list = words.words
# selects and saves a random word from list
chosen_word = random.choice(word_list)
# saves the length of the word that was chosen
word_length = len(chosen_word)
# number of chances left
lives = 6

# test hint
print(f'The solution is {chosen_word}')


# set a blank space per word
display = []

for _ in range(word_length):
    display += "_"
print(display)


# starts the game. Will continue until end_of_game is true
while not end_of_game:
    print(art.stages[lives])

    # asks user to guess a letter
    guess = input('Guess a letter: ').lower()

    if guess in display:
        print("You Have chosen that letter already")

    # check if letter is in the chosen word
    for position in range(word_length):
        letter = chosen_word[position]
        # if the letter is in the word, will change the display to the letter
        if letter == guess:
            display[position] = letter
  # if it is not in the word, it will take a chance away and print stage.
    if guess not in chosen_word:
        lives -= 1
        print("You have chosen unwisely.")

        # when no more chances, the end_of_game = true and game is over
        if lives == 0:
            end_of_game = True
            print("You lose!")

    print(f"{' '.join(display)}")

    # if all letters are chosen correctly, the end_of_game turns true and game is won
    if "_" not in display:
        end_of_game = True
        print("You win")

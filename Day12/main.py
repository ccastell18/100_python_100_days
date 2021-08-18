import random


# global variables
EASY_LEVEL = 10
HARD_LEVEL = 5


# checks your guess vs computer answer
def check_answer(guess, answer, turns):
  if guess > answer:
    print("Too high")
    return turns - 1
  elif guess < answer:
    print("Too low")
    return turns - 1
  else:
    print("You got it right!" )
   

# sets the difficulty using global variables 
def set_difficulty():
  level = input("Choose your difficulty. Type 'easy' or 'hard': ")
  if level == 'easy':
    return EASY_LEVEL
  else: 
    return HARD_LEVEL
 
def game():   

  print("Welcome to the Number guessing game!")
  print("I am thinking of a number between 1 and 100.")
  answer = random.randint(1, 101)
  print(f"The answer is {answer}")

  turns = set_difficulty()

  guess = 0
    
  while guess != answer:

    print(f'You have {turns} attempts remaining to guess the number.')
    
    guess = int(input("Make a guess: "))
    
    turns = check_answer(guess, answer, turns)

    if turns == 0:
      print('You have run out of turns.  You lose.')
      return

game()


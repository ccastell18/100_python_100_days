import art
from game_data import data
import random
import os

#format the account data into printable format
def format_account(account):
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
  """check that the guess is correct by comparing the counts."""
  if a_followers > b_followers:
    return guess == 'a'
  else: 
    return guess == 'b'
def game():
  # Display art
  print(art.logo)
  score = 0
  game_should_continue = True
  account_b = random.choice(data)

  while game_should_continue:
    #Generate a random account from the game data
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
      account_b = random.choice(data)

    print(f"Compare A: {format_account(account_a)}")

    print(art.vs)

    print(f"Compare B: {format_account(account_b)}")
    #Ask user for a guess
    guess = input("Which has more followers? Type: 'A' or 'B': ").lower()
    #Check if user is correct
    ##Get follower account
    a_followers_count = account_a["follower_count"]
    b_followers_count = account_b["follower_count"]
    ## Use if statement to check if user is correct
    is_correct = check_answer(guess, a_followers_count, b_followers_count)
    os.system('clear')
    print(art.logo)
    #Give user feedback
    #Score keeping
    if is_correct:
      score += 1
      print(f"You are right! Current score: {score}")
    else:
      game_should_continue = False
      print(f"Sorry.  You are wrong.  Final score: {score}")
game()
    


#make the game repeatable

#Making account at positon B become the next account at position A

#Clear screen
  
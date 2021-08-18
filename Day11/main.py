import random
import os

# deals random cards

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card
def play_game():
  # players in game
  user_cards = []
  computer_cards = []
  is_game_over = False

  # figures out the scores from sum of cards and makes changes if necessary
  def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
      return 0
    # changes Ace from 11 to 1
    if 11 in cards and sum(cards) > 21:
      cards.remove(11)
      cards.append(1) 
    return sum(cards)

  def compare(user_score, computer_score):
    if user_score == computer_score:
      return "Draw"
    elif computer_score == 0:
      return "Lose, opponent has blackjack"
    elif user_score == 0:
      return "Winner with BlackJack"
    elif computer_score > 21:
      return "Your opponent busts"
    elif user_score > 21:
      return "You bust"
    elif user_score > computer_score:
      return "You Win"
    else:
      return "You lose"

  # add the cards into user list
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())


  while not is_game_over:
    # deals the cards
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards} and a score {user_score}")
    print(f"Computers first cards: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Type 'y' if you would like another card or 'n' to stay: ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)


  print(f"Your final cards were {user_cards} and your final score was {user_score}" )
  print(f"Your opponent's final cards were {computer_cards} and final score {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play another game? 'y' or 'n': ") == 'y':
  os.system('clear')
  play_game()
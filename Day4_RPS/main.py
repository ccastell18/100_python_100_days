import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input(
    "What do you choose: \n 0 for Rock \n 1 for Paper \n 2 for scissor \n "))

print(game_images[user_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number")
else:
    computer_choice = random.randint(0, 2)

    print("Computer chooses: ")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print('You win')
    elif computer_choice == 0 and user_choice == 2:
        print("You Lose")
    elif computer_choice > user_choice:
        print("You Lose")
    elif user_choice > computer_choice:
        print("You win")
    elif user_choice == computer_choice:
        print("It is a tie")

    print(f"computer chose {computer_choice}")

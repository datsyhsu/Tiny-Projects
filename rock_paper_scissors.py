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

#Write your code below this line 👇
import random

game_image = [rock, paper, scissors]

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors.\n"))
if your_choice >= 3 or your_choice < 0:
  print("You typed an invalid number. You lose!")
else:
  print(game_image[your_choice])

  computer_choice = random.randint(0, 2)
  print("Computer choose:")
  print(game_image[computer_choice])


  if your_choice == 0 and computer_choice == 2:
    print("You win!")
  elif computer_choice == 0 and your_choice == 2:
    print("You lose.")
  elif computer_choice > your_choice:
    print("You lose.")
  elif your_choice > computer_choice:
    print("You win!")
  elif computer_choice == your_choice:
    print("It's a draw.")


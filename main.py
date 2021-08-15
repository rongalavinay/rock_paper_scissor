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

game_images=[rock,paper,scissors]
run=True

while run:
  user_choice=int(input("type 0 for rock, 1 for paper, 2 for scissor\n"))
  comp_choice=random.randint(0,2)
  print(game_images[user_choice])
  print("computers choice:")
  print(game_images[comp_choice])
  if comp_choice==2 and user_choice==0:
    print("you wins")
  elif user_choice==2 and comp_choice==0:
    print("you lose")
  elif user_choice>=3:
    print("you typed invalid number, you lose")
  elif comp_choice>user_choice:
    print("you lose")
  elif comp_choice==user_choice:
    print("draw")
  elif comp_choice<user_choice:
    print("you wins")
  again=input('want to play again type "y" for yes and "n" for no ').lower()
  if again=='n':
    run=False

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

request = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ? \n")
print(request)
'''if request == "0":
    print("You have selected ROCK. Play NOW\n       ---'   ____) \n      (_____) \n      (_____) \n      (____) \n     ---.__(___)")'''

computer_option = random.randrange(0, 3)
valid_options = ['0' , '1' , '2']
if request in valid_options and computer_option == 0:
    print('you win')
else:
    print("Sorry, You Loose")




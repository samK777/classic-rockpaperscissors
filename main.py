import random

# Defining the ASCII art for rock, paper, and scissors
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
    ---'    ____)____
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

# List of choices
my_choice = [rock, paper, scissors]

# Prompt for user input
print("Welcome to RPS!")
choice = input("Rock, Paper, or Scissors: ").lower()

# Get a random choice for the computer
cc = random.choice(my_choice)

# Display both choices
print(f"\nYour choice:\n{choice}")
print(f"\nComputer's choice:\n{cc}")

# Determine the winner
if cc == rock and choice == "paper":
    print("You win!")
elif cc == paper and choice == "rock":
    print("Computer wins!")
elif cc == rock and choice == "scissors":
    print("Computer wins!")
elif cc == scissors and choice == "rock":
    print("You win!")
elif cc == paper and choice == "scissors":
    print("You win!")
elif cc == scissors and choice == "paper":
    print("Computer wins!")
else:
    print("Wrong input!")

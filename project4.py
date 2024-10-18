#Project - 4 - Rock Paper Scissors Game

print("Project - 4 - Rock Paper Scissors")

import random
print("Welcome to Rock Paper Scissors Game")

human_choice = int(input("What do you choose? Type 0 for 'Rock', 1 for 'Paper' and 2 for 'Scissors':"))
computer_choice = print("Computer's choice:",random.randint(0,2))
if human_choice == 0 and computer_choice == 2:
    print("You Won!")
elif computer_choice == 1 and human_choice == 2:
    print("You Won!")
elif computer_choice == 0 and human_choice == 2:
    print("You Lost!")
elif computer_choice == human_choice:
    print("No Result, please try again!")
else:
    print("You Lost!")
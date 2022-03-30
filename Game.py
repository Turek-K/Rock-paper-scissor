from secrets import choice
import random

choice = ["Rock", "Paper", "Scissors "]

computer_choice = random.choice(choice)
print(computer_choice)
human_choice = input("choice between Rock, Paper, Scissors: ")
human_choice = human_choice.capitalize()
print(human_choice)

human_score = 0
computer_score = 0

def display(computer_choice, human_choice, computer_score, human_score):
    print("Computer choice:", computer_choice)
    print("Human choice:", human_choice)
    print("Computer score: ", computer_score)
    print("Human score: ", human_score)



if computer_choice == human_choice:
    display(computer_choice, human_choice, computer_score, human_score)
    print("Draw!")
elif human_choice == "Scissors":
    if computer_choice == "Rock":
        computer_score += 1
        display(computer_choice, human_choice, computer_score, human_score)
        print("Computer Win")
    else:
        human_score += 1
        display(computer_choice, human_choice, computer_score, human_score)
        print("You Win!")
elif human_choice == "Paper":
    if computer_choice == "Scissors":
        computer_score += 1
        display(computer_choice, human_choice, computer_score, human_score)
        print("Computer Win")
    else:
        human_score += 1
        display(computer_choice, human_choice, computer_score, human_score)
        print("You Win!")

elif human_choice == "Rock":
    if computer_choice == "Paper":
        computer_score += 1
        display(computer_choice, human_choice, computer_score, human_score)
        print("Computer Win")
    else:
        human_score += 1
        display(computer_choice, human_choice, computer_score, human_score)
        print("You Win!")

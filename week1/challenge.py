import random

# player1 = "rock"
choices = ["rock", "paper", "scissors"]
num = random.randint(0, 2)
choice2 = choices[num]

player1 = input("Player 1: ")



if player1 == choice2:
    print("Player 1: " + player1)
    print("Computer: " + choice2)
    print("You Draw")
elif player1 == "paper" and choice2 == "rock" or player1 == "scissors" and choice2 == "paper" or player1 == "rock" and choice2 == "scissors":
    print("Player 1: " + player1)
    print("Computer: " + choice2)
    print("You win :)!!")
else:
    print("Player 1: " + player1)
    print("Computer: " + choice2)
    print("You Lose :( !!")
            
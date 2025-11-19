import random

choices = ["rock", "paper", "scissors"]

for i in range(1, 11):
    print(f"\n Round {i}")

    computer = random.choice(choices)

    player = input("Enter rock, paper or scissors").lower()

    if player == computer:
        print("It's a draw.")

    elif(player == "rock" and computer == "scissors") or \
            (player == "scissors" and computer == "paper") or \
                (player == "paper" and computer == "rock"):
        print("Player wins this round.")
    else:
        print("Computer wins this round.")


    print(f"The computer chose {computer}")
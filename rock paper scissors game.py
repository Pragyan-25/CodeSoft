import random

options = ["rock", "paper", "scissors"]

print("Welcome to Rock, Paper, Scissor Game!")
while True:
    user = input("Enter your choice (rock/paper/scissors): ").lower()


    if user not in options:
        print("Invalid option!")
        continue
    
    computer = random.choice(options)

    print(f"Computer chose: {computer}")
    print(f"User chose:{user}")

    if user==computer:
        print("Game is tie!")
    elif user=="rock" and computer=="scissors":
        print("You won the game!")
    elif user=="scissors" and computer=="paper":
        print("You won the game!")
    elif user=="paper" and computer=="rock":
        print("You won the game!")
    else:
        print("You Lose the game!")


    want_to_play = input("Do you want to play again? (Y/N): ").lower()
    if want_to_play != "y":
        print("Thanks for playing the game!")
        break


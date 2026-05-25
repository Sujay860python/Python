
import random

print("Welcome to Rock Paper Scissor Game")

choices = ["rock", "paper", "scissor"]

while True:

    user_choice = input("Enter Rock, Paper, Scissor (Type 'quit' to exit): ").strip().lower()

    if user_choice == "quit":
        print("Thanks for playing!")
        break

    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")

    elif (
        (user_choice == "rock" and computer_choice == "scissor") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissor" and computer_choice == "paper")
    ):
        print("You won the game! 🏆🎉")

    else:
        print("You lose the game! 💀")

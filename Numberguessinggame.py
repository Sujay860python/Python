import random

secret_number=random.randint(1,100)

print("Welcome to the number guessing game")
print("In this game,I'm thinking of a number from 1 to 100")
print("You have to guess the number that I will think of it.")

while True:
  user_guess = int(input("Enter your guess :"))
        
  if user_guess<secret_number:
     print("Too low! Guess a high number")

  elif user_guess>secret_number:
     print("Too high! Guess a low number")

  else:
   print("Congratulations!You won the game ,you guessed the number")
   break

import random

print("Welcome to Rock,Paper Scissor game: ")


#Choices of game
choice=["rock,paper,scissors: "]

student_user=input("Enter rock,paper,scissor['or quit to exit']:")

while True:

    if student_user=="quit":
       print("Thanks for playing our game.")
    break   #break the loop

    if student_user not in choices:
        print("Invalid choice .Please try again.")
    continue

    #Computer Choices
    computer_choice=random.choices(choice)
    print("Computer chose:"  ,(computer_choice))

    elif:
    (if student_user=="paper" and computer_choice=="stone":)or\
    (if student_user=="stone" and computer_choice=="scissor":)or\
    (if student_user=="scissor" and computer_choice=="paper":)or\
    print("Hurray!You won the game.")

    else:
    print("You lose the game.")
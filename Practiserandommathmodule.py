#Q1.Write a program to find the square root of 49 using the math module.
#Answer:-
import math
print(math.sqrt(49))

#Q2.Write a program to find the factorial of 6.
#Answer:-
print(math.factorial(6))

#Q3.Create a list of 5 colors and print a random color.
#Answe:-
import random

colors=["black","blue","brown","white","red"]
print(random.choice(colors))

#Q4.Create a dice rolling program using random.randint().
#Answer:-

dice=random.randint(1,6)
print("Dice number is :", dice)

#Q5.Write a program to find the square root of 81 using the math module.
#Answer:-
print(math.sqrt(81))
#Q6.Write a program to generate a random number between 10 and 20.
#Answer:-
number=random.randint(11,19)
print("The Random number is:", number )

#Q7.Create a list of names and print a random name using random.choice().
#Answer:-
names=["Rohan","Ram","Shyam","Suresh","Sujay"]
print(random.choice(names))

#Q8.Write a dice game that generates a number from 1 to 6.
#Answer:-
dice_num=random.randint(1,6)
print("The dice number is :", dice_num)

#Q9.Write a program to find the factorial of 7 using the math module
#Answer:-
print(math.factorial(7))

#Q10.Create a coin toss program using the random module.
#Answer:-
coin_toss=["The result of coin_toss is: heads ","The result of coin_toss is :tails "]
print(random.choice(coin_toss))

#Q11.Find Area of Circle and calculate area of a circle for radius = 7.
#Answer:-
#I have a doubt in this question.
#Q12.Create an OTP generator that generates a 4-digit OTP.
#Answer:

otp_generator=random.randint(1000,9999)
print("Your OTP is (Please don't share it to everyone):", otp_generator)
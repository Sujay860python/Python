#1. Write a program to check whether a number is positive or negative.
#Answer:-
num_user=int(input("Enter a number: "))

if num_user<0:
    print("It is  a negative number.")

elif num_user==0:
    print("0 is neither positive either negative.")

else:
    print("It is a positive number.")
#2. Write a program to check whether a number is even or odd.
#Answer:-
student_user=int(input("Enter a number: "))

if student_user%2==0:
    print("It is a even number.")

else:
    print("It is a odd number.")

#3. Write a program to find the largest of two numbers.
#Answer:-
def print_large(y,z):
    large=max(y,z)
    print("The largest number is :" ,large)

#Usage Example
print_large(78,43)

#4. Write a program using a loop to print numbers from 1 to 10.
#Answer:-
for i in range(1,11):
    print(i)
#5. Write a program to print even numbers from 1 to 20.
#Answer:-
i=2

while i<=20:
    print(i)
    i+=2
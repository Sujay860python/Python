#Q1. Write a program to check whether a number is:
#Positive
#Negative
#Zero
#Answer:-
num_code=int (input("Enter a number: "))

if num_code<0:
    print("It is a negative number.")

elif num_code==0:
    print("0 is neither positive nor negative.")

else:
    print("It is a positive number.")

#Q2. Write a program to find the largest of three numbers using if-elif-else.
#Answer:-
student_num1=int(input("Enter first number: "))
student_num2=int(input("Enter  second number: "))
student_num3=int(input("Enter third number: "))

if (student_num1>=student_num2)and(student_num1>=student_num3):
   largest=student_num1

elif(student_num2>=student_num1)and (student_num2>=student_num3):
    largest=student_num2

else:
    largest=student_num3

print(f"The largest number is {largest}")
     
#Q4. Write a program to display grades:

#Marks                          Grade
#90-100                          A
#75-89                           B
#50-74                           C
#Below 50                        Fail
#Answer:-
marks=int(input("Enter marks: "))

if marks<0 or marks >100:
    print("Invalid Choice! Please enter a value between 0 and 100.")
 
elif marks>=90:
    print("Grade 'A'")

elif marks>=75:
    print("Grade 'B'")

elif marks >=50:
    print(" Grade 'C'")

else:
    print("Fail")

#Q5. Create a function named welcome() that prints:
#Answer:-
def welcome():
    print("Welcome to Python.")
welcome()

#Q6.Create a function that accepts two numbers and prints their sum.
#Answer:-
def print_sum(num1,num2):
    total=num1+num2
    print(f"The sum of {num1} and {num2} is {total}")

print_sum(39,51)

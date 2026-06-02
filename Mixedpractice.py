#Q1. What is the purpose of the return statement? 
#Answer:-Purpose of return statement is used to send a value back from a function.

#Q2. Write a program to return the sum of two numbers. 
#Answer:-
def add (x,y):
    return x +y 

result=add(10,20)
print(result)

#Q3. What is the difference between break and continue? 
#Answer:-Break-
# i)It used to end the loop immediately.
#ii)It jump outside the loop.
#iii)It skips the condition check.

#Continue-
#i)It is used to skip the  current itteration and move .
#ii)It jumps to the next step.
#iii)It runs  the conition check.

#Q4. Write a program to print numbers from 1 to 15 but skip 7 using continue. 
#Answer:-
for i in range(1,16):
    if i==7:
        continue
    print(i)

#Q5. Write a program to print numbers from 1 to 20 and stop at 12 using break. 
#Answer:-
for i in range(1,21):
    if i==12:
        break 
    print(i)

#Q6. What is the use of 'pass' in Python? 
#Answer:-ussualy 'pass' does nothing.It is used as a 'placeholder' when we write a code.

#Q7. Create an empty function named student() using pass. 
#Answer:-
def student():
    pass

#Q8. Write a program using break to stop a loop when the user enters 0. 
#Answer:
while True:

    num_user= int(input("Enter a number(Type 0 to quit'): "))

    if num_user==0:
      print("Loop stoped because you enterd 0.")
      break
    else:
        print(f"You entered:{num_user} ")

#Q9. Write a program using continue to print only odd numbers from 1 to 10. 
#Answer:-
i=0
while i<10:
    i+=1
    if i%2==0:
      continue
    print(i)

#Q10. Create a function that returns the area of a rectangle.
#Answer:-
def area (y,z):
    return y*z

result=area (20,30)
print(result)

#----x-----x----x----
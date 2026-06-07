#Student Result System
#Write a Python program that:

#1.Creates a function result(name, marks). 
#2. Uses if-elif-else to display: 
        #a. A Grade (90+) 
        #b. B Grade (75-89) 
        #c. C Grade (50-74) 
        #d. Fail (Below 50) 
#3. Returns the grade using return. 
#4. Prints today's date using the datetime module.

#Sample Output
#Student Name : Rahul
#Marks : 82
#Grade : B
#Date : 2026-06-06

while True:

  print("Student Name: Rahul")

  marks=int(input("Enter marks: "))
  print("Marks:", marks )

  if marks>=90:
     print("Grade :A")
     break
  elif marks>=75:
     print("Grade :B")
     break
   
  elif marks>=50:
     print("Grade :C")
     break

  elif marks <50:
     print("Fail")
     break
  
  else :
     print("Invalid Choice!Please try again.")
     continue
  
import datetime

today=datetime.datetime.today()
print("Date: ", today)
 



#Activity 1. Print today's date using the datetime module.
#Answer:-
import datetime

today=datetime.date.today()
print("Today's date is: ", today)

#Activity 2. Print current year, month, and day separately.
#Answer:-
today=datetime.date.today()
print("Year is: ",today.year)
print("Month is :", today.month)
print("Today's day is :", today.day)

#Activity 3. Create a date for your birthday and print it.
#Answer:-
d=datetime.date(2026,7,9)
print("My birthday's date is :", d)
      
#Activity 4. Display the calendar for the current month.
#Answer:-
import calendar

print(calendar.month(2025,6))

#Acitivity 5. Check whether 2028 is a leap year.
#Answer:-
print(calendar.isleap(2028))

#Activity 6. What is the purpose of the datetime module?
#Answer:-
#Datetime module is used in python to work with date and time.

#Activity 7. Write a program to display the current date and time.
#Answer:-
now=datetime.datetime.now()
print(now)

#Activity 8. Write a program to display only the current year.
#Answer:-
today=datetime.datetime.today()
print(today.year)

#Activity 9. Write a program to display the calendar of December 2025.
#Answer:-
print(calendar.month(2025,12))

#Activity 10. Write a program to check whether 2032 is a leap year.
#Answer:-
print(calendar.isleap(2032))
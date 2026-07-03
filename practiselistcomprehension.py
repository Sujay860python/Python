#Q1. Create a list of numbers from 1 to 5.
#Answer:-
numbers_print=[x for x in range(1,6)]
print(numbers_print)

#Q2. Create a list of squares from 1 to 5.
#Answer:-
numbers_square=[1,2,3,4,5]
square=[x**2 for x in numbers_square]
print(square)

#Q3. Create a list of even numbers from 1 to 10.
#Answer:-
numbers_even=[x for x in range (1,11) if x%2==0]
print(numbers_even)

#Q4. Create a list of odd numbers from 1 to 10.
#Answer:-
numbers_odd=[x for x in range (1,11) if x%2==1]
print(numbers_odd)

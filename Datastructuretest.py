#1.Create a list of 10 numbers and print only the even numbers.
#Answer:-
numbers_even=[12,14,14,56,64,88,97,86,78,32]
print(numbers_even)

#2.Create a tuple of 5 fruits and print the first and last fruit.
#Answer:-
fruits_print=("Grapes","Dragon Fruit","Banana","Mango")
print(fruits_print[3])

#3.Create a dictionary containing student name, age, and marks.
#Answer:-
student_id={
     "student name":"Sujay",
     "age":13,
    "marks":"99 marks"
}
print(student_id)

#4.Create a set of numbers and remove all duplicate values from a given list.
#Answer:-
numbers_dupicate={14,56,14,87,14}
print(numbers_dupicate)

#5.Find the largest number in a list.
#Answer:-
number_largest=[12,23,65]
large=[max(12,13,65)]
print(large)
#6.Count the number of times a value appears in a tuple.
#Answer:-

#7.Add a new key-value pair to a dictionary and display the updated dictionary.
#Answer:-
student_add={
    "student name":"Rohan Kumar",
    "class":8,
    "age":13
}
student_add["school name"]="O.p.Jindal School"
print(student_add)
#8.Find the union of two sets.
#Answer:-

#9.Create a list of squares from 1 to 20 using list comprehension.
#Answer:-
number_square=[1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
square=[x**2 for x in number_square]
print(square)

#10.Create a dictionary where keys are numbers from 1 to 10 and values are their cubes using dictionary comprehension.
#Answer:-
cube_dict={1,2,3,45,6,7,8,9,10}
cube=[x**3 for x in cube_dict ]
print(cube)
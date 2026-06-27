#Dictionary Questions
#Q1. Create a Dictionary

#Create a dictionary to store:

#Name: Rahul
#Age: 14
#Class: 8

#Print the dictionary.
#Answer:-
student_store={
    "Name":"Rahul",
    "Age":14,
    "Class":"8th"
}

print(student_store)

#Q2. Access a Value

#Create a dictionary:

#student = {
    #"name": "Aman",
    #"age": 15
#}

#Print only the student's name.
#Answer:-
student_values= {
     "name": "Aman",
     "age": 15
  }
print(student_values.pop("age"))
print(student_values.values())


#Q3. Add a New Item

#Create a dictionary:

#student = {
    #"name": "Riya",
    #"age": 13
#}

#Add a new key city with value Delhi and print the dictionary.
#Answer:-
student_city = {
    "name": "Riya",
    "age": 13
}
student_city["city"]="Delhi"
print(student_city)

#Q4. Update a Value

#Create a dictionary:

#student = {
    #"name": "Rohan",
   # "age": 14
#}

#Update age to 15 and print the dictionary.
#Answer:-
student_age = {
    "name": "Rohan",
   "age": 14
}
student_age["age"]=15
print(student_age)

#Q5. Print All Keys

#Create a dictionary:

#book = {
    #"title": "Python",
   # "author": "ABC",
   # "price": 250
#}

#Print all keys.
#Answer:-
book = {
    "title": "Python",
   "author": "ABC",
   "price": 250
}
print(book.keys())

#Q6. Print All Values

#Create a dictionary:

#car = {
    #"brand": "Toyota",
   # "model": "Innova",
   # "year": 2024
#}

#Print all values.
#Answer:-
car = {
    "brand": "Toyota",
   "model": "Innova",
   "year": 2024
}
print(car.values())
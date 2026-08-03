#Print numbers from 1 to 100.
#Answer:-
for i in range(1,101):
    print(i)

#Print all even numbers between 1 and 50.
#Answer:-
i=0
while i<=50:
    print(i)
    i+=2

#Find the sum of numbers from 1 to 100.
#Answer:-
total=0
for i in range(1,101):
    total+=1
    print(total)
    
#Print the multiplication table of a given number.
#Answer:-
total=1

while total <= 10:
    print("5*", total, "=", 5 * total)
    total += 1
 
#Count how many vowels are present in a word.
#Answer:-
word=("Apple")
count=0

for i in word.lower():
   if i in "aeiou":
    count+=1
print(count)


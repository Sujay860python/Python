print("🎮 Welcome to Calculator Game 🎮")

while True:

    print("\nChoose Operation")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "5":
        print("Game Ended!")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        result = num1 + num2
        print("Answer =", result)
    elif choice == "2":
        result = num1 - num2
        print("Answer =", result)

    elif choice == "3":
        result = num1 * num2
        print("Answer =", result)

    elif choice == "4":

        if num2 != 0:
            result = num1 / num2
            print("Answer =", result)

        else:
            print("Cannot divide by zero!")

    else:
        print("Invalid Choice")

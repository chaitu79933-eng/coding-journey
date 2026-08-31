while True:
    print("=== calculator ===")
    print("1. addition")
    print("2. subtraction")
    print("3. multiplication")
    print("4. division")

    choice = int(input("choose an operation (1-4): "))
    num1 = float(input("enter the first number: "))
    num2 = float(input("enter the second number: "))

    if choice == 1:
        print("result:", num1 + num2)

    elif choice == 2:
        print("result:", num1 - num2)

    elif choice == 3:
        print("result:", num1 * num2)

    elif choice == 4:
        print("result:", num1 / num2)

    else:
        print("invalid choice!")

    again = input("calculate again? (y/n): ")

    if again.lower () != "y":
        break 

print("thanks for using the calculator!")

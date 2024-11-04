

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "division by zero"
    else: 
        return x / y

while True:
    print("Select an operation:")
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")
    print("5. Exit")

    try:
        choice = int(input("Make a choice (1/2/3/4/5): "))
    except ValueError:
        print("Invalid choice, please enter a number between 1 and 5.")
        continue

    if choice in (1, 2, 3, 4):
        try:   
            num1 = float(input("Enter a number: "))
            num2 = float(input("Enter a second number: "))
        except ValueError:
            print("Invalid input, please enter a valid number.")
            continue

        if choice == 1:
            print("Result:", add(num1, num2))
        elif choice == 2:
            print("Result:", subtract(num1, num2))
        elif choice == 3:
            print("Result:", multiply(num1, num2))
        elif choice == 4:
            print("Result:", divide(num1, num2))

    elif choice == 5:
        print("Exiting the calculator. Goodbye!")
        break
    else:
        print("Invalid choice, please select a valid option.")




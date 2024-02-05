# calculator.py

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def compare(x, y):
    if x > y:
        return "First number is greater"
    elif x < y:
        return "Second number is greater"
    else:
        return "Both numbers are equal"

def logical_or(x, y):
    return x or y

def logical_and(x, y):
    return x and y

def logical_xor(x, y):
    return x != y

def modulus(x, y):
    if y != 0:
        return x % y
    else:
        return "Error: Modulus by zero"

def factorial(x):
    if x < 0:
        return "Error: Factorial not defined for negative numbers"
    elif x == 0 or x == 1:
        return 1
    else:
        result = 1
        for i in range(2, x + 1):
            result *= i
        return result

def main():
    while True:
        print("Welcome to the Calculator Application!")

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        while True:
            print("Select operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Comparison")
            print("6. Logical OR")
            print("7. Logical AND")
            print("8. Logical XOR")
            print("9. Modulus")
            print("10. Factorial of the first number")

            choice = input("Enter choice (1-10): ")

            if choice in {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10'}:
                choice = int(choice)
                if choice == 1:
                    print("Result: ", add(num1, num2))
                elif choice == 2:
                    print("Result: ", subtract(num1, num2))
                elif choice == 3:
                    print("Result: ", multiply(num1, num2))
                elif choice == 4:
                    print("Result: ", divide(num1, num2))
                elif choice == 5:
                    print("Result: ", compare(num1, num2))
                elif choice == 6:
                    print("Result: ", logical_or(num1, num2))
                elif choice == 7:
                    print("Result: ", logical_and(num1, num2))
                elif choice == 8:
                    print("Result: ", logical_xor(num1, num2))
                elif choice == 9:
                    print("Result: ", modulus(num1, num2))
                elif choice == 10:
                    print("Result: ", factorial(int(num1)))
            else:
                print("Invalid input. Please enter a number between 1 and 10.")

            continue_calculation = input("Do you want to continue with these numbers? (yes/no): ").lower()

            if continue_calculation != 'yes':
                break

if __name__ == "__main__":
    main()

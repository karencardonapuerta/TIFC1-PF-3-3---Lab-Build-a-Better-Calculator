
# Function to add multiple numbers
def addmultiplenumbers(numbers):
    return sum(numbers)


# Function to multiply multiple numbers
def multiplymultiplenumbers(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result


# Function to check if a number is even
def isiteven(num):
    return isitaninteger(num) and num % 2 == 0


# Function to check if a number is an integer
def isitaninteger(num):
    return isinstance(num, (int, float)) and num % 1 == 0


# Main calculator
def main():
    print("Welcome to my calculator!")

    while True:
        print("\nChoose an operation:")
        print("1. Add numbers")
        print("2. Multiply numbers")
        print("3. Check if a number is even")
        print("4. Check if a number is an integer")
        print("5. Exit")

        option = input("Choose an option: ")

        if option == "1":
            amount = int(input("How many numbers do you want to add? "))
            numbers = []

            for i in range(amount):
                num = float(input(f"Enter number {i + 1}: "))
                numbers.append(num)

            print("Result:", addmultiplenumbers(numbers))

        elif option == "2":
            amount = int(input("How many numbers do you want to multiply? "))
            numbers = []

            for i in range(amount):
                num = float(input(f"Enter number {i + 1}: "))
                numbers.append(num)

            print("Result:", multiplymultiplenumbers(numbers))

        elif option == "3":
            num = float(input("Enter a number: "))
            print("Result:", isiteven(num))

        elif option == "4":
            num = float(input("Enter a number: "))
            print("Result:", isitaninteger(num))

        elif option == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()


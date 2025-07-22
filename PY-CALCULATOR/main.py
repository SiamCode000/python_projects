print("Calculator...")

History_file = "History.txt"

def show_history():
    with open(History_file, "r") as file:
        lines = file.readlines()
    if len(lines) == 0:
        print("No History Found!")
    else:
        for line in reversed(lines):
            print(line.strip())

def clear_history():
    open(History_file, "w").close()
    print("History Cleared")

def save_history(equation, result):
    with open(History_file, "a") as file:
        file.write(equation + " = " + str(result) + "\n")

def calculate(user):
    try:
        parts = user.split()
        num1 = float(parts[0])
        operation = parts[1]
        num2 = float(parts[2])

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                print("Cannot divide by zero")
                return
            result = num1 / num2
        else:
            print("Invalid operation.")
            return

        print(f"Result is {result}")
        save_history(user, result)

    except (IndexError, ValueError):
        print("Invalid input format. Use format like: 5 + 3")

def main():
    print("__SIMPLE CALCULATOR___")
    while True:
        user = input("Choose operation (history, clear, exit) or enter calculation (+, -, *, /): ").lower()
        if user == "history":
            show_history()
        elif user == "clear":
            clear_history()
        elif user == "exit":
            print("Thank you for using our calculator app.")
            break
        else:
            calculate(user)

main()

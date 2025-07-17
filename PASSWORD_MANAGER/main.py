
def view():
    with open("password.txt", "r") as f:
        for line in f:
            if '|' in line:
                user, pwd = line.strip().split("|")
                print("User:", user, "| Password:", pwd)
            else:
                print(line.strip())


def add():
    acc = input("Enter account name: ")
    passw = input("Enter the password: ")
    with open("password.txt","a") as f:
        f.write(f"Account name: {acc}, Password name: {passw} \n")

while True:
    user = input("Do you Want to view or add? ").lower()
    if user == "view":
        view()
    elif user == "add":
        add()
    else:
        print("invalid mode")
        quit()
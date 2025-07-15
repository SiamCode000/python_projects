print("Calculator...")

def sum():
    try:
        option = input("Enter the operation(+,-,*,/): ")
        num1 = int(input("Enter number 1: "))
        num2 = int(input("Enter number 2: "))
    except Exception as e:
        print("Something went wrong!")
    
    if(option == "+"):
        print(num1+num2)
    elif(option== "-"):
        print(num1-num2)
    elif(option== "*"):
        print(num1*num2)
    elif(option== "/"):
        print(num1/num2)
sum()
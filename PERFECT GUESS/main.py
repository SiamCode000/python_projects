import random
n = random.randint(1,100)
guesses = 0
user = 0
while (user!=n):
    user = int(input("Guess the Number: "))
    if (user>n):
        print("\tLower Number please")
    elif(user<n):
        print("\tHigher Number please")
    guesses+= 1
print(f"You have perfectly guess the number {n} in {guesses} attempt")
'''
"rock" = 0
"paper" = 1
"scissor" = 2
'''

import random

youinput = input("Enter your choice:").lower()
youDict = {
    "r":0,
    "p":1,
    "s":2
}
you = youDict[youinput]

computer = random.choice([0, 1, 2])
reverseDict = {
    0: "rock",
    1: "paper",
    2: "scissor"
}
comp = reverseDict[computer]

print(f"You choose {reverseDict[you]} and computer choose {comp}")
# Logic =>

if(you == computer):
    print('Its a Draw')
else:
    if(you == 0 and computer == 1):
        print("You lose")
    elif(you == 1 and computer == 0):
        print("You win")
    elif(you == 2 and computer == 0):
        print("You lose")
    elif(you == 0 and computer == 2):
        print("You win")
    elif(you == 0 and computer == 1):
        print("You lose")
    elif(you == 1 and computer == 0):
        print("You win")
    elif(you == 1 and computer == 2):
        print("You lose")
    elif(you == 2 and computer == 1):
        print("You win")
    else:
        print("Something went wrong !")
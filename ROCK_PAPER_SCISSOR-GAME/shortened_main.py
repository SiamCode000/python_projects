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

# logic =>
if(you == computer):
    print("its a Draw")
else:
    '''
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

    ## The below logic2 is written on the basis of the value of computer - you
    '''
# logic 2 =>
    if((computer - you) == 1 or  (computer - you) == 0 ):
        print("You lose!")
    else:
        print("You win!") 
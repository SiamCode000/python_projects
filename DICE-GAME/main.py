import random
print("Welcome to the DICE game")

start = input("Do you want to play the game,(yes or no): ")

if start.lower() == "yes":
    print("Lets start")
elif start.lower() == "no":
    print("Thanks for visiting :)")
    quit()
else:
    print("Invalid Option")
    quit()

def roll():
    roll = random.randint(1,6)
    return roll

while True:
    players = input("Choose players between 2-4: ")
    if players.isdigit():
        players = int(players)
        if players >= 2 or players <= 4:
            break
        else:
            print("Must be in 2-4")
    else:
        print("Invalid , Try again")
        raise ValueError
    
max_Score = 50
player_Score = [0 for _ in range(players)]
# print(player_Score)


while max(player_Score) < max_Score:
    for player_idx in range(players):
        print("\nPlayer number", player_idx + 1, "turn has just started!")
        print("Your total score is:", player_Score[player_idx], "\n")
        current_score = 0
        while True:
            should_roll = input("would you like to roll (y) ? ")
            if should_roll.lower() == "y":
                value = roll()
            else:
                break
            if value == 1:
                print("You rolled a 1 Turned Down!")
                current_score = 0
                break
            else:
                current_score += value
                print(f"You rolled a {value}")
            print(f"Your current score is {current_score}")


player_Score[player_idx] += current_score
print("Your total score is:", player_Score[player_idx])

max_Score = max(player_Score)
winning_idx = player_Score.index(max_Score)
print("Player number", winning_idx + 1,"is the winner with a score of:", max_Score)



            

import random
import statistics

for i in range(100):
    possible_actions = ["rock", "paper", "scissors"]
    user_action = random.choice(possible_actions)
    computer_action = random.choice(possible_actions)
    print(f"\nUser chose {user_action}, computer chose {computer_action}.\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
        file = open("rps.csv","a")
        file.write("Draw,")
        file.close()
        
    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
            file = open("rps.csv","a")
            file.write("Rock,")
            file.write("\nPlayerWins,")
            file.close()
        else:
            print("Paper covers rock! You lose.")
            
    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
            file = open("rps.csv","a")
            file.write("Paper,")
            file.close()
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
            file = open("rps.csv","a")
            file.write("Scissors,")
            file.close()
        else:
            print("Rock smashes scissors! You lose.")
    

file = open("rps.csv","r")
dataIn = file.read()
rpsList = dataIn.split(",")
rockCount = 0
paperCount = 0
scissorCount = 0
drawCount = 0
for i in rpsList:
    if i == "Rock":
        rockCount+=1
    elif i == "Paper":
        paperCount+=1
    elif i == "Scissors":
        scissorCount+=1
    else:
        drawCount +=1
print("Rock = ", rockCount)
print("Paper = ", paperCount)
print("Scissors = ", scissorCount)
print("Draw = ", drawCount)
print("Total plays: ",rockCount+paperCount+scissorCount+drawCount)


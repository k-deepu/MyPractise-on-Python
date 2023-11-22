import sys
import random

print("Choose the Number")
playerchoice = input("Enter....\n 1.Rock \n 2.Scissor \n 3.Stone \n\n\n" )

player = int(playerchoice)

if(player <1 or player>3):
    sys.exit("you must enter 1, 2 or 3 ")
    
    
computer = random.randint(1,3)
choice = {1:'Rock', 2:'Scissor', 3:'Stone'}

print('you choose ' + choice[player] )
print('Computer choose ' + choice[computer] )

if(player == 1 and computer == 3):
    print("🎉🥳you won")
elif(player == 2 and computer == 1):
    print("🎉🥳you won")
elif(player == 3 and computer == 2):
    print("🎉🥳you won")
elif(player == computer):
    print("😒Tie")
else:
    print("😒computer Won")
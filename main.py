
import sys
import random
choices = ["Snake", "Water", "Gun"] #choices
print("Snake, Water, Gun") #print
youstr = str(input("Enter your choice --> ")).capitalize() #input
you_dict = {"Snake":1, "Water":-1, "Gun":0} #dictionary
if not youstr in you_dict: #error handling
        print("Invalid Option! Try again")
        sys.exit()
reverse_dict={1:"Snake", -1:"Water", 0:"Gun"} #reverse dict
computer_choice = random.choice(choices) #computer choice
computer = you_dict[computer_choice] #computer choice conversion
you=you_dict[youstr] #user choice conversion

print(f"Computer choose {reverse_dict[computer]}")
#1
if computer == -1 and you ==1:
    print("You win!")

elif computer == -1 and you == 0:
    print("You Loose!")

elif computer == -1 and you == -1:
    print("Tie! choose again")
#2
elif computer == 1 and you == 0:
    print("You win!")

elif computer == 1 and you == -1:
    print("You Loose!")

elif computer == 1 and you == 1:
    print("Tie! choose again")

#3
elif computer == 0 and you == 1:
    print("You Loose!")

elif computer == 0 and you == -1:
    print("You win!")

elif computer == 0 and you == 0:
    print("Tie! choose again")





from random import choice

#
# USER SELECTION
#

#removing duplication?
#goal is so that in the future we only need to update some concept in one place
#so we aren't able to forget to update all the places 


u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
print("USER CHOICE:", u)
if u not in valid_choices:
    print("OOPS, TRY AGAIN")
    exit()

#
# COMPUTER SELECTION
#
valid_choices = ["rock", "paper", "scissors"]
c = choice(valid_choices)
print("COMPUTER CHOICE:", c)

#
# DETERMINATION OF WINNER
#

if u == "rock" and c == "rock":
    print("It's a tie!")
elif u == "rock" and c == "paper":
    print("The computer wins")
elif u == "rock" and c == "scissors":
    print("The user wins")

elif u == "paper" and c == "rock":
    print("The computer wins")
elif u == "paper" and c == "paper":
    print("It's a tie!")
elif u == "paper" and c == "scissors":
    print("The user wins")

elif u == "scissors" and c == "rock":
    print("The computer wins")
elif u == "scissors" and c == "paper":
    print("The user wins")
elif u == "scissors" and c == "scissors":
    print("It's a tie!")





from random import choice

#
# USER SELECTION
#

#removing duplication?
#goal is so that in the future we only need to update some concept in one place
#so we aren't able to forget to update all the places 
valid_choices = ["rock", "paper", "scissors"]

def winner(user_choice, computer_choice):
    return "OOPS - TODO"

#ONLY RUN THE FOLLOWING CODE IF WE RUN THE SCRIPT FROM THE COMMAND LIN
#BUT NOT IF WE ARE IMPORTING SOME CODE FROM THIS FILE TO ANOTHER FILE
#PREVENTS EXECUTION OF THE CODE BELOW WHEN ALL WE WANT TO DO IS TEST ONE ISOLATED PART
if __name__ == "__main__":

    u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
    print("USER CHOICE:", u)
    if u not in valid_choices:
       return "OOPS, TRY AGAIN"
        exit()

    #
    # COMPUTER SELECTION
    #

    c = choice(valid_choices)
    return "COMPUTER CHOICE:"

    #
    # DETERMINATION OF WINNER
    #

    if user_choice == "rock" and computer_choice == "rock":
        return "It's a tie!"
    elif user_choice == "rock" and computer_choice == "paper":
        return "The computer wins"
    elif user_choice == "rock" and computer_choice == "scissors":
        return "The user wins"

    elif user_choice == "paper" and computer_choice == "rock":
        return "The computer wins"
    elif user_choice == "paper" and computer_choice == "paper":
        return "It's a tie!"
    elif user_choice == "paper" and computer_choice == "scissors":
        #return "The user wins" bug 
         return "The computer wins"

    elif user_choice == "scissors" and computer_choice == "rock":
        return "The computer wins"
    elif user_choice == "scissors" and computer_choice == "paper":
        return "The user wins"
    elif user_choice == "scissors" and computer_choice == "scissors":
        return "It's a tie!"

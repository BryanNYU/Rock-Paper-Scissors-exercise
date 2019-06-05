# game.py

print("Rock, Paper, Scissors, Shoot!") # this is also a comment

# CAPTURE INPUT
user_choice = input("Please choice one of the following options: 'rock', 'paper', or 'scissors' (without the quotes):")
print("------------------------")
print("YOU CHOSE", user_choice)

# VALIDATE INPUTS

if user_choice not in ["rock", "paper", "scissors"]: # Make a list
    print("INVALID SELECTION, PLEASE TRY AGAIN...")
    exit()


# GENERATE COMPUTER SELECTION

print("GENERATING...")


# DETERMINE THE WINNER

# DISPLAY FINAL OUTPUTS / OUTCOMES
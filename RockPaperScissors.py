import random
import tkinter

# Initialize a list to keep track of game results
stats = []

def get_winner(call):
    # Simplify the computer's choice selection using random.choice()
    throw = random.choice(["rock", "scissors", "paper"])
    
    # Determine the winner based on the rules of Rock, Paper, Scissors
    if (throw == "rock" and call == "paper") or \
       (throw == "paper" and call == "scissors") or \
       (throw == "scissors" and call == "rock"):
        stats.append('W')
        result = "You won"
    elif throw == call:
        stats.append('D')
        result = "It's a draw"
    else:
        stats.append('L')
        result = "You lost"
    
    # Update the output label with the result of the game
    global output
    output.config(text="Computer did: " + throw + "\n" + result)

# Define functions for each player choice
def pass_s():
    get_winner("scissors")

def pass_r():
    get_winner("rock")

def pass_p():
    get_winner("paper")

# Set up the main window using tkinter
window = tkinter.Tk()

# Create buttons for each choice
scissors = tkinter.Button(window, text="Scissors", bg="#ff9999", padx=50, pady=100, command=pass_s, width=20)
rock = tkinter.Button(window, text="Rock", bg="#80ff80", padx=50, pady=100, command=pass_r, width=20)
paper = tkinter.Button(window, text="Paper", bg="#3399ff", padx=50, pady=100, command=pass_p, width=20)

# Create an output label to display the result
output = tkinter.Label(window, width=20, fg="red", text="What's your call?")

# Arrange the buttons and label on the window
scissors.pack(side="left")
rock.pack(side="left")
paper.pack(side="left")
output.pack(side="right")

# Start the tkinter event loop
window.mainloop()

# After the window is closed, print the game results
for i in stats: print(i, end=" ")
if stats.count('L') > stats.count('W'):
    result = "\nYou lost the series."
elif stats.count('L') == stats.count('W'):
    result = "\nSeries ended in a draw."
else:
    result = "\nYou won the series."
print(result)

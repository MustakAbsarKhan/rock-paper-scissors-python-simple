import random

def get_choices():
  
  player_choice = input("Enter a Choice (rock, paper, scissors) : ")
  
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)

  choices = {"player": player_choice, "computer": computer_choice}
  return choices
  
# Evaluating the results
def check_win(player, computer):
  # f string will concatinate while putting variable in the string
  print(f"You Chose {player}, Computer Chose {computer}")
    
  if player == computer:
    return "It is a tie!"
  elif player == "rock":
    return "Rock smashes scissors! You Win!" if computer == "scissors" else "Paper covers Rock! You Lose." #using ternary operator in Python
  elif player == "paper":
    return "Scissors cut Paper! You Lose." if computer == "scissors" else "Paper covers Rock! You Win!"
  elif player == "scissors":
    return "Rock smashes scissors! You Lose." if computer == "rock" else "Scissors cut Paper! You Win!"

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
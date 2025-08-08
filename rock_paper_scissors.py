import random

# Options the player and computer can choose from
options = ['rock', 'paper', 'scissors']

print("Welcome to Rock, paper, Scissors!")
while True:
  # Get player's choice
  player_choice = input("Enter your choice (rock, paper, scissors): ").lower().strip()

  # Get computer's choice
  computer_choice = random.choice(options)

  print(f"You chose: {player_choice}")
  print(f"Computer chose: {computer_choice}")

  #Decide who wins
  if player_choice == computer_choice:
    print("It's a tie!")

  elif (player_choice == 'rock' and computer_choice == 'scissors') or (player_choice == 'paper' and computer_choice == 'rock') or (player_choice == 'scissors' and computer_choice == 'paper'):
    print("You win!")

  elif player_choice in options:
    print("You Lose!")

  else:
    print("Invalid choice! Please choose rock, paper, or scissors.")

  play_again = input("Would you like to play again? (yes/no): ").lower().strip()
  if play_again not in ['yes', 'y']:
    print("Tanks for playing!")
    break
    
 
    


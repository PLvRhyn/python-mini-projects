import random

while True:
   
    print("Welcome to the number guessing game!!")
    print("Im thinking of a number between 1 and 100!\n")

    SecretNr = random.randint(1,100)
   
    tries = 0

    while True:

      try:
          NrGuess = int(input("Guess the Number between 1 and 100: "))
      except ValueError:
       print(f"Enter a valid number!")
       continue

      tries += 1

      if NrGuess < SecretNr:
        if SecretNr - NrGuess >= 20:
            print("Too low, you're way off!\n")
        if SecretNr - NrGuess <= 10:
            print("Too low, but you're getting closer!\n")
      elif NrGuess > SecretNr:
        if NrGuess - SecretNr >= 20:
            print("Too high, you're way off!\n")
        if NrGuess - SecretNr <= 10:
            print("Too high, but you're getting closer!\n")
        
      else:
        print(f"Congratulations! You guessed the number {SecretNr} in {tries} tries!\n")
        break
  
    play_again = input("Would you like to play again? (Yes/No): ").strip().lower()
    print("\n")
    if play_again not in ['yes', 'y']:
       print("Thanks for playing!!")
       break






   


        



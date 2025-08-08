import random

def roll_dice():
    dice = random.randint(1,6)
    print(f"You rolled a {dice}")

while True:
    user_input = input("Press enter to roll the dice (or type 'q and press enter to quit): ")

    if user_input.strip().lower() == 'q':
        print("Thanks for playing!")
        break
    else:
        roll_dice()
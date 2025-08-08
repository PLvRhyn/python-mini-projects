name = input("Please enetr your name: ")
FavWord = input("Please enter your favorite word: ")
import random
number = random.randint(10,99)
print(f"Your generated password is: {name[:2]}{FavWord[-2:]}{number}")
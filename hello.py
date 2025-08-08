print("Hello, Python!")
name = input("Please enter your name: ")
print("Hello, " + name)
age = input("Enter your age: ")
#print("You are " + age + " years old")
print(f"You are {age} years old")
CurrYear = 2025
#print("Hey " + name + " you will turn a 100 years old in the year, " + str(CurrYear + (100 - int(age))))
print(f"Hey {name} will turn 100 in the year {CurrYear + (100 - int(age))}")

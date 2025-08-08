
bill = float(input("Enter the total bill amount: "))
tip_percentage = int(input("Enter the tip percentage (e.g., 15 for 15%): "))
NrPeople = int(input("The number of people to split the bill: "))
tip = (bill * tip_percentage)/100
total = bill + tip
each_person = total / NrPeople
print("\n----- Tip Calculator Result -----")
print (f"Each person should pay: R{each_person:.2f}")
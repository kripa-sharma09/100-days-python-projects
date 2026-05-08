print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill? "))
tip_percent = int(input("What percentage tip would you like to give? 10 12 15 "))
tip = (bill*(tip_percent/100))
total_bill = round((bill + tip),2)
print(f"Each person should pay: {total_bill}")




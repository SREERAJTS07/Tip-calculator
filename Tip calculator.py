print("Welcome to the tip calculator")
bill = float(input('What was the total bill?\n'))
tip = int(input('What percentage tip would you like to give? 10, 12, or 15\n'))
number_of_people = int(input('How many people to split the bill?\n'))

amount_to_be_paid = round(((bill*(tip/100)) + bill )/number_of_people,2)
print(f"Each person should pay: {amount_to_be_paid}")
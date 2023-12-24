print("Welcome to the tip calculator")

# Taking user inputs
bill = float(input('What was the total bill? $'))
tip = int(input('What percentage tip would you like to give? 10, 12, or 15? '))
number_of_people = int(input('How many people to split the bill? '))

# Calculating the amount to be paid per person
total_bill_with_tip = bill * (1 + tip / 100)
amount_per_person = total_bill_with_tip / number_of_people
amount_per_person_rounded = round(amount_per_person, 2)

# Displaying the result
print(f"Each person should pay: ${amount_per_person_rounded}")

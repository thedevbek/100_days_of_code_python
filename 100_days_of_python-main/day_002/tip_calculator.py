#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator.")
bill = int(input("What was the total bill? "))
tip = int(input("What percentage tip would you like to give? 12, 15, or 20? "))
people = int(input("How many people are splitting the bill? "))

tip_percentage = tip / 100
total_tip = bill * tip_percentage
total_bill = bill + total_tip
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)

print("Each person should pay ${:.2f}".format(final_amount))
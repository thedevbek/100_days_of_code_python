import math
#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
print('Welcome to the tip calculator!')
bill = float(input('How much was the total bill? $'))
tip = int(float(input('How much of a tip would you like to give? 10, 12, or 15\n'))) 
people = int(input('How many people is the bill split between? '))
percentage = tip / 100 
total = (bill * percentage) + bill
total_per_person = total /people
pay = round(total_per_person, 2)
pay = "{:.2f}".format(pay)
print(f'Each person should pay ${pay}. ')



age = int(input("What is your current age?"))

years_remaining = 90 - age

days = years_remaining * 365
months = years_remaining * 12
weeks = years_remaining * 52

print(f'You have {days} days, {weeks} weeks, and {months} months left.')
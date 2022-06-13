# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

# It will take your current age as the input and output a message with our time left in this format:
#     You have x days, y weeks, and z months left.
# Where x, y and z are replaced with the actual calculated numbers.

age = input("What is your current age?")

years_remaining = 90 - int(age)
months = years_remaining / 12
weeks = years_remaining / 52
days = years_remaining / 356.25

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
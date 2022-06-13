# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.
# Based on a user's order, work out their final bill.

# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

# Example input:
# size = "L"
# add_pepperoni = "Y"
# extra_cheese = "N"

# Example output:
# "Your final bill is: $28."

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0

if size == "S":
    bill += 15
    if add_pepperoni == "Y":
        bill += 2
elif size == "M" or size == "L":
    bill += 20
    if size == "L":
        bill += 5
    if add_pepperoni == "Y":
        bill += 3

if extra_cheese == "Y":
	bill += 1

print(f"Your final bill is: ${bill}.")
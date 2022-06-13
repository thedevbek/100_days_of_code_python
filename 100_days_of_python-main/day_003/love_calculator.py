# # You are going to write a program that tests the compatibility between two people.
# # To work out the love score between two people:
# # Take both people's names and check for the number of times the letters in the word TRUE occurs.
# # Then check for the number of times the letters in the word LOVE occurs.
# # Then combine these numbers to make a 2 digit number.

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name_one_lower = name1.lower()
name_two_lower = name2.lower()

true_count = 0
love_count = 0

true_count += name_one_lower.count("t") + name_two_lower.count("t")
true_count += name_one_lower.count("r") + name_two_lower.count("r")
true_count += name_one_lower.count("u") + name_two_lower.count("u")
true_count += name_one_lower.count("e") + name_two_lower.count("e")

love_count += name_one_lower.count("l") + name_two_lower.count("l")
love_count += name_one_lower.count("o") + name_two_lower.count("o")
love_count += name_one_lower.count("v") + name_two_lower.count("v")
love_count += name_one_lower.count("e") + name_two_lower.count("e")

print(str(true_count) + str(love_count))
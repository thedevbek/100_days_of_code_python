# You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
# There are many ways of doing this. But to practice what we learnt in the last lesson,
# you should generate a random number, either 0 or 1. Then use that number to print out Heads or Tails.

#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
 # 🚨 Don't change the code above 👆 It's only for testing your code.

#Write the rest of your code below this line 👇

if random.randint(0, 1):
    print("Heads")
else:
    print("Tails")
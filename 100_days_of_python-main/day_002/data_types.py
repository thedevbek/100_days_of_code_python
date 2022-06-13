# Write a program that adds the digits in a 2 digit number.
# e.g. if the input was 35, then the output should be 3 + 5 = 8
two_digit_number = input("Type a two digit number: ")

digit_one = two_digit_number[0]
digit_two = two_digit_number[1]

print(int(digit_one) + int(digit_two))
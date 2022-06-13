def prime_checker(number):
    for i in range(2, number):
        if number % i == 0:
            print("It's not a prime number.")
            return False

    print("It's a prime number.")
    return True

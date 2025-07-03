import math


# Recursive Prime Checker
def is_prime(n, divisor=None):
    if n < 2:
        return False
    if divisor is None:
        divisor = 2

    if divisor > int(n**0.5):
        return True

    if n % divisor == 0:
        return False

    return is_prime(n, divisor + 1)

#Test
for num in range(1000):
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

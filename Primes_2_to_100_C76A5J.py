import math

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

def print_primes(start, end):
    if start > end:
        return

    if is_prime(start):
        print(f"{start} is a prime number.")

    print_primes(start + 1, end)

start = 2
end = 100

print_primes(start, end)

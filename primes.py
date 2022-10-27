"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <= 0:
        raise ValueError(f"{number_of_primes} should have been a positive number greater than 0")
    list = []
    with open('primes.txt', 'r') as p:
        for i in range(number_of_primes):
            prime = int(p.readline())
            list.append(prime)

    return list
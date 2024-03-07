# The prime number generator
def prime_generator(num):
    primes = []
    while num > 1:
        for i in range(num):
            if
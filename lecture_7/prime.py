import math

def is_prime(n):

    if n < 2: # We know numbers less than 2 are not prime
        return False

    for i in range(2, int(math.sqrt(n))): # Checking factors up to sqrt(n)

        if n % i == 0: # If i is a factor, return false
            return False

    return True # If no factors were found, return true
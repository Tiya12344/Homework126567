print("These are the prime numbers from 1-100:")
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

number = 2
while number <= 100:
    if is_prime(number):
        print(number, end=', ')
    number += 1
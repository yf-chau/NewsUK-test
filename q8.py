def max_prime_factor (num):

    max_prime_factor = 1

    for i in range (2, int(num/2)):
        while num % i == 0:
            num /= i
            max_prime_factor = i

    return max_prime_factor


print(max_prime_factor(9))          # Max prime factor is 3
print(max_prime_factor(15))         # Max prime factor is 5
print(max_prime_factor(121))        # Max prime factor is 11
print(max_prime_factor(1))          # Max prime factor is 1
print(max_prime_factor(754))        # Max prime factor is 29
print(max_prime_factor(35123))      # Max prime factor is 103
print(max_prime_factor(347235))     # Max prime factor is 3307



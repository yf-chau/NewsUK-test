def max_prime_factor (num):

    # Divide the input by numbers starting from 2
    # After it is not divisiable by 2, move up to the next number which is 3, and update the max prime number if it is divisiable
    # End the loop when num = 1, which means the last divisiable i is the max prime factor
    # End the loop when i > half of num, which means num is also a prime number and so the function will return num

    max_prime_factor = 1

    for i in range (2, num//2 + 1):
        while num % i == 0:
            num //= i
            max_prime_factor = i
        if num == 1:
            break

    return num if max_prime_factor == 1 else max_prime_factor


print(max_prime_factor(9))          # Max prime factor is 3
print(max_prime_factor(15))         # Max prime factor is 5
print(max_prime_factor(121))        # Max prime factor is 11
print(max_prime_factor(1))          # Max prime factor is 1
print(max_prime_factor(754))        # Max prime factor is 29
print(max_prime_factor(35123))      # Max prime factor is 103
print(max_prime_factor(347235))     # Max prime factor is 3307
print(max_prime_factor(1000003))    # Max prime factor is 1000003




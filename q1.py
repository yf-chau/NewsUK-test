def print_numbers (max = 100):
    #Use map function to create a list of numbers from 1 up to max, then join them together with ', '
    output_str = ', '.join(map(str, range(1, max + 1)))
    print(output_str)

print_numbers()

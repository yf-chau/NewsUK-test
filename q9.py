def pandigital (input_number):
    # Stringify the input number and change it to a set, which remove duplicate digits
    # Create a set which contain all digits from 1 to n, where n is the length of the input number
    # Compare the two sets to see if it is pandigital
    
    input_str = str(input_number)
    digits = set(input_str)
    req_digits = set(str(i) for i in range (1, len(input_str)+1))
    return 'Pandigital' if digits == req_digits else 'Not pandigital'

print(pandigital(15234))     # Pandigital
print(pandigital(463215))    # Pandigital
print(pandigital(123442))    # Not pandigital
print(pandigital(123794))    # Not pandigital
print(pandigital(921456783))    # Pandigital
print(pandigital(921427873))    # Not pandigital
print(pandigital(821458273))    # Not pandigital

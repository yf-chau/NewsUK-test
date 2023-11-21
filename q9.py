def pandigital (input_number):
    input_str = str(input_number)
    digits = set(input_str)
    req_digits = set(str(i) for i in range (1, len(input_str)+1))
    return digits == req_digits

print(pandigital(15234))     # True
print(pandigital(463215))    # True
print(pandigital(123442))    # False
print(pandigital(921456783))    # True
print(pandigital(921427873))    # False
print(pandigital(821458273))    # False

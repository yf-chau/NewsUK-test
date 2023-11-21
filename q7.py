def anagram (str1, str2):
    return sorted(str1) == sorted(str2)

print(anagram('listen', 'silent'))          # True
print(anagram('hello', 'world'))            # False
print(anagram('Triangle', 'Integral'))      # False
print(anagram('dormitory', 'dirtyroom'))    # True
print(anagram('debit card', 'bad credit'))  # True


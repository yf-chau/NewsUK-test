def palindrome (input):
    if input == '':
        print('Empty string')
        return;
    else:
        for i in range(0, int(len(input)//2)):
            if input[i] != input[-i-1]:
                print('Not palindrome')
                return;
    print('Palindrome')


palindrome('')          # Empty String
palindrome('racecar')   # Palindrome
palindrome('madam')     # Palindrome
palindrome('hello')     # Not palindrome
palindrome('a')         # Palindrome
palindrome('1234321')   # Palindrome
palindrome('abcddcba')  # Palindrome

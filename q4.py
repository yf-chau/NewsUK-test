def palindrome (input):
    # check if input string is empty
    if input == '':
        print('Empty string')
        return;
    # if not, compare the first char with the last char, the second char with the second last char etc...
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

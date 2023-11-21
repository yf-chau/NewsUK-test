def search_char(string, target_char):
    # Loop through the input string and compare each char with the target. Return index when the target char is found, else return -1.
    for index, char in enumerate(string):
        if target_char == char:
            return index
    return -1
    
test_string = 'You should also write some test code to show that your function works as expected.'

# Should output 19 as the first 't' is in 'test'
print(search_char(test_string, 't'))
# Validation
print(test_string.find('t'))

# Should output -1 as there is no 'z' in the string
print(search_char(test_string, 'z'))
# Validation
print(test_string.find('z'))

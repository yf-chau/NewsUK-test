def duplicates (input_list):
    # Use set to remove all duplicates
    # If the len of the set is not the same as the input, there must be duplicates
    if len(input_list) != len(set(input_list)):
        print('Contains duplicates.')
    else:
        print('Does not contains duplicates.')

duplicates([1, 2, 3, 4, 5])              # No duplicates
duplicates([1, 2, 2, 3, 4])              # Contains duplicates
duplicates([])                           # Empty list, no duplicates
duplicates(['a', 'b', 'c', 'a'])         # Contains duplicates
duplicates([True, False, True])          # Contains duplicates

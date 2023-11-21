def duplicates (input_list):
    if len(input_list) != len(set(input_list)):
        print('Contains duplicates.')
    else:
        print('Does not contains duplicates.')

duplicates([1, 2, 3, 4, 5])              # No duplicates
duplicates([1, 2, 2, 3, 4])              # Contains duplicates
duplicates([])                           # Empty list, no duplicates
duplicates(['a', 'b', 'c', 'a'])         # Contains duplicates
duplicates([True, False, True])          # Contains duplicates

def deduplicates (input_list):
    return list(set(input_list))

# Set will only holds a single copy of each value (and not retaining the order), hence removing duplicates

print(deduplicates([1, 2, 2, 3, 4, 4, 5]))
print(deduplicates(['apple', 'banana', 'apple', 'cherry']))
print(deduplicates([]))
print(deduplicates([1, '1', 2, '2', 1]))
print(deduplicates([True, False, True, False]))
print(deduplicates([42, 42, 42, 42]))

# A simple bubble sort implementation.

def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            return arr
    return arr

print(bubbleSort([34, 7, 23, 32, 5, 62]))
print(bubbleSort([1, 2, 3, 4, 5, 6]))
print(bubbleSort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
print(bubbleSort([22, 17, 22, 11, 3, 5, 11]))
print(bubbleSort([42]))
print(bubbleSort(list("aaabbbccc")))
print(bubbleSort(list("hello world")))
